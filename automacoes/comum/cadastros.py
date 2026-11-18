# -*- coding: utf-8 -*-
"""Leitura dos cadastros locais (config/clientes.json, colaboradores.json, despesas_fixas.json).

Esses arquivos tem dado pessoal (CPF, chave Pix, telefone): ficam fora do Git (.gitignore) e
entram no backup cifrado da VPS.
"""
from __future__ import annotations

from .config import carregar_json, so_digitos


def clientes() -> dict:
    return carregar_json("clientes")


def lista_clientes() -> list[dict]:
    return clientes().get("clientes") or []


def cliente_por_asaas(customer_id: str = "", cpf_cnpj: str = "") -> dict | None:
    doc = so_digitos(cpf_cnpj)
    for c in lista_clientes():
        if customer_id and c.get("asaas_customer_id") == customer_id:
            return c
        if doc and so_digitos(c.get("cpf_cnpj")) == doc:
            return c
    return None


def _mesmo_telefone(a: str, b: str) -> bool:
    """Celular gravado com ou sem o 9 extra: compara DDD + 8 ultimos digitos."""
    a, b = so_digitos(a)[-11:], so_digitos(b)[-11:]
    return bool(a and b) and len(a) >= 10 and (a == b or (a[:2] == b[:2] and a[-8:] == b[-8:]))


def cliente_por_telefone(telefone: str) -> dict | None:
    if len(so_digitos(telefone)) < 10:
        return None
    for c in lista_clientes():
        fones = list(c.get("whatsapps") or [])
        fones.append((c.get("contato_financeiro") or {}).get("whatsapp"))
        if any(_mesmo_telefone(f, telefone) for f in fones if f):
            return c
    return None


def cliente_por_email(email: str) -> dict | None:
    alvo = (email or "").strip().lower()
    if not alvo:
        return None
    for c in lista_clientes():
        emails = [c.get("email"), (c.get("contato_financeiro") or {}).get("email")]
        if alvo in [(e or "").strip().lower() for e in emails]:
            return c
    return None


def cliente_por_id(cid: str) -> dict | None:
    for c in lista_clientes():
        if c.get("id") == cid:
            return c
    return None


# ---- advogados parceiros (demandas externas de calculo): clientes.json -> "parceiros"

def lista_parceiros() -> list[dict]:
    return clientes().get("parceiros") or []


def parceiro_por_id(pid: str) -> dict | None:
    return next((p for p in lista_parceiros() if p.get("id") == pid), None)


def parceiro_por_telefone(telefone: str) -> dict | None:
    if len(so_digitos(telefone)) < 10:
        return None
    for p in lista_parceiros():
        if any(_mesmo_telefone(f, telefone) for f in (p.get("whatsapps") or []) if f):
            return p
    return None


def parceiro_por_email(email: str) -> dict | None:
    alvo = (email or "").strip().lower()
    if not alvo:
        return None
    return next((p for p in lista_parceiros() if (p.get("email") or "").strip().lower() == alvo), None)


def demandas_abertas(parceiro: dict) -> list[dict]:
    return [d for d in parceiro.get("demandas") or [] if (d.get("caso") and not d.get("entregue_em"))]


def colaboradores() -> dict:
    return carregar_json("colaboradores")


def lista_colaboradores(ativos=True) -> list[dict]:
    out = []
    for c in colaboradores().get("colaboradores") or []:
        if ativos and c.get("desligado_em"):
            continue
        out.append(c)
    return out


def colaborador_por_id(cid: str) -> dict | None:
    for c in colaboradores().get("colaboradores") or []:
        if c.get("id") == cid:
            return c
    return None


def despesas() -> dict:
    return carregar_json("despesas_fixas")


def lista_despesas(ativas=True) -> list[dict]:
    return [d for d in despesas().get("despesas") or [] if (d.get("ativo") or not ativas)]
