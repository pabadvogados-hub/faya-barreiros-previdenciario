---
tipo: parecer-recalculo-de-rmi
titulo: RELATÓRIO - PARECER - RECÁLCULO DE RENDA MENSAL INICIAL
grupo: relatorio
objetivo: Demonstrar erro na concessão por omissão de período contributivo (ex. contribuinte individual) e recalcular tempo, carência, descartes, divisor e RMI, com comparativo carta x recálculo
documentos_necessarios:
  - Carta de concessão e memória de cálculo do benefício
  - Processo administrativo (com as provas do período omitido, ex. guias de recolhimento)
  - CNIS completo
  - Guias de recolhimento (GPS/DARF) do período omitido
  - Planilha de apuração de tempo e RMI (anexo)
campos:
  - SEGURADO_NOME
  - ESPECIE_BENEFICIO
  - NB
  - DIB
  - DATA_CONCESSAO
  - RMI_INSS
  - RMI_INSS_EXTENSO
  - CATEGORIA_PERIODO_OMITIDO
  - EMPRESA_PERIODO_OMITIDO
  - PERIODO_OMITIDO_INICIO
  - PERIODO_OMITIDO_FIM
  - BASE_RECOLHIMENTO_PERIODO_OMITIDO
  - SEGURADO_CPF
  - SEGURADO_DATA_NASCIMENTO
  - SEGURADO_SEXO
  - DER
  - REGRA_APLICADA
  - TEMPO_INSS_SEM_DESCARTE
  - TEMPO_INSS_COM_DESCARTE
  - CARENCIA_INSS_SEM_DESCARTE
  - CARENCIA_INSS_COM_DESCARTE
  - IDADE_NA_DER
  - DESCARTES_INSS
  - SOMA_SALARIOS_INSS
  - DIVISOR_INSS
  - COMPETENCIA_ANTES_LACUNA
  - COMPETENCIA_DEPOIS_LACUNA
  - INTERVALO_NAO_COMPUTADO
  - TEMPO_PERIODO_OMITIDO
  - CARENCIA_PERIODO_OMITIDO
  - FLS_PROVAS_PA
  - TEMPO_RECALCULO
  - CARENCIA_RECALCULO
  - TOTAL_COMPETENCIAS_INSS
  - DESCARTES_RECALCULO
  - PERFIL_COMPETENCIAS_DESCARTADAS
  - TEMPO_MINIMO_REGRA
  - CARENCIA_MINIMA_REGRA
  - SOMA_SALARIOS_RECALCULO
  - DIVISOR_RECALCULO
  - RMI_RECALCULO
  - RMI_RECALCULO_EXTENSO
  - VANTAGEM_RMI
  - VANTAGEM_RMI_EXTENSO
  - CIDADE
  - DATA_PARECER
  - ADVOGADA_NOME
  - ADVOGADA_OAB
citacoes:
  - Emenda Constitucional nº 103/2019
  - art. 20 da Emenda Constitucional nº 103/2019
  - Art. 20 da EC 103/2019 (idade mínima + tempo de contribuição + pedágio de 100%)
  - art. 26, § 6º, da EC 103/2019
  - prazo decadencial de 10 (dez) anos, contado do primeiro dia do mês seguinte ao do recebimento da primeira prestação
---

# RECÁLCULO DE RENDA MENSAL INICIAL

**Segurado(a):** {{SEGURADO_NOME}}
**Benefício:** {{ESPECIE_BENEFICIO}}
**NB:** {{NB}}
**DIB:** {{DIB}}

## RELATÓRIO

Trata-se de recálculo da Renda Mensal Inicial (RMI) do benefício de {{ESPECIE_BENEFICIO}}, NB {{NB}}, concedido em favor do(a) segurado(a) {{SEGURADO_NOME}}, com Data de Entrada do Requerimento (DER) e Data de Início do Benefício (DIB) em {{DIB}}, concessão publicada em {{DATA_CONCESSAO}}, com RMI fixada em R$ {{RMI_INSS}} ({{RMI_INSS_EXTENSO}}).

Da análise do processo administrativo e da respectiva memória de cálculo, constatou-se que o INSS não considerou, na apuração do tempo de contribuição, da carência e da base de cálculo dos salários de contribuição, o período em que o(a) segurado(a) exerceu atividade como {{CATEGORIA_PERIODO_OMITIDO}} junto à empresa {{EMPRESA_PERIODO_OMITIDO}}, entre {{PERIODO_OMITIDO_INICIO}} e {{PERIODO_OMITIDO_FIM}}, cujos recolhimentos foram efetuados sobre {{BASE_RECOLHIMENTO_PERIODO_OMITIDO}}.

A ausência desse período no cômputo administrativo impactou negativamente tanto o tempo de contribuição total quanto a quantidade de descartes de salários de contribuição autorizados por lei, resultando em RMI inferior à que o(a) segurado(a) efetivamente faz jus, conforme demonstrado a seguir.

## DADOS DO(A) SEGURADO(A)

| Campo | Informação |
|---|---|
| Segurado(a) | {{SEGURADO_NOME}} |
| CPF | {{SEGURADO_CPF}} |
| Data de Nascimento | {{SEGURADO_DATA_NASCIMENTO}} |
| Sexo | {{SEGURADO_SEXO}} |
| Benefício | {{ESPECIE_BENEFICIO}} |
| NB | {{NB}} |
| DER | {{DER}} |
| DIB | {{DIB}} |
| Data da concessão | {{DATA_CONCESSAO}} |

## DA METODOLOGIA APLICADA

Os cálculos ora apresentados seguem os mesmos parâmetros da legislação previdenciária vigente (Emenda Constitucional nº 103/2019 e legislação correlata), utilizando os dados de vínculos e remunerações constantes do CNIS do(a) segurado(a), acrescidos do período de {{CATEGORIA_PERIODO_OMITIDO}} objeto do presente parecer.

O resultado ora exposto é puramente matemático, obtido a partir das mesmas regras de transição utilizadas pelo INSS na concessão do benefício.

## DA RENDA MENSAL INICIAL DO BENEFÍCIO CONCEDIDO

O valor da Renda Mensal Inicial concedida pelo INSS foi de R$ {{RMI_INSS}}, apurado com base na regra de transição do {{REGRA_APLICADA}} [ex.: "art. 20 da Emenda Constitucional nº 103/2019 (idade mínima + tempo de contribuição + pedágio de 100%)"], conforme carta de concessão em anexo, considerando os seguintes parâmetros:

| Parâmetro | Apurado pelo INSS |
|---|---|
| Regra aplicada | {{REGRA_APLICADA}} |
| Tempo de contribuição (sem descarte) | {{TEMPO_INSS_SEM_DESCARTE}} |
| Tempo de contribuição (com descarte) | {{TEMPO_INSS_COM_DESCARTE}} |
| Carência (sem descarte) | {{CARENCIA_INSS_SEM_DESCARTE}} meses |
| Carência (com descarte) | {{CARENCIA_INSS_COM_DESCARTE}} meses |
| Idade na DER | {{IDADE_NA_DER}} |
| Quantidade de descartes utilizados | {{DESCARTES_INSS}} salários de contribuição |
| Soma dos salários (com descarte) | R$ {{SOMA_SALARIOS_INSS}} ÷ {{DIVISOR_INSS}} competências |
| RMI apurada | R$ {{RMI_INSS}} |

## DO RECÁLCULO

### DA OMISSÃO DO PERÍODO COMO {{CATEGORIA_PERIODO_OMITIDO}}

Da análise pormenorizada da memória de cálculo constante na carta de concessão, verifica-se que a relação de competências consideradas pelo INSS salta diretamente da competência {{COMPETENCIA_ANTES_LACUNA}} para a competência {{COMPETENCIA_DEPOIS_LACUNA}}, evidenciando que nenhuma competência do intervalo compreendido entre {{INTERVALO_NAO_COMPUTADO}} foi computada na apuração do benefício.

Tal lacuna corresponde, precisamente, ao período em que o(a) segurado(a) {{SEGURADO_NOME}} exerceu atividade como {{CATEGORIA_PERIODO_OMITIDO}} junto à empresa {{EMPRESA_PERIODO_OMITIDO}}, entre {{PERIODO_OMITIDO_INICIO}} e {{PERIODO_OMITIDO_FIM}} ({{TEMPO_PERIODO_OMITIDO}} de tempo de contribuição, com {{CARENCIA_PERIODO_OMITIDO}} meses de carência), com recolhimentos efetuados sobre {{BASE_RECOLHIMENTO_PERIODO_OMITIDO}}, período este que deveria ter sido integralmente considerado tanto para fins de tempo de contribuição e carência quanto para a apuração da média dos salários de contribuição do benefício.

É conveniente salientar que no processo administrativo houve informação acerca do período e produção de provas, tais como juntada de guias de recolhimento, a rigor das fls. {{FLS_PROVAS_PA}} e seguintes. [AJUSTAR AO CASO]

Procedendo-se ao recálculo com a devida inclusão desse período, permanece aplicável a mesma regra de transição do {{REGRA_APLICADA}} (a mais vantajosa ao segurado, dispensando a incidência do fator previdenciário), porém com sensível alteração dos parâmetros de tempo, carência e, principalmente, da base de cálculo da RMI. [AJUSTAR SE A REGRA MAIS VANTAJOSA MUDAR]

### DA CONFERÊNCIA DE TEMPO

Com a inclusão do período junto à {{EMPRESA_PERIODO_OMITIDO}}, o tempo de contribuição total do(a) segurado(a), apurado até a DER ({{DER}}), passa a ser de {{TEMPO_RECALCULO}}, com carência de {{CARENCIA_RECALCULO}} meses, conforme comparativo abaixo:

| Parâmetro | Carta de Concessão (INSS) | Recálculo |
|---|---|---|
| Tempo de contribuição | {{TEMPO_INSS_COM_DESCARTE}} | {{TEMPO_RECALCULO}} |
| Carência | {{CARENCIA_INSS_COM_DESCARTE}} meses | {{CARENCIA_RECALCULO}} meses |

### DA CONFERÊNCIA DA RMI E DOS DESCARTES

A legislação previdenciária autoriza o descarte dos salários de contribuição menos vantajosos ao segurado, desde que mantidos o tempo mínimo de contribuição e a carência exigidos para a regra de transição aplicável (art. 26, § 6º, da EC 103/2019). No cálculo original realizado pelo INSS, em razão do reduzido número de competências disponíveis ({{TOTAL_COMPETENCIAS_INSS}} ao todo, sem o período omitido), foram aplicados apenas {{DESCARTES_INSS}} descartes, resultando em uma média de R$ {{RMI_INSS}} (soma de R$ {{SOMA_SALARIOS_INSS}} dividida por {{DIVISOR_INSS}} competências).

Com a inclusão do período de {{PERIODO_OMITIDO_INICIO}} a {{PERIODO_OMITIDO_FIM}} como {{CATEGORIA_PERIODO_OMITIDO}}, o total de competências disponíveis para a apuração da média foi ampliado, elevando de {{DESCARTES_INSS}} para {{DESCARTES_RECALCULO}} a quantidade máxima de salários de contribuição passíveis de descarte na regra do {{REGRA_APLICADA}}.

Tais descartes recaem justamente sobre as competências mais antigas e de menor valor real ({{PERFIL_COMPETENCIAS_DESCARTADAS}}), sem prejuízo do tempo mínimo de contribuição ({{TEMPO_MINIMO_REGRA}}) e da carência mínima ({{CARENCIA_MINIMA_REGRA}} contribuições) exigidos para o direito ao benefício.

Utilizando a totalidade dos {{DESCARTES_RECALCULO}} descartes autorizados por lei, a soma dos salários de contribuição válidos passa a R$ {{SOMA_SALARIOS_RECALCULO}}, dividida por {{DIVISOR_RECALCULO}} competências remanescentes, aumentando a RMI para:

R$ {{RMI_RECALCULO}} – {{RMI_RECALCULO_EXTENSO}}.

[INSERIR IMAGEM: demonstrativo do recálculo da RMI com descartes]

## DO COMPARATIVO CARTA DE CONCESSÃO X RECÁLCULO

| Parâmetro | Carta de Concessão | Recálculo |
|---|---|---|
| Regra aplicável | {{REGRA_APLICADA}} | {{REGRA_APLICADA}} |
| Tempo de contribuição | {{TEMPO_INSS_COM_DESCARTE}} | {{TEMPO_RECALCULO}} |
| Carência | {{CARENCIA_INSS_COM_DESCARTE}} meses | {{CARENCIA_RECALCULO}} meses |
| Descartes utilizados | {{DESCARTES_INSS}} | {{DESCARTES_RECALCULO}} |
| Soma dos salários | R$ {{SOMA_SALARIOS_INSS}} | R$ {{SOMA_SALARIOS_RECALCULO}} |
| Divisor | {{DIVISOR_INSS}} | {{DIVISOR_RECALCULO}} |
| RMI apurada | R$ {{RMI_INSS}} | R$ {{RMI_RECALCULO}} |
| VANTAGEM NA RMI | - | R$ {{VANTAGEM_RMI}} |

## CONCLUSÃO

Diante do exposto, conclui-se pela existência de erro na concessão do benefício NB {{NB}}, decorrente da não inclusão, pelo INSS, do período de {{PERIODO_OMITIDO_INICIO}} a {{PERIODO_OMITIDO_FIM}}, no qual o(a) segurado(a) {{SEGURADO_NOME}} exerceu atividade como {{CATEGORIA_PERIODO_OMITIDO}} junto à empresa {{EMPRESA_PERIODO_OMITIDO}}, com recolhimentos sobre {{BASE_RECOLHIMENTO_PERIODO_OMITIDO}}.

A inclusão desse período, além de acrescer tempo de contribuição e carência ao benefício (de {{TEMPO_INSS_COM_DESCARTE}} para {{TEMPO_RECALCULO}}), amplia significativamente a quantidade de descartes de salários de contribuição menos vantajosos autorizados em lei — de {{DESCARTES_INSS}} para {{DESCARTES_RECALCULO}} —, elevando a Renda Mensal Inicial de R$ {{RMI_INSS}} para R$ {{RMI_RECALCULO}}, uma diferença mensal de R$ {{VANTAGEM_RMI}} ({{VANTAGEM_RMI_EXTENSO}}) em favor do(a) segurado(a), sem prejuízo dos reflexos sobre os valores em atraso desde a DIB.

Recomenda-se, portanto, a interposição de pedido administrativo de revisão do benefício perante o INSS (ou, se necessário, judicial), com o recálculo da RMI nos termos ora apresentados, observado o prazo decadencial de 10 (dez) anos, contado do primeiro dia do mês seguinte ao do recebimento da primeira prestação, previsto para a revisão de benefícios previdenciários.

Encerra-se o presente parecer, elaborado com base nos documentos apresentados pelo(a) segurado(a) (carta de concessão do benefício e planilha de apuração de tempo e RMI).

{{CIDADE}}, {{DATA_PARECER}}.

{{ADVOGADA_NOME}}
{{ADVOGADA_OAB}}
Especialista em Cálculos Previdenciários
