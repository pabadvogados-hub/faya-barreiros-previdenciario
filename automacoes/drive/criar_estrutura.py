# -*- coding: utf-8 -*-
"""Cria a estrutura de pastas do escritorio no OneDrive (ESTRUTURA_PASTAS.md). Idempotente: pasta
que ja existe e reaproveitada, nunca duplicada. Nada e apagado nem movido.

Subcomandos:
  base             [--ano 2026]                00_ESCRITORIO/*, FINANCEIRO/<ano>/<01..12>/*, CLIENTES,
                                               DEMANDAS_EXTERNAS_CALCULO
  cliente          --id ID | --todos           CLIENTES/<NOME>/00_CONTRATACAO ... 99_A_CLASSIFICAR + processos
  processo         --cliente ID --numero N [--parte INSS] [--tipo T]
  demanda-externa  --parceiro "Dr. Fulano" --caso "Revisao Joao" [--recebida AAAA-MM-DD] [--prazo AAAA-MM-DD]
                                               DEMANDAS_EXTERNAS_CALCULO/<PARCEIRO>/<AAAA-MM-DD - CASO>/01..04
                                               + tarefa [CALCULO EXTERNO] no Notion com o prazo de entrega
  docs                                         copia pops/, checklists/, mensagens/ e modelos/ para 00_ESCRITORIO
                                               (nao sobrescreve arquivo com o mesmo nome e conteudo)

Opcoes: --offline mostra o plano sem tocar no disco; --go cria de verdade.
Raiz: ONEDRIVE_RAIZ em config/.env (pasta sincronizada pelo OneDrive; na VPS, a montagem do rclone).

Uso:
    python automacoes/drive/criar_estrutura.py base --offline
    python automacoes/drive/criar_estrutura.py base --go
    python automacoes/drive/criar_estrutura.py cliente --todos --go
    python automacoes/drive/criar_estrutura.py demanda-externa --parceiro "Dr. Fulano de Tal" --caso "Revisao da vida toda - Joao" --prazo 2026-12-10 --go
"""
from __future__ import annotations

import argparse
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from comum import db, drive, notion  # noqa: E402
from comum.cadastros import cliente_por_id, lista_clientes, parceiro_por_id  # noqa: E402
from comum.config import RAIZ, add_modo, banner, bloquear_exemplo, escritorio, hoje, utf8_stdout  # noqa: E402
from comum.estrutura import (E, caminho_cliente, caminho_demanda_externa, caminho_processo,  # noqa: E402
                             subpastas_cliente)


def _arvore(prefixo: list[str], no: dict) -> list[list[str]]:
    out = []
    for nome, filhos in no.items():
        out.append(prefixo + [nome])
        out += _arvore(prefixo + [nome], filhos or {})
    return out


def plano_base(ano: int) -> list[list[str]]:
    p = _arvore([], E["raiz"])
    p.append(["FINANCEIRO", str(ano)])
    for mes in range(1, 13):
        p.append(["FINANCEIRO", str(ano), f"{mes:02d}"])
        p += [["FINANCEIRO", str(ano), f"{mes:02d}", s] for s in E["financeiro_mes"]]
    p += [["00_ESCRITORIO", "CONTROLADORIA", str(ano)]]
    return p


def plano_cliente(c: dict) -> list[list[str]]:
    base = caminho_cliente(c)
    p = [base] + [base + s for s in subpastas_cliente(c)]
    for proc in c.get("processos") or []:
        if proc.get("numero"):
            p.append(caminho_processo(c, proc))
    return p


def plano_demanda_externa(parceiro, dem: dict) -> list[list[str]]:
    cd = caminho_demanda_externa(parceiro, dem)
    return [cd[:2], cd] + [cd + [s] for s in E["demanda_externa"]]


def aplicar(plano: list[list[str]], executar: bool, offline: bool):
    vistos = set()
    plano = [p for p in plano if not (tuple(p) in vistos or vistos.add(tuple(p)))]
    if offline:
        for p in plano:
            print("  " + "    " * (len(p) - 1) + p[-1] + "/")
        print(f"\n{len(plano)} pastas no plano (offline: nada foi consultado no disco).")
        return
    svc = drive.servico()
    for p in plano:
        drive.garantir_caminho(svc, None, p, executar=executar, log=print)
    print(f"\n{len(plano)} pastas conferidas em {svc}.")


def docs(executar: bool, offline: bool):
    pares = [("pops", ["00_ESCRITORIO", "POPS"]), ("checklists", ["00_ESCRITORIO", "CHECKLISTS"]),
             ("mensagens", ["00_ESCRITORIO", "MENSAGENS"]), ("modelos", ["00_ESCRITORIO", "MODELOS"])]
    svc = None if offline else drive.servico()
    for pasta_local, destino in pares:
        if not (RAIZ / pasta_local).is_dir():
            continue
        for arq in sorted((RAIZ / pasta_local).rglob("*.md")):
            rel = arq.relative_to(RAIZ / pasta_local)
            alvo = destino + list(rel.parent.parts)
            print(f"  {pasta_local}/{rel.as_posix()} -> {'/'.join(alvo)}/")
            if svc:
                pid = drive.garantir_caminho(svc, None, alvo, executar=executar, log=None)
                drive.enviar_arquivo(svc, arq, pid, executar=executar)


def _util_antes(d: date, n: int) -> date:
    while n > 0:
        d -= timedelta(days=1)
        if d.weekday() < 5:
            n -= 1
    return d


def tarefa_demanda_externa(parceiro: str, caso: str, prazo: str | None, pasta: str, cfg: dict, executar: bool) -> dict:
    """Prazo da demanda externa e INEGOCIAVEL: a tarefa sai com prazo interno = entrega - 2 dias uteis
    e prazo fatal = a data de entrega combinada com o parceiro. Sem prazo -> tarefa para HOJE
    'definir prazo com o parceiro' (nunca fica demanda sem data)."""
    n = cfg.get("notion") or {}
    quem = (n.get("responsaveis") or {}).get("calculos")
    tipo = (n.get("tipos_tarefa") or {}).get("calculo_externo") or (n.get("tipos_tarefa") or {}).get("prazo")
    if prazo:
        fatal = date.fromisoformat(prazo)
        interno = max(_util_antes(fatal, 2), hoje())   # POP-PREV-06: parceiro - 2 dias uteis
        titulo = f"[CALCULO EXTERNO] {caso} - {parceiro} - entrega {fatal.strftime('%d/%m/%Y')}"
        texto = (f"{titulo}\n\nDemanda externa de calculo para o(a) advogado(a) parceiro(a) {parceiro}.\n"
                 f"Entrega combinada: {fatal.strftime('%d/%m/%Y')} (prazo fatal). Prazo interno: "
                 f"{interno.strftime('%d/%m/%Y')}.\nPasta no OneDrive: {pasta}\n"
                 "Entregou: mover o arquivo final para 03_ENTREGUE e preencher entregue_em em clientes.json.")
        return notion.criar_tarefa(None, tipo, [quem] if quem else [], None, texto, start_date=hoje().isoformat(),
                                   end_date=interno.isoformat(), date_deadline=fatal.isoformat(),
                                   urgent=(fatal - hoje()).days <= 3, executar=executar)
    titulo = f"[CALCULO EXTERNO] DEFINIR PRAZO - {caso} - {parceiro}"
    texto = f"{titulo}\n\nDemanda recebida sem prazo de entrega. Combinar a data com o parceiro hoje.\nPasta: {pasta}"
    return notion.criar_tarefa(None, tipo, [quem] if quem else [], None, texto, start_date=hoje().isoformat(),
                               date_deadline=hoje().isoformat(), urgent=True, executar=executar)


def main():
    utf8_stdout()
    ap = argparse.ArgumentParser(description="Estrutura de pastas do escritorio no OneDrive")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = add_modo(sub.add_parser("base"))
    s.add_argument("--ano", type=int, default=date.today().year)
    s = add_modo(sub.add_parser("cliente"))
    s.add_argument("--id")
    s.add_argument("--todos", action="store_true")
    s = add_modo(sub.add_parser("processo"))
    s.add_argument("--cliente", required=True)
    s.add_argument("--numero", required=True)
    s.add_argument("--parte", default="INSS")
    s.add_argument("--tipo", default="")
    s = add_modo(sub.add_parser("demanda-externa"))
    s.add_argument("--parceiro", required=True, help="id em clientes.json -> parceiros, ou o nome do advogado")
    s.add_argument("--caso", required=True)
    s.add_argument("--recebida", default=date.today().isoformat())
    s.add_argument("--prazo", default="", help="data de entrega combinada (AAAA-MM-DD)")
    add_modo(sub.add_parser("docs"))
    for p in sub.choices.values():
        p.add_argument("--offline", action="store_true", help="so mostra o plano")
    a = ap.parse_args()
    banner(a.go, f"OneDrive: {a.cmd}")
    cfg = escritorio()
    bloquear_exemplo(cfg, "escritorio", a.go)
    offline = a.offline or not drive.credenciais_disponiveis()
    if offline and not a.offline:
        print("  ONEDRIVE_RAIZ nao definida ou pasta inexistente: mostrando so o plano.")
        if a.go:
            raise SystemExit("ERRO: --go precisa de ONEDRIVE_RAIZ (config/.env) apontando para a pasta sincronizada.")

    if a.cmd == "base":
        plano = plano_base(a.ano)
    elif a.cmd == "cliente":
        alvos = lista_clientes() if a.todos else [cliente_por_id(a.id)]
        if not all(alvos):
            raise SystemExit(f"cliente {a.id} nao esta em config/clientes.json")
        plano = [p for c in alvos for p in plano_cliente(c)]
    elif a.cmd == "processo":
        c = cliente_por_id(a.cliente) or {"nome": a.cliente}
        plano = [caminho_processo(c, {"numero": a.numero, "parte_contraria": a.parte, "tipo_acao": a.tipo})]
    elif a.cmd == "demanda-externa":
        parceiro = parceiro_por_id(a.parceiro) or {"nome": a.parceiro}
        dem = {"caso": a.caso, "recebida_em": a.recebida, "prazo_entrega": a.prazo}
        plano = plano_demanda_externa(parceiro, dem)
        aplicar(plano, a.go, offline)
        pasta = "/".join(caminho_demanda_externa(parceiro, dem))
        con = db.conectar()
        chave = f"{parceiro.get('id') or parceiro.get('nome')}|{pasta}"
        if db.ja_existe(con, "demandas_externas", chave=chave):
            print(f"  Tarefa da demanda ja criada antes ({chave}).")
        else:
            r = tarefa_demanda_externa(parceiro.get("nome") or a.parceiro, a.caso, a.prazo or None, pasta, cfg, a.go)
            print("  Notion:", r)
            if a.go and isinstance(r, dict) and not r.get("erro") and not r.get("_dry_run"):
                db.gravar(con, "demandas_externas", chave=chave, parceiro=parceiro.get("nome") or a.parceiro,
                          caso=a.caso, prazo_entrega=a.prazo, pasta=pasta, tarefa=str(r.get("id")))
            elif a.go and isinstance(r, dict) and r.get("erro"):
                print("  ! TAREFA NAO CRIADA NO NOTION: lance a mao, com o prazo de entrega.")
        print("  Lembrete: registre a demanda em clientes.json -> parceiros[].demandas (roteia os documentos).")
        return
    else:
        docs(a.go, offline)
        return
    aplicar(plano, a.go, offline)


if __name__ == "__main__":
    main()
