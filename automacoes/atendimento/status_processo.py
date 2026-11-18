# -*- coding: utf-8 -*-
""""Como esta o meu processo?" — busca no Notion (SO LEITURA) e devolve os dados para o agente de
atendimento redigir a resposta em linguagem simples (POP-ATD-01 / MSG-01).

Nao envia nada ao cliente: imprime o processo, a fase e as ultimas movimentacoes registradas no
Notion. O agente redige; a Barbara confere e envia pelo WhatsApp do escritorio.
O Notion so tem o que a equipe lancou: andamento novo do tribunal se confere no PJe (ou na
Tramitacao Inteligente, enquanto nao houver integracao).

Uso:
    python automacoes/atendimento/status_processo.py --processo 1001234-56.2026.4.01.3300
    python automacoes/atendimento/status_processo.py --telefone 71999999999     (processos do cadastro)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from comum import notion  # noqa: E402
from comum.cadastros import cliente_por_telefone  # noqa: E402
from comum.config import utf8_stdout  # noqa: E402
from comum.nomes import formatar_cnj  # noqa: E402


def resumo(numero: str) -> dict:
    if not notion.configurado("processos"):
        return {"processo": numero, "erro": "Notion nao configurado (NOTION_TOKEN e notion.databases.processos): "
                                            "consulte o processo direto no Notion/PJe"}
    achados = notion.buscar_processo(formatar_cnj(numero) or numero)
    if not achados:
        return {"processo": numero, "erro": "nao encontrado no Notion"}
    if len(achados) > 1:
        return {"processo": numero, "erro": f"{len(achados)} paginas com esse numero no Notion — conferir a mao",
                "paginas": [a.get("url") for a in achados]}
    p = achados[0]
    try:
        movs = notion.ultimas_movimentacoes(p["id"], 8)
    except notion.NotionErro as e:
        movs, p["aviso_andamentos"] = [], str(e)
    return {
        "processo": p.get("numero") or p.get("titulo") or numero,
        "notion_url": p.get("url"),
        "tipo": p.get("tipo"),
        "fase": p.get("fase"),
        "responsavel": p.get("responsavel"),
        "cliente": p.get("cliente"),
        "ultimas_movimentacoes": [{"data": m.get("data"), "texto": (m.get("descricao") or "")[:400]} for m in movs],
        **({"aviso": p["aviso_andamentos"]} if p.get("aviso_andamentos") else {}),
    }


def main():
    utf8_stdout()
    ap = argparse.ArgumentParser(description="Status do processo no Notion (leitura)")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--processo")
    g.add_argument("--telefone")
    a = ap.parse_args()
    if a.processo:
        numeros = [a.processo]
    else:
        c = cliente_por_telefone(a.telefone)
        if not c:
            raise SystemExit("telefone sem cliente em config/clientes.json")
        numeros = [p["numero"] for p in c.get("processos") or [] if p.get("numero")]
        print(f"Cliente: {c.get('nome')} — {len(numeros)} processo(s) no cadastro")
    for n in numeros:
        print(json.dumps(resumo(n), ensure_ascii=False, indent=2, default=str))


if __name__ == "__main__":
    main()
