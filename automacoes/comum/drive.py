# -*- coding: utf-8 -*-
"""Documentos do escritorio no OneDrive/SharePoint, por uma PASTA LOCAL SINCRONIZADA.

Nao ha API da Microsoft aqui (nem app no Azure, nem token): o script grava numa pasta do disco
que o OneDrive sincroniza.
  - Na maquina do escritorio (Windows): a pasta do OneDrive/SharePoint sincronizada pelo cliente
    do OneDrive, ex.: C:\\Users\\<usuario>\\OneDrive - Faya Barreiros\\ESCRITORIO
  - Na VPS (Linux): a mesma biblioteca montada pelo rclone (ver automacoes/README.md, secao
    OneDrive na VPS). Ex.: /mnt/onedrive/ESCRITORIO
A raiz vem de ONEDRIVE_RAIZ em config/.env.

Interface mantida da versao Google Drive do pacote de origem (os chamadores nao mudaram de forma):
    svc = servico()                                   -> a raiz (Path)
    pasta = garantir_caminho(svc, None, ["CLIENTES", "FULANO", "04_SAUDE"], executar=...)
    f = enviar_arquivo(svc, "laudo.pdf", pasta, "2026-11-18_LAUDO_ortopedista.pdf", executar=...)
    f["link"]  -> caminho RELATIVO a raiz ("CLIENTES/FULANO/04_SAUDE/2026-11-18_...pdf"), e o que
                  vai para a tarefa no Notion (o OneDrive de cada pessoa resolve o resto)

Regras:
  - pasta IDEMPOTENTE: existe -> reusa; nunca duplica, nunca apaga, nunca move;
  - arquivo com o mesmo nome e o MESMO conteudo -> nao copia de novo (ja_existia);
    mesmo nome e conteudo DIFERENTE -> grava como "<nome> (2).ext" (nunca sobrescreve);
  - em dry-run nada e criado: pasta que nao existe volta como "DRY:<caminho>".
"""
from __future__ import annotations

import hashlib
import os
import shutil
import subprocess
from pathlib import Path

_NOME_PROIBIDO = ("/", "\\", "..", "\0")


def raiz() -> Path | None:
    v = (os.getenv("ONEDRIVE_RAIZ") or "").strip().strip('"').strip("'")
    return Path(v).expanduser() if v else None


def credenciais_disponiveis() -> bool:
    """True quando ONEDRIVE_RAIZ esta definida e a pasta existe (nome mantido do modulo antigo)."""
    r = raiz()
    return bool(r and r.is_dir())


disponivel = credenciais_disponiveis


def servico() -> Path:
    """Devolve a raiz do OneDrive (o 'servico' da versao antiga). Erro claro se nao houver."""
    r = raiz()
    if not r:
        raise RuntimeError("ONEDRIVE_RAIZ nao definida em config/.env")
    if not r.is_dir():
        raise RuntimeError(f"ONEDRIVE_RAIZ aponta para uma pasta que nao existe: {r} "
                           "(OneDrive sincronizado? rclone montado?)")
    return r


def _base(svc, raiz_id) -> Path:
    base = Path(svc) if svc else servico()
    if raiz_id:
        p = Path(str(raiz_id))
        base = p if p.is_absolute() else base / p
    return base


def link(caminho: str | Path, svc=None) -> str:
    """Caminho relativo a raiz, com '/' (o 'link' que vai para o Notion e para os relatorios)."""
    c = str(caminho)
    if c.startswith("DRY:"):
        c = c[4:]
    r = Path(svc) if svc else raiz()
    try:
        return Path(c).resolve().relative_to(r.resolve()).as_posix() if r else Path(c).as_posix()
    except ValueError:
        return Path(c).as_posix()


def garantir_pasta(svc, nome: str, pai: str | Path, executar=False) -> tuple[str, bool]:
    """Devolve (caminho, criada). Ja existe -> reusa. Em dry-run, pasta inexistente volta como
    'DRY:<caminho>' (e as filhas dela tambem)."""
    nome = str(nome).strip()
    if not nome or any(x in nome for x in _NOME_PROIBIDO):
        raise ValueError(f"nome de pasta invalido: {nome!r}")
    dry = str(pai).startswith("DRY:")
    alvo = Path(str(pai)[4:] if dry else str(pai)) / nome
    if dry:
        return f"DRY:{alvo}", True
    if alvo.is_dir():
        return str(alvo), False
    if alvo.exists():
        raise RuntimeError(f"ja existe um ARQUIVO com o nome da pasta: {alvo}")
    if not executar:
        return f"DRY:{alvo}", True
    alvo.mkdir(parents=False, exist_ok=True)
    return str(alvo), True


def garantir_caminho(svc, raiz_id, partes: list[str], executar=False, log=print) -> str:
    """Garante a cadeia de pastas sob a raiz (ou sob raiz_id: subpasta relativa ou caminho absoluto)."""
    atual = str(_base(svc, raiz_id))
    if not Path(atual).is_dir():
        raise RuntimeError(f"raiz inexistente: {atual}")
    feito = []
    for p in partes:
        feito.append(p)
        atual, criada = garantir_pasta(svc, p, atual, executar)
        if criada and log:
            log(f"    {'[DRY-RUN] criaria' if not executar else 'criada'}: {'/'.join(feito)}")
    return atual


def _hash(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for bloco in iter(lambda: f.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def _destino_livre(pasta: Path, nome: str, conteudo_hash: str) -> tuple[Path, bool]:
    """(destino, ja_existia). Mesmo nome e mesmo conteudo -> o existente; conteudo diferente -> ' (n)'."""
    alvo = pasta / nome
    n = 2
    stem, suf = Path(nome).stem, Path(nome).suffix
    while alvo.exists():
        if alvo.is_file() and _hash(alvo) == conteudo_hash:
            return alvo, True
        alvo = pasta / f"{stem} ({n}){suf}"
        n += 1
    return alvo, False


def _resultado(svc, destino: Path, ja: bool) -> dict:
    rel = link(destino, svc)
    return {"id": rel, "link": rel, "webViewLink": rel, "caminho": str(destino), "ja_existia": ja}


def enviar_arquivo(svc, local: str | Path, pasta_id: str, nome: str | None = None,
                   executar=False, **_ignorado) -> dict:
    """Copia o arquivo para a pasta (copy2: preserva data). Nunca sobrescreve."""
    local = Path(local)
    nome = nome or local.name
    if any(x in nome for x in _NOME_PROIBIDO):
        raise ValueError(f"nome de arquivo invalido: {nome!r}")
    if str(pasta_id).startswith("DRY:"):
        return {"_dry_run": True, "nome": nome, "destino": link(Path(str(pasta_id)[4:]) / nome, svc)}
    destino, ja = _destino_livre(Path(pasta_id), nome, _hash(local))
    if ja:
        return _resultado(svc, destino, True)
    if not executar:
        return {"_dry_run": True, "nome": destino.name, "destino": link(destino, svc)}
    shutil.copy2(local, destino)
    return _resultado(svc, destino, False)


copiar_arquivo = enviar_arquivo


def enviar_bytes(svc, conteudo: bytes, nome: str, pasta_id: str, mime: str | None = None, executar=False) -> dict:
    """Grava bytes (ex.: comprovante baixado do Asaas) como arquivo. `mime` e ignorado (compatibilidade)."""
    if any(x in nome for x in _NOME_PROIBIDO):
        raise ValueError(f"nome de arquivo invalido: {nome!r}")
    if str(pasta_id).startswith("DRY:") or not executar:
        base = Path(str(pasta_id)[4:] if str(pasta_id).startswith("DRY:") else str(pasta_id))
        return {"_dry_run": True, "nome": nome, "destino": link(base / nome, svc)}
    destino, ja = _destino_livre(Path(pasta_id), nome, hashlib.sha256(conteudo).hexdigest())
    if not ja:
        destino.write_bytes(conteudo)
    return _resultado(svc, destino, ja)


# ------------------------------------------------------------------ docx -> pdf

def _soffice() -> str | None:
    for nome in ("soffice", "libreoffice"):
        achado = shutil.which(nome)
        if achado:
            return achado
    for c in (r"C:\Program Files\LibreOffice\program\soffice.exe",
              r"C:\Program Files (x86)\LibreOffice\program\soffice.exe"):
        if Path(c).exists():
            return c
    return None


def docx_para_pdf(docx: str | Path, destino_dir: str | Path | None = None) -> Path | None:
    """Converte .docx em PDF com o LibreOffice em modo headless (VPS: apt install libreoffice-writer).
    Devolve o caminho do PDF, ou None com AVISO se o LibreOffice nao estiver instalado (nesse caso,
    gere o PDF pelo Word: Arquivo > Salvar como > PDF)."""
    exe = _soffice()
    docx = Path(docx)
    if not exe:
        print("  AVISO: LibreOffice nao encontrado: PDF nao gerado. Instale (VPS: apt install "
              "libreoffice-writer) ou salve o PDF pelo Word.")
        return None
    saida = Path(destino_dir) if destino_dir else docx.parent
    saida.mkdir(parents=True, exist_ok=True)
    r = subprocess.run([exe, "--headless", "--convert-to", "pdf", "--outdir", str(saida), str(docx)],
                       capture_output=True, text=True, timeout=180)
    pdf = saida / (docx.stem + ".pdf")
    if r.returncode != 0 or not pdf.exists():
        print(f"  AVISO: conversao para PDF falhou: {(r.stderr or r.stdout).strip()[:300]}")
        return None
    return pdf
