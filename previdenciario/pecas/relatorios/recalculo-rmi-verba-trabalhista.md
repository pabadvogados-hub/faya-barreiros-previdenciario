---
tipo: recalculo-rmi-verba-trabalhista
titulo: RELATÓRIO - PARECER TÉCNICO - RECÁLCULO DE RMI (VERBA TRABALHISTA)
grupo: relatorio
objetivo: Recalcular a RMI integrando aos salários de contribuição as verbas salariais reconhecidas em reclamação trabalhista e apurar vantagem na RMI/RMA e valor da causa (com e sem vincendas)
documentos_necessarios:
  - Carta de concessão e memória de cálculo do benefício
  - Sentença/acórdão/acordo da reclamação trabalhista
  - Planilha de cálculos trabalhistas com a remuneração mês a mês (salário base e verbas reconhecidas)
  - CNIS
  - Planilha de recálculo da RMI e do valor da causa (anexos)
campos:
  - SOLICITANTE
  - SEGURADO_NOME
  - SEGURADO_CPF
  - ESPECIE_BENEFICIO
  - NB
  - DIB
  - EMPREGADOR_RECLAMADO
  - NUMERO_PROCESSO_TRABALHISTA
  - PERIODO_VERBAS
  - RMI_INSS
  - RMI_INSS_EXTENSO
  - VERBAS_RECONHECIDAS
  - RMI_RECALCULO
  - RMI_RECALCULO_EXTENSO
  - VANTAGEM_RMI
  - VANTAGEM_RMI_EXTENSO
  - COMPETENCIA_AJUIZAMENTO
  - VALOR_CAUSA_ADMINISTRATIVO
  - VALOR_CAUSA_ADMINISTRATIVO_EXTENSO
  - COMPETENCIA_PRESCRICAO
  - VALOR_CAUSA
  - VALOR_CAUSA_EXTENSO
  - COMPETENCIA_ATUAL
  - RMA_RECALCULO
  - RMA_RECALCULO_EXTENSO
  - VANTAGEM_RMA
  - VANTAGEM_RMA_EXTENSO
  - RMA_INSS
  - TETO_ANO_DIB
  - CIDADE
  - DATA_PARECER
  - ADVOGADA_NOME
  - ADVOGADA_OAB
citacoes:
  - Lei nº 8.213/91
  - prescrição quinquenal
  - Manual de Cálculos da Justiça Federal
---

# PARECER TÉCNICO

**RECÁLCULO DE RENDA MENSAL INICIAL**

## DADOS INICIAIS

| Solicitante: | {{SOLICITANTE}} |
|---|---|
| Segurado(a): | {{SEGURADO_NOME}} |
| CPF: | {{SEGURADO_CPF}} |
| Benefício: | {{ESPECIE_BENEFICIO}} |
| NB: | {{NB}} |
| DIB / DII: | {{DIB}} |

## RELATÓRIO

Trata-se de recálculo da Renda Mensal Inicial (RMI) do benefício de {{ESPECIE_BENEFICIO}}, NB {{NB}}, concedido em favor do(a) segurado(a) {{SEGURADO_NOME}}, com Data de Início do Benefício (DIB) e Data do Início da Incapacidade (DII) fixada em {{DIB}}. [AJUSTAR SE O BENEFÍCIO NÃO FOR POR INCAPACIDADE]

O objetivo do presente trabalho consiste em recalcular a Renda Mensal Inicial com base na integração, aos salários de contribuição do(a) segurado(a), das verbas de natureza salarial reconhecidas em sede de reclamação trabalhista movida em face de {{EMPREGADOR_RECLAMADO}} (Processo nº {{NUMERO_PROCESSO_TRABALHISTA}}), relativas ao período de {{PERIODO_VERBAS}}, projetando-se o novo salário de benefício e a consequente vantagem na RMI.

## DA METODOLOGIA APLICADA

Os cálculos seguem os mesmos parâmetros e critérios da legislação previdenciária vigente à época da Data de Início da Incapacidade (Lei nº 8.213/91 e regulamentação correlata), com atualização monetária dos salários de contribuição pelos índices oficiais aplicáveis a cada competência, de modo que o resultado apresentado é de natureza puramente matemática, extraído de calculadora previdenciária especializada.

## DA RENDA MENSAL INICIAL DO BENEFÍCIO

O valor da Renda Mensal Inicial concedida administrativamente pelo INSS foi de:

R$ {{RMI_INSS}} ({{RMI_INSS_EXTENSO}}), conforme Carta de Concessão do Benefício, reproduzida abaixo:

[INSERIR IMAGEM: carta de concessão do benefício com a RMI]

## DA ALTERAÇÃO DA BASE DE CÁLCULO

O(A) segurado(a) manejou reclamação trabalhista em face de seu empregador, {{EMPREGADOR_RECLAMADO}} (Processo nº {{NUMERO_PROCESSO_TRABALHISTA}}), tendo sido reconhecida judicialmente a incorporação, à sua remuneração, das verbas de {{VERBAS_RECONHECIDAS}} [no original: "Gratificação de Função e Adicional por Tempo de Serviço (ATS)"], as quais deixaram de compor, à época, os salários de contribuição informados à Previdência Social.

Em razão desse reconhecimento, a base de cálculo do benefício deve ser retificada para incluir, nos salários de contribuição do período de {{PERIODO_VERBAS}}, a remuneração total reconhecida na esfera trabalhista (salário base acrescido de {{VERBAS_RECONHECIDAS}}), em substituição aos valores até então considerados para as mesmas competências, com reflexo direto sobre o salário de benefício e sobre a Renda Mensal Inicial.

[INSERIR IMAGEM: trecho da decisão trabalhista que reconhece as verbas]

## DA BASE DE CÁLCULO

### DOS SALÁRIOS DA DEMANDA TRABALHISTA

Considerando a inclusão do período acima na base dos salários de contribuição, conforme tabela de apuração encaminhada pela reclamação trabalhista (competências {{PERIODO_VERBAS}}), tem-se a seguinte composição remuneratória (salário base e {{VERBAS_RECONHECIDAS}}):

[INSERIR IMAGEM: tabela da composição remuneratória mês a mês (salário base + verbas reconhecidas)]

Nesse cenário, o valor da RMI apresenta vantagem ao(à) segurado(a), sendo apurado, na DIB/DER ({{DIB}}), o valor de:

R$ {{RMI_RECALCULO}} ({{RMI_RECALCULO_EXTENSO}})

[INSERIR IMAGEM: demonstrativo do recálculo da RMI]

Logo, tem-se uma vantagem na RMI, na DIB, no valor de:

R$ {{VANTAGEM_RMI}} ({{VANTAGEM_RMI_EXTENSO}})

## DA APURAÇÃO DO VALOR DA CAUSA

### DO VALOR DA CAUSA ADMINISTRATIVO (SEM PARCELAS VINCENDAS)

Considerando eventual pleito de revisão exclusivamente na via administrativa, computadas apenas as diferenças vencidas até a data do ajuizamento/protocolo ({{COMPETENCIA_AJUIZAMENTO}}), sem parcelas vincendas, o valor é de:

R$ {{VALOR_CAUSA_ADMINISTRATIVO}} ({{VALOR_CAUSA_ADMINISTRATIVO_EXTENSO}})

### DO VALOR DA CAUSA — DESDE A DIB, COM PARCELAS VINCENDAS

Considerando as diferenças mensais devidas desde a DIB ({{DIB}}) até o ajuizamento da ação ({{COMPETENCIA_AJUIZAMENTO}}), aplicada a prescrição quinquenal (parcelas anteriores a {{COMPETENCIA_PRESCRICAO}}), acrescidas de correção monetária, SELIC e taxa legal previdenciária, nos termos do Manual de Cálculos da Justiça Federal, e computadas ainda 12 (doze) parcelas vincendas, o valor da causa é de:

R$ {{VALOR_CAUSA}} ({{VALOR_CAUSA_EXTENSO}})

[INSERIR IMAGEM: resumo do cálculo do valor da causa]

## DA RENDA MENSAL ATUAL

Atualizando-se os valores para a data atual ({{COMPETENCIA_ATUAL}}), a Renda Mensal Atual (RMA) do benefício revisado corresponde a:

R$ {{RMA_RECALCULO}} ({{RMA_RECALCULO_EXTENSO}})

O que representa uma vantagem mensal, em valores atuais, de R$ {{VANTAGEM_RMA}} ({{VANTAGEM_RMA_EXTENSO}}), a se repetir em todas as competências futuras enquanto mantido o benefício.

[CONFERIR: o original diz "RMA do benefício efetivamente pago" mas o valor indicado é a RMA revisada (a conclusão confirma: RMA atual do INSS → RMA revisada); redação ajustada para "benefício revisado"]

## CONCLUSÃO

Diante do exposto, é possível concluir pelo cabimento da revisão da Renda Mensal Inicial do benefício NB {{NB}}, titularizado por {{SEGURADO_NOME}}, tendo em vista a comprovada vantagem decorrente da inclusão, na base de cálculo, das verbas de {{VERBAS_RECONHECIDAS}} reconhecidas na Justiça do Trabalho (Processo nº {{NUMERO_PROCESSO_TRABALHISTA}} — {{EMPREGADOR_RECLAMADO}}).

O período de cálculo alterado pela presente revisão compreende as competências de {{PERIODO_VERBAS}}, nas quais os salários de contribuição originalmente considerados foram substituídos pela remuneração total reconhecida na demanda trabalhista, resultando em:

- Aumento da RMI, na DIB ({{DIB}}), de R$ {{RMI_INSS}} para R$ {{RMI_RECALCULO}}, vantagem de: R$ {{VANTAGEM_RMI}};
- Aumento da RMA atual ({{COMPETENCIA_ATUAL}}), de R$ {{RMA_INSS}} para R$ {{RMA_RECALCULO}}, vantagem mensal de R$ {{VANTAGEM_RMA}};
- Valor da causa, para fins de ajuizamento em {{COMPETENCIA_AJUIZAMENTO}}, de R$ {{VALOR_CAUSA}} (com vincendas) ou R$ {{VALOR_CAUSA_ADMINISTRATIVO}} (apenas via administrativa, sem vincendas).

[SE A RMI ESTIVER PRÓXIMA DO TETO] É importante considerar que no ano de concessão do benefício o teto previdenciário era de R$ {{TETO_ANO_DIB}}, portanto o(a) segurado(a) já recebia valor próximo ao limite máximo.

Assim, conclui-se pelo cabimento da revisão pleiteada, finalizando-se o presente parecer, acompanhado dos respectivos anexos de cálculo.

{{CIDADE}}, {{DATA_PARECER}}.

{{ADVOGADA_NOME}}
{{ADVOGADA_OAB}}
Especialista em Cálculos Previdenciários
