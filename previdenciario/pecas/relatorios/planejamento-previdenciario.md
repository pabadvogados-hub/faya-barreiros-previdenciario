---
tipo: planejamento-previdenciario
titulo: RELATÓRIO - PLANEJAMENTO PREVIDENCIÁRIO
grupo: relatorio
objetivo: Planejamento no RGPS (análise pré e pós-reforma, indicadores do CNIS e datas/RMI de implemento de cada regra), com seção opcional de RPPS estadual (BA)
documentos_necessarios:
  - CNIS completo (com indicadores)
  - CTPS
  - CTC (Certidão de Tempo de Contribuição) do RPPS, quando houver vínculo com regime próprio
  - Planilha de apuração de tempo e simulação de RMI (anexos)
  - Histórico de remunerações do RPPS, quando houver
campos:
  - SEGURADO_NOME
  - SEGURADO_DATA_NASCIMENTO
  - SEGURADO_NIT
  - CATEGORIAS_DE_VINCULACAO
  - CARENCIA_MESES
  - TEMPO_APURADO
  - TEMPO_APURADO_POS_REFORMA
  - OBSERVACAO_TEMPO_PRE_POS
  - COMPETENCIA
  - DER
  - SEGURADO_PRIMEIRO_NOME
  - DATA_REFERENCIA
  - COMPETENCIA_REFERENCIA
  - MEDIA_SALARIOS_RGPS
  - MEDIA_SALARIOS_RGPS_EXTENSO
  - COMPETENCIA_MEDIA_RGPS
  - ALIQUOTA_PLANO
  - DATA_IMPLEMENTO_ART_18
  - RMI_ART_18
  - DATA_IMPLEMENTO_ART_16
  - RMI_ART_16
  - DATA_IMPLEMENTO_ART_15
  - RMI_ART_15
  - DATA_IMPLEMENTO_ART_20
  - RMI_ART_20
  - ORGAO_EMISSOR_CTC
  - ORGAO_DESTINO_RPPS
  - DATA_INGRESSO_SERVICO_PUBLICO
  - MEDIA_REMUNERACOES_RPPS
  - COMPETENCIA_MEDIA_RPPS
  - DATA_REGRA_GERAL_IDADE
  - DATA_REGRA_GERAL_CONTRIBUICAO
  - DATA_REGRA_GERAL_EXERCICIO
  - DATA_IMPLEMENTO_REGRA_GERAL
  - DATA_PONTOS_IDADE
  - DATA_PONTOS_CONTRIBUICAO
  - DATA_PONTOS_EXERCICIO
  - PONTOS_NA_DATA_CONTRIBUICAO
  - DATA_TETO_PONTOS_ATINGIDO
  - DATA_IMPLEMENTO_PONTOS
  - TEMPO_CONTRIB_EM_31_01_2020
  - TEMPO_FALTANTE_EM_31_01_2020
  - PEDAGIO_60_CALCULO
  - TEMPO_TOTAL_COM_PEDAGIO
  - DATA_IMPLEMENTO_PEDAGIO
  - DATA_PEDAGIO_IDADE
  - DATA_PEDAGIO_EXERCICIO
  - DATA_PRIMEIRO_BENEFICIO_RGPS
  - TEMPO_ATE_PRIMEIRO_BENEFICIO
  - REGRA_PRIMEIRO_BENEFICIO
  - DATA_PRIMEIRO_BENEFICIO_RPPS
  - VALOR_ESTIMADO_RPPS
  - VALOR_ESTIMADO_RPPS_EXTENSO
  - NUMERO_LAUDAS
  - NUMERO_ANEXOS
  - CIDADE
  - DATA_PARECER
  - ADVOGADA_NOME
  - ADVOGADA_OAB
citacoes:
  - art. 3º da EC 103/2019
  - CF/88, art. 201, § 7º, inc. I, com redação dada pela EC 20/98
  - EC 20/98, art. 9°, § 1°, inc. I
  - art. 48 da Lei 8.213/91
  - art. 15 da EC 103/19
  - art. 16 da EC 103/19
  - art. 17 das regras de transição da EC 103/19
  - art. 20 das regras de transição da EC 103/19
  - art. 18 das regras de transição da EC 103/19
  - EC 103/2019
  - EC 26/2020 (BA)
  - Manual de Aposentadoria da PGE-BA (2025)
  - EC nº 41/2003
  - Lei 10.887/2004
  - art. 42, §1º-A, III, CE c/c art. 6º, §1º, I, EC 26/2020
  - art. 3º, caput c/c art. 9º, caput, I
  - art. 4º, caput c/c art. 9º, §1º, I
---

# PLANEJAMENTO PREVIDENCIÁRIO

**Segurado(a):** {{SEGURADO_NOME}}
**Data de Nascimento:** {{SEGURADO_DATA_NASCIMENTO}}
**NIT:** {{SEGURADO_NIT}}

## RELATÓRIO

O presente parecer tem por objetivo realizar dentro das regras vigentes do Regime Geral da Previdência Social um planejamento previdenciário, demonstrando ao final as possibilidades para um futuro requerimento de benefício.

## DADOS DO SEGURADO

[INSERIR IMAGEM: quadro-resumo com os dados do(a) segurado(a) extraído da planilha de cálculo]

## DA METODOLOGIA APLICADA

Para realização do trabalho é realizado um estudo com base na vida previdenciária do segurado, bem como verificação dos vínculos, analisando eventuais divergências a serem corrigidas, além de simulação de RMI e possíveis benefícios.

## DOS VÍNCULOS

Os vínculos constantes no CNIS foram computados para a totalização do tempo de contribuição.

O(A) Segurado(a) apresenta vinculação na categoria de {{CATEGORIAS_DE_VINCULACAO}}.

Assim, temos os vínculos da tabela abaixo:

[INSERIR IMAGEM: tabela de vínculos do CNIS (nome do período, início, fim, fator, tempo, carência) gerada pela planilha de cálculo]

## DOS INDICADORES NO CNIS

O CNIS do(a) segurado(a) apresenta os indicadores de pendência abaixo:

[USAR APENAS OS INDICADORES QUE CONSTAREM NO CNIS DO CASO]

1. **IREM-INDPEND** Remunerações com indicadores/pendências
Significa "Indicador de Remuneração com Pendência". Ele aparece nos vínculos empregatícios quando há inconsistências nos seus salários, como remunerações informadas fora do período do contrato, valores divergentes ou informações faltando. Enquanto não for resolvido, o INSS pode desconsiderar o período para sua aposentadoria.

2. **IVIN-JORN-DIFERENCIADA** Vínculo possui regime de jornada diferenciada
Indica que o vínculo foi registrado com um regime de jornada de trabalho diferente da jornada padrão (ex: tempo parcial, jornada reduzida, regime intermitentes). Isso é relevante porque, dependendo do tipo de jornada, o INSS pode precisar verificar como aquele período deve ser contado para fins de tempo de contribuição (às vezes de forma proporcional).

3. **PEXT** Vínculo com informação extemporânea, passível de comprovação
Sinaliza que a informação daquele vínculo foi lançada no sistema fora do prazo legal (extemporânea), ou seja, depois do período em que normalmente deveria ter sido declarada pela empresa/empregador. Como foi um registro "atrasado", o sistema entende que é passível de comprovação. O segurado pode precisar apresentar documentos como CTPS, contrato de trabalho, ou outros registros para validar que o vínculo realmente existiu daquela forma e período.

4. **PREM-EXT** Remuneração informada fora do prazo, passível de comprovação
Indica que os valores de salário de contribuição daquele vínculo foram informados fora do prazo. Também é passível de comprovação — pode ser exigido, por exemplo, holerites (contracheques), para confirmar que os valores lançados estão corretos, já que informações extemporâneas de remuneração podem impactar o cálculo do benefício.

5. **PRPPS** Vínculo de empregado com informações de Regime Próprio (Servidor Público)
Aponta que aquele vínculo está registrado com características de um servidor público vinculado a Regime Próprio de Previdência Social (RPPS), e não ao Regime Geral (RGPS), que é o regime do INSS. Essa pendência é importante porque, se o período for de fato de RPPS, ele geralmente não pode ser contado como tempo de contribuição do INSS (para evitar contagem em duplicidade entre os dois regimes).

6. **PSC-MEN-SM-EC103** Pendência na competência em que o somatório dos salários de contribuição é menor que o mínimo. Competência pode ser passível de complementação, utilização ou agrupamento, de acordo com a EC 103/2019.
Indica Pendência de Salário de Contribuição, significando que o valor recolhido em um mês ficou abaixo do salário-mínimo nacional, regra estabelecida pela Emenda Constitucional 103 (Reforma da Previdência). Esse período não contará para tempo de serviço ou carência até que a diferença seja paga.

## ANÁLISE PRÉ REFORMA – 13/11/2019

Assim, em 13/11/2019 temos:

[INSERIR IMAGEM: quadro de tempo de contribuição, carência, idade e pontos por marco temporal até 13/11/2019]

### DA CARÊNCIA E TEMPO DE CONTRIBUIÇÃO APURADOS

Carência é número mínimo de meses (competências) pagos ao INSS para que o cidadão, ou em alguns casos o seu dependente, possa ter direito de receber um benefício.

Nesse cenário o(a) segurado(a) possui {{CARENCIA_MESES}} meses de carência.
E o tempo apurado até a data atual foi de: {{TEMPO_APURADO}}.

[CONCLUSÃO-MODELO — AJUSTAR "TEM/NÃO TEM" E OS REQUISITOS AO SEXO E AO CASO]

Em 13/11/2019 (último dia de vigência das regras pré-reforma da Previdência - art. 3º da EC 103/2019), o(a) segurado(a) NÃO tem direito à aposentadoria integral por tempo de contribuição (CF/88, art. 201, § 7º, inc. I, com redação dada pela EC 20/98), porque não preenche o tempo mínimo de contribuição de 30 anos e nem a carência de 180 contribuições.

Ainda, não tem interesse na aposentadoria proporcional por tempo de contribuição (regras de transição da EC 20/98) porque o pedágio da EC 20/98, art. 9°, § 1°, inc. I, é superior a 5 anos.

NÃO tem direito adquirido à aposentadoria por idade do art. 48 da Lei 8.213/91, porque não cumpre a idade mínima exigida (60 anos).

[CONFERIR: os requisitos numéricos deste modelo (30 anos, 60 anos, 62 anos, 93 pontos) estão na versão feminina do original; ajustar ao sexo do segurado e ao ano da DER]

## DA ANÁLISE PÓS-REFORMA

### DA CARÊNCIA E TEMPO DE CONTRIBUIÇÃO APURADOS

Nesse cenário o(a) segurado(a) possui {{CARENCIA_MESES}} meses de carência.

E o tempo apurado até a data atual foi de: {{TEMPO_APURADO_POS_REFORMA}}.

{{OBSERVACAO_TEMPO_PRE_POS}}
[EXEMPLO DE REDAÇÃO DO ORIGINAL: "O tempo pré e pós-reforma é o mesmo, tendo em vista que a única contribuição para o RGPS foi feita em {{COMPETENCIA}} e está abaixo do salário do mínimo, sendo desconsiderada para todas as finalidades."]

Considerando as regras de transição é possível afirmar que em {{DER}} (DER), o(a) segurado(a):

NÃO tem direito à aposentadoria conforme art. 15 da EC 103/19, porque não cumpre a carência de 180 meses, o tempo mínimo de contribuição (30 anos) e nem a quantidade mínima de pontos (93 pontos).

NÃO tem direito à aposentadoria conforme art. 16 da EC 103/19, não cumpre a carência de 180 meses e o tempo mínimo de contribuição (30 anos).

NÃO tem direito à aposentadoria conforme art. 17 das regras de transição da EC 103/19, porque não cumpre a carência de 180 meses, o tempo mínimo de contribuição até a data da entrada em vigor da EC 103/19 (mais de 28 anos), o tempo mínimo de contribuição (30 anos).

NÃO tem direito à aposentadoria conforme art. 20 das regras de transição da EC 103/19, porque não cumpre a carência de 180 meses, o tempo mínimo de contribuição (30 anos).

NÃO tem direito à aposentadoria conforme art. 18 das regras de transição da EC 103/19, porque não cumpre a carência de 180 meses, e a idade mínima (62 anos).

## O PLANEJAMENTO

### DATA DO IMPLEMENTO DOS DEMAIS BENEFÍCIOS

O planejamento previdenciário é feito a partir da situação de {{SEGURADO_PRIMEIRO_NOME}} na data de hoje ({{DATA_REFERENCIA}}), e presume que continuará recolhendo daqui em diante, incluindo o recolhimento deste mês ({{COMPETENCIA_REFERENCIA}}).

A média atual dos salários de contribuição de {{SEGURADO_PRIMEIRO_NOME}} é de: R$ {{MEDIA_SALARIOS_RGPS}} – {{MEDIA_SALARIOS_RGPS_EXTENSO}} (até {{COMPETENCIA_MEDIA_RGPS}}).

[SE O SEGURADO FOR VINCULADO A RPPS] **OBSERVAÇÃO RELEVANTE:** Como o(a) segurado(a) é vinculado(a) a RPPS, para que seja retomada a qualidade de segurado(a) no RGPS precisa voltar a contribuir na modalidade contribuinte individual, uma vez que é vedada a inscrição como segurado(a) facultativo(a) nesses casos.

Com base na situação atual do(a) segurado(a), é possível afirmar que caso volte a contribuir mensalmente, na alíquota de {{ALIQUOTA_PLANO}} (plano normal) fará jus ao implemento dos benefícios nas seguintes datas:

Em {{DATA_IMPLEMENTO_ART_18}}, cumprirá os requisitos do art. 18 com RMI de R$ {{RMI_ART_18}};

Em {{DATA_IMPLEMENTO_ART_16}}, cumprirá os requisitos do art. 16 com RMI de R$ {{RMI_ART_16}};

Em {{DATA_IMPLEMENTO_ART_15}}, cumprirá os requisitos do art. 15 com RMI de R$ {{RMI_ART_15}};

Em {{DATA_IMPLEMENTO_ART_20}}, cumprirá os requisitos do art. 20 com RMI de R$ {{RMI_ART_20}};

[ORDENAR AS REGRAS PELA DATA DE IMPLEMENTO]

## DO RPPS

[SEÇÃO OPCIONAL — USAR SOMENTE QUANDO HOUVER VÍNCULO COM REGIME PRÓPRIO; O TEXTO ABAIXO É DO RPPS DO ESTADO DA BAHIA]

### DOS VÍNCULOS COM O RPPS

O(A) segurado(a) é também servidor(a) em RPPS e para elaboração deste trabalho, houve apresentação de CTC do(a) {{ORGAO_EMISSOR_CTC}} com migração de tempo para {{ORGAO_DESTINO_RPPS}}, veja:

[INSERIR IMAGEM: trecho da CTC com os períodos certificados]

Assim, para fins de planejamento no RPPS os períodos acima serão apurados na forma da tabela abaixo:

[INSERIR IMAGEM: tabela de apuração dos períodos do RPPS]

Que totalizam:

[INSERIR IMAGEM: totalização do tempo de contribuição e de exercício no RPPS]

Com base nas regras oficiais da EC 26/2020 (BA), do Manual de Aposentadoria da PGE-BA (2025), seguem as datas de implemento para o(a) segurado(a):

[INSERIR IMAGEM: quadro das hipóteses de aposentadoria do RPPS com as datas de implemento]

Ponto central que afeta 2 das 5 hipóteses: as regras de transição com paridade/integralidade da EC 26/2020 exigem que o servidor tenha ingressado no serviço público até a EC nº 41/2003 (31/12/2003).

Como o(a) segurado(a) ingressou em {{DATA_INGRESSO_SERVICO_PUBLICO}} já sob a Lei 10.887/2004, não preenche esse requisito em nenhuma hipótese, por mais tempo que trabalhe. Logo:

Para as três hipóteses efetivamente alcançáveis, temos:

[INSERIR IMAGEM: quadro das três hipóteses alcançáveis (regra geral, pontos e pedágio)]

### Cálculo do valor do benefício

A fórmula é: Provento = Média das 90% maiores remunerações (desde 07/1994 ou início da contribuição) × percentual aplicável da regra escolhida.

Considerando os salários de contribuição vertidos até a presente data, a média atual dos salários de contribuição de {{SEGURADO_PRIMEIRO_NOME}} é de R$ {{MEDIA_REMUNERACOES_RPPS}} (até {{COMPETENCIA_MEDIA_RPPS}}).

Assim, temos a seguinte simulação:

[INSERIR IMAGEM: simulação do provento por regra (média, percentual aplicável, valor estimado)]

### Detalhamento:

[ADAPTAR A ORDEM CONFORME AS DATAS DO CASO] A regra geral definitiva é atingida antes da regra de pontos, então normalmente é a rota mais rápida, mesmo com percentual um pouco menor.
A regra de pedágio, dado o tempo de contribuição que tinha em 01/02/2020, exige tanto tempo adicional que dificilmente é vantajosa nesse caso.

**1) Regra Geral (sem paridade/média 90%) — art. 42, §1º-A, III, CE c/c art. 6º, §1º, I, EC 26/2020**
- Idade 61 anos → {{DATA_REGRA_GERAL_IDADE}}
- Contribuição 25 anos → {{DATA_REGRA_GERAL_CONTRIBUICAO}}
- Exercício 10 anos → {{DATA_REGRA_GERAL_EXERCICIO}}
- Implemento pelo requisito mais tardio: {{DATA_IMPLEMENTO_REGRA_GERAL}}

**2) Regra de Pontos (sem paridade/média 90%) — art. 3º, caput c/c art. 9º, caput, I**
- Idade 54 anos → {{DATA_PONTOS_IDADE}}
- Contribuição 30 anos → {{DATA_PONTOS_CONTRIBUICAO}}
- Exercício 15 anos → {{DATA_PONTOS_EXERCICIO}}
- Pontuação exigida parte de 86 pontos (mulher) em 31/01/2020 e sobe 1 ponto a cada 1 ano e 3 meses até o teto de 96. Na data em que completa os 30 anos de contribuição, a soma idade + contribuição é de {{PONTOS_NA_DATA_CONTRIBUICAO}} pontos, contra exigência de 96 (teto atingido em {{DATA_TETO_PONTOS_ATINGIDO}}).
- Continuando a somar 2 pontos por ano trabalhado, atinge 96 pontos em {{DATA_IMPLEMENTO_PONTOS}}.

**3) Regra de Pedágio (sem paridade/média 90%) — art. 4º, caput c/c art. 9º, §1º, I**
- Em 31/01/2020 (vigência da EC 26/2020), tinha {{TEMPO_CONTRIB_EM_31_01_2020}} de contribuição — faltavam {{TEMPO_FALTANTE_EM_31_01_2020}} para completar 30.
- Pedágio de 60% sobre o faltante: {{PEDAGIO_60_CALCULO}} anos adicionais.
- Tempo total de contribuição exigido: {{TEMPO_TOTAL_COM_PEDAGIO}}, alcançado em {{DATA_IMPLEMENTO_PEDAGIO}}.
- Idade 57 ({{DATA_PEDAGIO_IDADE}}) e exercício 20 anos ({{DATA_PEDAGIO_EXERCICIO}}) [já estariam cumpridos bem antes, então o requisito que prevalece é o tempo de contribuição com pedágio — AJUSTAR AO CASO].

[CONFERIR: os requisitos de idade/pontos do RPPS acima (61, 54, 57 anos; 86 a 96 pontos) estão na versão feminina do original; ajustar ao sexo do servidor]

## DA CONCLUSÃO

As regras constantes nesse planejamento trata-se de uma estimativa de quando e quanto o segurado poderá ser aposentar, cabendo somente a ele próprio escolher a melhor regra de aposentadoria que lhe convém.

Nossa análise demonstrou que o(a) segurado(a) não possui direito a nenhuma aposentadoria nas regras anteriores a reforma da previdência, no cenário pós-reforma, ainda não cumpriu a carência necessária de 180 meses, além dos demais requisitos. [AJUSTAR AO CASO]

Considerando que volte a contribuir como segurado(a) individual, passará a fazer jus aos benefícios a partir de {{DATA_PRIMEIRO_BENEFICIO_RGPS}} - daqui a {{TEMPO_ATE_PRIMEIRO_BENEFICIO}}, quando alcançará os requisitos do {{REGRA_PRIMEIRO_BENEFICIO}}.

[SE HOUVER RPPS] Em relação ao RPPS, o(a) segurado(a) ainda não faz jus a nenhum benefício, passando a se enquadrar na Regra definitiva a partir de {{DATA_PRIMEIRO_BENEFICIO_RPPS}}, com valor estimado de aposentadoria apurado em R$ {{VALOR_ESTIMADO_RPPS}} – {{VALOR_ESTIMADO_RPPS_EXTENSO}}.

Os cálculos anexos demonstram a renda mensal inicial e tempo de contribuição de maneira detalhada.

Assim, encerra-se o presente parecer contendo {{NUMERO_LAUDAS}} laudas e {{NUMERO_ANEXOS}} anexos.

{{CIDADE}}, {{DATA_PARECER}}.

{{ADVOGADA_NOME}}
{{ADVOGADA_OAB}}
Especialista em Cálculos Previdenciários
