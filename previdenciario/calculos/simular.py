"""
simular.py - CLI: lê um caso em JSON e imprime um relatório em Markdown.

Uso:
    python simular.py caso.json
    python simular.py caso.json -o relatorio.md

Formato do JSON: veja exemplo_caso.json e o README.md.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date

from periodo_graca import analisar_qualidade
from regras_ec103 import (CONFERIR, Opcoes, Segurado, idade_amd, melhores_regras,
                          simular_regras)
from tempo import (DATA_EC103, Convencao, LinhaDoTempo, Periodo, calcular_tempo,
                   formatar_amd, para_data)

AVISO = "Simulação de apoio. Não substitui o cálculo no software do escritório nem a conferência da advogada."


def br(d: date | None) -> str:
    return d.strftime("%d/%m/%Y") if d else "-"


def pct(c: float | None, com_fator: bool = False) -> str:
    if c is None:
        return "-"
    txt = f"{c * 100:.0f}%".replace(".", ",")
    return txt + " x FP" if com_fator else txt


def carregar_caso(caminho: str) -> dict:
    with open(caminho, encoding="utf-8-sig") as f:  # tolera BOM do Bloco de Notas
        return json.load(f)


def montar(caso: dict):
    seg_d = caso["segurado"]
    segurado = Segurado(nascimento=seg_d["nascimento"], sexo=seg_d["sexo"], nome=seg_d.get("nome", ""))
    data_base = para_data(caso.get("data_base") or date.today())
    periodos = []
    for p in caso["periodos"]:
        p = dict(p)
        if not p.get("fim"):
            p["fim"] = data_base  # vínculo em aberto: vai até a data-base
        periodos.append(Periodo.de_dict(p))
    conv_d = caso.get("convencao", {})
    conv = Convencao(dias_ano=int(conv_d.get("dias_ano", 365)), dias_mes=int(conv_d.get("dias_mes", 30)))
    op_d = caso.get("opcoes", {})
    opcoes = Opcoes(
        convencao=conv,
        metodo_pontos=op_d.get("metodo_pontos", "amd"),
        professor_pontos_tempo=op_d.get("professor_pontos_tempo", "magisterio"),
        tempo_convertido_nas_regras_idade=bool(op_d.get("tempo_convertido_nas_regras_idade", True)),
        horizonte_anos=int(op_d.get("horizonte_anos", 45)),
    )
    return segurado, data_base, periodos, opcoes, op_d


def gerar_relatorio(caso: dict) -> str:
    segurado, data_base, periodos, opcoes, op_d = montar(caso)
    conv = opcoes.convencao
    projetar = bool(caso.get("projetar_contribuicao", False))
    L: list[str] = []
    w = L.append

    w("# Simulação de aposentadoria - RGPS (EC 103/2019)")
    w("")
    w(f"> **{AVISO}**")
    w("")
    ia, im, idd = idade_amd(segurado.nascimento, data_base)
    w("## Dados")
    w("")
    w(f"- Segurado(a): {segurado.nome or '-'}")
    w(f"- Sexo: {'Feminino' if segurado.sexo == 'F' else 'Masculino'}")
    w(f"- Nascimento: {br(segurado.nascimento)} (idade na data-base: {ia}a {im}m {idd}d)")
    w(f"- Data-base: {br(data_base)}")
    w(f"- Projeção de contribuição contínua após a data-base: {'sim' if projetar else 'não'}")
    w(f"- Convenção: dias corridos; ano = {conv.dias_ano} dias, mês = {conv.dias_mes} dias")
    w("")

    # --- Períodos ---
    t = calcular_tempo(periodos, segurado.sexo, ate=data_base, conv=conv)
    w("## Quadro de períodos (até a data-base)")
    w("")
    w("| # | Descrição | Início | Fim | Tipo | Dias | Fator | Convertido | Concomitante |")
    w("|---|---|---|---|---|---:|---:|---:|---|")
    for i, l in enumerate(t["periodos"], 1):
        fator = f"{l['fator']:.2f}".replace(".", ",")
        w(f"| {i} | {l['descricao'] or '-'} | {br(l['inicio'])} | {br(l['fim'])} | {l['tipo']} | "
          f"{l['dias']} | {fator} | {formatar_amd(l['dias_convertidos'], conv)} | "
          f"{'sim' if l['concomitante'] else 'não'} |")
    w("")
    w("Fator de conversão aplicado só aos dias até 13/11/2019 (EC 103, art. 25, §2º). "
      "Na coluna \"Convertido\" cada período aparece isolado; nos totais abaixo os dias concomitantes contam uma vez, pelo maior fator.")
    w("")

    w("## Tempo de contribuição e carência (até a data-base)")
    w("")
    w("| Item | Resultado |")
    w("|---|---|")
    w(f"| Tempo comum (união, sem conversão) | {formatar_amd(t['tempo_bruto_dias'], conv)} ({t['tempo_bruto_dias']} dias) |")
    w(f"| Acréscimo da conversão especial -> comum | {formatar_amd(t['acrescimo_conversao_dias'], conv)} ({t['acrescimo_conversao_dias']:.2f} dias) |")
    w(f"| Tempo de contribuição (com conversão) | {formatar_amd(t['tempo_contribuicao_dias'], conv)} ({t['tempo_contribuicao_dias']:.2f} dias) |")
    w(f"| Tempo em 13/11/2019 (com conversão) | {formatar_amd(t['tempo_ate_ec103_dias'], conv)} |")
    if t["tempo_magisterio_dias"]:
        w(f"| Tempo de magistério | {formatar_amd(t['tempo_magisterio_dias'], conv)} |")
    w(f"| Carência (competências com contribuição) | {t['carencia_meses']} |")
    w("")

    # --- Qualidade de segurado ---
    lt_real = LinhaDoTempo(periodos, segurado.sexo)
    forcado = caso.get("mais_de_120_sem_perda")
    q = analisar_qualidade(
        lt_real.intervalos_contribuicao(), data_base,
        categoria=caso.get("segurado", {}).get("categoria", "obrigatorio"),
        desemprego=bool(caso.get("desemprego_comprovado", False)),
        criterio_120=op_d.get("criterio_120", "qualquer_sequencia"),
        minimo_120_inclusive=bool(op_d.get("minimo_120_inclusive", False)),
        mais_de_120_forcado=forcado if isinstance(forcado, bool) else None,
    )
    w("## Qualidade de segurado (Lei 8.213/91, art. 15)")
    w("")
    w(f"- Situação na data-base: **{q['situacao']}**")
    if "perde_em" in q:
        a, m = q["ultima_competencia"]
        w(f"- Última competência: {m:02d}/{a}; período de graça: {q['meses_graca']} meses")
        w(f"- Mantém a qualidade até {br(q['mantem_ate'])}; perde em {br(q['perde_em'])}")
        for f in q["fundamentos"]:
            w(f"  - {f}")
    if "mais_de_120_sem_perda" in q:
        w(f"- Mais de 120 contribuições sem perda: {'sim' if q['mais_de_120_sem_perda'] else 'não'} "
          f"(contribuições na sequência atual: {q['contribuicoes_sequencia']}; critério: {q['criterio_120']}) [CONFERIR]")
    for p in q.get("perdas", []):
        w(f"- Perda no histórico: última contribuição {br(p['ultima_contribuicao'])}, "
          f"perdeu em {br(p['perdeu_em'])}, voltou em {br(p['voltou_em'])}")
    w("")

    # --- Regras ---
    res = simular_regras(periodos, segurado, data_base, projetar=projetar, opcoes=opcoes)
    w("## Regras de aposentadoria")
    w("")
    w("| Regra | Fundamento | Cumpre na data-base | Data em que cumpre | Coeficiente |")
    w("|---|---|---|---|---|")
    for r in res:
        if not r.aplicavel:
            w(f"| {r.nome} | {r.fundamento} | não se aplica | - | - |")
            continue
        w(f"| {r.nome} | {r.fundamento} | {'SIM' if r.cumpre else 'não'} | "
          f"{br(r.data_cumprimento)} | {pct(r.coeficiente, r.com_fator)} |")
    w("")
    if projetar:
        w("Datas futuras pressupõem contribuição contínua a partir do dia seguinte à data-base.")
    else:
        w("Sem projeção: datas futuras só aparecem quando falta apenas idade.")
    w("FP = fator previdenciário (não calculado; exige tábua do IBGE e salários de contribuição).")
    w("")

    w("### Detalhes por regra")
    w("")
    for r in res:
        w(f"**{r.nome}** ({r.fundamento})")
        w("")
        if not r.aplicavel:
            w(f"- Não se aplica: {r.motivo_inaplicavel}")
        else:
            if r.faltantes:
                w(f"- Faltava na data-base (ou em 13/11/2019, no direito adquirido):")
                for f in r.faltantes:
                    w(f"  - {f}")
            else:
                w("- Todos os requisitos cumpridos na data-base.")
        for o in r.observacoes:
            w(f"- {o}")
        w("")

    m = melhores_regras(res)
    w("## Melhor regra")
    w("")
    pd_, pc = m["por_data"], m["por_coeficiente"]
    if pd_:
        w(f"- **Pela data mais próxima:** {pd_.nome} - {br(pd_.data_cumprimento)} - coeficiente {pct(pd_.coeficiente, pd_.com_fator)}")
    else:
        w("- Nenhuma regra cumprida dentro do horizonte simulado.")
    if pc:
        w(f"- **Pelo maior coeficiente (regras sem fator):** {pc.nome} - {br(pc.data_cumprimento)} - coeficiente {pct(pc.coeficiente)}")
    if any(r.com_fator and r.data_cumprimento for r in res):
        w("- Regras com fator previdenciário (100% x FP) não entram na comparação de coeficiente: "
          "dependem do FP, que pode ficar abaixo ou acima de 1.")
    w("- O coeficiente não é o valor do benefício: a RMI depende da média dos salários de contribuição.")
    w("")

    w("## Pontos a conferir [CONFERIR]")
    w("")
    for c in CONFERIR:
        w(f"- [CONFERIR] {c}")
    w("")
    w(f"> **{AVISO}**")
    return "\n".join(L)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Simulação de aposentadoria RGPS (EC 103/2019) em Markdown.")
    ap.add_argument("caso", help="arquivo JSON do caso")
    ap.add_argument("-o", "--saida", help="grava o relatório neste arquivo .md")
    args = ap.parse_args(argv)
    relatorio = gerar_relatorio(carregar_caso(args.caso))
    if args.saida:
        with open(args.saida, "w", encoding="utf-8") as f:
            f.write(relatorio + "\n")
        print(f"Relatório gravado em {args.saida}")
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        print(relatorio)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
