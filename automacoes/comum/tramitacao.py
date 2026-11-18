# -*- coding: utf-8 -*-
"""Adaptador da TRAMITACAO INTELIGENTE (assinatura digital e andamento processual).

>>> ESQUELETO. NAO HA CHAMADA DE API AQUI E configurado() DEVOLVE False. <<<

A API da Tramitacao Inteligente NAO foi documentada para nos: nao sabemos endpoints, forma de
autenticacao, limites nem campos. Inventar isso seria documentacao falsa com cara de verificada.
Por isso este modulo fixa so a INTERFACE que as automacoes vao usar e o contrato de cada funcao.

ATE A API CHEGAR, A ASSINATURA SEGUE MANUAL NA PLATAFORMA: a automacao gera o documento
(contrato, procuracao, declaracao, termo de renuncia) na pasta 00_CONTRATACAO do cliente no
OneDrive, e a Barbara sobe o arquivo na Tramitacao Inteligente e manda para assinatura por la.
O andamento processual tambem segue sendo consultado na plataforma (ou no PJe/DJEN, que a
controladoria ja le).

Para implementar, o escritorio precisa fornecer:
    1. a documentacao da API (ou o contato do suporte da Tramitacao Inteligente);
    2. o token/credencial de integracao (vai em config/.env, ex.: TRAMITACAO_API_TOKEN);
    3. um documento de teste para homologar o envio e o retorno do status.
Quem implementar: manter as assinaturas abaixo, preencher funcao por funcao, apagar o raise e
so entao fazer configurado() olhar a credencial.
"""
from __future__ import annotations

from pathlib import Path

PENDENTE = ("Integracao com a Tramitacao Inteligente ainda nao implementada: a API nao foi "
            "documentada para nos. Envie o documento para assinatura manualmente na plataforma.")


def configurado() -> bool:
    """Sempre False ate a integracao existir. As automacoes usam isto para cair no modo manual."""
    return False


def enviar_para_assinatura(arquivo: str | Path, nome_documento: str, signatarios: list[dict],
                           mensagem: str = "", executar: bool = False) -> dict:
    """Sobe o documento e cria o envelope de assinatura.

    signatarios: [{"nome", "email", "telefone", "cpf", "papel"}]  (papel: cliente | escritorio | testemunha)
    Retorno esperado: {"id": <id do envelope/documento>, "link_assinatura": {...por signatario...},
                       "status": "enviado"}  |  {"_dry_run": True, ...}  |  {"erro": "..."}"""
    raise NotImplementedError(PENDENTE)


def consultar_assinatura(documento_id: str) -> dict:
    """Status do envelope: {"id", "status": pendente|assinado|recusado|expirado,
    "signatarios": [{"nome", "assinou_em"}], "arquivo_assinado_url"}."""
    raise NotImplementedError(PENDENTE)


def baixar_assinado(documento_id: str, destino: str | Path) -> Path:
    """Baixa o PDF assinado para `destino` (a pasta 00_CONTRATACAO do cliente no OneDrive)."""
    raise NotImplementedError(PENDENTE)


def consultar_andamento(numero_processo: str, desde: str | None = None) -> list[dict]:
    """Andamentos do processo acompanhados pela plataforma, mais recente primeiro:
    [{"data", "descricao", "tribunal", "link"}]."""
    raise NotImplementedError(PENDENTE)
