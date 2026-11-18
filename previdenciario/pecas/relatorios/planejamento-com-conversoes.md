---
tipo: planejamento-com-conversoes
titulo: RELATÓRIO - PLANEJAMENTO PREVIDENCIÁRIO - COM CONVERSÕES (TEMPO ESPECIAL)
grupo: relatorio
objetivo: Apurar o tempo exclusivamente especial e o tempo comum com conversão (fator) dos períodos especiais até 13/11/2019, verificar a aposentadoria especial e indicar datas/RMI das aposentadorias programadas
documentos_necessarios:
  - CNIS completo (com indicadores, ex. IEAN)
  - PPP (Perfil Profissiográfico Previdenciário) de cada vínculo com exposição a agente nocivo
  - LTCAT, quando necessário
  - CTPS
  - Planilha de apuração de tempo especial, tempo convertido e simulação de RMI (anexos)
campos:
  - SEGURADO_NOME
  - SEGURADO_DATA_NASCIMENTO
  - SEGURADO_CPF
  - SEGURADO_NIT
  - FUNCAO_ESPECIAL
  - SEGURADO_SEXO
  - EMPRESAS_COM_PPP
  - CBO
  - AGENTE_NOCIVO
  - ENQUADRAMENTO_AGENTE
  - FUNDAMENTO_EPI
  - FATOR_CONVERSAO
  - TEMPO_ESPECIAL_EXIGIDO
  - EMPRESAS_CONCOMITANTES
  - EMPREGADOR
  - DATA_INICIO
  - DATA_FIM
  - CARGO_AGENTE_PPP
  - INDICADOR_CNIS
  - FUNCAO_PPP
  - DATA_INICIO_IEAN
  - TEMPO_ESPECIAL
  - CARENCIA
  - DER
  - TEMPO_ESPECIAL_TOTAL
  - CARENCIA_TOTAL
  - TEMPO_ESPECIAL_ATE_EC103
  - FATOR
  - TEMPO_CONVERTIDO
  - TEMPO_COMUM_TOTAL
  - TEMPO_FALTANTE_ESPECIAL
  - DATA_ULTIMA_EXPOSICAO
  - DATA_INICIO_ATIVIDADE_ATUAL
  - EMPREGADOR_ATUAL
  - SEGURADO_PRIMEIRO_NOME
  - MEDIA_SALARIOS
  - MEDIA_SALARIOS_EXTENSO
  - COMPETENCIA_MEDIA
  - ULTIMO_SALARIO
  - DATA_IMPLEMENTO_ART15
  - IDADE_IMPLEMENTO_ART15
  - RMI_ART15
  - DATA_IMPLEMENTO_ART16_18
  - RMI_ART16_18
  - ANTECIPACAO_MESES
  - CIDADE
  - DATA_PARECER
  - ADVOGADA_NOME
  - ADVOGADA_OAB
citacoes:
  - código 1.0.1 do Decreto nº 53.831/64
  - Anexo IV do Decreto nº 3.048/99, item 2.0.0
  - Tema 555/STF
  - Súmula 66 da TNU
  - art. 70 do Decreto nº 3.048/99
  - Emenda Constitucional nº 103/2019
  - art. 25, § 2º, da EC nº 103/2019
  - Art. 15 da EC nº 103/2019 (tempo de contribuição/idade/pontos)
  - Arts. 16 e 18 da EC nº 103/2019 (idade mínima urbana – 65 anos)
  - art. 15 da EC nº 103/2019
---

# PLANEJAMENTO PREVIDENCIÁRIO

**Segurado(a):** {{SEGURADO_NOME}}
**Data de Nascimento:** {{SEGURADO_DATA_NASCIMENTO}}
**CPF:** {{SEGURADO_CPF}}
**NIT:** {{SEGURADO_NIT}}

## RELATÓRIO

O presente parecer tem por objetivo apurar, dentro das regras vigentes do Regime Geral de Previdência Social, o tempo de serviço exercido pelo(a) segurado(a) {{SEGURADO_NOME}} na função de {{FUNCAO_ESPECIAL}}, indicando ao final a data de implemento dos requisitos para o benefício de aposentadoria cabível e a conclusão técnica correspondente.

## DADOS DO(A) SEGURADO(A)

| Segurado(a) | {{SEGURADO_NOME}} |
|---|---|
| CPF | {{SEGURADO_CPF}} |
| NIT | {{SEGURADO_NIT}} |
| Data de Nascimento | {{SEGURADO_DATA_NASCIMENTO}} |
| Sexo | {{SEGURADO_SEXO}} |

## DA METODOLOGIA APLICADA

A apuração foi realizada com base no Extrato Previdenciário (CNIS) do(a) segurado(a) e nos Perfis Profissiográficos Previdenciários (PPP) apresentados pelas empresas {{EMPRESAS_COM_PPP}}, todos referentes ao exercício da atividade de {{FUNCAO_ESPECIAL}} (CBO {{CBO}}).

Para o reconhecimento da natureza especial da atividade foi considerada a exposição ao agente {{AGENTE_NOCIVO}}, enquadrado no {{ENQUADRAMENTO_AGENTE}} [no original, para radiação ionizante: "código 1.0.1 do Decreto nº 53.831/64 e no Anexo IV do Decreto nº 3.048/99, item 2.0.0"], sendo dispensada a análise de eficácia de EPI para esse agente, nos termos do entendimento consolidado pelo {{FUNDAMENTO_EPI}} [no original: "Tema 555/STF e pela Súmula 66 da TNU"]. [AJUSTAR AO AGENTE NOCIVO DO CASO]

Para a conversão do tempo especial em comum foi aplicado o fator {{FATOR_CONVERSAO}} ({{SEGURADO_SEXO}}, especial de {{TEMPO_ESPECIAL_EXIGIDO}} anos), na forma do art. 70 do Decreto nº 3.048/99, exclusivamente aos períodos de labor especial exercidos até 13/11/2019, data da entrada em vigor da Emenda Constitucional nº 103/2019. Os períodos especiais posteriores a essa data não foram convertidos em comum, em razão da vedação expressa do art. 25, § 2º, da EC nº 103/2019, sendo computados apenas pelo tempo calendário, tanto para fins de tempo de contribuição comum quanto para a eventual aposentadoria especial.

Foram ajustadas as concomitâncias entre vínculos simultâneos ({{EMPRESAS_CONCOMITANTES}}), de modo a evitar a contagem em duplicidade do mesmo intervalo de tempo.

## DOS VÍNCULOS EXERCIDOS NA FUNÇÃO DE {{FUNCAO_ESPECIAL}}

[INSERIR IMAGEM: trecho do CNIS/PPP com os vínculos na função especial]

O(A) segurado(a) exerceu a função de {{FUNCAO_ESPECIAL}} nos seguintes vínculos:

| Empregador | Início | Fim | Cargo/Função e agente nocivo (PPP) |
|---|---|---|---|
| {{EMPREGADOR}} | {{DATA_INICIO}} | {{DATA_FIM}} | {{CARGO_AGENTE_PPP}} [ex.: "função (CBO); agente físico ... (PPP com indicador ...)" / "Vínculo sem PPP apresentado; CNIS traz indicador IEAN (exposição a agente nocivo informada pelo empregador, passível de comprovação)" / "PPP registra função administrativa, sem menção a agente nocivo"] |

[USAR OS PARÁGRAFOS ABAIXO QUANDO HOUVER DIVERGÊNCIA ENTRE CNIS E PPP OU VÍNCULO SEM PPP]

Observa-se que o vínculo mantido junto a {{EMPREGADOR}} ({{DATA_INICIO}} a {{DATA_FIM}}) foi computado como tempo especial na apuração em razão do indicador {{INDICADOR_CNIS}} constante do CNIS;

Contudo, o PPP apresentado para esse período registra a função administrativa de “{{FUNCAO_PPP}}”, sem qualquer menção a agente nocivo ou ao exercício da {{FUNCAO_ESPECIAL}}. Recomenda-se a confirmação junto ao empregador e, se for o caso, a retificação do PPP, de modo a compatibilizar o documento com a real atividade exercida, sob pena de questionamento desse período pelo INSS.

Da mesma forma, o vínculo com {{EMPREGADOR}} ({{DATA_INICIO}} a {{DATA_FIM}}) apresenta indicador IEAN no CNIS a partir de {{DATA_INICIO_IEAN}}, sinalizando possível exposição a agente nocivo informada pelo empregador; como não foi apresentado o respectivo PPP, esse período foi computado apenas como tempo comum, podendo ser objeto de nova análise caso o documento seja localizado.

## DO TEMPO EXCLUSIVAMENTE ESPECIAL

Considerando exclusivamente os períodos em que restou comprovada a exposição a agente nocivo ({{AGENTE_NOCIVO}}) no exercício da função de {{FUNCAO_ESPECIAL}}, apurou-se o seguinte tempo de atividade especial:

| Empregador | Início | Fim | Tempo especial apurado | Carência |
|---|---|---|---|---|
| {{EMPREGADOR}} | {{DATA_INICIO}} | {{DATA_FIM}} | {{TEMPO_ESPECIAL}} [anotar "ajustada por concomitância", "integralmente concomitante" ou "posterior à EC 103/2019 – não conversível"] | {{CARENCIA}} |
| TOTAL até a DER ({{DER}}) |  |  | {{TEMPO_ESPECIAL_TOTAL}} | {{CARENCIA_TOTAL}} |

Até a data da Reforma da Previdência (EC nº 103/2019, em 13/11/2019), o(a) segurado(a) possuía {{TEMPO_ESPECIAL_ATE_EC103}} de tempo especial. Com o acréscimo do período especial posterior, não conversível, o tempo total exclusivamente especial apurado até a data de hoje e até a DER ({{DER}}) totaliza {{TEMPO_ESPECIAL_TOTAL}}, com {{CARENCIA_TOTAL}} meses de carência.

## DO TEMPO COM CONVERSÕES (TEMPO COMUM)

Aplicando-se o fator de conversão {{FATOR_CONVERSAO}} aos períodos especiais exercidos até 13/11/2019 e somando-se os demais períodos de natureza comum, o tempo de contribuição do(a) segurado(a), com conversões, restou apurado da seguinte forma:

| Empregador | Início | Fim | Fator | Tempo convertido em comum | Carência |
|---|---|---|---|---|---|
| {{EMPREGADOR}} | {{DATA_INICIO}} | {{DATA_FIM}} | {{FATOR}} [1,00 para comum; {{FATOR_CONVERSAO}} para especial até 13/11/2019; "1,00 (sem conversão – pós EC 103/19)"] | {{TEMPO_CONVERTIDO}} | {{CARENCIA}} |
| TOTAL até a DER ({{DER}}) |  |  |  | {{TEMPO_COMUM_TOTAL}} | {{CARENCIA_TOTAL}} |

Dessa forma, o tempo de contribuição comum, já computadas as conversões dos períodos especiais anteriores à EC nº 103/2019, totaliza {{TEMPO_COMUM_TOTAL}} até a data de hoje e até a DER ({{DER}}), com {{CARENCIA_TOTAL}} meses de carência (carência mínima de 180 meses já cumprida).

## DA APOSENTADORIA ESPECIAL ({{TEMPO_ESPECIAL_EXIGIDO}} ANOS DE TEMPO EXCLUSIVAMENTE ESPECIAL)

Para a concessão da aposentadoria especial é exigido o cumprimento de {{TEMPO_ESPECIAL_EXIGIDO}} anos de tempo exclusivamente especial e carência de 180 meses. Na DER ({{DER}}), o(a) segurado(a) dispõe de apenas {{TEMPO_ESPECIAL_TOTAL}} de tempo especial, faltando {{TEMPO_FALTANTE_ESPECIAL}} para a integralização do requisito temporal. [AJUSTAR SE JÁ CUMPRIDO]

[SE NÃO HOUVER ATIVIDADE ESPECIAL EM CURSO] Verifica-se, ainda, que o último período com efetiva exposição a agente nocivo foi encerrado em {{DATA_ULTIMA_EXPOSICAO}}, estando o(a) segurado(a), desde {{DATA_INICIO_ATIVIDADE_ATUAL}}, vinculado(a) a {{EMPREGADOR_ATUAL}} em atividade de natureza comum, sem exposição a agente nocivo informada.

Assim, mantida a trajetória laboral atual, o(a) segurado(a) NÃO tem direito à aposentadoria especial na DER, e o implemento desse requisito é, no momento, INATINGÍVEL, uma vez que não há acréscimo de tempo especial em curso.

O direito ao benefício somente poderá ser reconstituído caso o(a) segurado(a) retorne a exercer atividade especial (na função de {{FUNCAO_ESPECIAL}} ou equivalente, com efetiva exposição a agente nocivo), hipótese em que o tempo faltante ({{TEMPO_FALTANTE_ESPECIAL}}) voltaria a ser computado a partir da nova data de reingresso na atividade especial.

## DA APOSENTADORIA POR TEMPO DE CONTRIBUIÇÃO/PONTOS E POR IDADE, COM CONVERSÕES

Diversamente da aposentadoria especial, o tempo comum resultante das conversões acima aproveita o(a) segurado(a) para fins de aposentadoria programada.

A média atual dos salários de contribuição de {{SEGURADO_PRIMEIRO_NOME}} é de:

R$ {{MEDIA_SALARIOS}} – {{MEDIA_SALARIOS_EXTENSO}} (até {{COMPETENCIA_MEDIA}}).

### DO IMPLEMENTO DOS REQUISITOS

Mantendo-se as contribuições mensais sobre o último salário de contribuição (R$ {{ULTIMO_SALARIO}}), o(a) segurado(a) implementará os requisitos das seguintes regras:

Art. 15 da EC nº 103/2019 (tempo de contribuição/idade/pontos): 35 anos de tempo de contribuição e 105 pontos – requisitos a serem implementados em {{DATA_IMPLEMENTO_ART15}}, data em que o(a) segurado(a) terá {{IDADE_IMPLEMENTO_ART15}}, com RMI estimada de R$ {{RMI_ART15}}.

Arts. 16 e 18 da EC nº 103/2019 (idade mínima urbana – 65 anos): requisitos a serem implementados em {{DATA_IMPLEMENTO_ART16_18}}, data em que o(a) segurado(a) completará 65 anos de idade, com RMI estimada de R$ {{RMI_ART16_18}}.

[CONFERIR: requisitos acima (35 anos, 105 pontos, 65 anos) são do segurado homem no original; ajustar ao sexo]

A regra do art. 15 se mostra mais vantajosa por antecipar o direito ao benefício em aproximadamente {{ANTECIPACAO_MESES}} meses em relação à regra etária, embora com RMI ligeiramente inferior. [AJUSTAR AO CASO]

## DA CONCLUSÃO

As informações constantes deste parecer representam uma estimativa técnica da situação previdenciária de {{SEGURADO_NOME}}, com base na documentação disponibilizada até a presente data.

Quanto ao tempo exclusivamente especial exercido na função de {{FUNCAO_ESPECIAL}}, apurou-se o total de {{TEMPO_ESPECIAL_TOTAL}} até a DER ({{DER}}), insuficiente para a aposentadoria especial ({{TEMPO_ESPECIAL_EXIGIDO}} anos exigidos).

Considerando que o(a) segurado(a) não mantém, atualmente, atividade especial em curso, o implemento desse requisito é INATINGÍVEL na trajetória presente, faltando {{TEMPO_FALTANTE_ESPECIAL}} de exposição a agente nocivo, os quais somente serão computados em caso de efetivo retorno à atividade especial.

Já o tempo comum apurado com as conversões dos períodos especiais anteriores à EC nº 103/2019 totaliza {{TEMPO_COMUM_TOTAL}} até a DER, e possibilitará ao(à) segurado(a) o implemento dos requisitos da aposentadoria por tempo de contribuição/pontos (art. 15 da EC nº 103/2019) em {{DATA_IMPLEMENTO_ART15}}, com RMI estimada de R$ {{RMI_ART15}}, ou, alternativamente, da aposentadoria por idade (arts. 16/18) em {{DATA_IMPLEMENTO_ART16_18}}, com RMI estimada de R$ {{RMI_ART16_18}}, caso o(a) segurado(a) mantenha as contribuições mensais no padrão atual.

Recomenda-se, por fim, a adoção das seguintes providências, com potencial de antecipar o direito ao benefício:

Obtenção do PPP relativo ao vínculo com {{EMPREGADOR}} ({{DATA_INICIO}} a {{DATA_FIM}}), tendo em vista o indicador IEAN constante do CNIS, o que pode agregar tempo especial adicional; [CONFERIR: lista de providências possivelmente incompleta no modelo original — só traz um item e termina em ponto e vírgula]

Os cálculos anexos demonstram de forma detalhada a apuração do tempo de contribuição e das conversões realizadas.

Assim, encerra-se o presente parecer.

{{CIDADE}}, {{DATA_PARECER}}.

{{ADVOGADA_NOME}}
{{ADVOGADA_OAB}}
Especialista em Cálculos Previdenciários
