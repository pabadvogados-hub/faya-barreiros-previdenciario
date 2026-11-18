# -*- coding: utf-8 -*-
"""Painel das DEMANDAS EXTERNAS DE CÁLCULO + link de pedido para advogados parceiros (POP-PREV-06).

    python automacoes/painel/servidor.py                 # sobe em http://127.0.0.1:8765
    python automacoes/painel/servidor.py --exemplo       # banco temporário com dados FICTÍCIOS (demonstração)
    python automacoes/painel/servidor.py --host 0.0.0.0 --porta 8765   # VPS (atrás de HTTPS: ver INSTALAR.md)

Rotas
    /painel                  painel da Dra. Faya e da Bárbara (usuário e senha: PAINEL_USUARIO / PAINEL_SENHA)
    /pedido?t=<token>        formulário do parceiro (token: PAINEL_TOKEN_PEDIDO). O link vai para os parceiros.
    /api/...                 JSON usado pelas duas páginas

O que acontece quando um parceiro manda um pedido:
    1. a demanda entra no banco local (dados/escritorio.db, tabela calculos_externos) com protocolo CE-AAAA-NNNN;
    2. os arquivos vão para DEMANDAS_EXTERNAS_CALCULO/<parceiro>/<AAAA-MM-DD - caso>/01_RECEBIDO_DO_PARCEIRO
       no OneDrive (ONEDRIVE_RAIZ). Sem OneDrive configurado, ficam em dados/demandas_externas/;
    3. se o Notion estiver configurado e PAINEL_TAREFA_NOTION=1, nasce a tarefa [CALCULO EXTERNO] com o prazo.

Prazo: o parceiro informa o prazo dele (fatal). O prazo interno é o fatal MENOS 2 DIAS ÚTEIS (POP-PREV-06).
Dinheiro: o painel registra valor e pagamento. Cobrança no Asaas só com PAINEL_PERMITE_COBRANCA=1 (senão, simula).
Sem dependência além da biblioteca padrão (o Asaas e o Notion usam os módulos de automacoes/comum).
"""
from __future__ import annotations

import argparse
import base64
import email.parser
import email.policy
import hmac
import json
import os
import re
import secrets
import shutil
import sqlite3
import sys
import tempfile
import unicodedata
from datetime import date, datetime, timedelta
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent))
from comum.config import DADOS_DIR, garantir_dir, utf8_stdout  # noqa: E402

TIPOS = [
    "Liquidação de sentença",
    "Conferência / impugnação de cálculo do INSS ou da contadoria",
    "Cálculo de RMI / revisão",
    "Contagem de tempo de contribuição",
    "Valor da causa",
    "Planejamento previdenciário",
    "Parecer técnico",
    "Outro",
]
STATUS = ["RECEBIDO", "DOCUMENTOS PENDENTES", "EM CÁLCULO", "CONFERÊNCIA", "ENTREGUE", "CANCELADO"]
ABERTOS = {"RECEBIDO", "DOCUMENTOS PENDENTES", "EM CÁLCULO", "CONFERÊNCIA"}
EXTENSOES = {".pdf", ".jpg", ".jpeg", ".png", ".docx", ".doc", ".xlsx", ".xls", ".csv", ".txt", ".zip"}
LIMITE_BYTES = 40 * 1024 * 1024
DIAS_UTEIS_ANTES = 2

SCHEMA = """
CREATE TABLE IF NOT EXISTS calculos_externos (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    protocolo        TEXT UNIQUE,
    origem           TEXT,           -- link | manual
    parceiro_nome    TEXT,
    parceiro_oab     TEXT,
    parceiro_email   TEXT,
    parceiro_whatsapp TEXT,
    parceiro_doc     TEXT,           -- CPF/CNPJ para cobrança (opcional)
    processo         TEXT,
    caso             TEXT,           -- descrição curta, sem dado sensível
    tipo             TEXT,
    prazo_parceiro   TEXT,           -- AAAA-MM-DD (fatal)
    prazo_interno    TEXT,           -- fatal - 2 dias úteis
    status           TEXT,
    valor            REAL,
    pago             INTEGER DEFAULT 0,
    pago_em          TEXT,
    entregue_em      TEXT,
    observacoes      TEXT,
    pasta            TEXT,
    arquivos         TEXT,           -- JSON
    tarefa           TEXT,
    cobranca         TEXT,
    historico        TEXT,           -- JSON [{em, o_que}]
    criado_em        TEXT
);
"""


# ------------------------------------------------------------------ datas e prazo

def hoje() -> date:
    v = os.getenv("ESCRITORIO_HOJE")
    return date.fromisoformat(v[:10]) if v else date.today()


def _feriados() -> set[str]:
    """Feriados nacionais (com Páscoa) + BA/Salvador, do motor de prazos da controladoria.
    Aqui contar feriado é o lado SEGURO: o prazo interno fica mais cedo."""
    try:
        from controladoria import prazos
    except Exception:
        return set()
    datas: set[str] = set()
    for ano in (hoje().year - 1, hoje().year, hoje().year + 1):
        try:
            datas.update(d.isoformat() if hasattr(d, "isoformat") else str(d)
                         for d in prazos.feriados_do_ano(ano, uf="BA", comarca="salvador"))
        except Exception:
            pass
    return datas


def util(d: date, feriados: set[str]) -> bool:
    return d.weekday() < 5 and d.isoformat() not in feriados


def menos_dias_uteis(d: date, n: int, feriados: set[str]) -> date:
    while n > 0:
        d -= timedelta(days=1)
        if util(d, feriados):
            n -= 1
    return d


def dias_uteis_ate(alvo: date, feriados: set[str]) -> int:
    """Dias úteis de hoje (exclusive) até alvo (inclusive). Negativo se já passou."""
    h = hoje()
    if alvo == h:
        return 0
    passo = 1 if alvo > h else -1
    n, d = 0, h
    while d != alvo:
        d += timedelta(days=passo)
        if util(d, feriados) or passo < 0:
            n += passo
    return n


def situacao(r: dict, feriados: set[str]) -> tuple[str, str]:
    """(código, texto) do semáforo."""
    if r["status"] == "ENTREGUE":
        return "entregue", "Entregue"
    if r["status"] == "CANCELADO":
        return "cancelado", "Cancelado"
    if not r.get("prazo_parceiro"):
        return "sem_prazo", "Sem prazo: combinar hoje"
    fatal = date.fromisoformat(r["prazo_parceiro"])
    interno = date.fromisoformat(r["prazo_interno"]) if r.get("prazo_interno") else fatal
    h = hoje()
    if h > fatal:
        return "atrasada", "Prazo do parceiro vencido"
    if h > interno:
        return "critica", "Passou do prazo interno"
    faltam = dias_uteis_ate(interno, feriados)
    if faltam <= 2:
        return "atencao", f"{faltam} dia(s) útil(eis) para o prazo interno"
    return "ok", f"{faltam} dias úteis para o prazo interno"


# ------------------------------------------------------------------ banco

class Banco:
    def __init__(self, caminho: Path):
        self.caminho = caminho
        garantir_dir(caminho.parent)
        with self._con() as con:
            con.executescript(SCHEMA)

    def _con(self):
        con = sqlite3.connect(str(self.caminho), timeout=10)
        con.row_factory = sqlite3.Row
        return con

    def novo_protocolo(self, con) -> str:
        ano = hoje().year
        n = con.execute("SELECT COUNT(*) FROM calculos_externos WHERE protocolo LIKE ?", (f"CE-{ano}-%",)).fetchone()[0]
        return f"CE-{ano}-{n + 1:04d}"

    def inserir(self, dados: dict) -> dict:
        with self._con() as con:
            dados = dict(dados)
            dados["protocolo"] = self.novo_protocolo(con)
            dados.setdefault("status", "RECEBIDO")
            dados.setdefault("criado_em", datetime.now().isoformat(timespec="seconds"))
            dados["historico"] = json.dumps([{"em": dados["criado_em"], "o_que": f"Recebida ({dados.get('origem', '')})"}],
                                            ensure_ascii=False)
            cols = ", ".join(dados)
            con.execute(f"INSERT INTO calculos_externos ({cols}) VALUES ({', '.join('?' for _ in dados)})",
                        tuple(dados.values()))
            rid = con.execute("SELECT last_insert_rowid()").fetchone()[0]
        return self.obter(rid)

    def obter(self, rid: int) -> dict | None:
        with self._con() as con:
            r = con.execute("SELECT * FROM calculos_externos WHERE id = ?", (rid,)).fetchone()
        return dict(r) if r else None

    def listar(self) -> list[dict]:
        with self._con() as con:
            return [dict(r) for r in con.execute("SELECT * FROM calculos_externos ORDER BY id DESC")]

    def atualizar(self, rid: int, campos: dict, o_que: str) -> dict | None:
        atual = self.obter(rid)
        if not atual:
            return None
        hist = json.loads(atual.get("historico") or "[]")
        hist.append({"em": datetime.now().isoformat(timespec="seconds"), "o_que": o_que})
        campos = dict(campos, historico=json.dumps(hist, ensure_ascii=False))
        with self._con() as con:
            con.execute(f"UPDATE calculos_externos SET {', '.join(f'{k} = ?' for k in campos)} WHERE id = ?",
                        (*campos.values(), rid))
        return self.obter(rid)


# ------------------------------------------------------------------ regras

def _slug(s: str, n: int = 60) -> str:
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode()
    s = re.sub(r"[^A-Za-z0-9 ._-]+", " ", s).strip()
    return re.sub(r"\s+", " ", s)[:n] or "sem nome"


def calcular_prazo_interno(prazo: str | None, feriados: set[str]) -> str | None:
    if not prazo:
        return None
    return menos_dias_uteis(date.fromisoformat(prazo), DIAS_UTEIS_ANTES, feriados).isoformat()


def pasta_da_demanda(dados: dict) -> Path:
    """OneDrive (ONEDRIVE_RAIZ) se configurado; senão dados/demandas_externas."""
    raiz = (os.getenv("ONEDRIVE_RAIZ") or "").strip().strip('"').strip("'")
    base = Path(raiz) / "DEMANDAS_EXTERNAS_CALCULO" if raiz else DADOS_DIR / "demandas_externas"
    nome_caso = f"{hoje().isoformat()} - {_slug(dados.get('caso') or dados.get('processo') or 'caso')}"
    return base / _slug(dados.get("parceiro_nome")).upper() / nome_caso / "01_RECEBIDO_DO_PARCEIRO"


def salvar_arquivos(pasta: Path, arquivos: list[tuple[str, bytes]]) -> list[str]:
    salvos = []
    pasta.mkdir(parents=True, exist_ok=True)
    for nome, conteudo in arquivos:
        base = _slug(Path(nome).stem, 80)
        ext = Path(nome).suffix.lower()
        if ext not in EXTENSOES:
            continue
        destino = pasta / f"{base}{ext}"
        i = 2
        while destino.exists():
            destino = pasta / f"{base} ({i}){ext}"
            i += 1
        destino.write_bytes(conteudo)
        salvos.append(destino.name)
    return salvos


def tarefa_notion(r: dict) -> str:
    if os.getenv("PAINEL_TAREFA_NOTION") != "1":
        return ""
    try:
        from comum import notion
        if not notion.configurado():
            return "notion não configurado"
        titulo = f"[CALCULO EXTERNO] {r['protocolo']} - {r.get('caso') or r.get('processo')} - {r['parceiro_nome']}"
        texto = (f"{titulo}\n\nTipo: {r.get('tipo')}\nProcesso: {r.get('processo') or '-'}\n"
                 f"Prazo do parceiro: {r.get('prazo_parceiro') or 'DEFINIR HOJE'}\nPrazo interno: {r.get('prazo_interno') or '-'}\n"
                 f"Pasta: {r.get('pasta')}")
        res = notion.criar_tarefa(None, None, [], None, texto, start_date=hoje().isoformat(),
                                  end_date=r.get("prazo_interno") or hoje().isoformat(),
                                  date_deadline=r.get("prazo_parceiro") or hoje().isoformat(),
                                  urgent=not r.get("prazo_parceiro"), executar=True)
        return json.dumps(res, ensure_ascii=False)[:500]
    except Exception as e:  # o pedido nunca se perde por causa do Notion
        return f"erro notion: {e}"


def cobrar_no_asaas(r: dict) -> dict:
    """Cria a cobrança do cálculo no Asaas (externalReference = protocolo). Simula sem PAINEL_PERMITE_COBRANCA=1."""
    from comum.asaas import AsaasCliente
    if not r.get("valor"):
        return {"erro": "informe o valor antes de cobrar"}
    if not r.get("parceiro_doc"):
        return {"erro": "informe o CPF/CNPJ do parceiro para emitir a cobrança"}
    executar = os.getenv("PAINEL_PERMITE_COBRANCA") == "1"
    if not os.getenv("ASAAS_API_KEY"):
        return {"erro": "ASAAS_API_KEY ausente em config/.env"}
    cli = AsaasCliente()
    cliente = cli.buscar_cliente(r["parceiro_doc"])
    if not cliente:
        if not executar:
            return {"_dry_run": True, "aviso": "parceiro ainda não existe no Asaas; seria criado"}
        cliente = cli.criar_cliente(r["parceiro_nome"], r["parceiro_doc"], email=r.get("parceiro_email"),
                                    telefone=r.get("parceiro_whatsapp"))
    venc = (hoje() + timedelta(days=5)).isoformat()
    cob, ja, erros = cli.criar_cobranca((cliente or {}).get("id"), r["valor"], venc,
                                        f"Cálculo previdenciário {r['protocolo']} - {r.get('tipo')}",
                                        r["protocolo"], tipo="UNDEFINED", executar=executar)
    return {"cobranca": cob, "ja_existia": ja, "erros": erros, "executado": executar}


def resumo(linhas: list[dict]) -> dict:
    h = hoje()
    mes = h.strftime("%Y-%m")
    abertos = [r for r in linhas if r["status"] in ABERTOS]
    entregues = [r for r in linhas if r["status"] == "ENTREGUE"]
    ent_mes = [r for r in entregues if (r.get("entregue_em") or "").startswith(mes)]
    pontuais = [r for r in entregues if r.get("prazo_parceiro") and r.get("entregue_em")
                and r["entregue_em"][:10] <= r["prazo_parceiro"]]
    por_tipo: dict[str, dict] = {}
    for r in entregues:
        t = por_tipo.setdefault(r.get("tipo") or "Outro", {"qtd": 0, "valor": 0.0, "dias": []})
        t["qtd"] += 1
        t["valor"] += float(r.get("valor") or 0)
        if r.get("entregue_em") and r.get("criado_em"):
            t["dias"].append((date.fromisoformat(r["entregue_em"][:10]) - date.fromisoformat(r["criado_em"][:10])).days)
    tipos = [{"tipo": k, "qtd": v["qtd"], "ticket": round(v["valor"] / v["qtd"], 2) if v["qtd"] else 0,
              "dias_medios": round(sum(v["dias"]) / len(v["dias"]), 1) if v["dias"] else None}
             for k, v in sorted(por_tipo.items(), key=lambda x: -x[1]["qtd"])]
    parceiros: dict[str, dict] = {}
    for r in linhas:
        if r["status"] == "CANCELADO":
            continue
        p = parceiros.setdefault(r["parceiro_nome"], {"qtd": 0, "valor": 0.0, "em_aberto": 0.0, "ativos": 0})
        p["qtd"] += 1
        p["valor"] += float(r.get("valor") or 0)
        if r["status"] == "ENTREGUE" and not r.get("pago"):
            p["em_aberto"] += float(r.get("valor") or 0)
        if r["status"] in ABERTOS:
            p["ativos"] += 1
    return {
        "hoje": h.isoformat(),
        "em_andamento": len(abertos),
        "atencao": sum(1 for r in abertos if r["_sit"] in ("atencao", "sem_prazo")),
        "atrasadas": sum(1 for r in abertos if r["_sit"] in ("critica", "atrasada")),
        "entregues_mes": len(ent_mes),
        "faturado_mes": round(sum(float(r.get("valor") or 0) for r in ent_mes), 2),
        "recebido_mes": round(sum(float(r.get("valor") or 0) for r in linhas
                                  if r.get("pago") and (r.get("pago_em") or "").startswith(mes)), 2),
        "a_receber": round(sum(float(r.get("valor") or 0) for r in entregues if not r.get("pago")), 2),
        "pontualidade": round(100 * len(pontuais) / len(entregues)) if entregues else None,
        "por_tipo": tipos,
        "parceiros": sorted([{"nome": k, **{kk: round(vv, 2) if isinstance(vv, float) else vv for kk, vv in v.items()}}
                             for k, v in parceiros.items()], key=lambda x: (-x["valor"], -x["qtd"])),
    }


# ------------------------------------------------------------------ HTTP

def _multipart(cabecalho: str, corpo: bytes) -> tuple[dict, list[tuple[str, bytes]]]:
    msg = email.parser.BytesParser(policy=email.policy.default).parsebytes(
        b"Content-Type: " + cabecalho.encode() + b"\r\n\r\n" + corpo)
    campos, arquivos = {}, []
    for parte in msg.iter_parts():
        nome = parte.get_param("name", header="content-disposition")
        arq = parte.get_filename()
        dados = parte.get_payload(decode=True) or b""
        if arq:
            if dados:
                arquivos.append((arq, dados))
        elif nome:
            campos[nome] = dados.decode("utf-8", "replace").strip()
    return campos, arquivos


class App:
    def __init__(self, banco: Banco, usuario: str, senha: str, token: str):
        self.banco, self.usuario, self.senha, self.token = banco, usuario, senha, token
        self.feriados = _feriados()

    def enriquecer(self, r: dict) -> dict:
        r = dict(r)
        r["_sit"], r["_sit_texto"] = situacao(r, self.feriados)
        r["arquivos"] = json.loads(r.get("arquivos") or "[]")
        r["historico"] = json.loads(r.get("historico") or "[]")
        return r

    def linhas(self) -> list[dict]:
        return [self.enriquecer(r) for r in self.banco.listar()]

    def criar(self, campos: dict, arquivos: list[tuple[str, bytes]], origem: str) -> dict:
        obrig = ["parceiro_nome", "tipo", "caso"]
        faltam = [c for c in obrig if not campos.get(c)]
        if faltam:
            raise ValueError("faltam: " + ", ".join(faltam))
        prazo = campos.get("prazo_parceiro") or None
        if prazo:
            date.fromisoformat(prazo)
        dados = {k: (campos.get(k) or "").strip()[:500] for k in
                 ("parceiro_nome", "parceiro_oab", "parceiro_email", "parceiro_whatsapp", "parceiro_doc",
                  "processo", "caso", "tipo", "observacoes")}
        dados.update(origem=origem, prazo_parceiro=prazo, prazo_interno=calcular_prazo_interno(prazo, self.feriados))
        if campos.get("valor"):
            dados["valor"] = float(str(campos["valor"]).replace(".", "").replace(",", ".")) \
                if "," in str(campos["valor"]) else float(campos["valor"])
        pasta = pasta_da_demanda(dados)
        dados["pasta"] = str(pasta.parent)
        dados["arquivos"] = json.dumps(salvar_arquivos(pasta, arquivos) if arquivos else [], ensure_ascii=False)
        if not arquivos:
            pasta.mkdir(parents=True, exist_ok=True)
        r = self.banco.inserir(dados)
        tarefa = tarefa_notion(r)
        if tarefa:
            r = self.banco.atualizar(r["id"], {"tarefa": tarefa}, "Tarefa no Notion")
        return self.enriquecer(r)

    def editar(self, rid: int, campos: dict) -> dict | None:
        atual = self.banco.obter(rid)
        if not atual:
            return None
        muda, partes = {}, []
        for k in ("status", "valor", "pago", "observacoes", "prazo_parceiro", "parceiro_doc", "processo", "caso", "tipo"):
            if k not in campos:
                continue
            v = campos[k]
            if k == "status" and v not in STATUS:
                raise ValueError("status inválido")
            if k == "valor":
                v = float(v) if v not in ("", None) else None
            if k == "pago":
                v = 1 if v in (True, 1, "1", "true", "sim") else 0
            if k == "prazo_parceiro":
                v = v or None
                if v:
                    date.fromisoformat(v)
                muda["prazo_interno"] = calcular_prazo_interno(v, self.feriados)
            if v != atual.get(k):
                muda[k] = v
                partes.append(f"{k}: {atual.get(k)} -> {v}")
        if muda.get("status") == "ENTREGUE" and not atual.get("entregue_em"):
            muda["entregue_em"] = hoje().isoformat()
        if muda.get("pago") == 1 and not atual.get("pago_em"):
            muda["pago_em"] = hoje().isoformat()
        if not partes:
            return self.enriquecer(atual)
        return self.enriquecer(self.banco.atualizar(rid, muda, "; ".join(partes)))


def fabricar_handler(app: App):
    class H(BaseHTTPRequestHandler):
        server_version = "PainelCalculos/1.0"

        def log_message(self, fmt, *args):  # sem dado de cliente no log
            sys.stderr.write(f"{self.address_string()} {self.command} {urlparse(self.path).path}\n")

        # -------------------------------------------------- utilitários
        def _json(self, codigo, obj):
            corpo = json.dumps(obj, ensure_ascii=False, default=str).encode("utf-8")
            self.send_response(codigo)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(corpo)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(corpo)

        def _arquivo(self, nome):
            corpo = (AQUI / nome).read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(corpo)))
            self.send_header("X-Frame-Options", "DENY")
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(corpo)

        def _autenticado(self) -> bool:
            cab = self.headers.get("Authorization", "")
            if cab.startswith("Basic "):
                try:
                    u, _, s = base64.b64decode(cab[6:]).decode("utf-8").partition(":")
                    if hmac.compare_digest(u, app.usuario) and hmac.compare_digest(s, app.senha):
                        return True
                except (ValueError, UnicodeDecodeError):
                    pass
            self.send_response(401)
            self.send_header("WWW-Authenticate", 'Basic realm="Painel de calculos", charset="UTF-8"')
            self.send_header("Content-Length", "0")
            self.end_headers()
            return False

        def _token_ok(self, q) -> bool:
            t = (q.get("t") or [""])[0]
            return bool(app.token) and hmac.compare_digest(t, app.token)

        def _corpo(self) -> bytes:
            n = int(self.headers.get("Content-Length") or 0)
            if n > LIMITE_BYTES:
                raise ValueError("arquivos acima de 40 MB no total")
            return self.rfile.read(n) if n else b""

        # -------------------------------------------------- GET
        def do_GET(self):
            u = urlparse(self.path)
            q = parse_qs(u.query)
            if u.path in ("/", ""):
                self.send_response(302)
                self.send_header("Location", "/painel")
                self.end_headers()
                return
            if u.path == "/pedido":
                if not self._token_ok(q):
                    return self._json(403, {"erro": "link inválido. Peça o link atualizado ao escritório."})
                return self._arquivo("pedido.html")
            if u.path == "/api/tipos":
                if not self._token_ok(q) and not self._autenticado():
                    return
                return self._json(200, {"tipos": TIPOS, "status": STATUS})
            if not self._autenticado():
                return
            if u.path == "/painel":
                return self._arquivo("index.html")
            if u.path == "/api/demandas":
                return self._json(200, {"demandas": app.linhas()})
            if u.path == "/api/resumo":
                return self._json(200, resumo(app.linhas()))
            if u.path == "/api/link":
                return self._json(200, {"link": f"/pedido?t={app.token}" if app.token else None})
            return self._json(404, {"erro": "não encontrado"})

        # -------------------------------------------------- POST
        def do_POST(self):
            u = urlparse(self.path)
            q = parse_qs(u.query)
            try:
                if u.path == "/api/pedido":
                    if not self._token_ok(q):
                        return self._json(403, {"erro": "link inválido"})
                    campos, arquivos = _multipart(self.headers.get("Content-Type", ""), self._corpo())
                    if campos.get("site"):          # armadilha simples contra robô
                        return self._json(200, {"ok": True})
                    r = app.criar(campos, arquivos, "link")
                    return self._json(201, {"ok": True, "protocolo": r["protocolo"], "prazo_parceiro": r["prazo_parceiro"],
                                            "arquivos": len(r["arquivos"])})
                if not self._autenticado():
                    return
                if u.path == "/api/demandas":
                    tipo = self.headers.get("Content-Type", "")
                    if tipo.startswith("multipart/"):
                        campos, arquivos = _multipart(tipo, self._corpo())
                    else:
                        campos, arquivos = json.loads(self._corpo() or b"{}"), []
                    return self._json(201, app.criar(campos, arquivos, "manual"))
                m = re.fullmatch(r"/api/demandas/(\d+)(/cobrar)?", u.path)
                if m:
                    rid = int(m.group(1))
                    if m.group(2):
                        r = app.banco.obter(rid)
                        if not r:
                            return self._json(404, {"erro": "não encontrado"})
                        res = cobrar_no_asaas(r)
                        if res.get("executado") and res.get("cobranca"):
                            app.banco.atualizar(rid, {"cobranca": json.dumps(res["cobranca"], ensure_ascii=False)[:2000]},
                                                "Cobrança emitida no Asaas")
                        return self._json(200, res)
                    r = app.editar(rid, json.loads(self._corpo() or b"{}"))
                    return self._json(200 if r else 404, r or {"erro": "não encontrado"})
                return self._json(404, {"erro": "não encontrado"})
            except ValueError as e:
                return self._json(400, {"erro": str(e)})
    return H


def semear_exemplo(app: App):
    """Dados FICTÍCIOS para demonstração (nenhum parceiro ou processo real)."""
    h = hoje()
    def d(n):
        return (h + timedelta(days=n)).isoformat()
    exemplos = [
        ("Dr. Advogado Exemplo A", "Liquidação de sentença", "Liquidação - aposentadoria especial", d(9), 650, "EM CÁLCULO"),
        ("Dra. Advogada Exemplo B", "Conferência / impugnação de cálculo do INSS ou da contadoria", "Impugnação do cálculo do INSS", d(3), 480, "CONFERÊNCIA"),
        ("Dr. Advogado Exemplo A", "Cálculo de RMI / revisão", "Revisão - atividade concomitante", d(1), 380, "EM CÁLCULO"),
        ("Escritório Parceiro Exemplo C", "Valor da causa", "Valor da causa - BPC", None, 250, "RECEBIDO"),
        ("Dra. Advogada Exemplo B", "Contagem de tempo de contribuição", "Tempo especial - vigilante", d(-1), 300, "DOCUMENTOS PENDENTES"),
        ("Escritório Parceiro Exemplo C", "Liquidação de sentença", "Liquidação - auxílio por incapacidade", d(14), 700, "RECEBIDO"),
    ]
    for parceiro, tipo, caso, prazo, valor, status in exemplos:
        r = app.criar({"parceiro_nome": parceiro, "tipo": tipo, "caso": caso, "prazo_parceiro": prazo or "",
                       "valor": str(valor), "processo": "0000000-00.0000.0.00.0000"}, [], "manual")
        if status != "RECEBIDO":
            app.editar(r["id"], {"status": status})
    for parceiro, tipo, caso, dias, valor, pago in [
        ("Dr. Advogado Exemplo A", "Liquidação de sentença", "Liquidação - pensão por morte", 6, 620, True),
        ("Dra. Advogada Exemplo B", "Cálculo de RMI / revisão", "Revisão - inclusão de verbas trabalhistas", 4, 420, False),
        ("Escritório Parceiro Exemplo C", "Parecer técnico", "Parecer - viabilidade de revisão", 3, 350, True),
    ]:
        r = app.criar({"parceiro_nome": parceiro, "tipo": tipo, "caso": caso, "prazo_parceiro": d(2),
                       "valor": str(valor)}, [], "manual")
        app.banco.atualizar(r["id"], {"criado_em": (h - timedelta(days=dias)).isoformat() + "T09:00:00"}, "exemplo")
        app.editar(r["id"], {"status": "ENTREGUE", "pago": pago})


def main():
    utf8_stdout()
    ap = argparse.ArgumentParser(description="Painel das demandas externas de cálculo",
                                 formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    ap.add_argument("--host", default=os.getenv("PAINEL_HOST", "127.0.0.1"))
    ap.add_argument("--porta", type=int, default=int(os.getenv("PAINEL_PORTA", "8765")))
    ap.add_argument("--exemplo", action="store_true", help="banco temporário com dados fictícios")
    ap.add_argument("--banco", help="caminho do SQLite (padrão: dados/escritorio.db)")
    a = ap.parse_args()

    usuario = os.getenv("PAINEL_USUARIO", "faya")
    senha = os.getenv("PAINEL_SENHA", "")
    token = os.getenv("PAINEL_TOKEN_PEDIDO", "")
    if a.exemplo:
        tmp = Path(tempfile.mkdtemp(prefix="painel_exemplo_"))
        os.environ["ONEDRIVE_RAIZ"] = str(tmp / "onedrive")
        banco = Banco(tmp / "exemplo.db")
        senha = senha or "exemplo"
        token = token or "exemplo"
    else:
        banco = Banco(Path(a.banco) if a.banco else DADOS_DIR / "escritorio.db")
    if not senha:
        raise SystemExit("ERRO: defina PAINEL_SENHA em config/.env (o painel tem dado de cliente). "
                         "Para demonstrar sem configurar nada: --exemplo")
    if not token:
        token = secrets.token_urlsafe(18)
        print(f"AVISO: PAINEL_TOKEN_PEDIDO vazio; gerei um temporário para esta execução: {token}\n"
              "       Grave em config/.env para o link dos parceiros não mudar a cada reinício.")
    app = App(banco, usuario, senha, token)
    if a.exemplo:
        semear_exemplo(app)
    srv = ThreadingHTTPServer((a.host, a.porta), fabricar_handler(app))
    base = f"http://{'127.0.0.1' if a.host in ('0.0.0.0', '') else a.host}:{a.porta}"
    print(f"Painel:            {base}/painel   (usuário {usuario}{' / senha exemplo' if a.exemplo else ''})")
    print(f"Link dos parceiros: {base}/pedido?t={token}")
    print(f"Banco: {banco.caminho}")
    if a.host not in ("127.0.0.1", "localhost"):
        print("ATENÇÃO: exposto na rede. Na internet, só atrás de HTTPS (Caddy/Nginx) - ver INSTALAR.md.")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        srv.server_close()
        if a.exemplo:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
