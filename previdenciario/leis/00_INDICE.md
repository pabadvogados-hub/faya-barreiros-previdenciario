# Banco de Leis Previdenciário — Faya Barreiros

Montado em 18/11/2026 com as normas que sustentam as peças previdenciárias (RGPS, BPC/LOAS, JEF).
Texto **vigente**: o que está riscado no Planalto (revogado) sai do texto. Cada norma é cortada por artigo e
indexada para busca (SQLite FTS5, sem acento). Arquivo gerado por `montar_banco_leis.py` — não editar à mão.

## Como usar

```
python previdenciario/leis/buscar_lei.py "qualidade de segurado"        # busca livre
python previdenciario/leis/buscar_lei.py --lei 8213 --art 15            # artigo exato (período de graça)
python previdenciario/leis/buscar_lei.py --lei EC103 --art 15           # regra de pontos
python previdenciario/leis/buscar_lei.py L8213 29-C                     # forma curta (sigla + artigo)
python previdenciario/leis/buscar_lei.py --lei 8742 "deficiência"       # busca livre só numa norma
python previdenciario/leis/montar_banco_leis.py                         # baixa tudo de novo (atualiza)
```

Regra: antes de citar um artigo numa peça, puxar o texto daqui (não de memória) e conferir a data em
`normas.json` (`baixado_em`). `--lei` aceita a sigla ou o número (8213, 3048, 103, LOAS, RPS, JEF, LBI...).

## Normas (16 no banco)

| Sigla | Norma | Artigos | Baixado em | Fonte | Para que serve |
| --- | --- | --- | --- | --- | --- |
| L8213 | Lei 8.213/1991 (Planos de Beneficios da Previdencia Social) | 156 | 2026-11-18 | [link](https://www.planalto.gov.br/ccivil_03/leis/l8213cons.htm) | qualidade de segurado e periodo de graca (15), carencia (24-27), aposentadorias, auxilios, pensao (74), salario-maternidade (71), revisao/decadencia (103) |
| L8212 | Lei 8.212/1991 (Custeio da Seguridade Social) | 88 | 2026-11-18 | [link](https://www.planalto.gov.br/ccivil_03/leis/l8212cons.htm) | segurados obrigatorios (12), contribuicoes, salario-de-contribuicao (28), indenizacao de periodo (45-A) |
| L8742 | Lei 8.742/1993 (LOAS - Lei Organica da Assistencia Social) | 68 | 2026-11-18 | [link](https://www.planalto.gov.br/ccivil_03/leis/l8742.htm) | BPC/LOAS (20, 20-B, 21): idoso 65+, pessoa com deficiencia, criterio de renda 1/4, revisao bienal |
| D3048 | Decreto 3.048/1999 (Regulamento da Previdencia Social - RPS) | 473 | 2026-11-18 | [link](https://www.planalto.gov.br/ccivil_03/decreto/d3048compilado.htm) | regulamento: periodo de graca (13), carencia, atividade especial (64-70), calculo, Anexos (agentes nocivos) |
| EC103 | Emenda Constitucional 103/2019 (Reforma da Previdencia) | 36 | 2026-11-18 | [link](https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc103.htm) | regras de transicao: pontos (15), idade minima (16), pedagio 50% (17), pedagio 100% (20), especial (21), calculo (26), pensao (23) |
| EC113 | Emenda Constitucional 113/2021 (precatorios; SELIC na atualizacao) | 7 | 2026-11-18 | [link](https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc113.htm) | art. 3: SELIC para correcao e juros nas condenacoes da Fazenda Publica |
| LC142 | Lei Complementar 142/2013 (aposentadoria da pessoa com deficiencia no RGPS) | 11 | 2026-11-18 | [link](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp142.htm) | aposentadoria PcD por tempo (3, I-III) e por idade (3, IV), graus de deficiencia, conversao (7) |
| L10259 | Lei 10.259/2001 (Juizados Especiais Federais) | 27 | 2026-11-18 | [link](https://www.planalto.gov.br/ccivil_03/leis/leis_2001/l10259.htm) | competencia de 60 salarios minimos (3), tutela (4), recursos e uniformizacao (14), RPV (17) |
| L9876 | Lei 9.876/1999 (fator previdenciario; calculo do salario-de-beneficio) | 9 | 2026-11-18 | [link](https://www.planalto.gov.br/ccivil_03/leis/l9876.htm) | fator previdenciario, regra de transicao do art. 3 (revisao da vida toda - ja julgada) |
| L10741 | Lei 10.741/2003 (Estatuto da Pessoa Idosa) | 118 | 2026-11-18 | [link](https://www.planalto.gov.br/ccivil_03/leis/2003/l10.741.htm) | prioridade de tramitacao (71), BPC do idoso (34) |
| L13146 | Lei 13.146/2015 (Estatuto da Pessoa com Deficiencia - LBI) | 131 | 2026-11-18 | [link](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13146.htm) | conceito de deficiencia (2), avaliacao biopsicossocial (2, par. 1), prioridade (9), auxilio-inclusao (94) |
| L14126 | Lei 14.126/2021 (visao monocular = deficiencia sensorial) | 2 | 2026-11-18 | [link](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14126.htm) | visao monocular classificada como deficiencia sensorial (1) |
| L7713 | Lei 7.713/1988 (Imposto de Renda; isencao por molestia grave) | 50 | 2026-11-18 | [link](https://www.planalto.gov.br/ccivil_03/leis/l7713.htm) | art. 6, XIV e XXI: isencao de IR sobre aposentadoria/pensao por molestia grave |
| L1060 | Lei 1.060/1950 (assistencia judiciaria) | 11 | 2026-11-18 | [link](https://www.planalto.gov.br/ccivil_03/leis/l1060.htm) | gratuidade (o grosso foi revogado pelo CPC 98-102; restam dispositivos esparsos) |
| CPC | Codigo de Processo Civil - Lei 13.105/2015 | 1078 | 2026-11-06 | [link](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm) | gratuidade (98-102), tutela de urgencia (300), prova pericial (464-480), cumprimento contra a Fazenda (534-535) |
| IN128 | Instrucao Normativa PRES/INSS 128/2022 (REDACAO ORIGINAL do DOU) | 674 | 2026-11-18 | [link](https://www.in.gov.br/en/web/dou/-/instrucao-normativa-pres/inss-n-128-de-28-de-marco-de-2022-389275446) | regras e rotinas do INSS: filiacao, CNIS, comprovacao de atividade rural, beneficios, recursos administrativos |

## Avisos

- **L1060**: Arts. 2, 3, 4, 6, 7, 11, 12 e 17 foram revogados pelo CPC/2015 (art. 1.072, III): gratuidade hoje e CPC 98-102.
- **CPC**: Texto copiado da base tributaria (LAIS_TORRES_ADVOGADOS/tributario/leis/textos/CPC.txt); data do download e a da base de origem.
- **IN128**: Texto do DOU de 29/03/2022 em REDACAO ORIGINAL: nao traz as alteracoes posteriores das INs PRES/INSS que a modificaram. Antes de citar artigo da IN 128, conferir a redacao atual (consolidada no portal do INSS / Normas.gov.br).

## Pendências

| Item | Norma | Link | Situação |
| --- | --- | --- | --- |
| IN128-CONSOLIDADA | IN PRES/INSS 128/2022 com todas as alteracoes (texto consolidado) | [link](https://www.in.gov.br/en/web/dou/-/instrucao-normativa-pres/inss-n-128-de-28-de-marco-de-2022-389275446) | O DOU so tem a redacao original (que esta no banco como IN128). Nao ha fonte oficial consolidada limpa para baixar automaticamente; conferir alteracoes manualmente antes de citar. |

Fontes: [Planalto](https://www.planalto.gov.br/ccivil_03/) para leis, decretos, LC e emendas;
[DOU / in.gov.br](https://www.in.gov.br/) para a IN PRES/INSS 128/2022 (redação original).
