---
tipo: parecer-liquidacao
titulo: RELATÓRIO - PARECER - CÁLCULO DE LIQUIDAÇÃO DE SENTENÇA
grupo: relatorio
objetivo: Parecer que acompanha a conta de liquidação de sentença previdenciária (citação, sentença, acórdão, trânsito, implantação, RMI, parâmetros, honorários, abatimentos e total exequendo)
documentos_necessarios:
  - Sentença, acórdão e certidão de trânsito em julgado
  - Comprovante da data de citação do INSS
  - Carta de concessão e de revisão do benefício (RMI de concessão e de revisão)
  - Processo administrativo da revisão, quando houver
  - Extrato de pagamentos do benefício (HISCRE)
  - Memória de cálculo da liquidação (anexos)
campos:
  - NUMERO_PROCESSO
  - SEGURADO_NOME
  - ESPECIE_BENEFICIO
  - DATA_CITACAO
  - RMI_RECALCULADA
  - RMI_RECALCULADA_EXTENSO
  - PERCENTUAL_HONORARIOS
  - HONORARIOS
  - HONORARIOS_EXTENSO
  - FLS_COMPLEMENTO_POSITIVO
  - TOTAL_EXEQUENDO
  - TOTAL_EXEQUENDO_EXTENSO
  - NUMERO_LAUDAS
  - NUMERO_ANEXOS
  - CIDADE
  - DATA_PARECER
  - ADVOGADA_NOME
  - ADVOGADA_OAB
citacoes:
  - nenhuma citação legal no modelo original
---

# CÁLCULO DE LIQUIDAÇÃO DE SENTENÇA

**PROCESSO:** {{NUMERO_PROCESSO}}
**SEGURADO(A):** {{SEGURADO_NOME}}
**BENEFÍCIO:** {{ESPECIE_BENEFICIO}}

## RELATÓRIO

Trata-se de cálculo de liquidação de sentença referente aos autos {{NUMERO_PROCESSO}}, em que figuram como partes {{SEGURADO_NOME}} x INSS.

## DA CITAÇÃO

A citação do INSS ocorreu em {{DATA_CITACAO}}.

## DA R. SENTENÇA

A r. sentença prolatada julgou a demanda PROCEDENTE nos seguintes termos: [AJUSTAR O RESULTADO AO CASO]

[INSERIR IMAGEM: recorte do dispositivo da sentença]

## DO V. ACÓRDÃO

[INSERIR IMAGEM: recorte do dispositivo do acórdão]

## DO TRÂNSITO EM JULGADO

[INSERIR IMAGEM: certidão de trânsito em julgado]

## DA IMPLANTAÇÃO DO BENEFÍCIO

A implantação do benefício ainda não ocorreu, de modo que a liquidação foi realizada até a presente competência. [AJUSTAR AO CASO — se já implantado, indicar a DIP e limitar as parcelas até ela]

## DA RENDA MENSAL INICIAL RECALCULADA

A RMI recalculada do benefício foi de:

R$ {{RMI_RECALCULADA}} – {{RMI_RECALCULADA_EXTENSO}};

[INSERIR IMAGEM: demonstrativo da RMI recalculada]

## DOS PARÂMETROS DO CÁLCULO

Os cálculos de liquidação deverão seguir os seguintes parâmetros:

[INSERIR IMAGEM: quadro de critérios e parâmetros do cálculo (DIB, DIP, citação/início dos juros, índice de correção monetária, juros de mora, SELIC, honorários)]

## DOS HONORÁRIOS

Os honorários totalizam o percentual de {{PERCENTUAL_HONORARIOS}} até a data da r. sentença:

[INSERIR IMAGEM: demonstrativo do cálculo dos honorários de sucumbência]

E totalizam:
R$ {{HONORARIOS}} – {{HONORARIOS_EXTENSO}};

## DO ABATIMENTO DO BENEFÍCIO RECEBIDO

Para fins de apuração do crédito final, houve abatimento do valor recebido à título de {{ESPECIE_BENEFICIO}}, devidamente revisado.

É conveniente salientar que o benefício foi concedido no valor inicial de:

1 – RMI Concessão:

[INSERIR IMAGEM: carta de concessão com a RMI original]

1 – RMI Revisão:

[INSERIR IMAGEM: carta de revisão com a RMI revisada]

[OBSERVAÇÃO-MODELO — USAR QUANDO HOUVER COMPLEMENTO POSITIVO NÃO LOCALIZADO NO EXTRATO]
OBS: O Valor referente à diferença acima CONSTA COMO pago através de complemento positivo conforme fls. {{FLS_COMPLEMENTO_POSITIVO}} do PA da revisão.

[INSERIR IMAGEM: folha do processo administrativo que menciona o complemento positivo]

Contudo, não localizei esse valor no extrato de pagamento.

[INSERIR IMAGEM: extrato de pagamentos (HISCRE) do período]

O pedido de PAGAMENTO DE BENEFÍCIO NÃO RECEBIDO não abarca esse valor, e nos extratos de pagamento também não consta pagamento, de modo que inseri no valor da condenação.

## DO TOTAL EXEQUENDO

O somatório final da liquidação totaliza o valor de:

R$ {{TOTAL_EXEQUENDO}} – {{TOTAL_EXEQUENDO_EXTENSO}}.

[INSERIR IMAGEM: resumo final da conta (parcelas vencidas, juros, SELIC, honorários, total)]

São essas as conclusões do presente cálculo, finalizando o presente parecer em {{NUMERO_LAUDAS}} laudas e {{NUMERO_ANEXOS}} anexos.

{{CIDADE}}, {{DATA_PARECER}}.

{{ADVOGADA_NOME}}
{{ADVOGADA_OAB}}
Especialista em Cálculos Previdenciários
