# -*- coding: utf-8 -*-
"""Gera previdenciario/pecas/00_INDICE.md a partir do frontmatter dos modelos.

    python previdenciario/pecas/indice.py

O índice traz: a lista dos modelos por grupo, o juízo, quantos campos cada um tem, todas as citações
(quantas peças usam cada uma) e TODOS os [CONFERIR]/[ADAPTAR] que vieram dos originais — essa última
parte é a pauta de revisão da Dra. Faya. Rodar de novo sempre que um modelo mudar.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gerar_peca import todos_modelos, ler_modelo, CAMPO  # noqa: E402

AQUI = Path(__file__).resolve().parent
MARCA = re.compile(r"\[(CONFERIR|ADAPTAR)[^\]]*\]")
ORDEM = ["concessao", "revisao", "outras", "relatorio"]
NOMES = {"concessao": "Concessão", "revisao": "Revisão", "outras": "Outras ações", "relatorio": "Relatórios e pareceres"}


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    modelos = todos_modelos()
    citacoes: Counter = Counter()
    linhas = [f"# Índice dos modelos da Dra. Faya\n",
              f"Gerado por `indice.py` em {date.today():%d/%m/%Y}. **{len(modelos)} modelos**, tirados das peças reais dela "
              "e anonimizados (nenhum dado de cliente). Para usar: `python previdenciario/pecas/gerar_peca.py campos <tipo>`.\n"]
    pendencias = []
    for grupo in ORDEM + sorted({m.get("grupo", "-") for _, m in modelos.values()} - set(ORDEM)):
        do_grupo = [(t, a, m) for t, (a, m) in modelos.items() if m.get("grupo", "-") == grupo]
        if not do_grupo:
            continue
        linhas.append(f"\n## {NOMES.get(grupo, grupo)} ({len(do_grupo)})\n")
        linhas.append("| Tipo | Título | Juízo / objetivo | Campos | Pendências herdadas |")
        linhas.append("|---|---|---|---|---|")
        for tipo, arq, meta in sorted(do_grupo):
            _, corpo = ler_modelo(arq)
            campos = len(set(CAMPO.findall(corpo)))
            marcas = [m.group(0) for m in MARCA.finditer(corpo)]
            cits = meta.get("citacoes") or []
            if isinstance(cits, str):
                cits = [cits]
            citacoes.update({c.strip() for c in cits if c.strip()})
            onde = meta.get("juizo") or meta.get("objetivo") or ""
            linhas.append(f"| `{tipo}` | {meta.get('titulo', '')} | {onde} | {campos} | {len(marcas) or '-'} |")
            if marcas:
                pendencias.append((tipo, marcas))

    linhas.append("\n## Pauta de revisão da Dra. Faya: pontos marcados nos modelos\n")
    linhas.append("Estes pontos vieram dos próprios originais (lei citada com número errado, trecho de outro caso, "
                  "frase incompleta) ou são escolha que só ela pode fazer. Enquanto existirem, a peça gerada sai como "
                  "MINUTA.\n")
    for tipo, marcas in pendencias:
        linhas.append(f"- **`{tipo}`**")
        for m in dict.fromkeys(marcas):
            linhas.append(f"  - {m}")

    linhas.append("\n## Citações usadas nos modelos (nº de modelos)\n")
    linhas.append("Lista bruta, como está nas peças. A IA só cita o que está aqui, marcado para conferir vigência.\n")
    for cit, n in sorted(citacoes.items(), key=lambda x: (-x[1], x[0].lower())):
        linhas.append(f"- {cit} — {n}")

    destino = AQUI / "00_INDICE.md"
    destino.write_text("\n".join(linhas) + "\n", "utf-8")
    print(f"{destino} — {len(modelos)} modelos, {len(citacoes)} citações, {sum(len(m) for _, m in pendencias)} marcas.")


if __name__ == "__main__":
    main()
