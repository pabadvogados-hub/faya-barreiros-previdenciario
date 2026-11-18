# -*- coding: utf-8 -*-
"""Caminhos no OneDrive a partir de automacoes/drive/estrutura_pastas.json (fonte unica dos nomes).

Tudo aqui devolve LISTA de partes relativas a raiz (ONEDRIVE_RAIZ); quem grava e comum/drive.py.
"""
from __future__ import annotations

import json
from datetime import date

from .config import AUTOMACOES_DIR
from .nomes import limpar, pasta_cliente, pasta_demanda, pasta_processo

E = json.loads((AUTOMACOES_DIR / "drive" / "estrutura_pastas.json").read_text("utf-8"))


def caminho_cliente(cliente: dict) -> list[str]:
    return ["CLIENTES", pasta_cliente(cliente.get("nome") or cliente.get("id"))]


def subpastas_cliente(cliente: dict | None = None) -> list[list[str]]:
    return [[s] for s in E["cliente"]]


def caminho_processo(cliente: dict, proc: dict) -> list[str]:
    """CLIENTES/<CLIENTE>/08_PROCESSO_JUDICIAL/<CNJ> - <PARTE CONTRARIA> - <TIPO DE ACAO>"""
    return caminho_cliente(cliente) + [E["pasta_processos"],
                                       pasta_processo(proc.get("numero", ""), proc.get("parte_contraria", ""),
                                                      proc.get("tipo_acao", ""))]


def caminho_parceiro(parceiro: dict | str) -> list[str]:
    nome = parceiro if isinstance(parceiro, str) else (parceiro.get("nome") or parceiro.get("id"))
    return ["DEMANDAS_EXTERNAS_CALCULO", limpar(nome).upper()]


def caminho_demanda_externa(parceiro: dict | str, dem: dict) -> list[str]:
    """DEMANDAS_EXTERNAS_CALCULO/<ADVOGADO PARCEIRO>/<AAAA-MM-DD - CASO>"""
    return caminho_parceiro(parceiro) + [pasta_demanda(dem.get("caso") or dem.get("assunto", ""),
                                                       dem.get("recebida_em") or date.today())]


def caminho_financeiro(ano: int, mes: int, sub: str | None = None) -> list[str]:
    c = ["FINANCEIRO", str(ano), f"{int(mes):02d}"]
    return c + [sub] if sub else c


def palavras_chave() -> list[tuple[str, list[str]]]:
    return [(sub, chaves) for sub, chaves in E["palavras_chave"]["ordem"]]
