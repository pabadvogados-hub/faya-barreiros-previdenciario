# Kit previdenciário da Dra. Faya

| Pasta | O que tem | Comando principal |
|---|---|---|
| `pecas/iniciais/` | 27 modelos de petição inicial dela, anonimizados | `python previdenciario/pecas/gerar_peca.py listar` |
| `pecas/relatorios/` | 14 modelos de relatório, parecer e planejamento | idem |
| `pecas/00_INDICE.md` | Índice, citações e **pauta de revisão** (`[CONFERIR]` herdados) | `python previdenciario/pecas/indice.py` |
| `pecas/gerar_peca.py` | Preenche campos, confere pendências e põe no timbrado | `gerar_peca.py campos|preencher|conferir|docx` |
| `dna/DNA_PECAS.md` | Estilo, estrutura e regras de citação | — |
| `leis/` | Base oficial por artigo (16 normas) | `python previdenciario/leis/buscar_lei.py --lei 8213 --art 15` |
| `calculos/` | Calculadora de apoio (tempo, carência, período de graça, EC 103) e formato dos cálculos dela | `python previdenciario/calculos/simular.py caso.json` |
| `timbrado/` | Timbrado oficial (bordô) | usado pelo `gerar_peca.py docx` |

## Fluxo de uma peça

```
gerar_peca.py campos <tipo>          # o que o modelo pede
agente previdenciario/calculista     # escreve a minuta.md a partir do modelo + documentos do cliente
gerar_peca.py conferir minuta.md     # lista {{campos}}, [CONFERIR], [NARRAR], [INSERIR IMAGEM]
gerar_peca.py docx minuta.md         # timbrado; com pendência sai "MINUTA - NÃO PROTOCOLAR"
revisão da Dra. Faya (POP-OP-05)
```

## Sobre os dados

Os modelos foram gerados a partir das peças reais com **substituição de todo dado de cliente** por `{{CAMPOS}}`
e da narrativa por `[NARRAR: ...]`, e varridos por CPF, CNPJ, NB, nº CNJ, telefone, e-mail, CEP e nomes. Números
de processo que sobram são de **julgados públicos** citados em ementas. Os originais ficam fora do repositório.
