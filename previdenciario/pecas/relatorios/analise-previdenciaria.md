---
tipo: analise-previdenciaria
titulo: RELATÓRIO - ANÁLISE PREVIDENCIÁRIA
grupo: relatorio
objetivo: Análise completa da vida contributiva (vínculos, indicadores do CNIS, competências abaixo do mínimo, lacunas, carência e tempo), direito na DER, datas de implemento por regra da EC 103/2019, vantagem financeira, RMI e providências de acerto do CNIS
documentos_necessarios:
  - CNIS completo (com indicadores e remunerações)
  - CTPS (com anotações de admissão, saída e alteração de razão social/sucessão)
  - TRCT, extrato analítico do FGTS, ficha ou livro de registro de empregados, contrato de trabalho e holerites dos vínculos com pendência
  - Documentos de massa falida e/ou de reclamação trabalhista, quando o empregador for falido
  - Planilha de apuração de tempo, carência e simulação de RMI (anexos)
campos:
  - SEGURADO_NOME
  - SEGURADO_DATA_NASCIMENTO
  - SEGURADO_CPF
  - DER
  - EMPREGADOR_PENDENTE
  - DATA_ADMISSAO_PENDENTE
  - ULTIMO_SALARIO_CONTRIBUICAO
  - SEGURADO_SEXO
  - IDADE_NA_DER
  - N
  - EMPREGADOR
  - INDICADORES
  - DATA_INICIO
  - DATA_FIM
  - TEMPO
  - CARENCIA
  - TEMPO_TOTAL_DER
  - CARENCIA_TOTAL_DER
  - PERIODOS_AJUSTADOS_CONCOMITANCIA
  - DATA
  - PERIODOS
  - EMPREGADOR_PEXT_RISCO
  - TEMPO_CARENCIA_PERIODO_PEXT
  - TEMPO_SEM_PERIODO_PEXT
  - CARENCIA_SEM_PERIODO_PEXT
  - COMPETENCIA
  - SALARIO_CONTRIBUICAO
  - SALARIO_MINIMO_DA_COMPETENCIA
  - DIFERENCA
  - DURACAO
  - IDADE
  - PONTOS
  - OBSERVACAO_EVOLUCAO_TEMPO
  - REQUISITOS_E_SITUACAO
  - RMI
  - PEDAGIO
  - TEMPO_EM_13_11_2019
  - TEMPO_FALTANTE_ART_17
  - DATA_MELHOR_OPCAO
  - MELHOR_RMI
  - RETORNO
  - ACRESCIMO
  - VALOR_DEIXA_RECEBER
  - VALOR_TOTAL_EXPECTATIVA
  - IDADE_EXPECTATIVA_IBGE
  - MESES_EXPECTATIVA
  - REGRA_MELHOR_RMI
  - MELHOR_RMI_EXTENSO
  - QTD
  - QTD_DESCARTADOS
  - SOMA
  - MEDIA
  - COEFICIENTE
  - PERCENTUAL_SALARIO_MINIMO
  - SALARIO_MINIMO_VIGENTE
  - MEDIA_ATUAL_SALARIOS
  - COMPETENCIA_MEDIA_ATUAL
  - RECOLHIMENTO_MENSAL_SIMULADO
  - TOTAL_RECOLHIMENTOS_SIMULADOS
  - QTD_RECOLHIMENTOS_SIMULADOS
  - DATA_FIM_ULTIMO_VINCULO
  - VALOR_RECOLHIMENTO_20
  - TEMPO_ATE_MELHOR_OPCAO
  - DATAS_DEMAIS_REGRAS
  - CIDADE
  - DATA_PARECER
  - ADVOGADA_NOME
  - ADVOGADA_OAB
citacoes:
  - EC nº 103/2019
  - Súmula 75 da TNU
  - art. 29 da EC nº 103/2019
  - art. 195, §14, da CF/88 (incluído pela EC nº 103/2019) c/c arts. 189 e 209 da IN nº 128/2022
  - arts. 189, §8º, e 209, §2º, da IN nº 128/2022
  - arts. 15, 16 e 20
  - Art. 16 – Idade Mínima Progressiva
  - Art. 18 – Aposentadoria por Idade
  - Art. 15 – Pontos
  - Art. 20 – Pedágio de 100%
  - Art. 17 – Pedágio de 50%
  - Lei nº 9.876/99
  - EC nº 20/98
  - art. 18 da EC nº 103/2019
  - arts. 16 e 18 da EC nº 103/2019
---

# ANÁLISE PREVIDENCIÁRIA

**Segurado(a):** {{SEGURADO_NOME}}
**Data de Nascimento:** {{SEGURADO_DATA_NASCIMENTO}}
**CPF:** {{SEGURADO_CPF}}
**DER:** {{DER}}

## RELATÓRIO

O presente trabalho tem por objetivo analisar a vida previdenciária do(a) segurado(a) {{SEGURADO_NOME}}, apurar o tempo de contribuição e a carência, verificar o direito às aposentadorias programadas na data da DER e, não havendo direito imediato, identificar as datas em que serão implementados os requisitos de cada regra de transição da EC nº 103/2019, com a Renda Mensal Inicial (RMI) estimada e a opção mais vantajosa.

Especial atenção é dada às pendências e indicadores constantes do CNIS, notadamente o vínculo com a empresa {{EMPREGADOR_PENDENTE}}, com admissão em {{DATA_ADMISSAO_PENDENTE}} e sem data de saída registrada, bem como às competências com salário de contribuição inferior ao salário-mínimo, que dependem de complementação para serem validadas. [AJUSTAR AS PENDÊNCIAS DESTACADAS AO CASO]

## METODOLOGIA APLICADA

Para realização do presente trabalho, procedeu-se ao cálculo do tempo de contribuição, da carência e dos salários de contribuição do(a) segurado(a) constantes em seu CNIS, com ajuste dos períodos concomitantes, identificação dos indicadores de pendência e verificação das competências recolhidas abaixo do salário-mínimo. Em seguida, foi elaborado planejamento previdenciário a partir da situação do(a) segurado(a) na data de hoje ({{DER}}), presumindo-se a continuidade dos recolhimentos mensais sobre o valor do último salário de contribuição (R$ {{ULTIMO_SALARIO_CONTRIBUICAO}}), inclusive a competência da data de hoje.

Ressalta-se que os resultados apresentados pressupõem o cômputo dos vínculos tal como lançados no CNIS. Os períodos com indicadores de pendência poderão não ser reconhecidos pelo INSS sem a devida comprovação, o que pode alterar o tempo de contribuição, a carência, as datas de implemento e a RMI, conforme detalhado adiante.

## DADOS DO SEGURADO

| Segurado | {{SEGURADO_NOME}} |
|---|---|
| CPF | {{SEGURADO_CPF}} |
| Data de Nascimento | {{SEGURADO_DATA_NASCIMENTO}} |
| Sexo | {{SEGURADO_SEXO}} |
| Idade na DER | {{IDADE_NA_DER}} |
| DER (Data de Entrada do Requerimento) | {{DER}} |

## DOS VÍNCULOS

Da análise do CNIS, foram identificados os seguintes vínculos e períodos contributivos, com os respectivos indicadores:

| Nº | Vínculo / Período | Início | Fim | Tempo apurado | Carência |
|---|---|---|---|---|---|
| {{N}} | {{EMPREGADOR}} ({{INDICADORES}}) | {{DATA_INICIO}} | {{DATA_FIM}} [ou "SEM DATA FIM"] | {{TEMPO}} (ajustada concomitância, se for o caso / Não computado) | {{CARENCIA}} |
|  | TOTAL |  |  | {{TEMPO_TOTAL_DER}} | {{CARENCIA_TOTAL_DER}} |

Os períodos nº {{PERIODOS_AJUSTADOS_CONCOMITANCIA}} tiveram seus tempos ajustados em razão de concomitância com outros vínculos, de modo a evitar dupla contagem. Os salários de contribuição dos períodos concomitantes, contudo, são somados para fins de cálculo da RMI, respeitado o teto previdenciário.

Todos os períodos foram computados como tempo comum (fator 1,00), não havendo períodos especiais, rurais de segurado especial ou recolhidos com alíquotas reduzidas. [AJUSTAR SE HOUVER PERÍODOS ESPECIAIS/RURAIS/ALÍQUOTA REDUZIDA]

## DO VÍNCULO COM {{EMPREGADOR_PENDENTE}} – AUSÊNCIA DE DATA FIM

[SEÇÃO OPCIONAL — USAR QUANDO HOUVER VÍNCULO SEM DATA DE SAÍDA NO CNIS]

| ATENÇÃO – PENDÊNCIA PRIORITÁRIA O(A) segurado(a) possui vínculo com a empresa {{EMPREGADOR_PENDENTE}}, com admissão em {{DATA_ADMISSAO_PENDENTE}}, que não consta data fim no CNIS e está marcado com o indicador PEXT (vínculo com informação extemporânea). Por esse motivo, o período não foi computado no tempo de contribuição nem na carência. |
|---|

No CNIS, a mesma empregadora aparece em dois registros distintos: (i) o período nº {{N}}, com admissão em {{DATA}} e saída em {{DATA}}, marcado com o indicador PADM-EMPR (data de admissão incompatível com o período de atividade do empregador); e (ii) o período nº {{N}}, com admissão em {{DATA}} e sem data de saída, marcado com o indicador PEXT. [AJUSTAR AO CASO]

[SE APLICÁVEL] Chama atenção que a admissão de {{DATA}} coincide exatamente com a data de saída do vínculo anterior (período nº {{N}}). Esse quadro sugere possível sucessão de empregadores ou alteração de razão social/CNPJ – hipótese que explicaria o indicador PADM-EMPR e que deve ser confirmada com a CTPS.

A ausência de data de saída impede o INSS de reconhecer o vínculo, que permanece pendente até que o(a) segurado(a) comprove as datas de admissão e de saída, bem como as remunerações do período. A correção é relevante porque:

- elimina a pendência que, se não tratada, pode gerar exigência ou indeferimento no requerimento administrativo;
- define o período efetivamente trabalhado: caso a saída seja posterior a {{DATA}}, o vínculo poderá preencher lacunas contributivas e acrescer tempo de contribuição e carência;
- valida as remunerações do período, que, somadas às dos vínculos concomitantes, podem elevar a média dos salários de contribuição e, consequentemente, a RMI.

Para comprovação, recomenda-se reunir: CTPS com as anotações de admissão e saída (e eventuais anotações de alteração de razão social/sucessão), Termo de Rescisão (TRCT), extrato analítico do FGTS, ficha ou livro de registro de empregados, contrato de trabalho, holerites e, se houver, sentença ou acordo trabalhista. A CTPS sem defeito formal goza de presunção relativa de veracidade (Súmula 75 da TNU), e o segurado empregado não pode ser prejudicado pela ausência de recolhimento ou de informação pelo empregador.

## DOS INDICADORES DO CNIS

O CNIS utiliza siglas (indicadores) para sinalizar inconsistências nos vínculos e nas remunerações. Os indicadores de pendência exigem tratamento – normalmente mediante comprovação documental – e, enquanto não resolvidos, podem impedir o cômputo do período ou da competência pelo INSS. Os indicadores de alerta são apenas informativos. No CNIS do(a) segurado(a) foram identificados os seguintes:

[MANTER APENAS AS LINHAS DOS INDICADORES PRESENTES NO CASO E PREENCHER A COLUNA "PERÍODO(S)"]

| Indicador | Significado | Período(s) | Impacto | Providência |
|---|---|---|---|---|
| PEXT | Vínculo com informação extemporânea (inserido fora do prazo legal), passível de comprovação | {{PERIODOS}} | Sem comprovação, o período não é considerado para tempo de contribuição nem para cálculo da RMI | Comprovar o vínculo e as remunerações (CTPS, TRCT, FGTS, ficha de registro, holerites) |
| PADM-EMPR | Data de admissão incompatível com o período de atividade do empregador na Receita Federal | {{PERIODOS}} | Não impede o cômputo, desde que o vínculo seja comprovado e validado | Comprovar a data real de admissão (CTPS, contrato, registro de empregados) |
| PREM-EMPR | Remunerações incompatíveis com o período de atividade do empregador | {{PERIODOS}} | Impede o cômputo das competências afetadas nos sistemas de benefícios | Retificação do cadastro do empregador na RFB e/ou comprovação das remunerações |
| IREM-INDPEND | Remuneração com indicador de alerta ou pendência | {{PERIODOS}} | Depende do indicador específico vinculado à competência | Consultar o detalhamento da remuneração e tratar o indicador correspondente |
| PSC-MEN-SM-EC103 | Competência com salário de contribuição inferior ao salário-mínimo (a partir de 11/2019) | {{PERIODOS}} | A competência não conta para tempo de contribuição nem para carência | Complementação, utilização de excedente ou agrupamento (art. 29 da EC nº 103/2019) |

**a) PEXT – {{EMPREGADOR_PEXT_RISCO}} (período nº {{N}}) – risco relevante**

O vínculo com {{EMPREGADOR_PEXT_RISCO}} ({{DATA_INICIO}} a {{DATA_FIM}}) foi computado neste cálculo e responde por {{TEMPO_CARENCIA_PERIODO_PEXT}} de tempo de contribuição e de carência, após o ajuste de concomitância. Por estar marcado com PEXT, o INSS poderá desconsiderá-lo sem a devida comprovação.

Caso o período não seja reconhecido, o tempo de contribuição até a DER cairia para aproximadamente {{TEMPO_SEM_PERIODO_PEXT}} e a carência para cerca de {{CARENCIA_SEM_PERIODO_PEXT}} contribuições, postergando de forma significativa as regras que exigem 35 anos de contribuição (arts. 15, 16 e 20). Além disso, os salários desse vínculo compõem parte dos maiores salários do período básico de cálculo, de modo que sua exclusão também reduziria a RMI. [AJUSTAR AO CASO]

[SE O EMPREGADOR FOR FALIDO] Por se tratar de empresa falida, recomenda-se reunir, além da CTPS, TRCT e extrato do FGTS, eventuais documentos da habilitação de crédito na massa falida e/ou de reclamação trabalhista, que reforçam a prova do vínculo e das datas de admissão e saída.

**b) PADM-EMPR – {{EMPREGADOR}} (período nº {{N}})**

Indica que a data de admissão ({{DATA}}) é anterior ao início de atividade da empresa registrado na Receita Federal. Deve ser comprovada a data correta de admissão e, conjuntamente, regularizado o registro sem data fim, com a unificação das informações do contrato de trabalho. [AJUSTAR AO CASO]

**c) PREM-EMPR e IREM-INDPEND – {{EMPREGADOR}} (período nº {{N}})**

O período ({{DATA_INICIO}} a {{DATA_FIM}}) não acrescenta tempo, por ser integralmente concomitante, mas suas remunerações integram a soma dos salários de contribuição. O indicador PREM-EMPR aponta remunerações fora do período de atividade da empresa na Receita Federal e impede o uso dessas competências pelo INSS, podendo reduzir a média. Recomenda-se a comprovação das remunerações (holerites, CTPS, FGTS) e, se for o caso, a retificação do cadastro do empregador.

**d) PSC-MEN-SM-EC103 e IREM-INDPEND – {{EMPREGADOR}} (período nº {{N}})**

A competência {{COMPETENCIA}} apresenta salário de contribuição inferior ao salário-mínimo, sendo tratada no tópico seguinte.

## DAS COMPETÊNCIAS ABAIXO DO MÍNIMO

Nos termos do art. 195, §14, da CF/88 (incluído pela EC nº 103/2019) c/c arts. 189 e 209 da IN nº 128/2022, a competência abaixo foi desconsiderada para fins de tempo de contribuição e carência, por apresentar recolhimento inferior ao salário-mínimo:

| Competência | Salário de contribuição | Salário-mínimo | Diferença a complementar |
|---|---|---|---|
| {{COMPETENCIA}} | R$ {{SALARIO_CONTRIBUICAO}} | R$ {{SALARIO_MINIMO_DA_COMPETENCIA}} | R$ {{DIFERENCA}} |

Para que essa competência seja validada, o(a) segurado(a) deverá requerer, pelo Meu INSS, o ajuste previsto no art. 29 da EC nº 103/2019, por uma das seguintes formas:

- **Complementação:** recolhimento, via DARF, da contribuição incidente sobre a diferença entre o salário de contribuição e o salário-mínimo (base de R$ {{DIFERENCA}}). [INDICAR SE É A FORMA RECOMENDADA NO CASO]
- **Utilização de excedente:** aproveitamento do valor que exceder o mínimo em outra competência do mesmo ano civil. [AVALIAR SE HÁ EXCEDENTE SUFICIENTE NO ANO]
- **Agrupamento:** soma de competências para formar uma com valor mínimo. [AVALIAR SE HÁ GANHO EFETIVO DE TEMPO OU CARÊNCIA]

O impacto direto dessa regularização é pequeno (acréscimo de uma competência), mas ela é necessária para eliminar a pendência e validar integralmente o vínculo. [AJUSTAR AO CASO]

[SE HOUVER COMPETÊNCIA DE EMPREGADO ANTERIOR A 11/2019 ABAIXO DO MÍNIMO] A competência {{COMPETENCIA}}, embora abaixo do mínimo, foi considerada válida para tempo de contribuição e carência, por se tratar de segurado empregado em período anterior a 11/2019 (arts. 189, §8º, e 209, §2º, da IN nº 128/2022) – correspondendo, ademais, a mês de admissão com remuneração proporcional.

## DAS LACUNAS CONTRIBUTIVAS

Foram identificadas as seguintes lacunas no quadro contributivo, que podem representar oportunidade de reconhecimento de períodos trabalhados e não registrados no CNIS (ex.: vínculo em CTPS não reconhecido pelo INSS – Súmula 75 da TNU):

| Lacuna | Período | Duração |
|---|---|---|
| {{N}} | {{DATA_INICIO}} a {{DATA_FIM}} | {{DURACAO}} |

[SE HOUVER VÍNCULO SEM DATA FIM] Destaca-se que a definição da data de saída do vínculo com {{EMPREGADOR_PENDENTE}} deve ser confrontada com as lacunas posteriores: se o contrato se estendeu além do último registro, haverá acréscimo de tempo de contribuição.

## DA CARÊNCIA

Carência é o número mínimo de meses (competências) pagos ao INSS para que o segurado, ou em alguns casos o seu dependente, possa ter direito de receber um benefício.

Procedendo à apuração da carência, temos que:

{{CARENCIA_TOTAL_DER}} meses até a DER ({{DER}})

Assim, o(a) segurado(a) já cumpre a carência mínima de 180 contribuições exigida para todas as aposentadorias programadas – inclusive na hipótese de não reconhecimento do período com PEXT (cerca de {{CARENCIA_SEM_PERIODO_PEXT}} contribuições). [AJUSTAR AO CASO]

## DO TEMPO DE CONTRIBUIÇÃO

O tempo de contribuição é o período efetivo em que o segurado verteu contribuições ao INSS, seja como segurado obrigatório, seja como facultativo. Considerando os períodos computados, o(a) segurado(a) possui o tempo total de:

ATÉ A DER ({{DER}}): {{TEMPO_TOTAL_DER}}

| Marco Temporal | Tempo de Contribuição | Carência | Idade | Pontos |
|---|---|---|---|---|
| Até a EC nº 20/98 (16/12/1998) | {{TEMPO}} | {{CARENCIA}} | {{IDADE}} | --- |
| Até a Lei nº 9.876/99 (28/11/1999) | {{TEMPO}} | {{CARENCIA}} | {{IDADE}} | --- |
| Até a EC nº 103/19 (13/11/2019) | {{TEMPO}} | {{CARENCIA}} | {{IDADE}} | {{PONTOS}} |
| Até a DER ({{DER}}) | {{TEMPO}} | {{CARENCIA}} | {{IDADE}} | {{PONTOS}} |

{{OBSERVACAO_EVOLUCAO_TEMPO}} [EXEMPLO: "Observa-se que o tempo de contribuição permanece praticamente inalterado desde {{COMPETENCIA}}, estando o(a) segurado(a) sem contribuições desde {{DATA}}."]

## DO DIREITO À APOSENTADORIA

Considerando a data de hoje ({{DER}}), o(a) segurado(a) AINDA NÃO TEM DIREITO a qualquer aposentadoria programada. Embora já tenha cumprido a carência (180 contribuições) e o tempo mínimo da aposentadoria por idade (15 anos), resta pendente o requisito etário e, nas regras por tempo de contribuição, também o tempo mínimo de 35 anos. [AJUSTAR AO CASO E AO SEXO]

Mantendo-se os recolhimentos mensais sobre o último salário, os requisitos de cada regra serão implementados nas seguintes datas:

| Regra | Requisitos | Data de implemento | Melhor RMI estimada na data |
|---|---|---|---|
| Art. 16 – Idade Mínima Progressiva | {{REQUISITOS_E_SITUACAO}} | {{DATA}} | R$ {{RMI}} |
| Art. 18 – Aposentadoria por Idade | {{REQUISITOS_E_SITUACAO}} | {{DATA}} | R$ {{RMI}} |
| Art. 15 – Pontos | {{REQUISITOS_E_SITUACAO}} | {{DATA}} | R$ {{RMI}} |
| Art. 20 – Pedágio de 100% | {{REQUISITOS_E_SITUACAO}} (35 anos + pedágio de {{PEDAGIO}}) | {{DATA}} | R$ {{RMI}} |
| Art. 17 – Pedágio de 50% | Exigia mais de 33 anos de contribuição em 13/11/2019 (o(a) segurado(a) possuía {{TEMPO_EM_13_11_2019}}) | Inatingível | --- |

[SE O ART. 17 FOR INATINGÍVEL] A regra do art. 17 da EC nº 103/2019 (pedágio de 50%) é inatingível, pois em 13/11/2019 faltaram {{TEMPO_FALTANTE_ART_17}} para que o(a) segurado(a) alcançasse o tempo mínimo exigido. Somente a averbação de períodos anteriores a 13/11/2019 hoje não computados (ex.: lacunas) poderia viabilizá-la.

[SE APLICÁVEL] Importa registrar que a aposentadoria por idade do art. 18 em {{DATA}} não depende do período com PEXT, pois exige apenas 15 anos de contribuição. Já a do art. 16 na mesma data depende do reconhecimento desse vínculo e da continuidade dos recolhimentos até {{DATA}}.

O(A) segurado(a) NÃO TEM DIREITO à Aposentadoria Especial, à Aposentadoria Programada do Professor, às Aposentadorias da Pessoa com Deficiência e às Aposentadorias por Idade Rural e Internacional, por não possuir períodos que se enquadrem nos requisitos dessas espécies de benefício. [AJUSTAR AO CASO]

## DA ANÁLISE DA VANTAGEM FINANCEIRA

As regras com implemento posterior não resultam em RMI superior, pois a melhor renda é a mesma em todas as datas. A postergação do pedido implicaria apenas deixar de receber a aposentadoria já disponível a partir de {{DATA_MELHOR_OPCAO}}, além de exigir novos recolhimentos: [AJUSTAR AO CASO]

| Data | Melhor RMI | Acréscimo mensal | Valor que deixará de receber | Retorno do investimento |
|---|---|---|---|---|
| {{DATA_MELHOR_OPCAO}} | R$ {{MELHOR_RMI}} | --- | --- | {{RETORNO}} |
| {{DATA}} | R$ {{RMI}} | R$ {{ACRESCIMO}} | R$ {{VALOR_DEIXA_RECEBER}} | {{RETORNO}} [ou "Não é vantajoso esperar"] |

Desse modo, a opção mais vantajosa é requerer a aposentadoria em {{DATA_MELHOR_OPCAO}}, com expectativa de recebimento de R$ {{VALOR_TOTAL_EXPECTATIVA}} até os {{IDADE_EXPECTATIVA_IBGE}} anos de idade (expectativa de vida do IBGE – {{MESES_EXPECTATIVA}} meses, incluídas as gratificações natalinas).

## DA RENDA MENSAL INICIAL

O cálculo da Renda Mensal Inicial (RMI), considerando a média dos salários de contribuição, com os descartes permitidos pela legislação, apontou como mais vantajoso, em {{DATA_MELHOR_OPCAO}}, o cálculo pelo {{REGRA_MELHOR_RMI}}, no valor de:

| RMI ESTIMADA EM {{DATA_MELHOR_OPCAO}} – {{REGRA_MELHOR_RMI}} R$ {{MELHOR_RMI}} ({{MELHOR_RMI_EXTENSO}}) |
|---|

| Etapa do cálculo | Sem descartes | Com descartes (melhor RMI) |
|---|---|---|
| Salários de contribuição considerados | {{QTD}} | {{QTD}} ({{QTD_DESCARTADOS}} descartados) |
| Soma dos salários corrigidos | R$ {{SOMA}} | R$ {{SOMA}} |
| Média dos salários | R$ {{MEDIA}} | R$ {{MEDIA}} |
| Coeficiente | {{COEFICIENTE}} | {{COEFICIENTE}} |
| Renda Mensal Inicial | R$ {{RMI}} | R$ {{RMI}} |

O valor equivale a {{PERCENTUAL_SALARIO_MINIMO}} do salário-mínimo atual (R$ {{SALARIO_MINIMO_VIGENTE}}). A média atual dos salários de contribuição do(a) segurado(a) é de R$ {{MEDIA_ATUAL_SALARIOS}} (até {{COMPETENCIA_MEDIA_ATUAL}}).

Para essa simulação, considerou-se o recolhimento mensal de R$ {{RECOLHIMENTO_MENSAL_SIMULADO}} (alíquota aplicada sobre o último salário de R$ {{ULTIMO_SALARIO_CONTRIBUICAO}}), totalizando R$ {{TOTAL_RECOLHIMENTOS_SIMULADOS}} em {{QTD_RECOLHIMENTOS_SIMULADOS}} recolhimentos (incluindo os incidentes sobre gratificações natalinas) de hoje até {{DATA_MELHOR_OPCAO}}.

[SE O SEGURADO ESTIVER SEM VÍNCULO ATIVO] Ressalta-se que, desde o encerramento do último vínculo ({{DATA_FIM_ULTIMO_VINCULO}}), o(a) segurado(a) não possui atividade registrada. Caso passe a recolher como contribuinte individual ou segurado facultativo, deverá observar a alíquota de 20% (ou 11%, se contribuinte individual que presta serviço a empresa) para manter o direito às aposentadorias por tempo de contribuição – o que, sobre o mesmo salário, corresponderia a cerca de R$ {{VALOR_RECOLHIMENTO_20}} mensais na alíquota de 20%. As alíquotas reduzidas de 11% e 5% sobre o salário-mínimo dão direito apenas à aposentadoria por idade (art. 18).

A RMI estimada considera válidas as remunerações hoje lançadas no CNIS. A não comprovação dos períodos com PEXT e PREM-EMPR pode reduzir a média dos salários e, portanto, o valor do benefício; por outro lado, a validação das remunerações do vínculo sem data fim pode elevá-la. [AJUSTAR AO CASO]

## DAS PROVIDÊNCIAS PARA REGULARIZAÇÃO DO CNIS

Recomenda-se que, antes do requerimento do benefício, o(a) segurado(a) promova o acerto do CNIS pelo Meu INSS (serviço de atualização de vínculos e remunerações), apresentando a documentação abaixo:

| Nº | Pendência | Providência / Documentos |
|---|---|---|
| 1 | {{EMPREGADOR}} – vínculo sem data fim (PEXT) e/ou admissão incompatível (PADM-EMPR) | Comprovar as datas de admissão e saída e as remunerações: CTPS (incluindo anotações de alteração de razão social/sucessão), TRCT, extrato do FGTS, ficha de registro, contrato de trabalho e holerites |
| 2 | {{EMPREGADOR}} (PEXT) | CTPS, TRCT, extrato do FGTS, holerites, documentos da massa falida e/ou de reclamação trabalhista |
| 3 | {{EMPREGADOR}} (PREM-EMPR / IREM-INDPEND) | Comprovar as remunerações (holerites, CTPS, FGTS) e, se necessário, solicitar a retificação do cadastro do empregador na RFB |
| 4 | Competência {{COMPETENCIA}} abaixo do mínimo (PSC-MEN-SM-EC103) | Requerer o ajuste do art. 29 da EC nº 103/2019 (complementação) e recolher o DARF sobre a diferença de R$ {{DIFERENCA}} |
| 5 | Lacunas contributivas | Verificar, na CTPS e em outros documentos, a existência de vínculos não registrados no CNIS |

Indeferido o acerto na via administrativa, a comprovação poderá ser buscada judicialmente, com amparo na Súmula 75 da TNU e no entendimento de que o empregado não pode ser prejudicado pela omissão do empregador quanto aos recolhimentos e às informações prestadas ao INSS.

## CONCLUSÃO

A presente análise demonstra que o(a) segurado(a) {{SEGURADO_NOME}} possui {{TEMPO_TOTAL_DER}} de tempo de contribuição e {{CARENCIA_TOTAL_DER}} meses de carência até a DER ({{DER}}), mas AINDA NÃO TEM DIREITO a qualquer aposentadoria programada nesta data. [AJUSTAR AO CASO]

Mantidos os recolhimentos, o(a) segurado(a) implementará os requisitos do(s) {{REGRA_MELHOR_RMI}} em {{DATA_MELHOR_OPCAO}} (daqui a {{TEMPO_ATE_MELHOR_OPCAO}}), com RMI estimada de R$ {{MELHOR_RMI}}. Os requisitos das demais regras serão implementados em {{DATAS_DEMAIS_REGRAS}}, sem acréscimo de renda, sendo inatingível a regra do art. 17. Recomenda-se, portanto, o requerimento da aposentadoria em {{DATA_MELHOR_OPCAO}}.

Ressalta-se, contudo, a necessidade de regularização prévia do CNIS, especialmente: (i) a comprovação das datas de admissão e saída do vínculo com {{EMPREGADOR_PENDENTE}}, admitido em {{DATA_ADMISSAO_PENDENTE}} e sem data fim; (ii) a comprovação do vínculo com {{EMPREGADOR_PEXT_RISCO}}, cuja eventual exclusão reduziria o tempo para cerca de {{TEMPO_SEM_PERIODO_PEXT}}; (iii) a regularização das remunerações com indicador PREM-EMPR; e (iv) a complementação da competência {{COMPETENCIA}}, recolhida abaixo do salário-mínimo, para sua validação. [MANTER SÓ OS ITENS DO CASO]

As planilhas de cada cálculo seguem discriminadas em anexo ao presente parecer, que concluo a seguir.

{{CIDADE}}, {{DATA_PARECER}}.

[INSERIR IMAGEM: assinatura]

{{ADVOGADA_NOME}}
{{ADVOGADA_OAB}}
Especialista em cálculos previdenciários
