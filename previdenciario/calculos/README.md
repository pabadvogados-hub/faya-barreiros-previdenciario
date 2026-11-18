# Cálculos previdenciários (RGPS): simulador de apoio

Python 3.12, só biblioteca padrão. **Simulação de apoio. Não substitui o cálculo no software do escritório nem a conferência da advogada.**

## Arquivos

| Arquivo | O que faz |
|---|---|
| `tempo.py` | Une períodos sobrepostos (o dia concomitante conta uma vez, pelo maior fator), converte especial em comum (Dec. 3.048/99, art. 70) só até 13/11/2019 (EC 103, art. 25, §2º), separa o tempo de magistério e conta a carência por competência. |
| `periodo_graca.py` | Qualidade de segurado (Lei 8.213/91, art. 15): 12/24/36 meses, facultativo 6, perda no dia 16 do 2º mês seguinte. A soma é feita por competência (mês/ano), então 31/12/2024 perde em 16/02/2026. Também apura perdas no histórico e as "mais de 120 contribuições". |
| `regras_ec103.py` | Regras de aposentadoria: direito adquirido (tempo com fator; pontos 85/95 e 86/96 sem fator), arts. 15, 16, 17, 18 e 20 da EC 103 (com as variantes de professor) e a permanente (art. 19). Para cada regra devolve: cumpre ou não, data em que cumpre, o que falta e o coeficiente (art. 26). Os artigos estão documentados no topo do arquivo. |
| `simular.py` | CLI que gera o relatório em Markdown. |
| `exemplo_caso.json` | Caso **fictício** usado nos testes e como modelo. |
| `test_calculos.py` | 56 testes (unittest). |

## Como rodar

```
cd "C:\AUTOMAÇÕES CLIENTES\FAYA_BARREIROS_PREV\previdenciario\calculos"
python simular.py exemplo_caso.json                 # imprime o relatório
python simular.py exemplo_caso.json -o relatorio.md # grava em arquivo
python -m unittest test_calculos -v                 # testes
```

## Formato do caso (JSON)

- `segurado`: `nascimento` (AAAA-MM-DD ou DD/MM/AAAA), `sexo` (`F`/`M`), `categoria` (`obrigatorio`/`facultativo`), `nome`.
- `data_base`: data do cálculo. Se faltar, usa hoje.
- `projetar_contribuicao`: `true` supõe contribuição contínua a partir do dia seguinte à data-base.
- `desemprego_comprovado`: soma +12 meses ao período de graça.
- `mais_de_120_sem_perda`: `true`/`false` força o valor; `null` deixa o programa apurar pelos períodos.
- `periodos[]`: `inicio`, `fim` (vazio = até a data-base), `tipo` (`comum`, `especial25`, `especial20`, `especial15`, `professor`, `rural`), `descricao`, `competencias_sem_contribuicao` (ex.: `["2023-03"]`), `com_contribuicao` (só para rural), `conta_carencia` (opcional, força).
- `convencao`: `dias_ano` (365) e `dias_mes` (30).
- `opcoes`: `metodo_pontos` (`amd`/`decimal`), `professor_pontos_tempo` (`magisterio`/`total`), `tempo_convertido_nas_regras_idade`, `criterio_120` (`qualquer_sequencia`/`sequencia_atual`), `minimo_120_inclusive`, `horizonte_anos`.

## Convenções

- Dias corridos, com início e fim incluídos. Para exprimir em anos/meses/dias: ano = 365 dias e mês = 30 dias, ambos parametrizáveis. Com isso, os requisitos viram dias: 35 anos = 12.775 dias.
- O fator de conversão é somado em centésimos inteiros, sem erro de arredondamento. Na exibição, a fração de dia é truncada.
- A exigência que muda a cada ano (pontos e idade) é a do ano civil em que o último requisito se completa.
- Idade pelo calendário. Se o dia não existe no mês, vale o 1º dia do mês seguinte (CC, art. 132, §3º).
- Todas as regras exigem carência mínima de 180 contribuições (Lei 8.213/91, art. 25, II).
- O coeficiente é apurado na data mais tardia entre o cumprimento e a data-base. Regras com fator previdenciário aparecem como "100% x FP" e ficam fora da comparação por coeficiente.

## Tabelas (conferidas no texto da EC 103/2019, planalto.gov.br)

| Regra | Mulher | Homem |
|---|---|---|
| Art. 15, pontos | 86 em 2019, +1/ano, até 100 (2033) | 96 em 2019, +1/ano, até 105 (2028) |
| Art. 15, professor | 81, até 92 (2030); 25 anos | 91, até 100 (2028); 30 anos |
| Art. 16, idade | 56 em 2019, +6m/ano, até 62 (2031) | 61 em 2019, +6m/ano, até 65 (2027) |
| Art. 16, professor | 51, até 57 (2031); 25 anos | 56, até 60 (2027); 30 anos |
| Art. 18, idade | 60 em 2019, +6m/ano, até 62 (2023) | 65 |
| Art. 20 | 57 anos; 30 anos + pedágio de 100% (professora: 52; 25) | 60 anos; 35 anos + pedágio de 100% (professor: 55; 30) |

Atenção, art. 16 para mulher: em **2025 a exigência é 59 anos**. A de 59 anos e 6 meses vale para **2026**.

## Limitações

- Não calcula a RMI, o salário de benefício nem o fator previdenciário: dependem dos salários de contribuição e da tábua do IBGE.
- Não trata aposentadoria especial (art. 21, pontos 66/76/86), por incapacidade, da pessoa com deficiência, rural por idade nem híbrida; também não trata a aposentadoria por idade anterior à EC (70% + 1%) nem a proporcional da EC 20/98.
- Não lê o CNIS: os períodos são digitados. Não analisa indicadores (PEXT, PREM-EXT etc.) nem recolhimentos abaixo do mínimo (EC 103, art. 29).
- A atividade especial é tomada como já reconhecida. O programa não avalia PPP/LTCAT.

## Pontos marcados [CONFERIR]

1. Convenção 365/30 x decomposição por calendário em base 30/360 (como no CNIS).
2. Fração de dia da conversão: mantida no cálculo e truncada na exibição.
3. Rural: até 31/10/1991 conta tempo sem carência; depois, só com contribuição.
4. Frações nos pontos: soma de anos/meses/dias em base 30/360 (padrão) x decimal. No padrão, idade com resto de 30 dias (mês de 31) normaliza e os pontos podem fechar 1 dia antes do aniversário.
5. Professor: pontos com tempo de magistério (padrão) x tempo total.
6. Tempo convertido contando para os 15/20 anos das regras de idade (arts. 18/19). Não conta para a carência.
7. Homem filiado antes da EC (art. 18): acréscimo de 2% acima de 20 anos (texto) x acima de 15 (tese).
8. Coeficiente acima de 100% não é limitado (a RMI fica limitada ao teto).
9. Coeficiente apurado na data mais tardia entre o cumprimento e a data-base.
10. Período de graça: "mais de 120" lido como 121 ou mais (padrão) x 120. Também: a prorrogação de 24 meses, uma vez adquirida, se mantém (TNU, padrão) x vale só na sequência atual.
11. Período de graça: o desemprego não é considerado ao apurar perdas passadas do histórico.
