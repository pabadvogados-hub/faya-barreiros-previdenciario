---
tipo: parecer-revisao-tempo-especial
titulo: RELATÓRIO - PARECER - ANÁLISE DE REVISÃO (DIFERENÇA DE TEMPO, DESCARTES E COEFICIENTE)
grupo: relatorio
objetivo: Recontar o tempo de aposentadoria já concedida (ex. por idade, art. 18 da EC 103/2019), refazer descartes e coeficiente, apurar reflexos financeiros e concluir pela viabilidade (ou baixa viabilidade) da revisão
documentos_necessarios:
  - Carta de concessão e memória de cálculo do benefício
  - CNIS completo (com indicadores)
  - CTPS e, se houver período especial, PPP/LTCAT
  - Planilha de recálculo de tempo, RMI e atrasados (anexo)
campos:
  - SEGURADO_NOME
  - ESPECIE_BENEFICIO
  - NB
  - REGRA_APLICADA_INSS
  - SEGURADO_CPF
  - SEGURADO_DATA_NASCIMENTO
  - SEGURADO_SEXO
  - DIB
  - EMPREGADOR
  - INDICADORES_CNIS
  - DATA_INICIO
  - DATA_FIM
  - TEMPO_INSS
  - DESCARTES_INSS
  - TEMPO_INSS_APOS_DESCARTES
  - CARENCIA_INSS_APOS_DESCARTES
  - CARENCIA_INSS
  - TEMPO_RECALCULO
  - CARENCIA_RECALCULO
  - DIFERENCA_TEMPO
  - DIFERENCA_CARENCIA
  - REQUISITOS_REGRA
  - RMI_INSS
  - RMI_INSS_EXTENSO
  - RMI_RECALCULO
  - DIFERENCA_RMI
  - DIFERENCA_RMI_EXTENSO
  - PERCENTUAL_DIFERENCA_RMI
  - DESCARTES_RECALCULO
  - TEMPO_PISO_COEFICIENTE
  - COEFICIENTE_RECALCULO
  - COEFICIENTE_INSS
  - DIVISOR_INSS
  - DIVISOR_RECALCULO
  - MEDIA_INSS
  - MEDIA_RECALCULO
  - DATA_FINAL_CALCULO
  - COMPETENCIA_ATUAL
  - RMA_INSS
  - RMA_RECALCULO
  - AUMENTO_RMA
  - ATRASADOS_PRINCIPAL
  - ATRASADOS_COM_ENCARGOS
  - QTD_PARCELAS
  - CIDADE
  - DATA_PARECER
  - ADVOGADA_NOME
  - ADVOGADA_OAB
citacoes:
  - art. 18 da EC nº 103/2019
  - art. 195, §14, da CF/88 (incluído pela EC nº 103/2019)
  - arts. 189, 209 e 210 da IN PRES/INSS nº 128/2022
  - art. 26, §6º, da EC nº 103/2019
  - art. 26, §2º, da EC nº 103/2019
  - Manual de Cálculos da Justiça Federal
  - art. 103 da Lei nº 8.213/91
---

[CONFERIR: o arquivo original chama-se "Revisão Tempo Especial", mas o conteúdo é a revisão de aposentadoria por idade (art. 18 da EC nº 103/2019) por diferença de tempo comum, descartes e coeficiente, sem análise de período especial]

# ANÁLISE DE REVISÃO

**SEGURADO(A):** {{SEGURADO_NOME}}
**Benefício:** {{ESPECIE_BENEFICIO}}
**NB** {{NB}}

## RELATÓRIO

Trata-se de análise de benefício previdenciário de {{ESPECIE_BENEFICIO}}, concedida com base na regra de transição do {{REGRA_APLICADA_INSS}}, acerca da possibilidade de revisão e aumento da RMI, a partir da carta de concessão emitida pelo INSS e do recálculo elaborado por este escritório.

## DADOS DO(A) SEGURADO(A)

| Segurado(a) | {{SEGURADO_NOME}} |
|---|---|
| CPF | {{SEGURADO_CPF}} |
| Data de Nascimento | {{SEGURADO_DATA_NASCIMENTO}} |
| Sexo | {{SEGURADO_SEXO}} |
| DIB | {{DIB}} |

## DADOS DO BENEFÍCIO

[INSERIR IMAGEM: recorte da carta de concessão com os dados do benefício]

## DOS PERÍODOS DE TRABALHO

Os vínculos de trabalho e recolhimentos constantes no CNIS foram contabilizados e constam na tabela abaixo.

| Nome do período | Início | Fim |
|---|---|---|
| {{EMPREGADOR}} ({{INDICADORES_CNIS}}) | {{DATA_INICIO}} | {{DATA_FIM}} |
| RECOLHIMENTO ({{INDICADORES_CNIS}}) | {{DATA_INICIO}} | {{DATA_FIM}} |
| AGRUPAMENTO DE CONTRATANTES/COOPERATIVAS ({{INDICADORES_CNIS}}) | {{DATA_INICIO}} | {{DATA_FIM}} |

Todos os vínculos e recolhimentos foram conferidos com base no CNIS, observando-se, quanto às competências com recolhimento inferior ao salário mínimo, o disposto no art. 195, §14, da CF/88 (incluído pela EC nº 103/2019) e nos arts. 189, 209 e 210 da IN PRES/INSS nº 128/2022.

## TEMPO APURADO PELO INSS

O tempo de contribuição reconhecido pelo INSS até a DIB ({{DIB}}), sem descartes de contribuição, conforme a carta de concessão, foi de:

{{TEMPO_INSS}}

[INSERIR IMAGEM: recorte da carta de concessão com o tempo reconhecido pelo INSS]

Registre-se que, para obter a renda mais vantajosa, o INSS descartou {{DESCARTES_INSS}} salários de contribuição, o que reduziu o tempo considerado no cálculo para {{TEMPO_INSS_APOS_DESCARTES}}, com carência de {{CARENCIA_INSS_APOS_DESCARTES}} meses.

## DA CONFERÊNCIA DE TEMPO

Considerando os períodos de trabalho acima relacionados, constantes do CNIS, nosso recálculo apurou tempo de contribuição superior ao reconhecido pela Autarquia Previdenciária:

| Marco Temporal | Tempo de contribuição | Carência |
|---|---|---|
| Contagem do INSS – até a DIB ({{DIB}}) | {{TEMPO_INSS}} | {{CARENCIA_INSS}} meses |
| Recálculo – até a DIB ({{DIB}}) | {{TEMPO_RECALCULO}} | {{CARENCIA_RECALCULO}} meses |
| Diferença a favor do(a) segurado(a) | {{DIFERENCA_TEMPO}} | {{DIFERENCA_CARENCIA}} |

Verifica-se, assim, uma diferença de {{DIFERENCA_TEMPO}} de tempo de contribuição (e de {{DIFERENCA_CARENCIA}} de carência) a favor do(a) segurado(a) em relação à contagem do INSS. Essa diferença, embora existente, é de pequena expressão e não altera o direito ao benefício, cujos requisitos ({{REQUISITOS_REGRA}}) já estavam cumpridos com folga, repercutindo apenas no coeficiente de cálculo, conforme se demonstra a seguir. [AJUSTAR AO CASO]

## DA RENDA MENSAL INICIAL

A renda mensal inicial foi calculada pelo INSS no valor de:

R$ {{RMI_INSS}} – {{RMI_INSS_EXTENSO}}.

| Renda Mensal Inicial (RMI) (válida para {{DIB}} - DIB) | R$ {{RMI_INSS}} |
|---|---|

## DA CONFERÊNCIA DA RENDA MENSAL INICIAL

Considerando os salários de contribuição constantes no CNIS a partir de 07/1994, com a aplicação da média de 100% dos salários de contribuição, do descarte das contribuições que reduzem o valor do benefício (art. 26, §6º, da EC nº 103/2019) e do coeficiente de 60% acrescido de 2% por ano que exceder 15 anos de contribuição (art. 26, §2º, da EC nº 103/2019), a renda mensal inicial foi recalculada no valor de: [AJUSTAR O TEMPO-BASE DO COEFICIENTE AO SEXO/REGRA]

| Renda Mensal Inicial (RMI) (recálculo - válida para {{DIB}} - DIB) | R$ {{RMI_RECALCULO}} (diferença de R$ {{DIFERENCA_RMI}} em relação ao INSS) |
|---|---|

A diferença de R$ {{DIFERENCA_RMI}} ({{DIFERENCA_RMI_EXTENSO}}) na RMI, equivalente a cerca de {{PERCENTUAL_DIFERENCA_RMI}}, decorre essencialmente do maior tempo de contribuição apurado no recálculo, que permitiu descartar maior número de salários de contribuição de baixo valor ({{DESCARTES_RECALCULO}}, contra {{DESCARTES_INSS}} do INSS) sem que o tempo considerado ficasse abaixo de {{TEMPO_PISO_COEFICIENTE}}, preservando o coeficiente de {{COEFICIENTE_RECALCULO}}. No cálculo do INSS, os descartes reduziram o tempo para {{TEMPO_INSS_APOS_DESCARTES}} e, por consequência, o coeficiente para {{COEFICIENTE_INSS}}.

## DO COEFICIENTE E DO FATOR PREVIDENCIÁRIO

A aposentadoria do(a) segurado(a) foi calculada pelo INSS com aplicação de coeficiente de {{COEFICIENTE_INSS}} sobre a média dos salários de contribuição, sem incidência do fator previdenciário, que é inaplicável à regra do art. 18 da EC nº 103/2019. Nosso recálculo apurou coeficiente de {{COEFICIENTE_RECALCULO}}, conforme o comparativo abaixo:

| Parâmetro | Cálculo do INSS | Recálculo |
|---|---|---|
| Salários de contribuição descartados | {{DESCARTES_INSS}} | {{DESCARTES_RECALCULO}} |
| Divisor (salários considerados) | {{DIVISOR_INSS}} | {{DIVISOR_RECALCULO}} |
| Média dos salários de contribuição | R$ {{MEDIA_INSS}} | R$ {{MEDIA_RECALCULO}} |
| Tempo considerado após os descartes | {{TEMPO_INSS_APOS_DESCARTES}} | Não inferior a {{TEMPO_PISO_COEFICIENTE}} |
| Coeficiente | {{COEFICIENTE_INSS}} | {{COEFICIENTE_RECALCULO}} |
| Fator previdenciário | Inaplicável | Inaplicável |
| Renda Mensal Inicial ({{DIB}}) | R$ {{RMI_INSS}} | R$ {{RMI_RECALCULO}} |

Como se vê, o fator previdenciário não incide em nenhum dos cálculos, de modo que toda a diferença apurada decorre da combinação entre o tempo de contribuição, a quantidade de descartes e o coeficiente aplicado.

[INSERIR IMAGEM: demonstrativo do recálculo da RMI (descartes, divisor, média, coeficiente)]

## DA VIABILIDADE FINANCEIRA

Para aferir a viabilidade da revisão, foram apurados os reflexos financeiros do recálculo, com correção monetária e juros conforme o Manual de Cálculos da Justiça Federal, desde a DIB ({{DIB}}) até {{DATA_FINAL_CALCULO}}:

| Aumento na RMI | R$ {{DIFERENCA_RMI}} (≈ {{PERCENTUAL_DIFERENCA_RMI}}) |
|---|---|
| Renda mensal atual ({{COMPETENCIA_ATUAL}}) | R$ {{RMA_INSS}} (INSS) → R$ {{RMA_RECALCULO}} (recálculo) |
| Aumento na renda mensal atual | R$ {{AUMENTO_RMA}} por mês |
| Diferenças em atraso (principal) | R$ {{ATRASADOS_PRINCIPAL}} |
| Total de atrasados com encargos | R$ {{ATRASADOS_COM_ENCARGOS}} ({{QTD_PARCELAS}} parcelas, incluídas as gratificações natalinas) |

[INSERIR IMAGEM: resumo do cálculo de atrasados]

Verifica-se que o total das diferenças em atraso é de apenas R$ {{ATRASADOS_COM_ENCARGOS}}, valor do qual ainda seriam deduzidos os honorários contratuais e as eventuais despesas do procedimento. O acréscimo mensal futuro, por sua vez, é de aproximadamente R$ {{AUMENTO_RMA}}, montante modesto diante do custo, do tempo de tramitação e dos riscos inerentes a um pedido revisional, seja na via administrativa, seja na via judicial. [AJUSTAR AO CASO]

## DA CONCLUSÃO

Como se nota, o recálculo apurou tempo de contribuição de {{TEMPO_RECALCULO}}, superior em {{DIFERENCA_TEMPO}} ao reconhecido pelo INSS ({{TEMPO_INSS}}), o que, em tese, permitiria a revisão do benefício, com elevação da RMI de R$ {{RMI_INSS}} para R$ {{RMI_RECALCULO}}.

Contudo, o ganho financeiro decorrente da revisão é pequeno: aumento de R$ {{DIFERENCA_RMI}} na RMI (cerca de {{PERCENTUAL_DIFERENCA_RMI}}), de R$ {{AUMENTO_RMA}} na renda mensal atual e atrasados totais de R$ {{ATRASADOS_COM_ENCARGOS}} até a presente data. Após a dedução dos honorários e custos inerentes ao procedimento, e considerando o tempo de tramitação e os riscos próprios de qualquer demanda, o proveito líquido para o(a) segurado(a) seria pouco expressivo.

Nesse cenário, conclui-se pela BAIXA VIABILIDADE FINANCEIRA da revisão, não sendo recomendável, neste momento, a formulação de pedido revisional ou o ajuizamento de ação, ressalvado que o direito à revisão poderá ser exercido dentro do prazo decadencial de 10 (dez) anos previsto no art. 103 da Lei nº 8.213/91, caso surjam novos elementos que alterem significativamente o resultado do cálculo. [AJUSTAR SE A VIABILIDADE FOR ALTA]

Assim, encerro a presente análise.

{{CIDADE}}, {{DATA_PARECER}}.

{{ADVOGADA_NOME}}
{{ADVOGADA_OAB}}
Especialista em Cálculos Previdenciários
