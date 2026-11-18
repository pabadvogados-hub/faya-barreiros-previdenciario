# -*- coding: utf-8 -*-
"""Adaptador do sistema de gestao do escritorio: NOTION (processos, prazos/tarefas e clientes).

>>> IMPLEMENTADO PELA DOCUMENTACAO PUBLICA DO NOTION (https://developers.notion.com/reference,
>>> API v1, Notion-Version 2022-06-28). NAO TESTADO CONTRA O WORKSPACE DA DRA. FAYA. <<<
Antes do primeiro --go: rodar `python automacoes/comum/notion.py --esquema` com o token e os ids
preenchidos, conferir as colunas listadas, preencher o mapa de campos e fazer UMA tarefa de teste
numa base de teste (ou apagar a tarefa de teste depois).

Este modulo substitui o antigo conector de sistema juridico do pacote de origem. A interface
publica (nomes e assinaturas) foi mantida para as automacoes que importam daqui:
controladoria/intimacoes.py, drive/arquivar_documento.py, financeiro/pagamentos.py e
atendimento/status_processo.py.

POR QUE NAO HA NOME DE COLUNA NO CODIGO
    Nao conhecemos o Notion dela. As bases (Processos, Prazos/Tarefas, Clientes e, opcional,
    Andamentos) e os NOMES das colunas vem de config/escritorio.json -> "notion":
        "databases": {"processos": "<id>", "prazos": "<id>", "clientes": "<id>", "andamentos": ""}
        "campos":    {"prazos": {"prazo": "Data", "responsavel": "Responsavel", ...}, ...}
    O TIPO de cada coluna (texto, data, select, status, pessoa, relacao, checkbox...) NAO precisa
    ser informado: o modulo le o esquema da base (GET /databases/{id}) e monta o valor certo.
    Campo logico sem coluna mapeada (string vazia) e simplesmente ignorado; o titulo da pagina
    e achado sozinho (a coluna do tipo "title").

CONTRATO DE RETORNO
    - leitura: listas/dicts ja traduzidos para os nomes LOGICOS (numero, fase, responsavel...),
      mais "id" (id da pagina) e "url" (link da pagina no Notion);
    - escrita: recebe `executar`. Sem executar=True NADA vai para o Notion e o retorno e
      {"_dry_run": True, ...}. Erro de API em escrita NAO levanta excecao: volta {"erro": "..."}
      (os chamadores registram a pendencia e seguem); erro em leitura levanta NotionErro.

O QUE O NOTION NAO FAZ (erro claro, NaoSuportado):
    listar_documentos / url_temporaria_documento: documento do cliente mora no OneDrive (pasta do
    cliente), nao no Notion; no Notion vai so o caminho/link.

ASSINATURAS QUE DIVERGIAM ENTRE O ESQUELETO ANTIGO E OS CHAMADORES (resolvidas a favor dos chamadores):
    - buscar_processo(numero) devolve LISTA (o esqueleto dizia dict); os chamadores fazem achados[0]["id"].
    - criar_tarefa(processo_id, tipo, responsaveis, autor_id, descricao, *, start_date, end_date,
      date_deadline, urgent, executar) - e a forma usada pela controladoria, pelo arquivamento de
      documento e pelos pagamentos (o esqueleto tinha criar_tarefa(titulo, prazo, responsavel_id, ...)).
      O titulo e a 1a linha de `descricao` (ou o argumento nomeado `titulo`).
      Diferente do sistema antigo, o Notion NAO exige processo: tarefa sem processo e criada sem a
      relacao (o prazo nunca se perde por falta de cadastro).
    - buscar_cliente devolve LISTA (o esqueleto dizia dict), como buscar_processo.
    - autor_id e aceito por compatibilidade e ignorado (no Notion o autor e a integracao).

Credencial: NOTION_TOKEN em config/.env (token de uma "integracao interna" criada em
https://www.notion.so/my-integrations; cada base precisa ser COMPARTILHADA com a integracao em
"... > Conexoes", senao a API responde 404).
"""
from __future__ import annotations

import os
import re
import sys
import time
from datetime import date
from functools import lru_cache

import requests

try:
    from .config import escritorio
except ImportError:                                   # rodando como script: python automacoes/comum/notion.py
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from comum.config import escritorio  # noqa: E402

BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"
LIMITE_TEXTO = 2000          # limite da API por objeto de rich_text
BASES_OBRIGATORIAS = ("processos", "prazos")


class NotionErro(RuntimeError):
    pass


class NaoSuportado(NotImplementedError):
    pass


# ------------------------------------------------------------------ configuracao

def _cfg() -> dict:
    return (escritorio().get("notion") or {})


def _token() -> str:
    return (os.getenv("NOTION_TOKEN") or "").strip()


def _db_id(base: str) -> str:
    return str(((_cfg().get("databases") or {}).get(base)) or "").strip()


def _campo(base: str, logico: str) -> str:
    return str(((_cfg().get("campos") or {}).get(base) or {}).get(logico) or "").strip()


def configurado(*bases: str) -> bool:
    """True quando ha NOTION_TOKEN e o id de cada base pedida (padrao: processos e prazos).
    Use para escolher entre modo automatico e modo manual, em vez de estourar no meio."""
    bases = bases or BASES_OBRIGATORIAS
    return bool(_token()) and all(_db_id(b) for b in bases)


def _pendente(base: str = "") -> str:
    falta = []
    if not _token():
        falta.append("NOTION_TOKEN em config/.env")
    for b in ((base,) if base else BASES_OBRIGATORIAS):
        if not _db_id(b):
            falta.append(f'escritorio.json -> notion.databases.{b}')
    return ("Notion nao configurado (falta: " + ", ".join(falta) + "). "
            "Enquanto isso, lance manualmente no Notion.")


# ------------------------------------------------------------------ HTTP

_sessao = None


def _http():
    global _sessao
    if _sessao is None:
        _sessao = requests.Session()
        _sessao.headers.update({"Authorization": f"Bearer {_token()}", "Notion-Version": NOTION_VERSION,
                                "Content-Type": "application/json"})
    return _sessao


def _req(metodo: str, caminho: str, json_body: dict | None = None, tentativas: int = 4) -> dict:
    """Chamada com retry em 429 (respeita Retry-After) e 5xx. Limite medio do Notion: ~3 req/s."""
    if not _token():
        raise NotionErro(_pendente())
    espera = 1.0
    for i in range(tentativas):
        try:
            r = _http().request(metodo, BASE_URL + caminho, json=json_body, timeout=60)
        except requests.RequestException as e:
            if i == tentativas - 1:
                raise NotionErro(f"rede: {e}") from e
            time.sleep(espera)
            espera *= 2
            continue
        if r.status_code == 429 or r.status_code >= 500:
            if i == tentativas - 1:
                break
            time.sleep(float(r.headers.get("Retry-After") or espera))
            espera *= 2
            continue
        if r.status_code >= 400:
            try:
                d = r.json()
                msg = f"{d.get('code')}: {d.get('message')}"
            except ValueError:
                msg = r.text[:300]
            if r.status_code == 404:
                msg += " (a base/pagina foi compartilhada com a integracao em '... > Conexoes'?)"
            raise NotionErro(f"HTTP {r.status_code} em {metodo} {caminho}: {msg}")
        time.sleep(0.34)
        return r.json() if r.content else {}
    raise NotionErro(f"HTTP {r.status_code} em {metodo} {caminho} apos {tentativas} tentativas")


def _consultar(base: str, filtro: dict | None = None, ordem: list | None = None, limite: int = 100) -> list[dict]:
    """POST /databases/{id}/query com paginacao (start_cursor / has_more)."""
    db = _db_id(base)
    if not db:
        raise NotionErro(_pendente(base))
    out, cursor = [], None
    while len(out) < limite:
        corpo = {"page_size": min(100, limite - len(out))}
        if filtro:
            corpo["filter"] = filtro
        if ordem:
            corpo["sorts"] = ordem
        if cursor:
            corpo["start_cursor"] = cursor
        d = _req("POST", f"/databases/{db}/query", corpo)
        out += d.get("results") or []
        if not d.get("has_more"):
            break
        cursor = d.get("next_cursor")
    return out


# ------------------------------------------------------------------ esquema e conversao de valores

@lru_cache(maxsize=16)
def _esquema_db(db_id: str) -> dict:
    """{nome_da_coluna: tipo} lido de GET /databases/{id}."""
    d = _req("GET", f"/databases/{db_id}")
    return {nome: p.get("type") for nome, p in (d.get("properties") or {}).items()}


def esquema(base: str) -> dict:
    db = _db_id(base)
    if not db:
        raise NotionErro(_pendente(base))
    return _esquema_db(db)


def _coluna_titulo(base: str) -> str:
    mapeada = _campo(base, "titulo")
    if mapeada:
        return mapeada
    for nome, tipo in esquema(base).items():
        if tipo == "title":
            return nome
    raise NotionErro(f"base {base} sem coluna de titulo")


def _rich(texto: str) -> list[dict]:
    texto = str(texto or "")
    partes = [texto[i:i + LIMITE_TEXTO] for i in range(0, len(texto), LIMITE_TEXTO)] or [""]
    return [{"type": "text", "text": {"content": p}} for p in partes[:100]]


def _data_iso(v) -> str | None:
    if not v:
        return None
    if isinstance(v, date):
        return v.isoformat()
    s = str(v).strip()
    m = re.match(r"(\d{2})/(\d{2})/(\d{4})", s)
    return f"{m.group(3)}-{m.group(2)}-{m.group(1)}" if m else s[:10]


def _valor(tipo: str, v):
    """Monta o valor da propriedade do Notion conforme o TIPO da coluna (lido do esquema)."""
    if tipo == "title":
        return {"title": _rich(v)}
    if tipo == "rich_text":
        return {"rich_text": _rich(v)}
    if tipo == "date":
        if isinstance(v, (list, tuple)):
            return {"date": {"start": _data_iso(v[0]), "end": _data_iso(v[1]) if len(v) > 1 else None}}
        return {"date": {"start": _data_iso(v)}}
    if tipo == "select":
        return {"select": {"name": str(v)}}
    if tipo == "status":
        return {"status": {"name": str(v)}}
    if tipo == "multi_select":
        nomes = v if isinstance(v, (list, tuple)) else [v]
        return {"multi_select": [{"name": str(n)} for n in nomes if n]}
    if tipo == "people":
        ids = v if isinstance(v, (list, tuple)) else [v]
        return {"people": [{"id": str(i)} for i in ids if i]}
    if tipo == "relation":
        ids = v if isinstance(v, (list, tuple)) else [v]
        return {"relation": [{"id": str(i)} for i in ids if i]}
    if tipo == "checkbox":
        return {"checkbox": bool(v)}
    if tipo == "number":
        try:
            return {"number": float(v)}
        except (TypeError, ValueError):
            return {"number": None}
    if tipo in ("email", "phone_number", "url"):
        return {tipo: str(v)}
    raise NotionErro(f"coluna do tipo '{tipo}' nao e gravavel pela API (formula, rollup, created_time...)")


def _propriedades(base: str, valores: dict) -> tuple[dict, list[str]]:
    """{logico: valor} -> properties do Notion. Ignora campo sem coluna mapeada ou valor vazio.
    Devolve (properties, avisos)."""
    esq = esquema(base)
    props, avisos = {}, []
    for logico, v in valores.items():
        if v is None or v == "" or v == [] or (isinstance(v, (list, tuple)) and not any(v)):
            continue
        coluna = _coluna_titulo(base) if logico == "titulo" else _campo(base, logico)
        if not coluna:
            continue
        tipo = esq.get(coluna)
        if not tipo:
            avisos.append(f"coluna '{coluna}' (campo {logico}) nao existe na base {base}")
            continue
        try:
            props[coluna] = _valor(tipo, v)
        except NotionErro as e:
            avisos.append(f"{coluna}: {e}")
    return props, avisos


def _ler(prop: dict):
    """Valor simples (str, lista, numero, bool) de uma propriedade lida de uma pagina."""
    if not prop:
        return None
    t = prop.get("type")
    v = prop.get(t)
    if t in ("title", "rich_text"):
        return "".join(x.get("plain_text") or "" for x in v or [])
    if t in ("select", "status"):
        return (v or {}).get("name")
    if t == "multi_select":
        return [x.get("name") for x in v or []]
    if t == "date":
        return (v or {}).get("start")
    if t == "people":
        return [x.get("name") or x.get("id") for x in v or []]
    if t == "relation":
        return [x.get("id") for x in v or []]
    if t == "formula":
        return (v or {}).get((v or {}).get("type"))
    if t == "rollup":
        r = v or {}
        return r.get(r.get("type"))
    if t == "unique_id":
        return f"{(v or {}).get('prefix') or ''}{(v or {}).get('number')}"
    if t in ("created_by", "last_edited_by"):
        return (v or {}).get("name") or (v or {}).get("id")
    return v


def _para_dict(pagina: dict, base: str) -> dict:
    props = pagina.get("properties") or {}
    out = {"id": pagina.get("id"), "url": pagina.get("url"), "criado_em": pagina.get("created_time")}
    titulo = next((p for p in props.values() if p.get("type") == "title"), None)
    out["titulo"] = _ler(titulo) if titulo else ""
    for logico, coluna in ((_cfg().get("campos") or {}).get(base) or {}).items():
        if coluna and logico != "titulo":
            out[logico] = _ler(props.get(coluna))
    return out


def _filtro_texto(base: str, logico: str, valor: str, op: str = "contains") -> dict:
    """Filtro de texto/numero/select conforme o tipo da coluna (titulo se o campo nao estiver mapeado)."""
    coluna = _campo(base, logico) or _coluna_titulo(base)
    tipo = esquema(base).get(coluna) or "rich_text"
    if tipo in ("title", "rich_text", "phone_number", "email", "url"):
        return {"property": coluna, tipo: {op: valor}}
    if tipo in ("select", "status"):
        return {"property": coluna, tipo: {"equals": valor}}
    if tipo == "number":
        return {"property": coluna, "number": {"equals": float(re.sub(r"\D", "", valor) or 0)}}
    if tipo == "unique_id":
        return {"property": coluna, "unique_id": {"equals": int(re.sub(r"\D", "", valor) or 0)}}
    raise NotionErro(f"nao sei filtrar a coluna '{coluna}' do tipo {tipo}")


def _children_texto(texto: str) -> list[dict]:
    """Corpo da pagina: um paragrafo por bloco de ate 2000 caracteres (max. 100 blocos por chamada)."""
    blocos = []
    for par in str(texto or "").split("\n\n"):
        for i in range(0, max(len(par), 1), LIMITE_TEXTO):
            pedaco = par[i:i + LIMITE_TEXTO]
            if pedaco.strip():
                blocos.append({"object": "block", "type": "paragraph",
                               "paragraph": {"rich_text": _rich(pedaco)}})
    return blocos[:100]


def _criar_pagina(base: str, valores: dict, corpo: str = "", executar: bool = False) -> dict:
    if not executar:
        return {"_dry_run": True, "base": base, "campos": {k: v for k, v in valores.items() if v not in (None, "", [])},
                "_notion_configurado": configurado(base)}
    if not configurado(base):
        return {"erro": _pendente(base)}
    try:
        props, avisos = _propriedades(base, valores)
        body = {"parent": {"database_id": _db_id(base)}, "properties": props}
        filhos = _children_texto(corpo)
        if filhos:
            body["children"] = filhos
        p = _req("POST", "/pages", body)
    except NotionErro as e:
        return {"erro": str(e)}
    return {"id": p.get("id"), "url": p.get("url"), "avisos": avisos}


def _atualizar_pagina(base: str, page_id: str, valores: dict, executar: bool = False) -> dict:
    if not executar:
        return {"_dry_run": True, "base": base, "id": page_id, "campos": valores}
    if not configurado(base):
        return {"erro": _pendente(base)}
    try:
        props, avisos = _propriedades(base, valores)
        p = _req("PATCH", f"/pages/{page_id}", {"properties": props})
    except NotionErro as e:
        return {"erro": str(e)}
    return {"id": p.get("id"), "url": p.get("url"), "avisos": avisos}


# ------------------------------------------------------------------ leitura

def buscar_processo(numero: str) -> list[dict]:
    """Processos cujo numero (campo processos.numero; sem mapa, o titulo) contem `numero`.
    Tenta o numero como veio e, se nada achar, so os digitos. Lista vazia = nao encontrado.
    Cada item: {id, url, titulo, numero, cliente, fase, responsavel, tipo, valor_causa, ...}
    (as chaves alem de id/url/titulo sao as do mapa notion.campos.processos)."""
    if not configurado("processos"):
        raise NotionErro(_pendente("processos"))
    tentativas = [numero]
    digitos = re.sub(r"\D", "", numero or "")
    if digitos and digitos != numero:
        tentativas.append(digitos)
    for alvo in tentativas:
        achados = _consultar("processos", _filtro_texto("processos", "numero", alvo), limite=10)
        if achados:
            return [_para_dict(p, "processos") for p in achados]
    return []


def buscar_cliente(nome_ou_cpf: str) -> list[dict]:
    """Clientes por CPF/CNPJ (campo clientes.cpf_cnpj, se mapeado e o texto tiver 11+ digitos)
    ou por nome (titulo). Cada item: {id, url, titulo, cpf_cnpj, telefone, email, ...}."""
    if not configurado("clientes"):
        raise NotionErro(_pendente("clientes"))
    digitos = re.sub(r"\D", "", nome_ou_cpf or "")
    if len(digitos) >= 11 and _campo("clientes", "cpf_cnpj"):
        achados = _consultar("clientes", _filtro_texto("clientes", "cpf_cnpj", nome_ou_cpf), limite=10)
        if not achados and digitos != nome_ou_cpf:
            achados = _consultar("clientes", _filtro_texto("clientes", "cpf_cnpj", digitos), limite=10)
    else:
        achados = _consultar("clientes", {"property": _coluna_titulo("clientes"),
                                          "title": {"contains": nome_ou_cpf}}, limite=10)
    return [_para_dict(p, "clientes") for p in achados]


def listar_clientes(nome: str = "", limite: int = 50) -> list[dict]:
    """Clientes do escritorio (filtrados pelo nome, se informado)."""
    if not configurado("clientes"):
        raise NotionErro(_pendente("clientes"))
    filtro = {"property": _coluna_titulo("clientes"), "title": {"contains": nome}} if nome else None
    return [_para_dict(p, "clientes") for p in _consultar("clientes", filtro, limite=limite)]


def customer_id(nome_ou_cpf: str) -> str | None:
    """Id da pagina do cliente no Notion, ou None (nenhum ou mais de um encontrado)."""
    achados = buscar_cliente(nome_ou_cpf)
    return achados[0]["id"] if len(achados) == 1 else None


def _andamentos_da_base(processo_id: str, desde: str | None, limite: int) -> list[dict]:
    rel = _campo("andamentos", "processo")
    if not rel:
        raise NotionErro("notion.campos.andamentos.processo (coluna de relacao com o processo) nao mapeado")
    filtros = [{"property": rel, "relation": {"contains": processo_id}}]
    col_data = _campo("andamentos", "data")
    ordem = [{"property": col_data, "direction": "descending"}] if col_data else \
        [{"timestamp": "created_time", "direction": "descending"}]
    if desde and col_data:
        filtros.append({"property": col_data, "date": {"on_or_after": _data_iso(desde)}})
    filtro = filtros[0] if len(filtros) == 1 else {"and": filtros}
    out = []
    for p in _consultar("andamentos", filtro, ordem, limite=limite):
        d = _para_dict(p, "andamentos")
        out.append({"id": d["id"], "data": d.get("data") or (d.get("criado_em") or "")[:10],
                    "descricao": d.get("descricao") or d.get("titulo") or "", "tipo": d.get("tipo") or "", "url": d["url"]})
    return out


def _andamentos_do_corpo(processo_id: str, desde: str | None, limite: int) -> list[dict]:
    """Sem base de Andamentos: le o corpo da pagina do processo (GET /blocks/{id}/children).
    Cada paragrafo/item de lista = um andamento; data = 'dd/mm/aaaa' ou 'aaaa-mm-dd' no inicio do
    texto, senao a data de criacao do bloco. Mais recente primeiro."""
    blocos, cursor = [], None
    while True:
        d = _req("GET", f"/blocks/{processo_id}/children?page_size=100" + (f"&start_cursor={cursor}" if cursor else ""))
        blocos += d.get("results") or []
        if not d.get("has_more"):
            break
        cursor = d.get("next_cursor")
    out = []
    for b in blocos:
        t = b.get("type")
        if t not in ("paragraph", "bulleted_list_item", "numbered_list_item", "to_do", "callout", "quote"):
            continue
        texto = "".join(x.get("plain_text") or "" for x in (b.get(t) or {}).get("rich_text") or []).strip()
        if not texto:
            continue
        m = re.match(r"\s*(\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2})", texto)
        quando = _data_iso(m.group(1)) if m else (b.get("created_time") or "")[:10]
        if desde and quando and quando < _data_iso(desde):
            continue
        out.append({"id": b.get("id"), "data": quando, "descricao": texto, "tipo": t})
    out.sort(key=lambda x: x["data"] or "", reverse=True)
    return out[:limite]


def movimentacoes(processo_id: str, desde: str | None = None) -> list[dict]:
    """Andamentos do processo, mais recente primeiro: [{data, descricao, tipo, id}].
    Fonte: base 'andamentos' (se configurada) ou o corpo da pagina do processo."""
    if not _token():
        raise NotionErro(_pendente("processos"))
    if _db_id("andamentos"):
        return _andamentos_da_base(processo_id, desde, 500)
    return _andamentos_do_corpo(processo_id, desde, 500)


def ultimas_movimentacoes(processo_id: str, limite: int = 8) -> list[dict]:
    """Ultimos `limite` andamentos (usada por atendimento/status_processo.py)."""
    if not _token():
        raise NotionErro(_pendente("processos"))
    if _db_id("andamentos"):
        return _andamentos_da_base(processo_id, None, limite)
    return _andamentos_do_corpo(processo_id, None, limite)


def tarefas_abertas(responsavel_id: str | None = None, limite: int = 200) -> list[dict]:
    """Tarefas/prazos que nao estao concluidos (notion.status_concluido), por prazo crescente:
    [{id, url, titulo, prazo, prazo_fatal, responsavel, processo, status, ...}]."""
    if not configurado("prazos"):
        raise NotionErro(_pendente("prazos"))
    esq = esquema("prazos")
    filtros = []
    col_status = _campo("prazos", "status")
    if col_status:
        tipo = esq.get(col_status)
        if tipo == "checkbox":
            filtros.append({"property": col_status, "checkbox": {"equals": False}})
        elif tipo in ("status", "select"):
            for v in _cfg().get("status_concluido") or []:
                filtros.append({"property": col_status, tipo: {"does_not_equal": v}})
    col_resp = _campo("prazos", "responsavel")
    if responsavel_id and col_resp:
        tipo = esq.get(col_resp)
        if tipo == "people":
            filtros.append({"property": col_resp, "people": {"contains": responsavel_id}})
        elif tipo in ("select", "status"):
            filtros.append({"property": col_resp, tipo: {"equals": responsavel_id}})
        elif tipo == "multi_select":
            filtros.append({"property": col_resp, "multi_select": {"contains": responsavel_id}})
        else:
            filtros.append({"property": col_resp, "rich_text": {"contains": responsavel_id}})
    filtro = None if not filtros else (filtros[0] if len(filtros) == 1 else {"and": filtros})
    col_prazo = _campo("prazos", "prazo")
    ordem = [{"property": col_prazo, "direction": "ascending"}] if col_prazo else None
    return [_para_dict(p, "prazos") for p in _consultar("prazos", filtro, ordem, limite=limite)]


# ------------------------------------------------------------------ escrita

def criar_tarefa(processo_id: str | None, tipo: str | None = None, responsaveis: list | None = None,
                 autor_id: str | None = None, descricao: str = "", *, titulo: str | None = None,
                 start_date: str | None = None, end_date: str | None = None, date_deadline: str | None = None,
                 urgent: bool = False, executar: bool = False) -> dict:
    """Cria a tarefa/prazo na base 'prazos'.

    processo_id   id da pagina do processo (relacao 'processo'); None = tarefa sem processo.
    tipo          valor da coluna 'tipo' (ex.: o select 'Prazo'); vem de notion.tipos_tarefa.
    responsaveis  lista de valores da coluna 'responsavel' (id de usuario se a coluna for Pessoa,
                  nome se for select/texto); vem de notion.responsaveis.
    descricao     texto completo; a 1a linha vira o titulo (salvo `titulo`), o texto todo vai para
                  a coluna 'observacao' (se mapeada) e para o corpo da pagina.
    end_date      prazo de trabalho (prazo interno)   -> coluna 'prazo'
    date_deadline prazo fatal                         -> coluna 'prazo_fatal' (e 'prazo', se nao houver end_date)
    start_date    -> coluna 'inicio';   urgent -> coluna 'urgente' (checkbox/select).
    Retorno: {"_dry_run": True, ...} | {"id", "url", "avisos"} | {"erro": "..."}."""
    del autor_id  # compatibilidade: no Notion o autor e a propria integracao
    texto = str(descricao or "")
    titulo = (titulo or texto.strip().splitlines()[0] if texto.strip() else titulo or "Tarefa")[:200]
    quem = [r for r in (responsaveis or []) if r]
    valores = {
        "titulo": titulo,
        "tipo": tipo,
        "responsavel": quem,
        "processo": [processo_id] if processo_id else None,
        "inicio": start_date,
        "prazo": end_date or date_deadline,
        "prazo_fatal": date_deadline,
        "urgente": urgent if urgent else None,
        "observacao": texto,
        "status": (_cfg().get("status_inicial") or None),
    }
    if executar and configurado("prazos"):
        col = _campo("prazos", "urgente")
        if urgent and col:
            try:
                if esquema("prazos").get(col) in ("select", "status", "multi_select", "rich_text"):
                    valores["urgente"] = "Urgente"
            except NotionErro:
                pass
    return _criar_pagina("prazos", valores, corpo=texto, executar=executar)


def concluir_tarefa(tarefa_id: str, executar: bool = False) -> dict:
    """Marca a tarefa como concluida (notion.status_concluido[0] ou checkbox=True)."""
    col = _campo("prazos", "status")
    if not col:
        return {"erro": "notion.campos.prazos.status nao mapeado"}
    if not executar:
        return {"_dry_run": True, "id": tarefa_id, "status": "concluida"}
    try:
        tipo = esquema("prazos").get(col)
    except NotionErro as e:
        return {"erro": str(e)}
    valor = True if tipo == "checkbox" else ((_cfg().get("status_concluido") or [None])[0])
    if valor is None:
        return {"erro": "notion.status_concluido vazio"}
    return _atualizar_pagina("prazos", tarefa_id, {"status": valor}, executar=True)


def lancar_andamento(processo_id: str, data: str, descricao: str, executar: bool = False) -> dict:
    """Registra andamento: pagina nova na base 'andamentos' (se configurada) ou paragrafo
    'dd/mm/aaaa - descricao' no fim do corpo da pagina do processo (PATCH /blocks/{id}/children)."""
    if _db_id("andamentos"):
        titulo = str(descricao or "").strip().splitlines()[0][:200] if str(descricao or "").strip() else "Andamento"
        return _criar_pagina("andamentos", {"titulo": titulo, "data": data, "descricao": descricao,
                                            "processo": [processo_id]}, executar=executar)
    iso = _data_iso(data) or date.today().isoformat()
    linha = f"{iso[8:10]}/{iso[5:7]}/{iso[:4]} - {descricao}"
    if not executar:
        return {"_dry_run": True, "processo": processo_id, "bloco": linha}
    if not _token():
        return {"erro": _pendente("processos")}
    try:
        d = _req("PATCH", f"/blocks/{processo_id}/children", {"children": _children_texto(linha)})
    except NotionErro as e:
        return {"erro": str(e)}
    return {"id": ((d.get("results") or [{}])[0]).get("id"), "processo": processo_id}


def criar_cliente(nome: str, cpf_cnpj: str, telefone: str = "", email: str = "",
                  executar: bool = False, **extras) -> dict:
    """Cadastra cliente novo na base 'clientes' (POP-ATD-03). `extras` = outros campos logicos
    mapeados em notion.campos.clientes."""
    valores = {"titulo": nome, "cpf_cnpj": cpf_cnpj, "telefone": telefone, "email": email}
    valores.update(extras)
    return _criar_pagina("clientes", valores, executar=executar)


def criar_processo(cliente_id: str, numero: str = "", tipo: str = "", fase: str = "",
                   responsavel_id: str = "", executar: bool = False, **extras) -> dict:
    """Cadastra processo judicial ou requerimento administrativo na base 'processos'.
    O titulo e o numero (ou 'Caso sem numero')."""
    valores = {"titulo": numero or "Caso sem numero", "numero": numero, "cliente": [cliente_id] if cliente_id else None,
               "tipo": tipo, "fase": fase, "responsavel": [responsavel_id] if responsavel_id else None}
    valores.update(extras)
    return _criar_pagina("processos", valores, executar=executar)


# ------------------------------------------------------------------ IDs / configuracao do escritorio

def ids_do_escritorio() -> dict:
    """Configuracao do Notion do escritorio + as colunas reais de cada base (lidas da API).

    Os valores (ids de base, nomes de coluna, responsaveis, tipos de tarefa) NAO se adivinham:
    ficam em config/escritorio.json -> "notion". Use isto (ou --esquema na linha de comando)
    para conferir o mapa contra as colunas que existem de verdade."""
    cfg = dict(_cfg())
    cfg["_colunas_reais"] = {}
    for base in (cfg.get("databases") or {}):
        if _db_id(base) and _token():
            try:
                cfg["_colunas_reais"][base] = esquema(base)
            except NotionErro as e:
                cfg["_colunas_reais"][base] = {"_erro": str(e)}
    return cfg


# ------------------------------------------------------------------ o que o Notion nao faz

_SEM_DOC = ("O Notion nao guarda os documentos do processo neste escritorio: o documento mora no "
            "OneDrive, na pasta do cliente (automacoes/drive/ESTRUTURA_PASTAS.md); no Notion vai so o "
            "caminho. Para baixar peca/decisao do processo judicial, use o PJe.")


def listar_documentos(processo_id: str) -> list[dict]:
    raise NaoSuportado(_SEM_DOC)


def url_temporaria_documento(documento_id) -> str:
    raise NaoSuportado(_SEM_DOC)


# ------------------------------------------------------------------ linha de comando

def main():
    import argparse
    import json
    ap = argparse.ArgumentParser(description="Conector Notion: conferencia da configuracao (somente leitura)")
    ap.add_argument("--esquema", action="store_true", help="lista as colunas reais de cada base configurada")
    ap.add_argument("--processo", help="busca um processo pelo numero")
    ap.add_argument("--abertas", action="store_true", help="lista as tarefas em aberto")
    a = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    print(f"configurado(): {configurado()}")
    if a.esquema or not (a.processo or a.abertas):
        print(json.dumps(ids_do_escritorio(), ensure_ascii=False, indent=2))
    if a.processo:
        print(json.dumps(buscar_processo(a.processo), ensure_ascii=False, indent=2))
    if a.abertas:
        for t in tarefas_abertas():
            print(f"  {t.get('prazo') or '-':10}  {t.get('titulo')}")


if __name__ == "__main__":
    main()
