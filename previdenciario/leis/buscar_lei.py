"""Busca no banco de leis previdenciario.

    python previdenciario/leis/buscar_lei.py "qualidade de segurado"        # busca livre (todas as normas)
    python previdenciario/leis/buscar_lei.py --lei 8213 --art 15            # artigo exato
    python previdenciario/leis/buscar_lei.py --lei EC103 --art 15
    python previdenciario/leis/buscar_lei.py L8213 29-C                     # forma curta (sigla + artigo)
    python previdenciario/leis/buscar_lei.py --lei 8742 "deficiencia"       # busca livre so numa norma
    python previdenciario/leis/buscar_lei.py --normas                       # lista as normas do banco

--lei aceita a sigla (L8213, D3048, EC103, IN128, CPC...), o numero (8213, 3048, 103, 128, 13105) ou apelido
(LOAS, RPS, JEF, LBI, PBPS, PCSS).
"""
import argparse
import re
import sqlite3
import sys
from pathlib import Path

DB = Path(__file__).resolve().parent / 'banco_leis.db'


def _con():
    if not DB.exists():
        sys.exit('Banco nao encontrado (%s). Rode montar_banco_leis.py.' % DB)
    return sqlite3.connect(DB)


def resolver_lei(lei):
    """Sigla oficial a partir de sigla, numero ou apelido."""
    q = lei.upper().replace('.', '').replace(' ', '')
    with _con() as c:
        normas = c.execute('SELECT sigla, apelidos FROM normas').fetchall()
    for sigla, apel in normas:
        if q == sigla or q in (apel or '').upper().split():
            return sigla
    so_num = re.sub(r'\D', '', q.split('/')[0])
    achadas = [s for s, _ in normas if so_num and re.sub(r'\D', '', s) == so_num]
    if len(achadas) == 1:
        return achadas[0]
    return None


def norm_art(art):
    a = art.upper().replace('ART.', '').replace('ART', '').strip()
    a = re.sub(r'[º°]|(?<=\d)O\b', '', a).replace('.', '').replace(' ', '')
    a = re.sub(r'^(\d+)([A-Z]{1,2})$', r'\1-\2', a)          # 29A -> 29-A
    return a


def artigo(sigla, art):
    with _con() as c:
        return c.execute('SELECT sigla, art, texto FROM artigos WHERE sigla = ? AND art = ? ORDER BY id',
                         (sigla.upper(), norm_art(art))).fetchall()


def buscar(q, n=8, sigla=None):
    """Frase exata primeiro; completa com os artigos que tem todos os termos."""
    palavras = [t.replace('"', '') for t in q.split() if t.replace('"', '')]
    if not palavras:
        return []
    consultas = ['"%s"' % ' '.join(palavras)]
    if len(palavras) > 1:
        consultas.append(' '.join('"%s"' % t for t in palavras))
    filtro = ' AND sigla = ?' if sigla else ''
    vistos, res = set(), []
    with _con() as c:
        for mq in consultas:
            args = [mq] + ([sigla] if sigla else []) + [n]
            for rid, s, a, trecho in c.execute(
                    'SELECT rowid, sigla, art, snippet(artigos_fts, 2, "[", "]", " ... ", 30) FROM artigos_fts '
                    'WHERE artigos_fts MATCH ?' + filtro + ' ORDER BY rank LIMIT ?', args):
                if rid not in vistos and len(res) < n:
                    vistos.add(rid)
                    res.append((s, a, trecho))
    return res


def listar_normas():
    with _con() as c:
        return c.execute('SELECT n.sigla, n.nome, n.baixado_em, COUNT(a.id) FROM normas n '
                         'LEFT JOIN artigos a ON a.sigla = n.sigla AND a.art <> "ANEXOS" '
                         'GROUP BY n.sigla ORDER BY n.rowid').fetchall()


def aviso(sigla):
    with _con() as c:
        r = c.execute('SELECT aviso, baixado_em, url FROM normas WHERE sigla = ?', (sigla,)).fetchone()
    return r or (None, None, None)


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    ap = argparse.ArgumentParser(description='Busca no banco de leis previdenciario')
    ap.add_argument('termos', nargs='*', help='termos da busca livre, ou SIGLA ARTIGO')
    ap.add_argument('--lei', help='sigla, numero ou apelido da norma (8213, EC103, LOAS...)')
    ap.add_argument('--art', help='numero do artigo (15, 29-C, 1.015)')
    ap.add_argument('-n', type=int, default=8, help='maximo de resultados da busca livre')
    ap.add_argument('--normas', action='store_true', help='lista as normas do banco')
    a = ap.parse_args()

    if a.normas:
        for s, nome, dt, q in listar_normas():
            print('%-7s %4d arts  baixado %s  %s' % (s, q, dt, nome))
        return

    lei, art, termos = a.lei, a.art, a.termos
    # forma curta herdada do padrao: "L8213 15"
    if not lei and not art and len(termos) == 2 and termos[1][:1].isdigit() and resolver_lei(termos[0]):
        lei, art, termos = termos[0], termos[1], []

    sigla = None
    if lei:
        sigla = resolver_lei(lei)
        if not sigla:
            sys.exit('Nao conheco a norma "%s". Use --normas para ver a lista.' % lei)

    if art:
        if not sigla:
            sys.exit('Informe a norma: --lei 8213 --art 15')
        r = artigo(sigla, art)
        if not r:
            print('Nao achei o art. %s em %s (pode estar revogado ou nao existir).' % (art, sigla))
            return
        av, dt, url = aviso(sigla)
        if len(r) > 1:
            print('[atencao] %d trechos comecam com "Art. %s" nessa norma (ex.: artigo citado dentro de outro). '
                  'Todos abaixo.\n' % (len(r), norm_art(art)))
        print('\n\n'.join('%s art. %s\n%s' % x for x in r))
        print('\n-- fonte: %s (baixado em %s)' % (url, dt))
        if av:
            print('-- aviso: %s' % av)
        return

    if not termos:
        ap.print_help()
        return
    res = buscar(' '.join(termos), a.n, sigla)
    if not res:
        print('Nada encontrado.')
    for s, n, t in res:
        print('%s art. %s: %s\n' % (s, n, t.replace('\n', ' ')))


if __name__ == '__main__':
    main()
