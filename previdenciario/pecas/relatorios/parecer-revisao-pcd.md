---
tipo: parecer-revisao-pcd
titulo: RELATÓRIO - PARECER - ANÁLISE DE REVISÃO (APOSENTADORIA DA PESSOA COM DEFICIÊNCIA)
grupo: relatorio
objetivo: Avaliar a transformação de aposentadoria comum já concedida em aposentadoria da pessoa com deficiência (LC 142/2013), com cronologia dos laudos, conversão de tempo, nova RMI, atrasados e valor da causa
documentos_necessarios:
  - Carta de concessão e memória de cálculo do benefício ativo
  - CNIS completo
  - Laudos, declarações médicas e exames que comprovem a deficiência e sua data de início (em ordem cronológica)
  - Laudo de avaliação biopsicossocial/funcional (ex. IFBr-M), quando houver
  - Planilha de apuração de tempo convertido, RMI e valor da causa (anexo)
campos:
  - SEGURADO_NOME
  - ESPECIE_BENEFICIO
  - NB
  - SEGURADO_CPF
  - SEGURADO_DATA_NASCIMENTO
  - SEGURADO_SEXO
  - DIB
  - DATA_CONCESSAO
  - REGRA_APLICADA_INSS
  - TEMPO_CONSIDERADO_INSS
  - IDADE_NA_DIB
  - CARENCIA_INSS
  - MEDIA_INSS
  - COEFICIENTE_INSS
  - RMI_INSS
  - TIPOS_DOCUMENTOS_MEDICOS
  - DATA_DOCUMENTO
  - DOCUMENTO
  - CONTEUDO_CONCLUSAO
  - RELEVANCIA
  - DATA_MARCO_INICIAL_DEFICIENCIA
  - DOCUMENTO_MARCO_INICIAL
  - NATUREZA_DEFICIENCIA
  - DATAS_DOCUMENTOS_CONTINUIDADE
  - CIDS
  - GRAU_DEFICIENCIA_LAUDO
  - PERIODO_DEFICIENCIA_ATE_DIB
  - GRAU_DEFICIENCIA_ADOTADO
  - FATOR_CONVERSAO_PCD
  - PERIODO_SEM_DEFICIENCIA
  - QTD_PERIODOS_SEM_DEFICIENCIA
  - TEMPO_SEM_DEFICIENCIA_CONVERTIDO
  - PERIODO_COM_DEFICIENCIA
  - QTD_PERIODOS_COM_DEFICIENCIA
  - TEMPO_COM_DEFICIENCIA
  - TEMPO_TOTAL_CONVERTIDO
  - INCISO_ART_3
  - TEMPO_EXIGIDO_PCD
  - CARENCIA_CUMPRIDA
  - DATAS_LAUDOS
  - QTD_DESCARTES
  - MEDIA_PCD
  - FATOR_PREVIDENCIARIO
  - RMI_PCD
  - RMI_PCD_EXTENSO
  - COMPETENCIA_ATUAL
  - RMA_INSS
  - RMA_PCD
  - ACRESCIMO_RMI
  - PERCENTUAL_AUMENTO
  - COMPETENCIA_AJUIZAMENTO
  - COMPETENCIA
  - DEVIDO_PCD
  - INDICE_CM
  - DEVIDO_CORRIGIDO
  - RECEBIDO_INSS
  - RECEBIDO_CORRIGIDO
  - DIFERENCA_CORRIGIDA
  - ANO
  - TOTAL_DEVIDO_PCD
  - TOTAL_DEVIDO_CORRIGIDO
  - TOTAL_RECEBIDO
  - TOTAL_RECEBIDO_CORRIGIDO
  - ATRASADOS
  - ATRASADOS_EXTENSO
  - PERIODO_VENCIDAS
  - COMPETENCIAS_13_VINCENDAS
  - VINCENDAS_DEVIDO
  - VINCENDAS_RECEBIDO
  - VINCENDAS_DIFERENCA
  - SELIC_TAXA_LEGAL
  - VALOR_CAUSA_DEVIDO
  - VALOR_CAUSA_RECEBIDO
  - VALOR_CAUSA
  - VALOR_CAUSA_EXTENSO
  - SALARIO_MINIMO_VIGENTE
  - TETO_JEF_60_SM
  - CIDADE
  - DATA_PARECER
  - ADVOGADA_NOME
  - ADVOGADA_OAB
citacoes:
  - Lei Complementar nº 142/2013
  - art. 22 da Emenda Constitucional nº 103/2019
  - Art. 16 da EC nº 103/2019 – idade mínima progressiva + tempo de contribuição
  - IN RFB 1.769/2017
  - Lei nº 8.989/1995
  - art. 2º (LC 142/2013)
  - art. 3º da referida Lei Complementar
  - art. 3º da LC 142/2013 (Incisos I, II, III e IV)
  - art. 7º da LC 142/2013
  - art. 70-E do Decreto nº 3.048/1999
  - art. 8º, inciso I, da LC 142/2013
  - art. 9º, inciso I (LC 142/2013)
  - art. 3º, III (LC 142/2013)
  - art. 25, II, da Lei 8.213/91
  - art. 3º, inciso III, c/c art. 7º da LC 142/2013
  - art. 16 da EC nº 103/2019
  - art. 176-E do Decreto nº 3.048/1999
  - art. 3º, IV (LC 142/2013)
  - art. 26, § 6º, da EC nº 103/2019
  - art. 8º, I, da LC 142/2013
  - art. 9º, I, da LC 142/2013
  - Manual de Cálculos da Justiça Federal (Resolução CJF nº 990/2026)
  - art. 292, §§ 1º e 2º, do CPC
  - art. 3º, § 3º, da Lei nº 10.259/2001
  - art. 7º da LC 142/2013 e art. 70-E do Decreto nº 3.048/1999
  - art. 4º da LC 142/2013 e art. 70-D do Decreto nº 3.048/1999
  - art. 103 da Lei nº 8.213/1991
---

# ANÁLISE DE REVISÃO

**SEGURADO(A):** {{SEGURADO_NOME}}
**Benefício:** {{ESPECIE_BENEFICIO}}
**NB** {{NB}}

## RELATÓRIO

Trata-se de análise acerca da possibilidade de revisão do benefício de {{ESPECIE_BENEFICIO}} (NB {{NB}}) do(a) segurado(a), com vistas à sua transformação em aposentadoria da pessoa com deficiência, nos termos da Lei Complementar nº 142/2013, a partir da documentação médica apresentada para elaboração do presente trabalho.

## DADOS DO(A) SEGURADO(A)

| Segurado(a) | {{SEGURADO_NOME}} |
|---|---|
| CPF | {{SEGURADO_CPF}} |
| Data de Nascimento | {{SEGURADO_DATA_NASCIMENTO}} |
| Sexo | {{SEGURADO_SEXO}} |
| DIB | {{DIB}} |

## DADOS DO BENEFÍCIO

Conforme Carta de Concessão emitida pelo INSS, o benefício foi concedido com os seguintes parâmetros:

| Item | Dado |
|---|---|
| Espécie | {{ESPECIE_BENEFICIO}} |
| Número do Benefício (NB) | {{NB}} |
| DER / DIB | {{DIB}} |
| Data da concessão (DDB) | {{DATA_CONCESSAO}} |
| Regra aplicada | {{REGRA_APLICADA_INSS}} [ex.: "Art. 16 da EC nº 103/2019 – idade mínima progressiva + tempo de contribuição"] |
| Tempo de contribuição considerado | {{TEMPO_CONSIDERADO_INSS}} |
| Idade na DIB | {{IDADE_NA_DIB}} |
| Carência | {{CARENCIA_INSS}} meses |
| Média dos salários de contribuição | R$ {{MEDIA_INSS}} |
| Coeficiente | {{COEFICIENTE_INSS}} |
| Renda Mensal Inicial (RMI) | R$ {{RMI_INSS}} |

[INSERIR IMAGEM: recorte da carta de concessão do benefício ativo]

## DA DOCUMENTAÇÃO MÉDICA APRESENTADA E DA CRONOLOGIA DOS LAUDOS

Para a presente análise foram apresentados {{TIPOS_DOCUMENTOS_MEDICOS}} [ex.: exames de imagem, laudos de avaliação para isenção de IPI, declaração médica e laudo pericial de avaliação de pessoa com deficiência]. Os documentos foram organizados em ordem cronológica no quadro abaixo, com destaque para a data, o conteúdo e a relevância de cada um para a comprovação da condição de pessoa com deficiência (PCD):

| Data | Documento | Conteúdo / Conclusão | Relevância |
|---|---|---|---|
| {{DATA_DOCUMENTO}} | {{DOCUMENTO}} [ex.: "Laudo de Avaliação para Isenção de IPI – Anexo V (IN RFB 1.769/2017)", exame de imagem, declaração médica, laudo pericial de avaliação de PCD] | {{CONTEUDO_CONCLUSAO}} (natureza, caráter permanente, CID) | {{RELEVANCIA}} [ex.: "Não se relaciona à deficiência" / "Exame complementar" / "SIM – MARCO INICIAL DA DEFICIÊNCIA" / "SIM – confirma a continuidade" / "SIM – confirma a continuidade e o grau"] |

Da análise cronológica, extrai-se que a condição de pessoa com deficiência do(a) segurado(a) foi formalmente atestada, pela primeira vez, em {{DATA_MARCO_INICIAL_DEFICIENCIA}}, em {{DOCUMENTO_MARCO_INICIAL}} [se for laudo para isenção de IPI: "em laudo emitido para fins de isenção de IPI (Lei nº 8.989/1995)"], que reconheceu {{NATUREZA_DEFICIENCIA}}.

Os documentos posteriores – {{DATAS_DOCUMENTOS_CONTINUIDADE}} – reiteram o mesmo diagnóstico (CID {{CIDS}}), o que demonstra a continuidade e a permanência da deficiência desde o marco inicial, sem qualquer remissão. Os exames de imagem, por sua vez, corroboram a natureza do quadro. [AJUSTAR AO CASO]

| Marco temporal | Evento |
|---|---|
| {{DATA_MARCO_INICIAL_DEFICIENCIA}} | Marco inicial da deficiência – {{DOCUMENTO_MARCO_INICIAL}} |
| 13/11/2019 | Entrada em vigor da EC nº 103/2019 [indicar se já na condição de PCD] |
| {{DATAS_DOCUMENTOS_CONTINUIDADE}} | Laudos e declaração que confirmam a permanência da deficiência (grau {{GRAU_DEFICIENCIA_LAUDO}}) |
| {{DIB}} | DER/DIB do benefício concedido pelo INSS |
| {{DATA_MARCO_INICIAL_DEFICIENCIA}} a {{DIB}} | Período com deficiência até a DIB: {{PERIODO_DEFICIENCIA_ATE_DIB}} |

## DOS REQUISITOS DA LEI COMPLEMENTAR Nº 142/2013

A Lei Complementar nº 142/2013, mantida em vigor pelo art. 22 da Emenda Constitucional nº 103/2019, regulamenta a aposentadoria da pessoa com deficiência segurada do RGPS.

Nos termos do seu art. 2º, considera-se pessoa com deficiência aquela que tem impedimentos de longo prazo de natureza física, mental, intelectual ou sensorial, os quais, em interação com diversas barreiras, podem obstruir sua participação plena e efetiva na sociedade em igualdade de condições com as demais pessoas.

O art. 3º da referida Lei Complementar estabelece as seguintes hipóteses de concessão para o segurado do sexo masculino:

| Modalidade (art. 3º da LC 142/2013) | Requisito exigido – homem |
|---|---|
| Inciso I – por tempo de contribuição, deficiência grave | 25 anos de tempo de contribuição |
| Inciso II – por tempo de contribuição, deficiência moderada | 29 anos de tempo de contribuição |
| Inciso III – por tempo de contribuição, deficiência leve | 33 anos de tempo de contribuição |
| Inciso IV – por idade | 60 anos de idade + 15 anos de contribuição, comprovada a deficiência durante igual período |

[CONFERIR: o modelo original traz apenas a tabela do segurado homem; para segurada mulher, substituir pelos requisitos femininos do art. 3º da LC 142/2013]

Quando o segurado se torna pessoa com deficiência após a filiação ao RGPS como no caso, o art. 7º da LC 142/2013 determina que os parâmetros sejam proporcionalmente ajustados, considerando-se o número de anos em que exerceu atividade laboral sem e com deficiência.

O art. 70-E do Decreto nº 3.048/1999 disciplina esse ajuste por meio de fatores de conversão: para o homem com deficiência de grau leve (33 anos), o tempo comum é multiplicado pelo fator 0,94 (33/35), enquanto o tempo com deficiência é computado integralmente (fator 1,00). [AJUSTAR O FATOR AO SEXO E AO GRAU]

Quanto ao cálculo, o art. 8º, inciso I, da LC 142/2013 assegura à aposentadoria por tempo de contribuição da pessoa com deficiência o coeficiente de 100% do salário de benefício, e o art. 9º, inciso I, determina que o fator previdenciário somente seja aplicado se resultar em renda mensal de valor mais elevado.

## DA ANÁLISE DO CASO CONCRETO

Adotando-se como marco inicial da deficiência a data de {{DATA_MARCO_INICIAL_DEFICIENCIA}}, constante de {{DOCUMENTO_MARCO_INICIAL}}, e classificando-se a deficiência, de forma conservadora, como de grau {{GRAU_DEFICIENCIA_ADOTADO}} durante todo o período (embora o laudo mais recente a classifique como {{GRAU_DEFICIENCIA_LAUDO}}), foi realizada a contagem do tempo de contribuição com a conversão dos períodos anteriores ao marco inicial pelo fator {{FATOR_CONVERSAO_PCD}}, nos termos do art. 70-E do Decreto nº 3.048/1999:

| Período | Situação | Multiplicador | Tempo apurado |
|---|---|---|---|
| {{PERIODO_SEM_DEFICIENCIA}} ({{QTD_PERIODOS_SEM_DEFICIENCIA}} períodos) | Sem deficiência – tempo comum convertido | {{FATOR_CONVERSAO_PCD}} | {{TEMPO_SEM_DEFICIENCIA_CONVERTIDO}} |
| {{PERIODO_COM_DEFICIENCIA}} ({{QTD_PERIODOS_COM_DEFICIENCIA}} períodos) | Com deficiência {{GRAU_DEFICIENCIA_ADOTADO}} – contribuições efetivas | 1,00 | {{TEMPO_COM_DEFICIENCIA}} |
| TOTAL até a DER ({{DIB}}) | Tempo convertido para a deficiência preponderante ({{GRAU_DEFICIENCIA_ADOTADO}}) | - | {{TEMPO_TOTAL_CONVERTIDO}} |

Com isso, os requisitos para a aposentadoria por tempo de contribuição da pessoa com deficiência foram preenchidos na DER:

| Requisito | Exigido | Cumprido em {{DIB}} |
|---|---|---|
| Tempo de contribuição – deficiência {{GRAU_DEFICIENCIA_ADOTADO}} (art. 3º, {{INCISO_ART_3}}) | {{TEMPO_EXIGIDO_PCD}} | {{TEMPO_TOTAL_CONVERTIDO}} |
| Carência (art. 25, II, da Lei 8.213/91) | 180 contribuições | {{CARENCIA_CUMPRIDA}} contribuições |
| Comprovação da deficiência | Avaliação médica e funcional | Laudos de {{DATAS_LAUDOS}} |

Assim, verifica-se que, na data do requerimento administrativo ({{DIB}}), o(a) segurado(a) já fazia jus à aposentadoria por tempo de contribuição da pessoa com deficiência, nos termos do art. 3º, inciso {{INCISO_ART_3}}, c/c art. 7º da LC 142/2013, benefício mais vantajoso do que a aposentadoria concedida pelo INSS com base na regra de transição do {{REGRA_APLICADA_INSS}}. Registre-se que cabe ao INSS conceder o benefício mais vantajoso ao segurado, nos termos do art. 176-E do Decreto nº 3.048/1999.

Observa-se, ainda, que a modalidade por idade da pessoa com deficiência (art. 3º, IV) não é aplicável, pois o(a) segurado(a) não possui 15 anos de contribuição na condição de PCD. [AJUSTAR AO CASO]

## DA RENDA MENSAL INICIAL DA APOSENTADORIA PCD

Considerando os salários de contribuição constantes no CNIS a partir de 07/1994, com o descarte de {{QTD_DESCARTES}} contribuições que reduziam a média (art. 26, § 6º, da EC nº 103/2019), a média dos salários de contribuição foi apurada em R$ {{MEDIA_PCD}}.

Sobre ela incide o coeficiente de 100% (art. 8º, I, da LC 142/2013), sem aplicação do fator previdenciário ({{FATOR_PREVIDENCIARIO}}), por ser desfavorável ao(à) segurado(a) (art. 9º, I, da LC 142/2013). [AJUSTAR SE O FATOR FOR FAVORÁVEL]

A renda mensal inicial da aposentadoria da pessoa com deficiência foi, portanto, apurada em:

R$ {{RMI_PCD}} – {{RMI_PCD_EXTENSO}}.

| Parâmetro | Benefício concedido (INSS) | Aposentadoria PCD (revisão) |
|---|---|---|
| Espécie / regra | {{ESPECIE_BENEFICIO}} – {{REGRA_APLICADA_INSS}} | Aposentadoria por tempo de contribuição da PCD – art. 3º, {{INCISO_ART_3}}, LC 142/2013 |
| Tempo de contribuição | {{TEMPO_CONSIDERADO_INSS}} | {{TEMPO_TOTAL_CONVERTIDO}} (convertido – grau {{GRAU_DEFICIENCIA_ADOTADO}}) |
| Média dos salários de contribuição | R$ {{MEDIA_INSS}} | R$ {{MEDIA_PCD}} |
| Coeficiente | {{COEFICIENTE_INSS}} | 100% |
| Fator previdenciário | Não se aplica | Não aplicado ({{FATOR_PREVIDENCIARIO}} – desfavorável) |
| RMI em {{DIB}} | R$ {{RMI_INSS}} | R$ {{RMI_PCD}} |
| Renda mensal atual ({{COMPETENCIA_ATUAL}}) | R$ {{RMA_INSS}} | R$ {{RMA_PCD}} |

A revisão representa um acréscimo de R$ {{ACRESCIMO_RMI}} na renda mensal inicial, o equivalente a um aumento de {{PERCENTUAL_AUMENTO}} no valor do benefício, com reflexos em todas as parcelas futuras.

## DOS VALORES ATRASADOS

Os valores atrasados correspondem à diferença entre a renda devida na aposentadoria da pessoa com deficiência e a renda efetivamente paga pelo INSS no benefício ativo (NB {{NB}}), desde a DIB ({{DIB}}) até a data do ajuizamento ({{COMPETENCIA_AJUIZAMENTO}}), incluindo as gratificações natalinas, com correção monetária pelo INPC, conforme o Manual de Cálculos da Justiça Federal (Resolução CJF nº 990/2026):

| Competência | Devido (PCD) | Índice CM | Devido corrigido | Recebido (INSS) | Recebido corrigido | Diferença corrigida |
|---|---|---|---|---|---|---|
| {{COMPETENCIA}} | R$ {{DEVIDO_PCD}} | {{INDICE_CM}} | R$ {{DEVIDO_CORRIGIDO}} | R$ {{RECEBIDO_INSS}} | R$ {{RECEBIDO_CORRIGIDO}} | R$ {{DIFERENCA_CORRIGIDA}} |
| 13º/{{ANO}} | R$ {{DEVIDO_PCD}} | {{INDICE_CM}} | R$ {{DEVIDO_CORRIGIDO}} | R$ {{RECEBIDO_INSS}} | R$ {{RECEBIDO_CORRIGIDO}} | R$ {{DIFERENCA_CORRIGIDA}} |
| TOTAL | R$ {{TOTAL_DEVIDO_PCD}} | - | R$ {{TOTAL_DEVIDO_CORRIGIDO}} | R$ {{TOTAL_RECEBIDO}} | R$ {{TOTAL_RECEBIDO_CORRIGIDO}} | R$ {{ATRASADOS}} |

[UMA LINHA POR COMPETÊNCIA, INCLUINDO PARCELAS DE 13º]

O valor das parcelas vencidas até o ajuizamento, já deduzidos os valores recebidos pelo(a) segurado(a) no benefício concedido, é de:

R$ {{ATRASADOS}} – {{ATRASADOS_EXTENSO}}.

## DO VALOR DA CAUSA

Para fins de ajuizamento da ação em {{COMPETENCIA_AJUIZAMENTO}}, o valor da causa corresponde à soma das parcelas vencidas até o ajuizamento com doze parcelas vincendas (art. 292, §§ 1º e 2º, do CPC), em ambos os casos com o encontro de contas entre os valores devidos na aposentadoria da pessoa com deficiência e os valores recebidos no benefício ativo, conforme demonstrativo abaixo:

| Parcelas | Devido (PCD) | Recebido (INSS) | Diferença |
|---|---|---|---|
| Vencidas até o ajuizamento ({{PERIODO_VENCIDAS}}) | R$ {{TOTAL_DEVIDO_CORRIGIDO}} | R$ {{TOTAL_RECEBIDO_CORRIGIDO}} | R$ {{ATRASADOS}} |
| 12 parcelas vincendas (R$ {{RMA_PCD}} x R$ {{RMA_INSS}}, com gratificações natalinas de {{COMPETENCIAS_13_VINCENDAS}}) | R$ {{VINCENDAS_DEVIDO}} | R$ {{VINCENDAS_RECEBIDO}} | R$ {{VINCENDAS_DIFERENCA}} |
| SELIC / taxa legal previdenciária | - | - | R$ {{SELIC_TAXA_LEGAL}} |
| VALOR DA CAUSA | R$ {{VALOR_CAUSA_DEVIDO}} | R$ {{VALOR_CAUSA_RECEBIDO}} | R$ {{VALOR_CAUSA}} |

O valor da causa foi apurado em:

R$ {{VALOR_CAUSA}} – {{VALOR_CAUSA_EXTENSO}}.

O valor apurado não ultrapassa o limite de 60 salários mínimos (60 x R$ {{SALARIO_MINIMO_VIGENTE}} = R$ {{TETO_JEF_60_SM}}), de modo que a ação deverá ser ajuizada perante o Juizado Especial Federal, em razão de sua competência absoluta (art. 3º, § 3º, da Lei nº 10.259/2001). Não foram computados juros de mora, que incidirão a partir da citação, pela taxa legal previdenciária. [AJUSTAR SE ULTRAPASSAR 60 SALÁRIOS MÍNIMOS]

## DA CONCLUSÃO

Diante da cronologia dos laudos médicos apresentados, verifica-se que a condição de pessoa com deficiência do(a) segurado(a) está comprovada desde {{DATA_MARCO_INICIAL_DEFICIENCIA}}, data de {{DOCUMENTO_MARCO_INICIAL}}, com continuidade confirmada pelos documentos de {{DATAS_DOCUMENTOS_CONTINUIDADE}}.

Com a conversão dos períodos sem deficiência pelo fator {{FATOR_CONVERSAO_PCD}} (art. 7º da LC 142/2013 e art. 70-E do Decreto nº 3.048/1999), o(a) segurado(a) alcança {{TEMPO_TOTAL_CONVERTIDO}} de tempo de contribuição na DER ({{DIB}}), superando o mínimo de {{TEMPO_EXIGIDO_PCD}} exigido pelo art. 3º, inciso {{INCISO_ART_3}}, da LC 142/2013 para a deficiência de grau {{GRAU_DEFICIENCIA_ADOTADO}}.

Nesse cenário, é possível a revisão do benefício, com sua conversão em aposentadoria por tempo de contribuição da pessoa com deficiência, com renda mensal inicial de: R$ {{RMI_PCD}} (em substituição aos R$ {{RMI_INSS}} concedidos), renda mensal atual de R$ {{RMA_PCD}} ({{COMPETENCIA_ATUAL}}), valores atrasados de R$ {{ATRASADOS}} até o ajuizamento e valor da causa de R$ {{VALOR_CAUSA}}, apurado para ajuizamento em {{COMPETENCIA_AJUIZAMENTO}}.

Ressalva-se que o reconhecimento da deficiência e de sua data de início dependerá da avaliação médica e funcional a ser realizada pela perícia do INSS (art. 4º da LC 142/2013 e art. 70-D do Decreto nº 3.048/1999) ou, em juízo, por perícia judicial, sendo recomendável instruir o pedido com todos os laudos ora analisados, em especial o de {{DATA_MARCO_INICIAL_DEFICIENCIA}}.

Caso a perícia reconheça grau {{GRAU_DEFICIENCIA_LAUDO}} em parte do período, o tempo convertido poderá ser ainda maior. [AJUSTAR AO CASO]

Recomenda-se, assim, o ajuizamento de pedido de revisão administrativa ou de ação judicial perante o Juizado Especial Federal para a conversão do benefício, observado o prazo decadencial de 10 anos previsto no art. 103 da Lei nº 8.213/1991.

Assim, encerro a presente análise.

{{CIDADE}}, {{DATA_PARECER}}.

{{ADVOGADA_NOME}}
{{ADVOGADA_OAB}}
Especialista em Cálculos Previdenciários
