# -*- coding: utf-8 -*-
"""Peças e relatórios previdenciários no papel timbrado da Dra. Faya.

Os modelos ficam em previdenciario/pecas/iniciais/ e previdenciario/pecas/relatorios/ (Markdown com
frontmatter + corpo com {{CAMPOS}}). Foram tirados das peças reais da Dra. Faya, sem dado de cliente.

    python previdenciario/pecas/gerar_peca.py listar
    python previdenciario/pecas/gerar_peca.py campos aposentadoria-especial-ruido
    python previdenciario/pecas/gerar_peca.py preencher aposentadoria-especial-ruido --dados caso.json --saida minuta.md
    python previdenciario/pecas/gerar_peca.py docx minuta.md --saida minuta.docx
    python previdenciario/pecas/gerar_peca.py conferir minuta.md

Fluxo pensado para o Claude Code (agente `previdenciario`): o agente lê o modelo e os documentos do
cliente, escreve a minuta em Markdown (fatos narrados, cálculo do POP-PREV-02, [CONFERIR] onde faltar
dado) e só então este script põe a minuta no timbrado. O script NÃO protocola, NÃO envia e NÃO chama IA.

Trava: `docx` grava o arquivo mesmo com pendência (é minuta para revisão), mas imprime a lista do que
falta e põe "MINUTA - NÃO PROTOCOLAR" no topo enquanto houver {{campo}}, [CONFERIR], [NARRAR] ou
[INSERIR IMAGEM] no texto.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PASTAS = [AQUI / "iniciais", AQUI / "relatorios"]
TIMBRADO = AQUI.parent / "timbrado" / "timbrado_faya.docx"

COR_DESTAQUE = "4E151C"      # bordô do timbrado da Dra. Faya
FONTE, TAMANHO, ESPACO, RECUO_CM = "Times New Roman", 12, 1.5, 1.25

CAMPO = re.compile(r"\{\{\s*([A-Za-z0-9_]+)\s*\}\}")
PENDENCIAS = [
    (CAMPO, "campo não preenchido"),
    (re.compile(r"\[\s*CONFERIR[^\]]*\]", re.I), "ponto a conferir"),
    (re.compile(r"\[\s*A CONFIRMAR[^\]]*\]", re.I), "dado a confirmar"),
    (re.compile(r"\[\s*NARRAR[^\]]*\]", re.I), "trecho de fatos a narrar"),
    (re.compile(r"\[\s*INSERIR IMAGEM[^\]]*\]", re.I), "imagem/recorte a inserir"),
]


def utf8():
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass


# ------------------------------------------------------------------ modelos

def ler_modelo(caminho: Path) -> tuple[dict, str]:
    """Frontmatter simples ('chave: valor' e listas '  - item') + corpo."""
    txt = caminho.read_text("utf-8")
    meta: dict = {}
    corpo = txt
    if txt.startswith("---"):
        _, fm, corpo = txt.split("---", 2)
        chave = None
        for linha in fm.splitlines():
            if not linha.strip():
                continue
            m = re.match(r"^\s*-\s+(.*)$", linha)
            if m and chave:
                if not isinstance(meta.get(chave), list):
                    meta[chave] = []
                meta[chave].append(m.group(1).strip())
                continue
            m = re.match(r"^([\w\-]+):\s*(.*)$", linha)
            if m:
                chave, valor = m.group(1), m.group(2).strip()
                meta[chave] = valor if valor else []
    return meta, corpo.strip() + "\n"


def todos_modelos() -> dict[str, tuple[Path, dict]]:
    achados = {}
    for pasta in PASTAS:
        for arq in sorted(pasta.glob("*.md")):
            if arq.name.startswith(("00_", "README")):
                continue
            meta, _ = ler_modelo(arq)
            achados[meta.get("tipo") or arq.stem] = (arq, meta)
    return achados


def achar(tipo: str) -> tuple[Path, dict, str]:
    modelos = todos_modelos()
    if tipo not in modelos:
        parecidos = [t for t in modelos if tipo.lower() in t]
        raise SystemExit(f"Modelo '{tipo}' não existe." + (f" Parecidos: {', '.join(parecidos)}" if parecidos else
                                                             " Rode: gerar_peca.py listar"))
    arq, meta = modelos[tipo]
    return arq, meta, ler_modelo(arq)[1]


def pendencias(texto: str) -> list[str]:
    saida = []
    for rx, motivo in PENDENCIAS:
        for m in rx.finditer(texto):
            saida.append(f"{motivo}: {m.group(0)[:90]}")
    return saida


# ------------------------------------------------------------------ comandos

def cmd_listar(_a):
    modelos = todos_modelos()
    if not modelos:
        print("Nenhum modelo encontrado em", ", ".join(str(p) for p in PASTAS))
        return
    por_grupo: dict[str, list] = {}
    for tipo, (_, meta) in modelos.items():
        por_grupo.setdefault(meta.get("grupo") or "-", []).append((tipo, meta.get("titulo", "")))
    for grupo in sorted(por_grupo):
        print(f"\n[{grupo.upper()}]")
        for tipo, titulo in por_grupo[grupo]:
            print(f"  {tipo:<58} {titulo}")
    print(f"\n{len(modelos)} modelos.")


def cmd_campos(a):
    arq, meta, corpo = achar(a.tipo)
    print(f"{meta.get('titulo', a.tipo)}  ({arq.relative_to(AQUI.parent.parent)})\n")
    campos = sorted(dict.fromkeys(m.group(1) for m in CAMPO.finditer(corpo)))
    print("Campos:", ", ".join(campos) or "-")
    for chave in ("documentos_necessarios", "citacoes"):
        if meta.get(chave):
            print(f"\n{chave.replace('_', ' ').capitalize()}:")
            for item in meta[chave]:
                print("  -", item)
    if a.json:
        print("\nModelo de JSON para --dados:")
        print(json.dumps({c: "" for c in campos}, ensure_ascii=False, indent=2))


def cmd_preencher(a):
    _, meta, corpo = achar(a.tipo)
    dados = json.loads(Path(a.dados).read_text("utf-8")) if a.dados else {}
    faltando = []

    def troca(m):
        v = dados.get(m.group(1))
        if v is None or str(v).strip() == "":
            faltando.append(m.group(1))
            return m.group(0)
        return str(v)

    texto = CAMPO.sub(troca, corpo)
    destino = Path(a.saida or f"{a.tipo}_minuta.md")
    destino.write_text(texto, "utf-8")
    print(f"Minuta em Markdown: {destino}")
    if faltando:
        print(f"Campos sem valor ({len(set(faltando))}):", ", ".join(sorted(set(faltando))))
    print("Próximo passo: completar fatos/cálculo, rodar `conferir` e depois `docx`.")


def cmd_conferir(a):
    texto = Path(a.arquivo).read_text("utf-8")
    p = pendencias(texto)
    if not p:
        print("Sem pendência marcada. Ainda assim: revisão humana da Dra. Faya antes de protocolar.")
        return
    print(f"{len(p)} pendência(s):")
    for item in p:
        print("  -", item)
    sys.exit(1)


# ------------------------------------------------------------------ docx no timbrado

def _doc_timbrado():
    from docx import Document
    from docx.oxml.ns import qn
    from docx.shared import Pt
    if not TIMBRADO.exists():
        raise SystemExit(f"Timbrado não encontrado: {TIMBRADO}")
    doc = Document(str(TIMBRADO))
    corpo = doc.element.body
    for el in list(corpo):
        if el.tag != qn("w:sectPr"):
            corpo.remove(el)
    estilo = doc.styles["Normal"]
    estilo.font.name, estilo.font.size = FONTE, Pt(TAMANHO)
    return doc


def _runs(p, texto, negrito_base=False):
    """**negrito**, *itálico* e marcas de pendência em vermelho."""
    from docx.shared import RGBColor
    marca = re.compile(r"(\{\{[^}]+\}\}|\[(?:CONFERIR|A CONFIRMAR|NARRAR|INSERIR IMAGEM)[^\]]*\])", re.I)
    for i, parte in enumerate(re.split(r"\*\*", texto)):
        negrito = negrito_base or (i % 2 == 1)
        for j, sub in enumerate(re.split(r"(?<!\*)\*(?!\*)", parte)):
            for pedaco in marca.split(sub):
                if not pedaco:
                    continue
                r = p.add_run(pedaco)
                r.bold, r.italic = negrito, (j % 2 == 1)
                if marca.fullmatch(pedaco):
                    r.bold, r.font.color.rgb = True, RGBColor(0xC0, 0x00, 0x00)


def _formatar(p, alinhar="justify", recuo=False, depois=6):
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
    from docx.shared import Cm, Pt
    p.alignment = {"justify": WD_ALIGN_PARAGRAPH.JUSTIFY, "center": WD_ALIGN_PARAGRAPH.CENTER,
                   "left": WD_ALIGN_PARAGRAPH.LEFT}[alinhar]
    f = p.paragraph_format
    f.line_spacing_rule, f.line_spacing, f.space_after = WD_LINE_SPACING.MULTIPLE, ESPACO, Pt(depois)
    if recuo:
        f.first_line_indent = Cm(RECUO_CM)


def _tabela(doc, linhas):
    from docx.oxml import parse_xml
    from docx.oxml.ns import nsdecls
    from docx.shared import Pt, RGBColor
    celulas = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in linhas
               if not re.match(r"^\s*\|?\s*:?-{2,}", ln)]
    if not celulas:
        return
    ncol = max(len(c) for c in celulas)
    t = doc.add_table(rows=0, cols=ncol)
    t.style = "Table Grid"
    for i, linha in enumerate(celulas):
        cels = t.add_row().cells
        for k in range(ncol):
            p = cels[k].paragraphs[0]
            _runs(p, linha[k] if k < len(linha) else "", negrito_base=(i == 0))
            for r in p.runs:
                r.font.size = Pt(9)
                if i == 0:
                    r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            if i == 0:
                cels[k]._tc.get_or_add_tcPr().append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{COR_DESTAQUE}"/>'))
    doc.add_paragraph()


def markdown_para_docx(texto: str, destino: Path, minuta: bool) -> Path:
    from docx.shared import Cm, Pt, RGBColor
    doc = _doc_timbrado()
    cor = RGBColor.from_string(COR_DESTAQUE)
    if minuta:
        p = doc.add_paragraph()
        _formatar(p, "center")
        r = p.add_run("MINUTA - NÃO PROTOCOLAR - PENDÊNCIAS MARCADAS EM VERMELHO")
        r.bold, r.font.color.rgb = True, RGBColor(0xC0, 0x00, 0x00)
    blocos = re.split(r"\n\s*\n", texto.strip())
    for bloco in blocos:
        linhas = [ln.rstrip() for ln in bloco.splitlines() if ln.strip()]
        if not linhas:
            continue
        if all(ln.lstrip().startswith("|") for ln in linhas):
            _tabela(doc, linhas)
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", linhas[0])
        if m:
            p = doc.add_paragraph()
            nivel = len(m.group(1))
            _formatar(p, "center" if nivel == 1 else "justify", depois=8)
            p.paragraph_format.space_before = Pt(10 if nivel > 1 else 0)
            r = p.add_run(m.group(2).replace("**", "").upper() if nivel <= 2 else m.group(2).replace("**", ""))
            r.bold, r.font.color.rgb = True, cor
            if nivel == 1:
                r.font.size = Pt(14)
            linhas = linhas[1:]
            if not linhas:
                continue
        if all(re.match(r"^\s*([-*]|\d+[.)])\s+", ln) for ln in linhas):
            for ln in linhas:
                p = doc.add_paragraph()
                _formatar(p, depois=2)
                p.paragraph_format.left_indent = Cm(0.8)
                item = re.sub(r"^\s*[-*]\s+", "• ", ln)
                _runs(p, item.strip())
            continue
        if all(ln.startswith(">") for ln in linhas):          # citação (ementa, doutrina)
            p = doc.add_paragraph()
            _formatar(p, depois=8)
            p.paragraph_format.left_indent = Cm(4)
            _runs(p, " ".join(ln.lstrip("> ").strip() for ln in linhas))
            for r in p.runs:
                r.font.size = Pt(10)
            continue
        p = doc.add_paragraph()
        _formatar(p, recuo=True)
        _runs(p, " ".join(linhas))
    destino.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(destino))
    return destino


def cmd_docx(a):
    origem = Path(a.arquivo)
    texto = origem.read_text("utf-8")
    if texto.startswith("---"):
        texto = texto.split("---", 2)[2]
    p = pendencias(texto)
    destino = markdown_para_docx(texto, Path(a.saida or origem.with_suffix(".docx")), minuta=bool(p))
    print(f"Documento no timbrado: {destino}")
    if p:
        print(f"ATENÇÃO: {len(p)} pendência(s) - o arquivo saiu como MINUTA. Rode `conferir` para a lista.")
    print("Revisão humana da Dra. Faya antes de qualquer protocolo. O script não protocola.")


def main():
    utf8()
    ap = argparse.ArgumentParser(description="Peças previdenciárias no timbrado da Dra. Faya",
                                 formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("listar").set_defaults(f=cmd_listar)
    c = sub.add_parser("campos")
    c.add_argument("tipo")
    c.add_argument("--json", action="store_true", help="imprime um JSON vazio com os campos")
    c.set_defaults(f=cmd_campos)
    p = sub.add_parser("preencher")
    p.add_argument("tipo")
    p.add_argument("--dados", help="JSON {CAMPO: valor}")
    p.add_argument("--saida")
    p.set_defaults(f=cmd_preencher)
    d = sub.add_parser("docx")
    d.add_argument("arquivo")
    d.add_argument("--saida")
    d.set_defaults(f=cmd_docx)
    k = sub.add_parser("conferir")
    k.add_argument("arquivo")
    k.set_defaults(f=cmd_conferir)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
