---
tipo: conferencia-rmi-auxilio
titulo: RELATÓRIO DE CONFERÊNCIA DE RMI
grupo: relatorio
objetivo: Conferir de forma independente a RMI de um ou mais benefícios (ex. auxílio por incapacidade) apurada pelo INSS, comparando com o recálculo a partir do CNIS e apontando inconsistências no período de apuração
documentos_necessarios:
  - Cartas de concessão e memórias de cálculo de cada benefício
  - CNIS completo (vínculos e remunerações)
  - Contracheques, CTPS, extratos do FGTS ou outros documentos de remuneração, quando houver competências sem remuneração no CNIS
campos:
  - SEGURADO_NOME
  - SEGURADO_CPF
  - SEGURADO_NIT
  - SEGURADO_DATA_NASCIMENTO
  - NB
  - ESPECIE
  - DIB
  - DCB
  - RMI_INSS
  - RMI_RECALCULADA
  - DIFERENCA
  - LIMITE_DIFERENCA_RESIDUAL
  - NB_REFERENCIA
  - DIB_REFERENCIA
  - COMPETENCIA_INICIO_PBC_REFERENCIA
  - NBS_COMPARADOS
  - COMPETENCIA_INICIO_PBC_COMPARADO
  - FAIXA_VALORES_MINIMOS
  - NUMERO_VINCULO
  - EMPREGADOR
  - DATA_INICIO_VINCULO
  - DATA_FIM_VINCULO
  - COMPETENCIA_INICIO_REMUNERACOES
  - PERIODO_SEM_REMUNERACAO
  - FAIXA_SALARIAL_VINCULO
  - CIDADE
  - DATA_PARECER
  - ADVOGADA_NOME
  - ADVOGADA_OAB
citacoes:
  - Lei 8.213/91
  - Lei 9.876/99
  - Lei 13.135/2015
  - EC 103/2019
  - art. 103, parágrafo único, e no art. 41-A da Lei nº 8.213/91
---

# RELATÓRIO DE CONFERÊNCIA DE RMI

## 1. IDENTIFICAÇÃO DO(A) SEGURADO(A)

**Nome:** {{SEGURADO_NOME}}
**CPF:** {{SEGURADO_CPF}}
**NIT:** {{SEGURADO_NIT}}
**Data de nascimento:** {{SEGURADO_DATA_NASCIMENTO}}

## 2. OBJETO

O presente relatório tem por objeto a conferência técnica da Renda Mensal Inicial (RMI) apurada pelo INSS nas Cartas de Concessão/Memória de Cálculo referentes aos benefícios abaixo relacionados, com base nos salários de contribuição constantes do Cadastro Nacional de Informações Sociais (CNIS) do(a) segurado(a), confrontando-se os valores oficiais com os valores recalculados de forma independente.

| NB | Espécie | DIB | DCB | RMI (INSS) |
|---|---|---|---|---|
| {{NB}} | {{ESPECIE}} | {{DIB}} | {{DCB}} | R$ {{RMI_INSS}} |

[UMA LINHA POR BENEFÍCIO — ex. de espécie: "31 - Auxílio-Doença Previdenciário", "91 - Auxílio-Doença Acidentário"]

## 3. METODOLOGIA

A conferência foi realizada mediante a reconstituição do Salário de Benefício com base nos salários de contribuição constantes do CNIS, devidamente atualizados pelos índices de correção monetária vigentes, seguindo os critérios de apuração aplicáveis a cada espécie de benefício (Lei 8.213/91, Lei 9.876/99, Lei 13.135/2015 e EC 103/2019, conforme o caso), reproduzindo a mesma metodologia de cálculo empregada pelo INSS nas respectivas Cartas de Concessão.

## 4. RESULTADO DA CONFERÊNCIA

Os valores de RMI recalculados de forma independente foram os seguintes, comparados aos valores oficialmente apurados pelo INSS:

| NB | RMI apurada pelo INSS | RMI recalculada | Diferença |
|---|---|---|---|
| {{NB}} | R$ {{RMI_INSS}} | R$ {{RMI_RECALCULADA}} | {{DIFERENCA}} |

[CONCLUSÃO-MODELO PARA DIFERENÇAS RESIDUAIS] Observa-se que os valores recalculados se encontram muito próximos aos apurados pelo INSS, com diferenças residuais (inferiores a R$ {{LIMITE_DIFERENCA_RESIDUAL}} em todos os casos), compatíveis com pequenas variações de arredondamento e de índices de atualização monetária utilizados mês a mês, não configurando, isoladamente, indício relevante de erro de cálculo.

[INSERIR IMAGEM: quadro comparativo ou trecho da memória de cálculo do INSS]

## 5. PONTOS DE ATENÇÃO IDENTIFICADOS

[SEÇÃO OPCIONAL — USAR QUANDO HOUVER INCONSISTÊNCIA NO PERÍODO BÁSICO DE CÁLCULO ENTRE OS BENEFÍCIOS]

Não obstante a proximidade dos valores apurados, a análise comparativa entre as Cartas de Concessão demonstra uma inconsistência relevante quanto ao período de apuração dos salários de contribuição utilizado em cada benefício, que merece destaque:

No benefício NB {{NB_REFERENCIA}} (DIB {{DIB_REFERENCIA}}), a memória de cálculo do INSS considerou salários de contribuição a partir da competência {{COMPETENCIA_INICIO_PBC_REFERENCIA}}, sem computar remunerações anteriores a essa data.

Já nos benefícios NB {{NBS_COMPARADOS}}, o INSS retrocedeu o período de apuração até a competência {{COMPETENCIA_INICIO_PBC_COMPARADO}}, incluindo, inclusive, salários de contribuição fixados no patamar do salário-mínimo (valores de R$ {{FAIXA_VALORES_MINIMOS}}).

Ocorre que, conforme registrado no CNIS (vínculo nº {{NUMERO_VINCULO}} — {{EMPREGADOR}}, com início em {{DATA_INICIO_VINCULO}} e término em {{DATA_FIM_VINCULO}}), o(a) segurado(a) esteve empregado(a) durante todo esse intervalo, mas as remunerações constantes do extrato para esse vínculo somente se iniciam na competência {{COMPETENCIA_INICIO_REMUNERACOES}}, não havendo registro de remunerações para o período de {{PERIODO_SEM_REMUNERACAO}}.

Nas Cartas de Concessão dos benefícios NB {{NBS_COMPARADOS}}, esse hiato de remunerações não informadas foi preenchido pelo INSS com salários de contribuição no piso mínimo (indicador de competência sem remuneração declarada), o que reduz artificialmente a média apuratória, uma vez que tais valores mínimos, se comparados ao padrão salarial do(a) segurado(a) no período (patamar entre R$ {{FAIXA_SALARIAL_VINCULO}} no mesmo vínculo), muito provavelmente não refletem a remuneração efetivamente percebida junto ao empregador.

## 6. CONCLUSÃO

Diante dos elementos atualmente constantes do CNIS, os benefícios objeto deste relatório encontram-se calculados corretamente, porquanto os valores de RMI apurados pelo INSS são compatíveis com os salários de contribuição efetivamente registrados no cadastro, e as diferenças identificadas no recálculo independente são residuais e não configuram erro de cálculo.

Entretanto, caso o(a) segurado(a) logre comprovar, por meio de documentação idônea (contracheques, carteira de trabalho, extratos do FGTS ou outros documentos hábeis), os salários efetivamente recebidos junto a {{EMPREGADOR}} no período de {{PERIODO_SEM_REMUNERACAO}}, período em que o vínculo está registrado no CNIS sem a correspondente remuneração. [CONFERIR: trecho incompleto no modelo original — a frase começa com "caso ... logre comprovar" e não traz a oração principal]

É conveniente destacar que a inclusão desses valores na base de cálculo do Salário de Benefício dos NB {{NBS_COMPARADOS}} poderá resultar em elevação da RMI atualmente reconhecida, sendo, nessa hipótese, passível de pedido de revisão administrativa junto ao INSS, com fundamento no art. 103, parágrafo único, e no art. 41-A da Lei nº 8.213/91.

{{CIDADE}}, {{DATA_PARECER}}.

{{ADVOGADA_NOME}}
{{ADVOGADA_OAB}}
Especialista em Cálculos Previdenciários
