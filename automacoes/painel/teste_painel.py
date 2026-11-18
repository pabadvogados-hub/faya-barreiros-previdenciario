# -*- coding: utf-8 -*-
"""Teste offline do painel: sobe o servidor numa porta livre, com banco e OneDrive temporários.

    python automacoes/painel/teste_painel.py
"""
from __future__ import annotations

import base64
import json
import os
import shutil
import sys
import tempfile
import threading
import urllib.error
import urllib.request
import uuid
from datetime import date, timedelta
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
sys.path.insert(0, str(AQUI.parent))

TMP = Path(tempfile.mkdtemp(prefix="painel_teste_"))
os.environ["ONEDRIVE_RAIZ"] = str(TMP / "onedrive")
os.environ["ESCRITORIO_HOJE"] = "2026-11-18"          # quarta-feira
for k in ("ASAAS_API_KEY", "NOTION_TOKEN", "PAINEL_TAREFA_NOTION", "PAINEL_PERMITE_COBRANCA"):
    os.environ.pop(k, None)

import servidor as s  # noqa: E402
from http.server import ThreadingHTTPServer  # noqa: E402

FALHAS = []


def chk(nome, cond, extra=""):
    print(("  [ok] " if cond else "  [FALHOU] ") + nome + (f" -> {extra}" if extra and not cond else ""))
    if not cond:
        FALHAS.append(nome)


def req(url, metodo="GET", corpo=None, cab=None, auth=True):
    cab = dict(cab or {})
    if auth:
        cab["Authorization"] = "Basic " + base64.b64encode(b"faya:senha-teste").decode()
    r = urllib.request.Request(url, data=corpo, method=metodo, headers=cab)
    try:
        with urllib.request.urlopen(r, timeout=10) as resp:
            txt = resp.read().decode("utf-8")
            return resp.status, (json.loads(txt) if resp.headers.get_content_type() == "application/json" else txt)
    except urllib.error.HTTPError as e:
        txt = e.read().decode("utf-8", "replace")
        try:
            return e.code, json.loads(txt)
        except ValueError:
            return e.code, txt


def multipart(campos: dict, arquivos: list[tuple[str, bytes]]):
    b = uuid.uuid4().hex
    partes = []
    for k, v in campos.items():
        partes.append(f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode())
    for nome, dados in arquivos:
        partes.append(f'--{b}\r\nContent-Disposition: form-data; name="arquivos"; filename="{nome}"\r\n'
                      f'Content-Type: application/octet-stream\r\n\r\n'.encode() + dados + b"\r\n")
    partes.append(f"--{b}--\r\n".encode())
    return b"".join(partes), {"Content-Type": f"multipart/form-data; boundary={b}"}


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    print("# prazo")
    fer = set()
    chk("interno = fatal - 2 dias úteis (sex -> qua)", s.calcular_prazo_interno("2026-11-27", fer) == "2026-11-25")
    chk("interno pula fim de semana (ter -> sex)", s.calcular_prazo_interno("2026-11-24", fer) == "2026-11-20")
    chk("feriado conta como não útil", s.calcular_prazo_interno("2026-11-24", {"2026-11-20"}) == "2026-11-19")

    app = s.App(s.Banco(TMP / "t.db"), "faya", "senha-teste", "tok-teste")
    srv = ThreadingHTTPServer(("127.0.0.1", 0), s.fabricar_handler(app))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{srv.server_address[1]}"
    try:
        print("# acesso")
        st, _ = req(base + "/painel", auth=False)
        chk("painel sem senha = 401", st == 401)
        st, html = req(base + "/painel")
        chk("painel com senha abre", st == 200 and "Cálculos para advogados parceiros" in html)
        st, _ = req(base + "/pedido?t=errado", auth=False)
        chk("link com token errado = 403", st == 403)
        st, html = req(base + "/pedido?t=tok-teste", auth=False)
        chk("link do parceiro abre sem senha", st == 200 and "Pedido de cálculo" in html)

        print("# pedido do parceiro")
        prazo = "2026-11-27"
        corpo, cab = multipart({"parceiro_nome": "Dr. Parceiro Teste", "parceiro_email": "p@exemplo.com",
                                "tipo": s.TIPOS[0], "caso": "Liquidação teste", "prazo_parceiro": prazo,
                                "processo": "0000000-00.0000.0.00.0000"},
                               [("sentença.pdf", b"%PDF-1.4 teste"), ("virus.exe", b"MZ")])
        st, r = req(base + "/api/pedido?t=tok-teste", "POST", corpo, cab, auth=False)
        chk("pedido aceito com protocolo", st == 201 and r.get("protocolo", "").startswith("CE-2026-"), r)
        chk("só a extensão permitida foi salva", r.get("arquivos") == 1, r)
        salvos = list((TMP / "onedrive" / "DEMANDAS_EXTERNAS_CALCULO").rglob("*.pdf"))
        chk("arquivo na pasta do OneDrive (01_RECEBIDO_DO_PARCEIRO)",
            len(salvos) == 1 and salvos[0].parent.name == "01_RECEBIDO_DO_PARCEIRO", salvos)
        corpo, cab = multipart({"parceiro_nome": "X", "tipo": s.TIPOS[0]}, [])
        st, r = req(base + "/api/pedido?t=tok-teste", "POST", corpo, cab, auth=False)
        chk("pedido sem campo obrigatório = 400", st == 400, r)
        st, _ = req(base + "/api/demandas", auth=False)
        chk("lista de demandas exige senha", st == 401)

        print("# painel")
        st, r = req(base + "/api/demandas", "POST", json.dumps({
            "parceiro_nome": "Dra. Parceira Dois", "tipo": s.TIPOS[2], "caso": "Revisão atrasada",
            "prazo_parceiro": "2026-11-17", "valor": "400"}).encode(), {"Content-Type": "application/json"})
        chk("demanda manual criada", st == 201 and r.get("_sit") == "atrasada", r)
        atrasada = r["id"]
        st, r = req(base + "/api/demandas")
        dem = {d["caso"]: d for d in r["demandas"]}
        chk("prazo interno gravado", dem["Liquidação teste"]["prazo_interno"] == "2026-11-25")
        chk("semáforo 'no prazo' / 'atenção'", dem["Liquidação teste"]["_sit"] in ("ok", "atencao"))
        st, r = req(base + f"/api/demandas/{atrasada}", "POST",
                    json.dumps({"status": "ENTREGUE", "pago": True}).encode(), {"Content-Type": "application/json"})
        chk("entregue + pago grava datas", r.get("entregue_em") == "2026-11-18" and r.get("pago_em") == "2026-11-18", r)
        chk("histórico registra a mudança", any("status" in h["o_que"] for h in r.get("historico", [])))
        st, r = req(base + f"/api/demandas/{atrasada}", "POST", json.dumps({"status": "INVENTADO"}).encode(),
                    {"Content-Type": "application/json"})
        chk("status inválido = 400", st == 400)
        st, r = req(base + "/api/resumo")
        chk("resumo: 1 em andamento, 1 entregue no mês, R$ 400 recebido",
            r["em_andamento"] == 1 and r["entregues_mes"] == 1 and r["recebido_mes"] == 400.0, r)
        chk("resumo por parceiro", {p["nome"] for p in r["parceiros"]} == {"Dr. Parceiro Teste", "Dra. Parceira Dois"})
        st, r = req(base + f"/api/demandas/{atrasada}/cobrar", "POST", b"{}", {"Content-Type": "application/json"})
        chk("cobrança sem CPF/CNPJ é recusada com mensagem", "erro" in r, r)

        print("# exemplo")
        app2 = s.App(s.Banco(TMP / "ex.db"), "faya", "x", "y")
        s.semear_exemplo(app2)
        res = s.resumo(app2.linhas())
        chk("dados de exemplo geram painel cheio", res["em_andamento"] == 6 and res["entregues_mes"] == 3, res)
    finally:
        srv.shutdown()
        shutil.rmtree(TMP, ignore_errors=True)

    print("\nTUDO OK" if not FALHAS else f"\n{len(FALHAS)} FALHA(S): {FALHAS}")
    sys.exit(1 if FALHAS else 0)


if __name__ == "__main__":
    main()
