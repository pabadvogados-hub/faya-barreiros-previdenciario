"""Banco de leis PREVIDENCIARIO do escritorio: baixa o texto VIGENTE das normas usadas nas pecas
previdenciarias, corta por artigo e indexa (SQLite FTS5) para busca rapida pelos agentes e pelo painel.

    python previdenciario/leis/montar_banco_leis.py            # baixa/atualiza tudo (reconstroi do zero)
    python previdenciario/leis/montar_banco_leis.py --so-indexar   # so refaz o .db e o indice com os textos ja baixados

Mesma mecanica da base tributaria (LAIS_TORRES_ADVOGADOS/tributario/leis): download do Planalto, limpeza,
corte por artigo, SQLite FTS5 sem acento.
Texto riscado no Planalto (<strike>/<s>/<del> e trechos com text-decoration:line-through) = revogado: sai do texto.
A IN PRES/INSS 128/2022 vem do DOU (in.gov.br) em REDACAO ORIGINAL (o DOU nao consolida as alteracoes).
Saida: textos/<SIGLA>.txt, banco_leis.db (tabelas normas, artigos, artigos_fts), normas.json, 00_INDICE.md.
"""
import argparse
import html
import json
import re
import shutil
import sqlite3
import time
import urllib.request
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

PASTA = Path(__file__).resolve().parent
TEXTOS = PASTA / 'textos'
DB = PASTA / 'banco_leis.db'
INDICE = PASTA / '00_INDICE.md'
PL = 'https://www.planalto.gov.br/ccivil_03/'
DOU = 'https://www.in.gov.br/en/web/dou/-/'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36'
# CPC ja baixado na base tributaria do pacote padrao: copia em vez de baixar de novo (se nao existir, baixa)
CPC_PADRAO = Path(r'C:\AUTOMAÇÕES CLIENTES\LAIS_TORRES_ADVOGADOS\tributario\leis')

# sigla, nome, urls (tenta em ordem), para que serve nas pecas, apelidos aceitos no --lei
NORMAS = [
    ('L8213', 'Lei 8.213/1991 (Planos de Beneficios da Previdencia Social)', [PL + 'leis/l8213cons.htm'],
     'qualidade de segurado e periodo de graca (15), carencia (24-27), aposentadorias, auxilios, pensao (74), salario-maternidade (71), revisao/decadencia (103)',
     ['8213', 'PBPS']),
    ('L8212', 'Lei 8.212/1991 (Custeio da Seguridade Social)', [PL + 'leis/l8212cons.htm'],
     'segurados obrigatorios (12), contribuicoes, salario-de-contribuicao (28), indenizacao de periodo (45-A)',
     ['8212', 'PCSS']),
    ('L8742', 'Lei 8.742/1993 (LOAS - Lei Organica da Assistencia Social)', [PL + 'leis/l8742.htm'],
     'BPC/LOAS (20, 20-B, 21): idoso 65+, pessoa com deficiencia, criterio de renda 1/4, revisao bienal',
     ['8742', 'LOAS']),
    ('D3048', 'Decreto 3.048/1999 (Regulamento da Previdencia Social - RPS)', [PL + 'decreto/d3048compilado.htm', PL + 'decreto/d3048.htm'],
     'regulamento: periodo de graca (13), carencia, atividade especial (64-70), calculo, Anexos (agentes nocivos)',
     ['3048', 'RPS']),
    ('EC103', 'Emenda Constitucional 103/2019 (Reforma da Previdencia)', [PL + 'constituicao/emendas/emc/emc103.htm'],
     'regras de transicao: pontos (15), idade minima (16), pedagio 50% (17), pedagio 100% (20), especial (21), calculo (26), pensao (23)',
     ['103', 'EC103/2019', 'REFORMA']),
    ('EC113', 'Emenda Constitucional 113/2021 (precatorios; SELIC na atualizacao)', [PL + 'constituicao/emendas/emc/emc113.htm'],
     'art. 3: SELIC para correcao e juros nas condenacoes da Fazenda Publica',
     ['113', 'EC113/2021']),
    ('LC142', 'Lei Complementar 142/2013 (aposentadoria da pessoa com deficiencia no RGPS)', [PL + 'leis/lcp/lcp142.htm'],
     'aposentadoria PcD por tempo (3, I-III) e por idade (3, IV), graus de deficiencia, conversao (7)',
     ['142']),
    ('L10259', 'Lei 10.259/2001 (Juizados Especiais Federais)', [PL + 'leis/leis_2001/l10259.htm'],
     'competencia de 60 salarios minimos (3), tutela (4), recursos e uniformizacao (14), RPV (17)',
     ['10259', 'JEF']),
    ('L9876', 'Lei 9.876/1999 (fator previdenciario; calculo do salario-de-beneficio)', [PL + 'leis/l9876.htm'],
     'fator previdenciario, regra de transicao do art. 3 (revisao da vida toda - ja julgada)',
     ['9876']),
    ('L10741', 'Lei 10.741/2003 (Estatuto da Pessoa Idosa)', [PL + 'leis/2003/l10.741.htm'],
     'prioridade de tramitacao (71), BPC do idoso (34)',
     ['10741', 'ESTATUTOIDOSO']),
    ('L13146', 'Lei 13.146/2015 (Estatuto da Pessoa com Deficiencia - LBI)', [PL + '_ato2015-2018/2015/lei/l13146.htm'],
     'conceito de deficiencia (2), avaliacao biopsicossocial (2, par. 1), prioridade (9), auxilio-inclusao (94)',
     ['13146', 'LBI', 'ESTATUTOPCD']),
    ('L14126', 'Lei 14.126/2021 (visao monocular = deficiencia sensorial)', [PL + '_ato2019-2022/2021/lei/l14126.htm'],
     'visao monocular classificada como deficiencia sensorial (1)',
     ['14126']),
    ('L7713', 'Lei 7.713/1988 (Imposto de Renda; isencao por molestia grave)', [PL + 'leis/l7713.htm'],
     'art. 6, XIV e XXI: isencao de IR sobre aposentadoria/pensao por molestia grave',
     ['7713']),
    ('L1060', 'Lei 1.060/1950 (assistencia judiciaria)', [PL + 'leis/l1060.htm'],
     'gratuidade (o grosso foi revogado pelo CPC 98-102; restam dispositivos esparsos)',
     ['1060']),
    ('CPC', 'Codigo de Processo Civil - Lei 13.105/2015', [PL + '_ato2015-2018/2015/lei/l13105.htm'],
     'gratuidade (98-102), tutela de urgencia (300), prova pericial (464-480), cumprimento contra a Fazenda (534-535)',
     ['13105', 'CPC2015']),
    ('IN128', 'Instrucao Normativa PRES/INSS 128/2022 (REDACAO ORIGINAL do DOU)',
     [DOU + 'instrucao-normativa-pres/inss-n-128-de-28-de-marco-de-2022-389275446'],
     'regras e rotinas do INSS: filiacao, CNIS, comprovacao de atividade rural, beneficios, recursos administrativos',
     ['128', 'IN128/2022']),
]
# Pistas de que a pagina baixada e a norma certa (e nao pagina de erro / outra norma)
PISTA = {
    'L8213': 'planos de benefícios da previdência social', 'L8212': 'seguridade social',
    'L8742': 'assistência social', 'D3048': 'regulamento da previdência social', 'EC103': 'emenda constitucional',
    'EC113': 'emenda constitucional', 'LC142': 'pessoa com deficiência', 'L10259': 'juizados especiais',
    'L9876': 'contribuição previdenciária', 'L10741': 'pessoa idosa', 'L13146': 'pessoa com deficiência',
    'L14126': 'visão monocular', 'L7713': 'imposto de renda', 'L1060': 'assistência judiciária',
    'CPC': 'código de processo civil', 'IN128': 'instrução normativa pres/inss nº 128',
}
# Tamanho minimo do texto limpo (padrao 3000); lei curtissima precisa de excecao
MINIMO = {'L14126': 500}
# Avisos fixos que vao para o indice
AVISOS = {
    'IN128': 'Texto do DOU de 29/03/2022 em REDACAO ORIGINAL: nao traz as alteracoes posteriores das INs '
             'PRES/INSS que a modificaram. Antes de citar artigo da IN 128, conferir a redacao atual '
             '(consolidada no portal do INSS / Normas.gov.br).',
    'L1060': 'Arts. 2, 3, 4, 6, 7, 11, 12 e 17 foram revogados pelo CPC/2015 (art. 1.072, III): gratuidade hoje e CPC 98-102.',
    'CPC': 'Texto copiado da base tributaria (LAIS_TORRES_ADVOGADOS/tributario/leis/textos/CPC.txt); '
           'data do download e a da base de origem.',
}

# Pendencias conhecidas (registradas no indice; nao entram no banco)
PENDENTES_FIXAS = [
    ('IN128-CONSOLIDADA', 'IN PRES/INSS 128/2022 com todas as alteracoes (texto consolidado)',
     'https://www.in.gov.br/en/web/dou/-/instrucao-normativa-pres/inss-n-128-de-28-de-marco-de-2022-389275446',
     'O DOU so tem a redacao original (que esta no banco como IN128). Nao ha fonte oficial consolidada limpa '
     'para baixar automaticamente; conferir alteracoes manualmente antes de citar.'),
]


def baixar(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Language': 'pt-BR'})
    with urllib.request.urlopen(req, timeout=90) as r:
        bruto = r.read()
    for cod in ('utf-8', 'cp1252'):
        try:
            return bruto.decode(cod)
        except UnicodeDecodeError:
            continue
    return bruto.decode('latin-1')


BLOCO = {'p', 'div', 'li', 'tr', 'table', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ul', 'ol'}
VAZIAS = {'br', 'img', 'hr', 'meta', 'link', 'input', 'col', 'area', 'base', 'wbr'}


class _Limpa(HTMLParser):
    """Tira do HTML o que esta riscado (revogado): <strike>/<s>/<del> ate o fechamento (como o padrao) e
    elementos com text-decoration:line-through (que o Planalto usa nas paginas 'cons'). Um <span> riscado
    termina, no maximo, no fim do paragrafo em que esta (como o navegador faz)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.pula = None      # [tag, profundidade, eh_line_through]
        self.ignora = 0       # script/style/head

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'head'):
            self.ignora += 1
            return
        estilo = (dict(attrs).get('style') or '').lower().replace(' ', '')
        if self.pula:
            t, n, lt = self.pula
            if lt and t != 'p' and tag in BLOCO:          # span riscado nao atravessa paragrafo
                self.pula = None
            elif lt and t == 'p' and tag in BLOCO:        # <p> riscado sem </p>: o proximo bloco fecha
                self.pula = None
            elif tag == t:
                self.pula[1] += 1
                return
            else:
                return
        if tag in ('strike', 's', 'del'):
            self.pula = [tag, 1, False]
            return
        if 'line-through' in estilo and tag not in VAZIAS:
            self.pula = [tag, 1, True]
            return
        if tag == 'br':
            self.out.append('\n')
        elif tag in BLOCO:
            self.out.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'br' and not self.pula and not self.ignora:
            self.out.append('\n')

    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'head'):
            self.ignora = max(0, self.ignora - 1)
            return
        if self.pula:
            t, n, lt = self.pula
            if tag == t:
                self.pula[1] -= 1
                if self.pula[1] <= 0:
                    self.pula = None
            elif lt and tag == 'p':                         # fim do paragrafo encerra o span riscado
                self.pula = None
                self.out.append('\n')
            return
        if tag in BLOCO:
            self.out.append('\n')

    def handle_data(self, d):
        if not self.pula and not self.ignora:
            self.out.append(d)


def limpar(h):
    p = _Limpa()
    p.feed(h)
    p.close()
    t = html.unescape(''.join(p.out)).replace('\xa0', ' ')
    t = re.sub(r'[ \t\r\f\v]+', ' ', t)
    t = re.sub(r'\n\s*\n+', '\n', t)
    return '\n'.join(l.strip() for l in t.splitlines() if l.strip())


def cortar_rodape(t):
    """Planalto: depois de 'Este texto nao substitui o publicado no DOU' vem nota de rodape historica (redacao
    antiga de MP, tabelas de 1998...), que duplicaria artigos com texto velho. So corta se o que sobra depois da
    ULTIMA ocorrencia for pequeno (no Decreto 3.048 a frase aparece antes do Regulamento, que tem de ficar)."""
    ms = list(re.finditer(r'Este texto n[ãa]o substitui o publicado[^\n]*(\n[^\n]*\d{1,2}\.\d{1,2}\.\d{2,4}[^\n]*){0,2}', t))
    if not ms:
        return t
    fim = ms[-1].end()
    return t[:fim] if len(t) - fim < 0.2 * len(t) else t


def recortar_dou(h):
    """Pagina do in.gov.br: so o bloco do ato (div texto-dou), sem o portal."""
    i = h.find('class="texto-dou"')
    if i < 0:
        return None
    j = h.find('informacao-conteudo-dou', i)
    return h[h.rfind('<', 0, i):j if j > 0 else len(h)]


ART = re.compile(r'^Art\.?\s*(\d+(?:\.\d+)?)\s*[º°o]?\s*(?:-\s*([A-Z]{1,2}))?\b', re.M)
ANEXO = re.compile(r'^A ?N ?E ?X ?O(\s+[IVXL]+|\s+ÚNICO)?\s*\.?$', re.M)


def cortar_artigos(texto):
    # o que vem depois do primeiro "ANEXO" (linha sozinha) nao e artigo da norma: vira um bloco "ANEXOS"
    fim_arts = len(texto)
    ultimo_art = None
    for m in ART.finditer(texto):
        ultimo_art = m.start()
    for m in ANEXO.finditer(texto):
        if ultimo_art is not None and m.start() > len(texto) * 0.5:
            fim_arts = m.start()
            break
    corpo_arts = texto[:fim_arts]
    pos = [(m.start(), m.group(1).replace('.', '') + ('-' + m.group(2) if m.group(2) else ''))
           for m in ART.finditer(corpo_arts)]
    arts = []
    for i, (ini, num) in enumerate(pos):
        fim = pos[i + 1][0] if i + 1 < len(pos) else len(corpo_arts)
        corpo = corpo_arts[ini:fim].strip()
        if len(corpo) > 12:
            arts.append((num, corpo[:20000]))
    anexos = texto[fim_arts:].strip()
    if anexos:
        arts.append(('ANEXOS', anexos))
    return arts


def indexar(meta):
    DB.unlink(missing_ok=True)
    c = sqlite3.connect(DB)
    c.executescript('''
      CREATE TABLE normas (sigla TEXT PRIMARY KEY, nome TEXT, uso TEXT, url TEXT, baixado_em TEXT, caracteres INT,
                           apelidos TEXT, aviso TEXT);
      CREATE TABLE artigos (id INTEGER PRIMARY KEY, sigla TEXT, art TEXT, texto TEXT);
      CREATE INDEX ix_artigos ON artigos (sigla, art);
      CREATE VIRTUAL TABLE artigos_fts USING fts5(sigla, art, texto, content='artigos', content_rowid='id',
                                                  tokenize='unicode61 remove_diacritics 2');''')
    for m in meta:
        arq = TEXTOS / (m['sigla'] + '.txt')
        if not arq.exists():
            continue
        txt = arq.read_text(encoding='utf-8')
        c.execute('INSERT INTO normas VALUES (?,?,?,?,?,?,?,?)',
                  (m['sigla'], m['nome'], m['uso'], m.get('url'), m.get('baixado_em'), len(txt),
                   ' '.join(m.get('apelidos', [])), m.get('aviso')))
        for num, corpo in cortar_artigos(txt):
            cur = c.execute('INSERT INTO artigos (sigla, art, texto) VALUES (?,?,?)', (m['sigla'], num, corpo))
            c.execute('INSERT INTO artigos_fts (rowid, sigla, art, texto) VALUES (?,?,?,?)',
                      (cur.lastrowid, m['sigla'], num, corpo))
    c.commit()
    n = c.execute('SELECT sigla, COUNT(*) FROM artigos WHERE art <> "ANEXOS" GROUP BY sigla').fetchall()
    c.close()
    return dict(n)


def copiar_cpc(m):
    """CPC: copia o texto da base tributaria do pacote padrao, se existir."""
    src = CPC_PADRAO / 'textos' / 'CPC.txt'
    if not src.exists():
        return False
    shutil.copyfile(src, TEXTOS / 'CPC.txt')
    origem = {}
    try:
        origem = {x['sigla']: x for x in json.loads((CPC_PADRAO / 'normas.json').read_text(encoding='utf-8'))}.get('CPC', {})
    except Exception:
        pass
    m.update(url=origem.get('url', PL + '_ato2015-2018/2015/lei/l13105.htm'),
             baixado_em=origem.get('baixado_em', date.today().isoformat()), fonte='copiado da base tributaria')
    print('[ok] %-9s %8d caracteres  %s (copiado da base tributaria)' % ('CPC', src.stat().st_size, m['nome']))
    return True


def escrever_indice(meta, n, pendentes):
    hoje = date.today().strftime('%d/%m/%Y')
    L = ['# Banco de Leis Previdenciário — Faya Barreiros', '',
         'Montado em %s com as normas que sustentam as peças previdenciárias (RGPS, BPC/LOAS, JEF).' % hoje,
         'Texto **vigente**: o que está riscado no Planalto (revogado) sai do texto. Cada norma é cortada por artigo e',
         'indexada para busca (SQLite FTS5, sem acento). Arquivo gerado por `montar_banco_leis.py` — não editar à mão.',
         '', '## Como usar', '', '```',
         'python previdenciario/leis/buscar_lei.py "qualidade de segurado"        # busca livre',
         'python previdenciario/leis/buscar_lei.py --lei 8213 --art 15            # artigo exato (período de graça)',
         'python previdenciario/leis/buscar_lei.py --lei EC103 --art 15           # regra de pontos',
         'python previdenciario/leis/buscar_lei.py L8213 29-C                     # forma curta (sigla + artigo)',
         'python previdenciario/leis/buscar_lei.py --lei 8742 "deficiência"       # busca livre só numa norma',
         'python previdenciario/leis/montar_banco_leis.py                         # baixa tudo de novo (atualiza)',
         '```', '',
         'Regra: antes de citar um artigo numa peça, puxar o texto daqui (não de memória) e conferir a data em',
         '`normas.json` (`baixado_em`). `--lei` aceita a sigla ou o número (8213, 3048, 103, LOAS, RPS, JEF, LBI...).', '',
         '## Normas (%d no banco)' % len(n), '',
         '| Sigla | Norma | Artigos | Baixado em | Fonte | Para que serve |', '| --- | --- | --- | --- | --- | --- |']
    for m in meta:
        if m['sigla'] not in n:
            continue
        L.append('| %s | %s | %d | %s | [link](%s) | %s |' % (
            m['sigla'], m['nome'], n[m['sigla']], m.get('baixado_em', '?'), m.get('url', ''), m['uso']))
    avisos = [(m['sigla'], m['aviso']) for m in meta if m.get('aviso') and m['sigla'] in n]
    if avisos:
        L += ['', '## Avisos', '']
        L += ['- **%s**: %s' % a for a in avisos]
    L += ['', '## Pendências', '']
    if pendentes:
        L += ['| Item | Norma | Link | Situação |', '| --- | --- | --- | --- |']
        L += ['| %s | %s | [link](%s) | %s |' % p for p in pendentes]
    else:
        L.append('Nenhuma.')
    L += ['', 'Fontes: [Planalto](https://www.planalto.gov.br/ccivil_03/) para leis, decretos, LC e emendas;',
          '[DOU / in.gov.br](https://www.in.gov.br/) para a IN PRES/INSS 128/2022 (redação original).', '']
    INDICE.write_text('\n'.join(L), encoding='utf-8')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--so-indexar', action='store_true')
    a = ap.parse_args()
    TEXTOS.mkdir(parents=True, exist_ok=True)
    meta_arq = PASTA / 'normas.json'
    anterior = {m['sigla']: m for m in json.loads(meta_arq.read_text(encoding='utf-8'))} if meta_arq.exists() else {}
    meta, pendentes = [], []
    for sigla, nome, urls, uso, apelidos in NORMAS:
        m = dict(anterior.get(sigla, {}), sigla=sigla, nome=nome, uso=uso, apelidos=apelidos)
        m.pop('aviso', None)
        if sigla in AVISOS:
            m['aviso'] = AVISOS[sigla]
        if not a.so_indexar:
            ok = False
            if sigla == 'CPC':
                ok = copiar_cpc(m)
            if not ok:
                for u in urls:
                    try:
                        h = baixar(u)
                        if u.startswith(DOU):
                            h = recortar_dou(h)
                            if h is None:
                                print('  %s: pagina do DOU sem o bloco do ato (%s)' % (sigla, u))
                                continue
                        t = limpar(h)
                        if not u.startswith(DOU):
                            t = cortar_rodape(t)
                    except Exception as ex:
                        print('  falhou %s: %s' % (u, ex))
                        continue
                    pista = PISTA.get(sigla)
                    if len(t) < MINIMO.get(sigla, 3000) or (pista and pista.lower() not in t.lower()):
                        print('  %s: pagina sem o texto da norma (%s)' % (sigla, u))
                        continue
                    (TEXTOS / (sigla + '.txt')).write_text(t, encoding='utf-8')
                    m.update(url=u, baixado_em=date.today().isoformat())
                    m.pop('fonte', None)
                    print('[ok] %-9s %8d caracteres  %s' % (sigla, len(t), nome))
                    ok = True
                    break
                time.sleep(1)
            if not ok:
                print('[--] %-9s NAO BAIXADA (%s)' % (sigla, nome))
                (TEXTOS / (sigla + '.txt')).unlink(missing_ok=True)   # nao deixa texto velho fingindo ser atual
                m.pop('baixado_em', None)
        if not (TEXTOS / (sigla + '.txt')).exists():
            pendentes.append((sigla, nome, urls[0], 'download falhou ou pagina sem o texto da norma'))
        meta.append(m)
    pendentes += PENDENTES_FIXAS
    meta_arq.write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding='utf-8')
    n = indexar(meta)
    escrever_indice(meta, n, pendentes)
    print('\nIndexado: %d normas, %d artigos -> %s' % (len(n), sum(n.values()), DB))
    for s, q in sorted(n.items()):
        print('   %-9s %5d artigos' % (s, q))
    if pendentes:
        print('\nPendencias (ver 00_INDICE.md):')
        for p in pendentes:
            print('   %s: %s' % (p[0], p[3]))


if __name__ == '__main__':
    main()
