---
tipo: parecer-analise-de-revisao
titulo: RELATÓRIO - PARECER - ANÁLISE DE REVISÃO
grupo: relatorio
objetivo: Conferir tempo, carência, RMI, coeficiente e fator previdenciário de aposentadoria já concedida (direito adquirido pré-reforma) e concluir se há ou não vantagem em pedir revisão
documentos_necessarios:
  - Carta de concessão e memória de cálculo do benefício
  - CNIS completo
  - CTPS
  - Processo administrativo do benefício, quando houver
  - Planilha de recálculo de tempo e RMI (anexo)
campos:
  - SEGURADO_NOME
  - ESPECIE_BENEFICIO
  - NB
  - SEGURADO_CPF
  - SEGURADO_DATA_NASCIMENTO
  - SEGURADO_SEXO
  - DIB
  - EMPREGADOR
  - INDICADORES_CNIS
  - DATA_INICIO
  - DATA_FIM
  - TEMPO_INSS_EC103
  - TEMPO_RECALCULO_EC103
  - CARENCIA_EC103
  - RMI_INSS
  - RMI_INSS_EXTENSO
  - COMPETENCIA_DER
  - RMI_RECALCULO
  - DIFERENCA_RMI
  - DIFERENCA_RMI_EXTENSO
  - COEFICIENTE
  - CIDADE
  - DATA_PARECER
  - ADVOGADA_NOME
  - ADVOGADA_OAB
citacoes:
  - EC nº 103/2019
---

# ANÁLISE DE REVISÃO

**SEGURADO(A):** {{SEGURADO_NOME}}
**Benefício:** {{ESPECIE_BENEFICIO}}
**NB** {{NB}}

## RELATÓRIO

Trata-se de análise de benefício previdenciário de {{ESPECIE_BENEFICIO}} acerca da possibilidade de revisão e aumento da RMI.

## DADOS DO(A) SEGURADO(A)

| Segurado(a) | {{SEGURADO_NOME}} |
|---|---|
| CPF | {{SEGURADO_CPF}} |
| Data de Nascimento | {{SEGURADO_DATA_NASCIMENTO}} |
| Sexo | {{SEGURADO_SEXO}} |
| DIB | {{DIB}} |

## DADOS DO BENEFÍCIO

[INSERIR IMAGEM: recorte da carta de concessão com os dados do benefício (espécie, NB, DER/DIB, RMI)]

## DOS PERÍODOS DE TRABALHO

Os vínculos de trabalho constantes no CNIS foram contabilizados e constam na tabela abaixo.

| Nome do período | Início | Fim |
|---|---|---|
| {{EMPREGADOR}} ({{INDICADORES_CNIS}}) | {{DATA_INICIO}} | {{DATA_FIM}} |
| RECOLHIMENTO (CONTRIBUINTE INDIVIDUAL) | {{DATA_INICIO}} | {{DATA_FIM}} |

Todos os vínculos foram conferidos com base na CTPS apresentada para elaboração do presente trabalho, não tendo sido identificado nenhum período laborado que não tenha sido computado pelo INSS. [AJUSTAR AO CASO]

## TEMPO APURADO PELO INSS

O tempo de contribuição reconhecido pelo INSS, na data da Reforma da Previdência (EC nº 103/2019), utilizado para a apuração da Renda Mensal Inicial pela regra de direito adquirido, foi de:

{{TEMPO_INSS_EC103}}

[INSERIR IMAGEM: recorte da carta de concessão com o tempo de contribuição reconhecido pelo INSS]

## DA CONFERÊNCIA DE TEMPO

Considerando os períodos de trabalho acima relacionados, todos devidamente registrados em CTPS e no CNIS, nosso recálculo apurou o mesmo período total, confirmando a exatidão da contagem realizada pela Autarquia Previdenciária: [AJUSTAR SE HOUVER DIVERGÊNCIA]

| Marco Temporal | Tempo de contribuição | Carência |
|---|---|---|
| Até a data da Reforma - EC nº 103/2019 (13/11/2019) | {{TEMPO_RECALCULO_EC103}} | {{CARENCIA_EC103}} meses |

Assim, o tempo de contribuição apurado por este escritório é idêntico ao considerado pelo INSS na concessão do benefício, restando demonstrado que todos os vínculos constantes da CTPS do(a) segurado(a) foram corretamente computados.

## DA RENDA MENSAL INICIAL

A renda mensal inicial foi calculada pelo INSS no valor de:

R$ {{RMI_INSS}} – {{RMI_INSS_EXTENSO}}.

| Renda Mensal Inicial (RMI) (válida para {{DIB}} - DIB) | R$ {{RMI_INSS}} |
|---|---|

## DA CONFERÊNCIA DA RENDA MENSAL INICIAL

Considerando os salários de contribuição constantes no CNIS, com a aplicação da média aritmética dos 80% maiores salários de contribuição, do fator previdenciário e do coeficiente de cálculo previstos na legislação vigente na data da Reforma (EC nº 103/2019), a renda mensal inicial foi recalculada no valor de:

| Renda Mensal Inicial (RMI) (recálculo - válida para 13/11/2019, atualizada p/ DER {{COMPETENCIA_DER}}) | R$ {{RMI_RECALCULO}} (diferença de R$ {{DIFERENCA_RMI}} em relação ao INSS) |
|---|---|

A diferença de R$ {{DIFERENCA_RMI}} ({{DIFERENCA_RMI_EXTENSO}}) entre o valor apurado neste recálculo e o valor efetivamente concedido pelo INSS é irrisória, decorrendo de mera variação de arredondamento entre os índices de correção monetária utilizados, não representando qualquer prejuízo ao(à) segurado(a) nem indício de erro na concessão do benefício.

## DO COEFICIENTE E DO FATOR PREVIDENCIÁRIO

A aposentadoria do(a) segurado(a) foi calculada pelo INSS com aplicação de {{COEFICIENTE}} de coeficiente sobre o salário de benefício, com incidência do fator previdenciário:

[INSERIR IMAGEM: recorte da carta de concessão com coeficiente e fator previdenciário aplicados pelo INSS]

Nosso recálculo apontou o mesmo percentual de coeficiente, com fator previdenciário calculado em parâmetros equivalentes aos utilizados pelo INSS, considerando o tempo de contribuição, a idade do(a) segurado(a) e a expectativa de sobrevida na data de apuração (13/11/2019):

[INSERIR IMAGEM: recorte do recálculo com coeficiente, fator previdenciário, expectativa de sobrevida, tempo e idade]

## DA CONCLUSÃO

Como se nota, o valor da RMI apurado neste recálculo é praticamente idêntico ao calculado pelo INSS, com diferença ínfima e irrelevante do ponto de vista financeiro.

Verifica-se, assim, que a aposentadoria do(a) segurado(a) foi concedida considerando todos os períodos de trabalho constantes na CTPS/CNIS, e que todos os parâmetros de cálculo (tempo de contribuição, carência, salários de contribuição, fator previdenciário e coeficiente) estão em conformidade com a legislação vigente na data da concessão do benefício.

Nesse cenário, o valor da Renda Mensal Inicial concedido pelo INSS (R$ {{RMI_INSS}}) está correto, não sendo cabível a realização de procedimento de revisão, pois não há vantagem financeira para o(a) segurado(a).

Assim, encerro a presente análise.

{{CIDADE}}, {{DATA_PARECER}}.

{{ADVOGADA_NOME}}
{{ADVOGADA_OAB}}
Especialista em Cálculos Previdenciários
