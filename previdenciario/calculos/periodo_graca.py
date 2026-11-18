"""
periodo_graca.py - Manutenção da qualidade de segurado (Lei 8.213/91, art. 15).

REGRAS
------
  * art. 15, II  - até 12 meses após a cessação das contribuições (segurado
                   obrigatório que deixa de exercer atividade remunerada).
  * art. 15, §1º - prazo do inciso II prorrogado para até 24 meses se o
                   segurado já tiver pago MAIS DE 120 contribuições mensais
                   sem interrupção que acarrete a perda da qualidade.
  * art. 15, §2º - prazos acrescidos de 12 meses para o desempregado, desde
                   que comprovada a situação (máximo 36 meses).
  * art. 15, VI  - facultativo: até 6 meses após a cessação (sem as
                   prorrogações dos §§ 1º e 2º, que se referem ao inciso II).
  * art. 15, §4º - a perda ocorre no dia seguinte ao término do prazo para
                   recolher a contribuição referente ao mês imediatamente
                   posterior ao final do prazo de graça. Com o vencimento no
                   dia 15 (Lei 8.212/91, art. 30, II; Decreto 3.048/99,
                   art. 14), a perda ocorre no DIA 16 DO 2º MÊS SEGUINTE ao
                   término do prazo.

COMO SE CONTA (e o bug evitado)
-------------------------------
A soma é feita sobre a COMPETÊNCIA (mês/ano) da última contribuição, nunca
sobre o dia. Exemplo: última contribuição em 31/12/2024 (competência 12/2024)
  + 12 meses  -> fim do prazo de graça na competência 12/2025
  mês seguinte -> 01/2026, cujo recolhimento vence em 15/02/2026
  => mantém a qualidade até 15/02/2026 e PERDE em 16/02/2026.
Somar "12 meses + 1 mês + 15 dias" a partir do dia 31 fazia o calendário
transbordar (31/01 -> 03/03) e dava 15/03/2026 - errado.

PONTOS CONTROVERTIDOS
---------------------
  [CONFERIR] "mais de 120" lido literalmente (121 ou mais). Use
             `minimo_120_inclusive=True` para aceitar exatamente 120.
  [CONFERIR] Se a prorrogação de 24 meses, uma vez adquirida, se mantém
             depois de uma perda posterior. Padrão aqui: "qualquer_sequencia"
             (adquirida uma vez, incorpora-se - entendimento da TNU);
             alternativa "sequencia_atual" (só conta a sequência em curso).
  [CONFERIR] Na análise do HISTÓRICO (perdas passadas) o desemprego não é
             considerado; ele só entra no cálculo do prazo atual.
"""
from __future__ import annotations

from datetime import date

CATEGORIAS = ("obrigatorio", "facultativo")


def somar_meses(ano: int, mes: int, n: int) -> tuple[int, int]:
    """Soma n meses a uma competência (ano, mês). Sem dias - não transborda."""
    total = ano * 12 + (mes - 1) + n
    return total // 12, total % 12 + 1


def prazo_graca_meses(categoria: str = "obrigatorio", mais_de_120: bool = False,
                      desemprego: bool = False) -> int:
    if categoria not in CATEGORIAS:
        raise ValueError(f"Categoria inválida: {categoria!r}. Use {CATEGORIAS}")
    if categoria == "facultativo":
        return 6
    meses = 12
    if mais_de_120:
        meses += 12
    if desemprego:
        meses += 12
    return meses


def data_perda_qualidade(competencia: tuple[int, int], meses_graca: int) -> date:
    """
    Dia em que a qualidade é PERDIDA: dia 16 do 2º mês seguinte ao fim do prazo.
    competencia = (ano, mês) da última contribuição.
    """
    fim = somar_meses(competencia[0], competencia[1], meses_graca)
    a, m = somar_meses(fim[0], fim[1], 2)
    return date(a, m, 16)


def calcular_periodo_graca(ultima_contribuicao: date, categoria: str = "obrigatorio",
                           mais_de_120: bool = False, desemprego: bool = False) -> dict:
    """Prazo de graça a partir da data (ou competência) da última contribuição."""
    comp = (ultima_contribuicao.year, ultima_contribuicao.month)
    meses = prazo_graca_meses(categoria, mais_de_120, desemprego)
    perde = data_perda_qualidade(comp, meses)
    fim_prazo = somar_meses(comp[0], comp[1], meses)
    fundamentos = ["Lei 8.213/91, art. 15, " + ("VI (facultativo: 6 meses)"
                                               if categoria == "facultativo"
                                               else "II (12 meses)")]
    if categoria != "facultativo":
        if mais_de_120:
            fundamentos.append("art. 15, §1º (+12 meses: mais de 120 contribuições sem perda)")
        if desemprego:
            fundamentos.append("art. 15, §2º (+12 meses: desemprego comprovado)")
    fundamentos.append("art. 15, §4º c/c Dec. 3.048/99, art. 14 (perda no dia 16 do 2º mês seguinte)")
    return {
        "ultima_competencia": comp,
        "meses_graca": meses,
        "fim_prazo_competencia": fim_prazo,
        "mantem_ate": date(perde.year, perde.month, 15),
        "perde_em": perde,
        "fundamentos": fundamentos,
    }


def _meses_do_intervalo(ini: date, fim: date) -> set:
    res = set()
    a, m = ini.year, ini.month
    while (a, m) <= (fim.year, fim.month):
        res.add((a, m))
        a, m = somar_meses(a, m, 1)
    return res


def analisar_qualidade(intervalos: list[tuple[date, date]], data_referencia: date,
                       categoria: str = "obrigatorio", desemprego: bool = False,
                       criterio_120: str = "qualquer_sequencia",
                       minimo_120_inclusive: bool = False,
                       mais_de_120_forcado: bool | None = None) -> dict:
    """
    Percorre os intervalos de contribuição (ordenados, sem sobreposição), registra
    perdas de qualidade no histórico, conta as contribuições sem perda e diz se o
    segurado mantém a qualidade na `data_referencia`.
    `mais_de_120_forcado` (True/False) ignora a contagem automática.
    """
    if criterio_120 not in ("qualquer_sequencia", "sequencia_atual"):
        raise ValueError("criterio_120 deve ser 'qualquer_sequencia' ou 'sequencia_atual'")
    limite = 120 if minimo_120_inclusive else 121

    intervalos = sorted(i for i in intervalos if i[0] <= data_referencia)
    if not intervalos:
        return {"situacao": "sem contribuições até a data de referência",
                "segurado": False, "perdas": [], "contribuicoes_sequencia": 0}

    perdas = []
    seq: set = set()
    ja_teve_120 = False
    for k, (ini, fim) in enumerate(intervalos):
        fim = min(fim, data_referencia)
        seq |= _meses_do_intervalo(ini, fim)
        if len(seq) >= limite:
            ja_teve_120 = True
        if k + 1 < len(intervalos):
            prox_ini = intervalos[k + 1][0]
            tem_120 = ja_teve_120 if criterio_120 == "qualquer_sequencia" else len(seq) >= limite
            if mais_de_120_forcado is not None:
                tem_120 = mais_de_120_forcado
            meses = prazo_graca_meses(categoria, tem_120, False)
            perde = data_perda_qualidade((fim.year, fim.month), meses)
            if prox_ini >= perde:
                perdas.append({"ultima_contribuicao": fim, "perdeu_em": perde,
                               "voltou_em": prox_ini})
                seq = set()

    ultimo_fim = intervalos[-1][1]
    tem_120 = ja_teve_120 if criterio_120 == "qualquer_sequencia" else len(seq) >= limite
    if mais_de_120_forcado is not None:
        tem_120 = mais_de_120_forcado

    base = {"perdas": perdas, "contribuicoes_sequencia": len(seq),
            "mais_de_120_sem_perda": tem_120, "criterio_120": criterio_120}
    if ultimo_fim >= data_referencia:
        base.update({"situacao": "contribuindo na data de referência", "segurado": True})
        return base
    graca = calcular_periodo_graca(ultimo_fim, categoria, tem_120, desemprego)
    segurado = data_referencia < graca["perde_em"]
    base.update(graca)
    base.update({
        "situacao": ("em período de graça" if segurado else "qualidade de segurado PERDIDA"),
        "segurado": segurado,
    })
    return base
