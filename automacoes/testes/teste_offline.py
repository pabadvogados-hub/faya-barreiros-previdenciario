# -*- coding: utf-8 -*-
"""Teste offline de todas as automacoes — nenhuma chamada de rede, nenhuma credencial.

Usa fixtures FICTICIAS (fixture_asaas.json, fixture_djen.json), banco temporario, data simulada e
um "OneDrive" numa pasta temporaria. O Notion e testado de dois jeitos: NAO configurado (o modo
real hoje) e com um servidor FALSO no lugar do HTTP (confere o payload montado, sem rede).
Uso: python automacoes/testes/teste_offline.py
"""
from __future__ import annotations

import os
import sys
import tempfile
from datetime import date
from pathlib import Path

TMP = tempfile.mkdtemp(prefix="escritorio_teste_")
ONEDRIVE = Path(TMP) / "onedrive"
ONEDRIVE.mkdir()
os.environ["ESCRITORIO_DADOS_DIR"] = str(Path(TMP) / "dados")
os.environ["ESCRITORIO_HOJE"] = "2026-12-05"
os.environ["ONEDRIVE_RAIZ"] = str(ONEDRIVE)
for k in ("ASAAS_API_KEY", "NOTION_TOKEN"):
    os.environ.pop(k, None)

AQUI = Path(__file__).resolve().parent
AUT = AQUI.parent
for p in (AUT, AUT / "financeiro", AUT / "controladoria", AUT / "drive"):
    sys.path.insert(0, str(p))

from comum.config import utf8_stdout  # noqa: E402

utf8_stdout()
FALHAS: list[str] = []


def chk(nome, cond, detalhe=""):
    print(f"  [{'ok' if cond else 'FALHA'}] {nome}{(' — ' + str(detalhe)) if detalhe and not cond else ''}")
    if not cond:
        FALHAS.append(nome)


def t_nomes():
    print("\n# nomes / convencao")
    from comum import nomes
    chk("CNJ formatado", nomes.formatar_cnj("10012345620264013300") == "1001234-56.2026.4.01.3300")
    chk("CNJ achado na legenda", nomes.achar_cnj("segue doc do proc 1001234-56.2026.4.01.3300 ok") ==
        "1001234-56.2026.4.01.3300")
    chk("nome de arquivo", nomes.nome_arquivo("cnis", "Extrato CNIS completo", "PDF", date(2026, 11, 16)) ==
        "2026-11-16_CNIS_extrato-cnis-completo.pdf")
    chk("pasta de demanda externa", nomes.pasta_demanda("revisão João", "2026-11-18") == "2026-11-18 - REVISÃO JOÃO")


def t_mensageria():
    print("\n# mensageria (so modo fila)")
    from comum import mensageria
    txt, falt = mensageria.render("Oi {{nome}}, link {{link}}", {"nome": "Ana"})
    chk("render mantem lacuna visivel", "{{link}}" in txt and falt == ["link"])
    chk("telefone 55", mensageria.telefone_whatsapp("(71) 99114-0000") == "5571991140000")
    r = mensageria.enviar("71991140000", "teste", "teste", executar=False, cfg={"mensageria": {"modo": "crm_card"}})
    chk("modo desconhecido cai na fila", r["modo"] == "fila" and r.get("dry_run"))


def t_regua():
    print("\n# regua de cobranca (fixture, 2026-12-05)")
    import regua_cobranca as rc
    from comum.asaas import AsaasCliente
    chk("marco 10", rc.escolher_marco(10) == 10)
    chk("marco 9 (tolerancia)", rc.escolher_marco(9) == 10)
    chk("dia 7 sem marco", rc.escolher_marco(7) is None)
    chk("marco 4 -> 5", rc.escolher_marco(4) == 5)
    chk("marco 0", rc.escolher_marco(0) == 0)
    mods = rc.ler_modelos()
    chk("MSG-07 lido (modelos 1,1-NF,2,3,4,6,7,8)", all(k in mods for k in ("1", "1-NF", "2", "3", "4", "6", "7", "8")),
        sorted(mods))
    chk("condicional da nota (sem nota)", "{{link_nota}}" not in rc.aplicar_condicional_nota(mods["6"], ""))
    chk("condicional da nota (com nota)", "nota fiscal" in rc.aplicar_condicional_nota(mods["6"], "x").lower())
    res = rc.rodar(AsaasCliente(fixture=str(AQUI / "fixture_asaas.json")), executar=False,
                   cfg={"regua": {}, "mensageria": {"modo": "fila"}}, ref=date(2026, 12, 5))
    env = " | ".join(res["enviadas"])
    chk("D-10 pay_T1", "D-10 pay_T1" in env, env)
    chk("D-5 pay_T2", "D-5 pay_T2" in env, env)
    chk("D0 pay_T4", "D0 pay_T4" in env, env)
    chk("PAGO pay_T6", "PAGO pay_T6" in env, env)
    chk("pay_T5 (7 dias) nao sai", "pay_T5" not in env)
    chk("PJ sem contato financeiro vira pendencia (nao sai com lacuna)",
        any("pay_T3" in p for p in res["pendencias"]), res["pendencias"])


def t_relatorio():
    print("\n# relatorio financeiro")
    import relatorio_diario as rd
    from comum.asaas import AsaasCliente
    d = rd.coletar(AsaasCliente(fixture=str(AQUI / "fixture_asaas.json")), date(2026, 12, 5))
    c = rd.consolidar(d)
    chk("entradas = recebido no mes", abs(c["entradas"] - 1500.0) < 0.01, c["entradas"])
    chk("saidas do extrato", abs(c["saidas"] - 1201.99) < 0.01, c["saidas"])
    chk("inadimplencia", abs(c["inadimplencia"] - 2000.0) < 0.01, c["inadimplencia"])
    chk("a receber ate fim do mes", abs(c["a_receber"] - (1500 + 800 + 2000 + 300 + 300)) < 0.01, c["a_receber"])
    md = rd.markdown(date(2026, 12, 5), d, c)
    chk("markdown com secoes", "## Inadimplentes" in md and "EMPRESA FICTICIA" in md)
    xl = rd.planilha(Path(TMP) / "rel.xlsx", d, c)
    chk("planilha gerada", xl.exists())


def t_nova_cobranca():
    print("\n# nova cobranca")
    import nova_cobranca as nc
    chk("CNPJ valido", nc.valida_doc("11.222.333/0001-81"))
    chk("CNPJ invalido", not nc.valida_doc("11.222.333/0001-82"))
    chk("CPF valido", nc.valida_doc("000.000.001-91"))
    chk("31/01 + 1 mes = 28/02", nc.somar_meses(date(2026, 1, 31), 1) == date(2026, 2, 28))

    class A:
        assessoria, meses, competencia_anterior, parcelas, ref = True, 12, False, 1, ""
        vencimento, doc, valor, referencia = "2026-12-10", "11222333000181", 1500.0, "honorários mensais"
    plano = nc.planejar(A)
    chk("12 boletos", len(plano) == 12)
    chk("vencimentos mensais", plano[1]["vencimento"] == "2027-01-10" and plano[11]["vencimento"] == "2027-11-10")
    chk("referencias unicas (idempotencia)", len({p["ref"] for p in plano}) == 12)

    class B(A):
        assessoria, parcelas, valor, ref = False, 3, 1000.0, "ct-1"
    p2 = nc.planejar(B)
    chk("parcelas somam o total", abs(sum(x["valor"] for x in p2) - 1000.0) < 0.001, [x["valor"] for x in p2])


def t_nota():
    print("\n# nota fiscal")
    import nota_fiscal as nf
    falta = nf.fiscal_incompleto({})
    chk("fiscal vazio bloqueia", "municipalServiceName" in falta and "emitir_desde (data de corte)" in falta)
    p = nf.montar_payload({"id": "pay_X", "value": 100, "description": "honorários"},
                          {"municipalServiceName": "SERV", "municipalServiceCode": "1", "taxes": {"iss": 2}},
                          date(2026, 12, 5))
    chk("payload com externalReference nf:<id>", p["externalReference"] == "nf:pay_X" and p["payment"] == "pay_X")


def t_pagamentos():
    print("\n# pagamentos")
    import pagamentos as pg
    chk("sabado antecipa para sexta", pg.data_pagamento("2026-12", 5) == date(2026, 12, 4))
    chk("dia 31 em fevereiro", pg.data_pagamento("2027-02", 31, antecipar_fds=False) == date(2027, 2, 28))


def t_prazos_classificador():
    print("\n# prazos (BA)")
    import prazos
    chk("auto-teste do motor de prazos", prazos._testes())
    print("\n# classificador")
    import classificador as cl
    casos = [
        ("SENTENCA. Ante o exposto, JULGO PROCEDENTE o pedido.", "TJBA", "", "APELACAO", 15),
        ("Julgo parcialmente procedentes os pedidos e condeno a reclamada.", "TRT5", "", "RECURSO_ORDINARIO", 8),
        ("Fica V. Sa. intimado para tomar ciencia da Sentenca ID 1 proferida nos autos. Arquivem-se os autos.",
         "TRT5", "", "MERO_ANDAMENTO", None),
        ("DEFIRO a tutela de urgencia requerida.", "TRF1", "", "AGRAVO", 15),
        ("Homologo os calculos de liquidacao.", "TRT5", "", "AGRAVO", 8),
        ("Intime-se a parte autora para, no prazo de 10 (dez) dias, manifestar-se.", "TJBA", "", "OUTROS", 10),
        ("Intime-se a parte embargada para se manifestar sobre os embargos de declaracao.", "TJBA", "",
         "EMBARGOS_DE_DECLARACAO", 5),
        ("Recebo a apelacao. Intime-se o apelado para contrarrazoes.", "TRF1", "", "OUTROS", 15),
        ("Certifico a juntada da peticao. Conclusos.", "TJBA", "", "MERO_ANDAMENTO", None),
        ("Julgo procedente o pedido de concessao do beneficio.", "TRF1", "Procedimento do Juizado Especial Civel",
         "OUTROS", 10),
        ("Indefiro o pedido de producao de prova testemunhal.", "TJBA", "", "OUTROS", None),
    ]
    for texto, trib, classe, cat, dias in casos:
        r = cl.classificar(texto, trib, classe)
        chk(f"{cat:22} {dias!s:>4}  <- {texto[:45]}", r["categoria"] == cat and r["dias"] == dias,
            f"{r['categoria']}/{r['subtipo']}/{r['dias']}")
    r = cl.classificar("Julgo procedente o pedido.", "TJBA")
    chk("sentenca traz ED em paralelo e pede confirmacao", r["tambem_cabe"] and r["confirmar_advogado"])


def t_intimacoes():
    print("\n# controladoria (fixture DJEN, Notion NAO configurado)")
    import json
    import intimacoes as it
    from comum import notion
    chk("notion.configurado() = False sem token", not notion.configurado())
    itens = json.loads((AQUI / "fixture_djen.json").read_text("utf-8"))["itens"]
    res = it.processar(itens, {"controladoria": {}, "notion": {}}, executar=False)
    cats = {x["numero"]: x["c"]["categoria"] for x in res["linhas"] if not x.get("ja")}
    chk("6 intimacoes classificadas", len(cats) == 6, cats)
    chk("sentenca TJBA -> apelacao", cats.get("0000001-00.2026.8.05.0001") == "APELACAO", cats)
    chk("tutela TRF1 -> agravo", cats.get("1000004-00.2026.4.01.3300") == "AGRAVO", cats)
    chk("cabecalho PJe nao vira recurso", cats.get("0000003-00.2026.5.05.0001") == "MERO_ANDAMENTO", cats)
    chk("sem processo no Notion vira pendencia", any("nao encontrado no Notion" in p for p in res["pendencias"]))
    sentenca = next(x for x in res["linhas"] if x.get("numero") == "0000001-00.2026.8.05.0001")
    chk("prazo NAO se perde sem processo: tarefa [PRAZO] em dry-run",
        any(t.startswith("[PRAZO]") and r.get("_dry_run") for t, r in sentenca["tarefas"]), sentenca["tarefas"])
    trf = next(x for x in res["linhas"] if x.get("numero") == "1000004-00.2026.4.01.3300")
    chk("TRF1 traz aviso da Lei 5.010", any("5.010" in a for a in trf["pz"].get("avisos") or []))
    rel = it.relatorio(res, date(2026, 12, 5))
    chk("relatorio gerado", "| Processo |" in rel and "Pendências" in rel)
    res2 = it.processar(itens[:1], {"controladoria": {}, "notion": {}}, executar=True)
    erros = [r for x in res2["linhas"] for _, r in x.get("tarefas", [])]
    chk("--go sem Notion: tarefa volta {'erro'} e vira pendencia (nao marca como tratada)",
        all(r.get("erro") for r in erros) and any("TAREFA NAO CRIADA" in p for p in res2["pendencias"]), res2)
    res3 = it.processar(itens[:1], {"controladoria": {}, "notion": {}}, executar=False)
    chk("comunicacao com tarefa falhada e reprocessada na proxima rodada", not res3["linhas"][0].get("ja"))


class _NotionFalso:
    """Servidor falso: responde as rotas que o conector usa e guarda o que foi enviado."""

    ESQ = {
        "db-proc": {"Processo": "title", "Numero CNJ": "rich_text", "Fase": "select", "Cliente": "relation"},
        "db-prazos": {"Nome": "title", "Tipo": "select", "Responsavel": "people", "Processo": "relation",
                      "Prazo": "date", "Fatal": "date", "Urgente": "checkbox", "Obs": "rich_text", "Status": "status"},
    }

    def __init__(self):
        self.chamadas = []

    def __call__(self, metodo, caminho, json_body=None, tentativas=4):
        self.chamadas.append((metodo, caminho, json_body))
        if metodo == "GET" and caminho.startswith("/databases/"):
            db = caminho.split("/")[2]
            return {"properties": {n: {"type": t} for n, t in self.ESQ[db].items()}}
        if metodo == "POST" and caminho == "/databases/db-proc/query":
            return {"results": [{"id": "pg-1", "url": "https://notion.so/pg1", "created_time": "2026-11-01T10:00:00.000Z",
                                 "properties": {
                                     "Processo": {"type": "title", "title": [{"plain_text": "Maria x INSS"}]},
                                     "Numero CNJ": {"type": "rich_text",
                                                    "rich_text": [{"plain_text": "1001234-56.2026.4.01.3300"}]},
                                     "Fase": {"type": "select", "select": {"name": "Pericia"}},
                                     "Cliente": {"type": "relation", "relation": [{"id": "cli-1"}]}}}],
                    "has_more": False}
        if metodo == "POST" and caminho == "/databases/db-prazos/query":
            return {"results": [], "has_more": False}
        if metodo == "POST" and caminho == "/pages":
            return {"id": "nova-pg", "url": "https://notion.so/nova"}
        if metodo == "GET" and caminho.startswith("/blocks/"):
            return {"results": [
                {"id": "b1", "type": "paragraph", "created_time": "2026-10-01T00:00:00.000Z",
                 "paragraph": {"rich_text": [{"plain_text": "05/11/2026 - Juntada do laudo pericial"}]}},
                {"id": "b2", "type": "bulleted_list_item", "created_time": "2026-11-10T00:00:00.000Z",
                 "bulleted_list_item": {"rich_text": [{"plain_text": "Peticao de impugnacao protocolada"}]}},
                {"id": "b3", "type": "heading_2", "heading_2": {"rich_text": [{"plain_text": "Andamentos"}]}}],
                "has_more": False}
        if metodo == "PATCH" and caminho.startswith("/blocks/"):
            return {"results": [{"id": "bloco-novo"}]}
        raise AssertionError(f"rota inesperada {metodo} {caminho}")


def t_notion():
    print("\n# notion (nao configurado + servidor falso, sem rede)")
    from comum import notion
    r = notion.criar_tarefa(None, "Prazo", ["Barbara"], None, "[PRAZO] Teste\n\ncorpo", end_date="2026-12-10",
                            date_deadline="2026-12-14", executar=False)
    chk("dry-run nao toca a API", r.get("_dry_run") and r["campos"]["prazo"] == "2026-12-10"
        and r["campos"]["prazo_fatal"] == "2026-12-14" and r["campos"]["titulo"] == "[PRAZO] Teste", r)
    r = notion.criar_tarefa(None, "Prazo", [], None, "x", executar=True)
    chk("--go sem config devolve erro claro (nao levanta)", "Notion nao configurado" in (r.get("erro") or ""), r)
    try:
        notion.buscar_processo("1001234-56.2026.4.01.3300")
        chk("leitura sem config levanta NotionErro", False)
    except notion.NotionErro:
        chk("leitura sem config levanta NotionErro", True)
    try:
        notion.listar_documentos("x")
        chk("documento do processo: NaoSuportado", False)
    except notion.NaoSuportado as e:
        chk("documento do processo: NaoSuportado (aponta o OneDrive)", "OneDrive" in str(e))

    cfg = {"databases": {"processos": "db-proc", "prazos": "db-prazos", "clientes": ""},
           "campos": {"processos": {"numero": "Numero CNJ", "fase": "Fase", "cliente": "Cliente"},
                      "prazos": {"tipo": "Tipo", "responsavel": "Responsavel", "processo": "Processo", "prazo": "Prazo",
                                 "prazo_fatal": "Fatal", "urgente": "Urgente", "observacao": "Obs", "status": "Status",
                                 "inicio": ""}},
           "status_inicial": "A fazer", "status_concluido": ["Feito"]}
    falso = _NotionFalso()
    orig_cfg, orig_req = notion._cfg, notion._req
    notion._cfg, notion._req = (lambda: cfg), falso
    notion._esquema_db.cache_clear()
    os.environ["NOTION_TOKEN"] = "token-falso"
    try:
        chk("configurado() com token + ids", notion.configurado() and not notion.configurado("clientes"))
        achados = notion.buscar_processo("1001234-56.2026.4.01.3300")
        filtro = next(b for m, c, b in falso.chamadas if c == "/databases/db-proc/query")["filter"]
        chk("filtro pelo tipo da coluna (rich_text contains)",
            filtro == {"property": "Numero CNJ", "rich_text": {"contains": "1001234-56.2026.4.01.3300"}}, filtro)
        chk("pagina traduzida para nomes logicos", achados and achados[0]["id"] == "pg-1"
            and achados[0]["fase"] == "Pericia" and achados[0]["cliente"] == ["cli-1"], achados)
        longo = "[PRAZO] Contestar - Maria - 1001234\n\n" + ("x" * 4500)
        r = notion.criar_tarefa("pg-1", "Prazo", ["user-1"], "ignorado", longo, start_date="2026-12-05",
                                end_date="2026-12-10", date_deadline="2026-12-14", urgent=True, executar=True)
        body = next(b for m, c, b in falso.chamadas if c == "/pages")
        pr = body["properties"]
        chk("tarefa criada devolve id", r.get("id") == "nova-pg", r)
        chk("titulo = 1a linha", pr["Nome"]["title"][0]["text"]["content"] == "[PRAZO] Contestar - Maria - 1001234")
        chk("datas: prazo interno e fatal", pr["Prazo"] == {"date": {"start": "2026-12-10"}}
            and pr["Fatal"] == {"date": {"start": "2026-12-14"}}, pr.get("Prazo"))
        chk("pessoa, relacao, select, status, checkbox", pr["Responsavel"] == {"people": [{"id": "user-1"}]}
            and pr["Processo"] == {"relation": [{"id": "pg-1"}]} and pr["Tipo"] == {"select": {"name": "Prazo"}}
            and pr["Status"] == {"status": {"name": "A fazer"}} and pr["Urgente"] == {"checkbox": True}, pr)
        chk("texto longo quebrado em blocos de 2000", len(pr["Obs"]["rich_text"]) == 3
            and all(len(x["text"]["content"]) <= 2000 for x in pr["Obs"]["rich_text"]))
        chk("campo sem coluna mapeada e ignorado (inicio)", "inicio" not in pr and len(pr) == 9, sorted(pr))
        chk("corpo da pagina com o texto", body["children"] and body["children"][0]["type"] == "paragraph")
        notion.tarefas_abertas()
        f = next(b for m, c, b in falso.chamadas if c == "/databases/db-prazos/query")["filter"]
        chk("tarefas abertas filtra status concluido", f == {"property": "Status", "status": {"does_not_equal": "Feito"}}, f)
        movs = notion.ultimas_movimentacoes("pg-1", 8)
        chk("andamentos do corpo da pagina, mais recente primeiro",
            [m["data"] for m in movs] == ["2026-11-10", "2026-11-05"], movs)
        r = notion.lancar_andamento("pg-1", "2026-12-05", "Protocolada replica", executar=True)
        bloco = next(b for m, c, b in falso.chamadas if m == "PATCH")["children"][0]
        chk("lancar andamento acrescenta paragrafo datado",
            bloco["paragraph"]["rich_text"][0]["text"]["content"] == "05/12/2026 - Protocolada replica", bloco)
    finally:
        notion._cfg, notion._req = orig_cfg, orig_req
        notion._esquema_db.cache_clear()
        os.environ.pop("NOTION_TOKEN", None)

    from comum import tramitacao
    chk("tramitacao.configurado() = False", tramitacao.configurado() is False)
    try:
        tramitacao.enviar_para_assinatura("x.pdf", "contrato", [])
        chk("tramitacao sem endpoint inventado (NotImplementedError)", False)
    except NotImplementedError:
        chk("tramitacao sem endpoint inventado (NotImplementedError)", True)


def t_onedrive():
    print("\n# OneDrive (pasta local temporaria) / estrutura / roteamento")
    import arquivar_documento as ad
    import criar_estrutura as ce
    from comum import drive
    chk("ONEDRIVE_RAIZ disponivel", drive.credenciais_disponiveis())
    svc = drive.servico()
    caminhos = {"/".join(p) for p in ce.plano_base(2026)}
    chk("estrutura base", {"00_ESCRITORIO/POPS", "00_ESCRITORIO/ENTRADA_DOCUMENTOS", "FINANCEIRO/2026/12/RELATORIOS",
                           "CLIENTES", "DEMANDAS_EXTERNAS_CALCULO"} <= caminhos)
    cli = {"id": "maria", "nome": "Maria Ficticia da Silva", "area_padrao": "previdenciario",
           "processos": [{"numero": "1001234-56.2026.4.01.3300", "parte_contraria": "INSS",
                          "tipo_acao": "Aposentadoria especial", "notion_page_id": "pg-1", "area": "previdenciario"}]}
    plano = {"/".join(p) for p in ce.plano_cliente(cli)}
    chk("11 subpastas previdenciarias do cliente",
        all(f"CLIENTES/MARIA FICTICIA DA SILVA/{s}" in plano for s in
            ("00_CONTRATACAO", "02_CNIS_E_VINCULOS", "03_PROVAS_ESPECIAIS", "04_SAUDE", "05_INSS_ADMINISTRATIVO",
             "06_CALCULOS", "09_FINANCEIRO", "99_A_CLASSIFICAR")), sorted(plano)[:5])
    chk("pasta do processo em 08_PROCESSO_JUDICIAL", "CLIENTES/MARIA FICTICIA DA SILVA/08_PROCESSO_JUDICIAL/"
        "1001234-56.2026.4.01.3300 - INSS - APOSENTADORIA ESPECIAL" in plano, sorted(plano))
    parc = {"id": "dr-x", "nome": "Dr. Fulano Parceiro", "demandas": [
        {"caso": "Revisao Joao", "recebida_em": "2026-11-18", "prazo_entrega": "2026-12-10",
         "palavras_chave": ["joao"]},
        {"caso": "RMI Pedro", "recebida_em": "2026-11-20", "palavras_chave": ["pedro"]}]}
    pd = ["/".join(p) for p in ce.plano_demanda_externa(parc, parc["demandas"][0])]
    chk("demanda externa fora de CLIENTES", pd[1] == "DEMANDAS_EXTERNAS_CALCULO/DR. FULANO PARCEIRO/2026-11-18 - REVISAO JOAO"
        and pd[-1].endswith("04_FINANCEIRO"), pd)

    casos = [
        ("segue doc do processo 1001234-56.2026.4.01.3300", "foto.jpg", "08_PROCESSO_JUDICIAL"),
        ("PPP da empresa", "ppp.pdf", "03_PROVAS_ESPECIAIS"),
        ("", "laudo_tecnico_ltcat.pdf", "03_PROVAS_ESPECIAIS"),
        ("laudo do ortopedista", "laudo.pdf", "04_SAUDE"),
        ("", "CNIS_atualizado.pdf", "02_CNIS_E_VINCULOS"),
        ("contrato de trabalho antigo", "ct.pdf", "02_CNIS_E_VINCULOS"),
        ("procuração assinada", "proc.pdf", "00_CONTRATACAO"),
        ("carta de indeferimento do INSS", "carta.pdf", "05_INSS_ADMINISTRATIVO"),
        ("meu RG", "rg.jpg", "01_DOCUMENTOS_PESSOAIS"),
        ("comprovante de residência", "luz.pdf", "01_DOCUMENTOS_PESSOAIS"),
        ("olha isso", "x.pdf", "99_A_CLASSIFICAR"),
    ]
    for legenda, arq, esperado in casos:
        r = ad.rotear(cli, legenda, arq)
        alvo = r["caminho"][2] if len(r["caminho"]) > 2 else r["caminho"][-1]
        chk(f"{arq:24} -> {esperado}", alvo == esperado, r["caminho"])
    r = ad.rotear(cli, "laudo", "l.pdf")
    chk("cliente com 1 processo: tarefa ligada ao processo no Notion", r["processo_id"] == "pg-1", r)
    r = ad.rotear(None, "oi", "x.pdf")
    chk("remetente desconhecido -> ENTRADA_DOCUMENTOS", r["caminho"] == ["00_ESCRITORIO", "ENTRADA_DOCUMENTOS"])
    r = ad.rotear(None, "calculos do pedro", "x.pdf", parceiro=parc)
    chk("parceiro + palavra-chave -> demanda certa", r["caminho"][2] == "2026-11-20 - RMI PEDRO"
        and r["caminho"][-1] == "01_RECEBIDO_DO_PARCEIRO", r["caminho"])
    r = ad.rotear(None, "segue", "x.pdf", parceiro=parc)
    chk("parceiro com 2 demandas e sem pista -> 99 do parceiro", r["caminho"][-1] == "99_A_CLASSIFICAR"
        and r["caminho"][0] == "DEMANDAS_EXTERNAS_CALCULO", r["caminho"])

    # pastas idempotentes e copia
    p = drive.garantir_caminho(svc, None, ["CLIENTES", "TESTE", "04_SAUDE"], executar=False, log=None)
    chk("dry-run nao cria pasta", p.startswith("DRY:") and not (ONEDRIVE / "CLIENTES").exists(), p)
    p = drive.garantir_caminho(svc, None, ["CLIENTES", "TESTE", "04_SAUDE"], executar=True, log=None)
    chk("--go cria a cadeia", Path(p).is_dir())
    p2 = drive.garantir_caminho(svc, None, ["CLIENTES", "TESTE", "04_SAUDE"], executar=True, log=None)
    chk("idempotente (mesma pasta, sem duplicar)", p2 == p and len(list((ONEDRIVE / "CLIENTES").iterdir())) == 1)
    orig = Path(TMP) / "laudo.pdf"
    orig.write_bytes(b"%PDF-1.4 laudo A")
    f = drive.enviar_arquivo(svc, orig, p, "2026-12-05_SAUDE_laudo.pdf", executar=True)
    chk("copia + link relativo", f["link"] == "CLIENTES/TESTE/04_SAUDE/2026-12-05_SAUDE_laudo.pdf"
        and Path(f["caminho"]).read_bytes() == b"%PDF-1.4 laudo A", f)
    f = drive.enviar_arquivo(svc, orig, p, "2026-12-05_SAUDE_laudo.pdf", executar=True)
    chk("mesmo conteudo: nao copia de novo", f["ja_existia"] is True)
    orig.write_bytes(b"%PDF-1.4 laudo B")
    f = drive.enviar_arquivo(svc, orig, p, "2026-12-05_SAUDE_laudo.pdf", executar=True)
    chk("conteudo diferente: nunca sobrescreve (vira ' (2)')", f["link"].endswith("laudo (2).pdf") and
        (Path(p) / "2026-12-05_SAUDE_laudo.pdf").read_bytes() == b"%PDF-1.4 laudo A", f)
    f = drive.enviar_bytes(svc, b"comprovante", "c.html", p, executar=True)
    chk("enviar_bytes grava", (Path(p) / "c.html").read_bytes() == b"comprovante")
    try:
        drive.garantir_pasta(svc, "../fora", str(ONEDRIVE))
        chk("nome com .. recusado", False)
    except ValueError:
        chk("nome com .. recusado", True)

    # arquivamento de ponta a ponta (Notion nao configurado)
    doc = Path(TMP) / "CNIS_maria.pdf"
    doc.write_bytes(b"%PDF cnis maria")
    r = ad.arquivar(doc, "extrato CNIS", cliente=cli, executar=False, cfg={"notion": {}})
    chk("arquivar dry-run: nada copiado, tarefa dry-run",
        r["onedrive"].get("_dry_run") and r["tarefa"].get("_dry_run")
        and not (ONEDRIVE / "CLIENTES" / "MARIA FICTICIA DA SILVA").exists(), r)
    r = ad.arquivar(doc, "extrato CNIS", cliente=cli, executar=True, cfg={"notion": {}})
    destino = ONEDRIVE / "CLIENTES" / "MARIA FICTICIA DA SILVA" / "02_CNIS_E_VINCULOS" / "2026-12-05_CNIS-E-VINCULOS_extrato-cnis.pdf"
    chk("arquivar --go: arquivo na pasta certa", destino.exists(), r)
    chk("arquivar --go sem Notion: tarefa com erro claro", "Notion nao configurado" in (r["tarefa"].get("erro") or ""), r)
    r = ad.arquivar(doc, "extrato CNIS", cliente=cli, executar=True, cfg={"notion": {}})
    chk("arquivar idempotente por hash", r.get("ja_arquivado") is True, r)

    # docx -> pdf: com LibreOffice converte; sem ele avisa e devolve None (nunca quebra)
    from comum import modelos
    docx = modelos.markdown_para_docx("# Teste\n\nTexto.", Path(TMP) / "t.docx")
    pdf = drive.docx_para_pdf(docx, Path(TMP) / "pdf")
    chk("docx_para_pdf: PDF gerado ou aviso (None)", pdf is None or (pdf.exists() and pdf.read_bytes()[:4] == b"%PDF"),
        pdf)
    print(f"    (LibreOffice {'encontrado: PDF gerado' if pdf else 'ausente: so aviso'})")


def t_modelos():
    print("\n# modelos")
    from comum import modelos
    tmp = Path(TMP) / "m.md"
    tmp.write_text("notas {{nao_entra}}\n<!-- INICIO_DOCUMENTO -->\nOla {{nome}}.\n{{#extra}}Bloco {{valor}}.{{/extra}}\n"
                   "Fim.\n<!-- FIM_DOCUMENTO -->\n", encoding="utf-8")
    txt, falt = modelos.render(tmp, {"nome": "Ana"})
    chk("so o corpo entre os marcadores", "notas" not in txt and "Ola Ana." in txt)
    chk("bloco opcional removido", "Bloco" not in txt and falt == [])
    txt, falt = modelos.render(tmp, {"nome": "Ana", "extra": True})
    chk("bloco opcional incluido e campo faltando apontado", "Bloco" in txt and falt == ["valor"])
    chk("fiscal barra {{campo}}", bool(modelos.fiscal(txt)))
    chk("fiscal barra [A CONFIRMAR]", bool(modelos.fiscal("data [A CONFIRMAR]")))
    docx = modelos.markdown_para_docx(txt, Path(TMP) / "m.docx")
    chk("docx gerado", docx.exists() and docx.stat().st_size > 1000)


if __name__ == "__main__":
    for t in (t_nomes, t_mensageria, t_regua, t_relatorio, t_nova_cobranca, t_nota, t_pagamentos,
              t_prazos_classificador, t_intimacoes, t_notion, t_onedrive, t_modelos):
        try:
            t()
        except Exception as e:  # noqa: BLE001
            import traceback
            traceback.print_exc()
            FALHAS.append(f"{t.__name__}: {e}")
    print(f"\n{'TUDO OK' if not FALHAS else str(len(FALHAS)) + ' FALHA(S): ' + '; '.join(FALHAS)}  (dados em {TMP})")
    sys.exit(1 if FALHAS else 0)
