# -*- coding: utf-8 -*-
"""Documento recebido (e-mail, WhatsApp, entregue em mao) -> pasta certa no OneDrive + tarefa no Notion.

Regra de ouro: o documento mora no OneDrive; no Notion vai so o CAMINHO (relativo a raiz do
OneDrive) dentro da tarefa.

COMO O DOCUMENTO CHEGA: o escritorio nao tem CRM de WhatsApp com API. A Barbara salva o anexo
(do e-mail ou do WhatsApp) numa pasta local e roda este script dizendo de quem e: --cliente <id>,
--parceiro <id>, --telefone ou --email. Varios arquivos de uma vez: --arquivo a.pdf b.jpg c.pdf.

ROTEAMENTO (na ordem; funcao pura `rotear`, testavel offline):
  1. Ninguem identificado -> 00_ESCRITORIO/ENTRADA_DOCUMENTOS + tarefa de triagem.
  2. Advogado PARCEIRO (demanda externa de calculo, config/clientes.json -> parceiros):
       palavra-chave/caso de uma demanda aberta, ou a unica demanda aberta
         -> DEMANDAS_EXTERNAS_CALCULO/<PARCEIRO>/<AAAA-MM-DD - CASO>/01_RECEBIDO_DO_PARCEIRO
       senao -> DEMANDAS_EXTERNAS_CALCULO/<PARCEIRO>/99_A_CLASSIFICAR
  3. Cliente, numero CNJ na legenda ou no nome do arquivo
         -> CLIENTES/<CLIENTE>/08_PROCESSO_JUDICIAL/<CNJ - PARTE - TIPO>
  4. Cliente, palavra-chave do tipo de documento (estrutura_pastas.json -> palavras_chave, em ordem):
         PPP/LTCAT -> 03_PROVAS_ESPECIAIS; CNIS/CTPS/carne -> 02_CNIS_E_VINCULOS;
         contrato/procuracao/declaracao/renuncia -> 00_CONTRATACAO; laudo/exame/atestado -> 04_SAUDE;
         requerimento/indeferimento/carta de concessao -> 05_INSS_ADMINISTRATIVO; calculo -> 06_CALCULOS;
         comprovante/boleto/recibo -> 09_FINANCEIRO; RG/CPF/certidao/comprovante de residencia -> 01_DOCUMENTOS_PESSOAIS
  5. Fora disso -> CLIENTES/<CLIENTE>/99_A_CLASSIFICAR (tarefa "classificar documento").
  Nunca chuta entre dois cadastros.

TAREFA NO NOTION: "[DOCUMENTO] Documento recebido - <quem> - <pasta>", com o caminho no OneDrive,
prazo de 1 dia util, ligada ao processo do cliente quando ha `notion_page_id` no cadastro.
Demanda externa: "[CALCULO EXTERNO] Documento recebido - ..." (o prazo da demanda e sagrado).

Idempotente por hash do arquivo (tabela documentos_recebidos). Dry-run por padrao.

Uso:
    python automacoes/drive/arquivar_documento.py --arquivo laudo.pdf --cliente maria-souza --legenda "laudo do ortopedista"
    python automacoes/drive/arquivar_documento.py --arquivo cnis.pdf ctps.jpg --telefone 71999999999 --go
    python automacoes/drive/arquivar_documento.py --arquivo docs.zip --parceiro dr-fulano --legenda "caso Joao - revisao" --go
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from datetime import timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from comum import db, drive, notion  # noqa: E402
from comum.cadastros import (cliente_por_email, cliente_por_id, cliente_por_telefone, demandas_abertas,  # noqa: E402
                             parceiro_por_email, parceiro_por_id, parceiro_por_telefone)
from comum.config import add_modo, banner, bloquear_exemplo, escritorio, hoje, utf8_stdout  # noqa: E402
from comum.estrutura import (E, caminho_cliente, caminho_demanda_externa, caminho_parceiro,  # noqa: E402
                             caminho_processo, palavras_chave)
from comum.nomes import achar_cnj, nome_arquivo, sem_acento  # noqa: E402


def _n(s: str) -> str:
    """minusculo, sem acento, so letras/numeros separados por espaco (o _ e o - do nome do arquivo viram espaco)."""
    return re.sub(r"[^a-z0-9]+", " ", sem_acento(s).lower()).strip()


def _tem(chave: str, texto: str) -> bool:
    k = _n(chave)
    return bool(k) and re.search(r"(?:^| )" + re.escape(k) + r"(?: |$)", texto) is not None


def _processo_unico_notion(cliente: dict) -> str | None:
    ids = [p.get("notion_page_id") for p in cliente.get("processos") or [] if p.get("notion_page_id")]
    return ids[0] if len(ids) == 1 else None


def rotear(cliente: dict | None, legenda: str, nome_original: str, parceiro: dict | None = None) -> dict:
    """Devolve {caminho, contexto, processo_id, area, motivo, subpasta}. Funcao pura."""
    texto = _n(f"{legenda} {nome_original}")
    if parceiro:
        abertas = demandas_abertas(parceiro)
        for d in abertas:
            chaves = list(d.get("palavras_chave") or []) + [d.get("caso", "")]
            if any(_tem(k, texto) for k in chaves if k):
                return {"caminho": caminho_demanda_externa(parceiro, d) + [E["demanda_externa"][0]],
                        "contexto": d.get("caso"), "processo_id": None, "area": "calculos",
                        "motivo": "palavra-chave da demanda externa", "subpasta": E["demanda_externa"][0],
                        "demanda": d}
        if len(abertas) == 1:
            d = abertas[0]
            return {"caminho": caminho_demanda_externa(parceiro, d) + [E["demanda_externa"][0]],
                    "contexto": d.get("caso"), "processo_id": None, "area": "calculos",
                    "motivo": "parceiro com uma unica demanda aberta", "subpasta": E["demanda_externa"][0],
                    "demanda": d}
        return {"caminho": caminho_parceiro(parceiro) + [E["a_classificar"]], "contexto": "demanda nao identificada",
                "processo_id": None, "area": "calculos", "motivo": "parceiro sem demanda identificavel",
                "subpasta": E["a_classificar"]}
    if not cliente:
        return {"caminho": ["00_ESCRITORIO", "ENTRADA_DOCUMENTOS"], "contexto": "remetente nao cadastrado",
                "processo_id": None, "area": "atendimento", "motivo": "remetente sem cadastro",
                "subpasta": "ENTRADA_DOCUMENTOS"}
    cnj = achar_cnj(f"{legenda} {nome_original}")
    if cnj:
        alvo = re.sub(r"\D", "", cnj)
        for p in cliente.get("processos") or []:
            if re.sub(r"\D", "", str(p.get("numero"))) == alvo:
                return {"caminho": caminho_processo(cliente, p), "contexto": cnj,
                        "processo_id": p.get("notion_page_id") or None, "area": p.get("area") or "previdenciario",
                        "motivo": "numero do processo na legenda", "subpasta": E["pasta_processos"]}
        return {"caminho": caminho_processo(cliente, {"numero": cnj}), "contexto": cnj, "processo_id": None,
                "area": "previdenciario", "subpasta": E["pasta_processos"],
                "motivo": "numero CNJ na legenda, processo ainda nao cadastrado em clientes.json"}
    for sub, chaves in palavras_chave():
        achada = next((k for k in chaves if _tem(k, texto)), None)
        if achada:
            return {"caminho": caminho_cliente(cliente) + [sub], "contexto": sub, "subpasta": sub,
                    "processo_id": _processo_unico_notion(cliente),
                    "area": "calculos" if sub == "06_CALCULOS" else ("financeiro" if sub == "09_FINANCEIRO"
                                                                     else "atendimento"),
                    "motivo": f"palavra-chave '{achada}'"}
    return {"caminho": caminho_cliente(cliente) + [E["a_classificar"]], "contexto": "a classificar",
            "processo_id": _processo_unico_notion(cliente), "area": "atendimento",
            "motivo": "sem pista do tipo de documento", "subpasta": E["a_classificar"]}


def _proximo_dia_util(n: int = 1):
    d = hoje()
    while n > 0:
        d += timedelta(days=1)
        if d.weekday() < 5:
            n -= 1
    return d


def _tipo_arquivo(subpasta: str) -> str:
    base = re.sub(r"^\d+_", "", subpasta or "")
    return {"A_CLASSIFICAR": "DOC-CLIENTE", "ENTRADA_DOCUMENTOS": "DOC-RECEBIDO",
            "RECEBIDO_DO_PARCEIRO": "DOC-PARCEIRO", "PROCESSO_JUDICIAL": "PROCESSO"}.get(base, base[:30] or "DOC")


def identificar(cliente_id: str = "", parceiro_id: str = "", telefone: str = "", email: str = "") -> tuple:
    """(cliente, parceiro). Cliente e parceiro com o mesmo telefone/e-mail -> ambiguo: nenhum (vai para a triagem)."""
    if cliente_id:
        c = cliente_por_id(cliente_id)
        if not c:
            raise SystemExit(f"cliente {cliente_id} nao esta em config/clientes.json")
        return c, None
    if parceiro_id:
        p = parceiro_por_id(parceiro_id)
        if not p:
            raise SystemExit(f"parceiro {parceiro_id} nao esta em config/clientes.json -> parceiros")
        return None, p
    c = cliente_por_telefone(telefone) if telefone else cliente_por_email(email)
    p = parceiro_por_telefone(telefone) if telefone else parceiro_por_email(email)
    if c and p:
        print("  AVISO: telefone/e-mail cadastrado como cliente E como parceiro: vai para a triagem.")
        return None, None
    return c, p


def arquivar(arquivo: str | Path, legenda: str = "", cliente: dict | None = None, parceiro: dict | None = None,
             remetente: str = "", executar: bool = False, cfg: dict | None = None) -> dict:
    cfg = cfg or escritorio()
    local = Path(arquivo)
    h = hashlib.sha256(local.read_bytes()).hexdigest()
    con = db.conectar()
    if db.ja_existe(con, "documentos_recebidos", hash=h):
        return {"ja_arquivado": True, "hash": h, "arquivo": local.name}
    rota = rotear(cliente, legenda, local.name, parceiro)
    nome = nome_arquivo(_tipo_arquivo(rota["subpasta"]), legenda or local.stem, local.suffix, quando=hoje())
    quem_e = (cliente or {}).get("nome") or (parceiro or {}).get("nome") or remetente or "remetente nao identificado"
    res = {"de": quem_e, "destino": "/".join(rota["caminho"]), "nome": nome, "motivo": rota["motivo"], "hash": h}

    if drive.credenciais_disponiveis():
        svc = drive.servico()
        pasta = drive.garantir_caminho(svc, None, rota["caminho"], executar=executar, log=None)
        f = drive.enviar_arquivo(svc, local, pasta, nome, executar=executar)
        res["onedrive"] = f
        caminho = f.get("link") or f.get("destino") or ""
    else:
        res["onedrive"] = "ONEDRIVE_RAIZ indisponivel: arquivo NAO copiado"
        caminho = ""
        if executar:
            res["tarefa"] = {"erro": "arquivo nao copiado; tarefa nao criada"}
            return res

    n = cfg.get("notion") or {}
    resp = n.get("responsaveis") or {}
    tipos = n.get("tipos_tarefa") or {}
    quem = resp.get(rota.get("area") or "") or resp.get("atendimento")
    prazo = _proximo_dia_util(1)
    externo = bool(parceiro)
    rotulo = "[CALCULO EXTERNO]" if externo else "[DOCUMENTO]"
    titulo = f"{rotulo} Documento recebido - {quem_e} - {rota['contexto']}"
    classificar = rota["subpasta"] in (E["a_classificar"], "ENTRADA_DOCUMENTOS")
    comentario = (f"{titulo}\n\nArquivo: {nome}\nPasta no OneDrive: {res['destino']}\nCaminho: {caminho or '(dry-run)'}\n"
                  f"Legenda/observacao: {legenda or '-'}\nRoteamento: {rota['motivo']}\n"
                  + (f"Prazo de entrega da demanda: {(rota.get('demanda') or {}).get('prazo_entrega') or '[sem prazo cadastrado]'}\n"
                     if externo else "")
                  + ("Conferir e mover para a subpasta certa.\n" if classificar else ""))
    res["tarefa"] = notion.criar_tarefa(rota["processo_id"],
                                        tipos.get("calculo_externo" if externo else "documento_recebido"),
                                        [quem] if quem else [], None, comentario,
                                        start_date=hoje().isoformat(), date_deadline=prazo.isoformat(),
                                        executar=executar)
    if executar and isinstance(res["onedrive"], dict) and not res["onedrive"].get("_dry_run"):
        db.gravar(con, "documentos_recebidos", hash=h, cliente=quem_e, destino=res["destino"],
                  drive_id=caminho, tarefa=str(res["tarefa"])[:200])
    return res


def main():
    utf8_stdout()
    ap = add_modo(argparse.ArgumentParser(description="Arquiva documento recebido no OneDrive + tarefa no Notion"))
    ap.add_argument("--arquivo", nargs="+", required=True, help="um ou mais arquivos")
    quem = ap.add_mutually_exclusive_group()
    quem.add_argument("--cliente", default="", help="id do cliente em config/clientes.json")
    quem.add_argument("--parceiro", default="", help="id do advogado parceiro (demanda externa de calculo)")
    quem.add_argument("--telefone", default="")
    quem.add_argument("--email", default="")
    ap.add_argument("--legenda", default="", help="o que o cliente escreveu / o que e o documento")
    a = ap.parse_args()
    banner(a.go, "Arquivar documento")
    cfg = escritorio()
    bloquear_exemplo(cfg, "escritorio", a.go)
    if a.go and not drive.credenciais_disponiveis():
        raise SystemExit("ERRO: --go precisa de ONEDRIVE_RAIZ (config/.env) apontando para a pasta sincronizada.")
    if not notion.configurado():
        print("  Notion nao configurado: a tarefa fica so no relatorio (lance a mao no Notion).")
    cliente, parceiro = identificar(a.cliente, a.parceiro, a.telefone, a.email)
    for arq in a.arquivo:
        print(f"\n{arq}")
        r = arquivar(arq, a.legenda, cliente, parceiro, remetente=a.telefone or a.email, executar=a.go, cfg=cfg)
        for k, v in r.items():
            print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
