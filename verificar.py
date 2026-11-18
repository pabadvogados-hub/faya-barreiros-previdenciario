# -*- coding: utf-8 -*-
"""Confere o pacote inteiro em uma rodada, sem rede e sem credencial.

    python verificar.py

Roda: teste offline das automações, testes da calculadora, teste do painel, gerador de peças, base de leis e o
índice dos modelos. Tudo com dados fictícios e pastas temporárias. Sai com código 1 se algo falhar.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
PY = sys.executable

ETAPAS = [
    ("Automações (Asaas, Notion, OneDrive, controladoria, financeiro)", [PY, "automacoes/testes/teste_offline.py"], "TUDO OK"),
    ("Calculadora previdenciária (EC 103, tempo, carência, graça)", [PY, "-m", "unittest", "-q", "test_calculos"], "OK",
     "previdenciario/calculos"),
    ("Painel das demandas externas + link dos parceiros", [PY, "automacoes/painel/teste_painel.py"], "TUDO OK"),
    ("Modelos de peça da Dra. Faya", [PY, "previdenciario/pecas/gerar_peca.py", "listar"], "modelos."),
    ("Base de leis (art. 15 da Lei 8.213)", [PY, "previdenciario/leis/buscar_lei.py", "--lei", "8213", "--art", "15"],
     "qualidade de segurado"),
    ("Índice e pauta de revisão dos modelos", [PY, "previdenciario/pecas/indice.py"], "modelos"),
]


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    falhas = 0
    for etapa in ETAPAS:
        nome, cmd, esperado = etapa[:3]
        cwd = RAIZ / etapa[3] if len(etapa) > 3 else RAIZ
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        saida = (r.stdout or "") + (r.stderr or "")
        ok = r.returncode == 0 and esperado.lower() in saida.lower()
        falhas += not ok
        print(f"[{'ok' if ok else 'FALHOU'}] {nome}")
        if not ok:
            print("      " + "\n      ".join(saida.strip().splitlines()[-15:]))
    print("\nPACOTE OK" if not falhas else f"\n{falhas} etapa(s) com falha")
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()
