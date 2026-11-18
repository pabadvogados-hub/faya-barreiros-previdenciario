---
tipo: parecer-viabilidade
titulo: PARECER JURÍDICO PREVIDENCIÁRIO - Viabilidade de ação judicial (Benefício por Incapacidade Temporária)
grupo: relatorio
objetivo: Avaliar a viabilidade de ação judicial de concessão/restabelecimento de benefício por incapacidade após indeferimento, com cronologia, requisitos, prova médica, riscos, estratégia, documentos e proposta de honorários
documentos_necessarios:
  - CNIS
  - CTPS (física ou digital)
  - Processo administrativo e comunicações de decisão do INSS dos benefícios anteriores e do indeferido
  - Carta de concessão e memória de cálculo do benefício anterior (para apurar a renda mensal)
  - Laudo da perícia administrativa (SABI/Meu INSS)
  - Atestados, relatórios médicos e prontuários (atualizados), receitas e comprovantes de compra de medicação
  - ASO (admissional, de retorno, periódico e demissional)
  - TRCT e informação sobre seguro-desemprego
  - Documento de identificação, comprovante de residência, procuração e contrato de honorários
campos:
  - CLIENTE_NOME
  - CLIENTE_CPF
  - CLIENTE_NIT
  - CLIENTE_DATA_NASCIMENTO
  - CLIENTE_IDADE
  - PROFISSAO
  - EMPREGADOR
  - PERIODO_VINCULO
  - ULTIMO_SALARIO
  - NB_INDEFERIDO
  - ESPECIE_NB_INDEFERIDO
  - MOTIVO_INDEFERIMENTO
  - DOCUMENTOS_APRESENTADOS
  - DATA_FATO
  - FATO
  - DOCUMENTO_FATO
  - SITUACAO_QUALIDADE_SEGURADO
  - CONCLUSAO_QUALIDADE_SEGURADO
  - SITUACAO_CARENCIA
  - SITUACAO_INCAPACIDADE
  - ANO_RECONHECIMENTO_ADMINISTRATIVO
  - NB_ANTERIOR
  - DATA_CONCESSAO_NB_ANTERIOR
  - TEMPO_TRATAMENTO
  - INICIO_TRATAMENTO
  - ALTERACAO_TERAPEUTICA
  - DESCRICAO_ATIVIDADE
  - COMORBIDADE
  - DATA_ULTIMO_RELATORIO
  - ANO_RELATORIO_ATUALIZADO
  - DATA_DIA_SEGUINTE_CESSACAO
  - DER_NB_INDEFERIDO
  - DATA_ENCERRAMENTO_VINCULO
  - COMPETENCIA_INICIO_SEGURO_DESEMPREGO
  - SUBSECAO_JUDICIARIA
  - SALARIO_MINIMO_60_VEZES
  - ANO_VIGENTE
  - ESPECIALIDADE_PERITO
  - RISCOS_OCUPACIONAIS
  - DOENCA_PRINCIPAL
  - ALTERACAO_TERAPEUTICA_RESUMO
  - PROBABILIDADE_EXITO
  - HONORARIOS
  - RENDA_MENSAL_HIPOTETICA
  - MEDIA_SALARIAL_APROXIMADA
  - PRAZO_IMPLANTACAO_ESTIMADO
  - DATA_PERICIA_ESTIMADA
  - MESES_CONSERVADOR
  - ATRASADOS_CONSERVADOR
  - HONORARIOS_CONSERVADOR
  - MESES_PROVAVEL
  - ATRASADOS_PROVAVEL
  - HONORARIOS_PROVAVEL
  - MESES_OTIMISTA
  - ATRASADOS_OTIMISTA
  - HONORARIOS_OTIMISTA
  - CIDADE
  - DATA_PARECER
  - ADVOGADA_NOME
  - ADVOGADA_OAB
citacoes:
  - art. 59 da Lei nº 8.213/91
  - art. 25, I
  - art. 61
  - art. 29, § 10
  - art. 15, II e § 1º
  - (art. 15) § 2º
  - Tema 277 da TNU
  - art. 124, parágrafo único
  - STF, Tema 350
  - STJ, Tema 1013
  - art. 118 da Lei 8.213/91
  - art. 109, I, CF
  - art. 23 da Lei 8.906/94
  - art. 22, § 4º, da Lei 8.906/94
---

# PARECER JURÍDICO PREVIDENCIÁRIO

**Viabilidade de ação judicial — Benefício por Incapacidade Temporária (Auxílio-Doença)**

| Dados do(a) cliente |  |
|---|---|
| Nome | {{CLIENTE_NOME}} |
| CPF / NIT | {{CLIENTE_CPF}} / {{CLIENTE_NIT}} |
| Nascimento / idade | {{CLIENTE_DATA_NASCIMENTO}} — {{CLIENTE_IDADE}} anos |
| Profissão | {{PROFISSAO}} ({{EMPREGADOR}} — {{PERIODO_VINCULO}}) |
| Último salário contratual | R$ {{ULTIMO_SALARIO}} |
| Benefício indeferido | NB {{NB_INDEFERIDO}} (espécie {{ESPECIE_NB_INDEFERIDO}}) — “{{MOTIVO_INDEFERIMENTO}}” |

## 1. SÍNTESE DOS FATOS

A partir da documentação apresentada ({{DOCUMENTOS_APRESENTADOS}} [ex.: CNIS, processo administrativo do benefício anterior, comunicações de decisão do INSS, atestados, relatórios médicos e ASO]), reconstrói-se a seguinte cronologia:

| Data | Fato | Documento |
|---|---|---|
| {{DATA_FATO}} | {{FATO}} | {{DOCUMENTO_FATO}} |

[UMA LINHA POR EVENTO, EM ORDEM CRONOLÓGICA — típico: evento de saúde inicial; último dia trabalhado; concessão de benefício anterior; ASO de retorno; início/evolução do tratamento; concessão e cessação (DCB) de novo benefício; novo atestado; novo requerimento indeferido; encerramento do vínculo]

## 2. REQUISITOS LEGAIS DO BENEFÍCIO

O auxílio por incapacidade temporária (art. 59 da Lei nº 8.213/91) exige: (i) qualidade de segurado; (ii) carência de 12 contribuições (art. 25, I), salvo hipóteses de isenção; e (iii) incapacidade para o trabalho ou atividade habitual por mais de 15 dias consecutivos. O valor corresponde a 91% do salário de benefício (art. 61), limitado à média dos 12 últimos salários de contribuição (art. 29, § 10).

| Requisito | Situação do(a) cliente | Conclusão |
|---|---|---|
| Qualidade de segurado | {{SITUACAO_QUALIDADE_SEGURADO}} [ex.: "Vínculo empregatício contínuo de ... a .... Com mais de 120 contribuições sem perda da qualidade, o período de graça é de 24 meses (art. 15, II e § 1º), podendo chegar a 36 meses com comprovação de desemprego involuntário (§ 2º)."] | {{CONCLUSAO_QUALIDADE_SEGURADO}} |
| Carência | {{SITUACAO_CARENCIA}} | Preenchida |
| Incapacidade | {{SITUACAO_INCAPACIDADE}} (diagnóstico/CID, tratamento e histórico) | Ponto controvertido — será definido por perícia judicial |

Note-se que os dois primeiros requisitos estão objetivamente comprovados pelo CNIS e pela CTPS digital. A controvérsia judicial ficará restrita à existência e à data de início da incapacidade, o que é favorável: o INSS já reconheceu administrativamente a incapacidade pela mesma doença em {{ANO_RECONHECIMENTO_ADMINISTRATIVO}} (NB {{NB_ANTERIOR}}). [AJUSTAR SE NÃO HOUVER RECONHECIMENTO ANTERIOR]

## 3. ANÁLISE DA DOENÇA E DA PROVA MÉDICA

### 3.1 Pontos favoráveis

[MANTER APENAS OS PONTOS APLICÁVEIS AO CASO]

- **Doença reconhecida pelo próprio INSS:** o NB {{NB_ANTERIOR}} foi concedido em {{DATA_CONCESSAO_NB_ANTERIOR}} com base no mesmo quadro. O indeferimento posterior contraria esse reconhecimento sem que haja prova de melhora clínica.
- **Tratamento contínuo e documentado** há {{TEMPO_TRATAMENTO}} (desde {{INICIO_TRATAMENTO}}), com profissionais diferentes chegando à mesma conclusão de afastamento.
- **Agravamento terapêutico:** {{ALTERACAO_TERAPEUTICA}} — indicativo objetivo de refratariedade/persistência dos sintomas, e não de remissão.
- **Natureza da atividade:** {{DESCRICAO_ATIVIDADE}} [descrever as exigências da função e, se constar do ASO, a exposição a riscos (ex.: psicossociais, sobrecarga de trabalho mental)]. Os sintomas são incompatíveis com essa rotina.
- **Comorbidade:** {{COMORBIDADE}} compõe o quadro global e deve ser considerada pelo perito, inclusive quanto aos esforços inerentes à função.

### 3.2 Pontos de atenção (riscos)

- **Ausência de relatório médico atualizado:** o documento médico mais recente é de {{DATA_ULTIMO_RELATORIO}}. É indispensável obter relatório de {{ANO_RELATORIO_ATUALIZADO}} (e, se possível, prontuário) que descreva sintomas atuais, evolução, medicação, resposta ao tratamento e prognóstico, com indicação expressa de incapacidade para a função de {{PROFISSAO}}.
- **Intervalo {{DATA_DIA_SEGUINTE_CESSACAO}} a {{DER_NB_INDEFERIDO}}:** é preciso esclarecer se houve pedido de prorrogação/novo requerimento, retorno ao trabalho ou recebimento de salário nesse período. Pelo Tema 277 da TNU, a continuidade do benefício após a alta programada pressupõe pedido de prorrogação, recurso ou reconsideração; sem isso, o restabelecimento desde {{DATA_DIA_SEGUINTE_CESSACAO}} tende a não ser acolhido, e o termo inicial provável passa a ser a DER de {{DER_NB_INDEFERIDO}}.
- **Encerramento do vínculo ({{DATA_ENCERRAMENTO_VINCULO}}):** deve-se verificar o ASO demissional. Se ele atestou aptidão, o documento será usado pelo INSS e precisará ser contraposto com a prova médica.
- **Seguro-desemprego:** não é acumulável com auxílio por incapacidade (art. 124, parágrafo único). Eventuais parcelas recebidas após {{COMPETENCIA_INICIO_SEGURO_DESEMPREGO}} serão descontadas dos atrasados.
- **Benefício temporário:** a sentença fixará data de cessação estimada (DCB). A conversão em aposentadoria por incapacidade permanente é possível, mas depende de o perito concluir pela irreversibilidade, o que é menos provável aos {{CLIENTE_IDADE}} anos e com tratamento em curso. [AJUSTAR AO CASO]

## 4. ESTRATÉGIA JUDICIAL PROPOSTA

### 4.1 Via e competência

Ação previdenciária de concessão/restabelecimento de benefício por incapacidade temporária, com pedido subsidiário de aposentadoria por incapacidade permanente, a ser ajuizada no Juizado Especial Federal da Subseção Judiciária do domicílio do(a) cliente ({{SUBSECAO_JUDICIARIA}}), desde que o valor da causa (atrasados + 12 parcelas vincendas) não ultrapasse 60 salários mínimos (R$ {{SALARIO_MINIMO_60_VEZES}} em {{ANO_VIGENTE}}). Não é necessário interpor recurso administrativo: o indeferimento do requerimento já configura o interesse de agir (STF, Tema 350).

### 4.2 Pedidos

- Tutela de urgência para implantação imediata do benefício, dado o caráter alimentar e a ausência de renda após o fim do vínculo.
- Concessão do benefício desde a DER do NB {{NB_INDEFERIDO}} ({{DER_NB_INDEFERIDO}}) ou, se comprovado pedido de prorrogação/requerimento no período, restabelecimento do NB {{NB_ANTERIOR}} desde {{DATA_DIA_SEGUINTE_CESSACAO}}.
- Subsidiariamente, aposentadoria por incapacidade permanente, caso a perícia conclua pela irreversibilidade, e encaminhamento à reabilitação profissional, se for o caso.
- Perícia judicial com médico {{ESPECIALIDADE_PERITO}}, com quesitos que abordem a função específica de {{PROFISSAO}}, a interação entre as doenças/comorbidades e a data de início da incapacidade (DII).
- Pagamento dos atrasados com correção monetária e juros, admitindo-se a percepção conjunta de eventual salário recebido no período de espera (STJ, Tema 1013).

### 4.3 Possível natureza acidentária (a investigar)

[SEÇÃO OPCIONAL — USAR QUANDO HOUVER INDÍCIO DE NEXO COM O TRABALHO]

O ASO registra exposição a {{RISCOS_OCUPACIONAIS}}. Se houver elementos de que a doença foi desencadeada ou agravada pelo trabalho (nexo causal ou nexo técnico epidemiológico — NTEP), o benefício poderia ser de natureza acidentária (B91), com reflexos trabalhistas relevantes (estabilidade de 12 meses — art. 118 da Lei 8.213/91 — e depósitos de FGTS durante o afastamento). Nesse caso, porém, a ação previdenciária tramitaria na Justiça Estadual (art. 109, I, CF). Recomenda-se avaliar esse ponto com o(a) cliente antes do ajuizamento, assim como a eventual validade da dispensa ocorrida durante o quadro de incapacidade, matéria de competência da Justiça do Trabalho.

## 5. DOCUMENTOS E PROVIDÊNCIAS NECESSÁRIOS

- Relatório médico atualizado ({{ANO_RELATORIO_ATUALIZADO}}), com CID, sintomas, evolução, medicação, prognóstico e indicação expressa de incapacidade para a função.
- Prontuários e receitas desde {{INICIO_TRATAMENTO}} (todas as especialidades envolvidas), comprovantes de compra de medicação, eventuais relatórios de terapias.
- Carta de concessão e memória de cálculo do NB {{NB_ANTERIOR}} (para apurar a renda mensal) e laudo da perícia do NB {{NB_INDEFERIDO}} (SABI/Meu INSS).
- Termo de rescisão (TRCT), ASO demissional e informação sobre seguro-desemprego.
- Esclarecimento sobre o período de {{DATA_DIA_SEGUINTE_CESSACAO}} a {{DER_NB_INDEFERIDO}} (pedido de prorrogação, retorno ao trabalho ou atestados).
- Documento de identificação, comprovante de residência atualizado e procuração/contrato de honorários assinados.

## 6. CONCLUSÃO QUANTO À VIABILIDADE

Considerando a natureza da doença ({{DOENCA_PRINCIPAL}}, com tratamento contínuo há {{TEMPO_TRATAMENTO}}{{ALTERACAO_TERAPEUTICA_RESUMO}}), o reconhecimento administrativo anterior da incapacidade pelo próprio INSS, a incompatibilidade dos sintomas com a função de {{PROFISSAO}} e o preenchimento inequívoco da qualidade de segurado(a) e da carência, a ação judicial é VIÁVEL, com probabilidade de êxito {{PROBABILIDADE_EXITO}}, condicionada essencialmente à obtenção de relatório médico atualizado que demonstre a persistência da incapacidade em {{ANO_RELATORIO_ATUALIZADO}}. [AJUSTAR AO CASO]

Ressalta-se que o resultado depende da perícia judicial, que é independente das conclusões dos médicos assistentes e do INSS, razão pela qual não é possível garantir o êxito.

## 7. PROPOSTA DE HONORÁRIOS

Os honorários advocatícios são propostos na modalidade ad exitum (quota litis), sem qualquer custo antecipado para o(a) cliente:

- {{HONORARIOS}} sobre o proveito econômico obtido, compreendendo todas as parcelas vencidas (atrasados) pagas por RPV ou precatório, inclusive 13º salário (abono anual), apuradas até a efetiva implantação do benefício.
- Não havendo êxito, nada será devido a título de honorários contratuais.
- Os honorários de sucumbência eventualmente fixados pertencem ao advogado (art. 23 da Lei 8.906/94) e não se compensam com os contratuais.
- Os honorários contratuais poderão ser destacados diretamente da RPV/precatório (art. 22, § 4º, da Lei 8.906/94), mediante juntada do contrato.
- Despesas eventuais (cópias, autenticações, deslocamentos, assistente técnico, se o(a) cliente optar por contratá-lo) serão de responsabilidade do(a) cliente, mediante prévia comunicação.

### Simulação ilustrativa

A renda mensal exata depende da memória de cálculo do NB {{NB_ANTERIOR}}. Para fins de estimativa, adota-se renda mensal hipotética de R$ {{RENDA_MENSAL_HIPOTETICA}} (91% de uma média salarial aproximada de R$ {{MEDIA_SALARIAL_APROXIMADA}}) e implantação em cerca de {{PRAZO_IMPLANTACAO_ESTIMADO}} meses após o ajuizamento:

| Cenário | Termo inicial (DIB) | Meses de atrasados* | Atrasados estimados | Honorários ({{HONORARIOS}}) |
|---|---|---|---|---|
| Conservador | Data da perícia judicial (~{{DATA_PERICIA_ESTIMADA}}) | ≈ {{MESES_CONSERVADOR}} | R$ {{ATRASADOS_CONSERVADOR}} | R$ {{HONORARIOS_CONSERVADOR}} |
| Provável | DER — {{DER_NB_INDEFERIDO}} | ≈ {{MESES_PROVAVEL}} | R$ {{ATRASADOS_PROVAVEL}} | R$ {{HONORARIOS_PROVAVEL}} |
| Otimista | Restabelecimento — {{DATA_DIA_SEGUINTE_CESSACAO}} | ≈ {{MESES_OTIMISTA}} | R$ {{ATRASADOS_OTIMISTA}} | R$ {{HONORARIOS_OTIMISTA}} |

\* Inclui 13º proporcional. Valores sem correção monetária e juros, antes do desconto de eventual seguro-desemprego e sujeitos à data de cessação fixada em sentença. No cenário otimista, o valor da causa pode superar 60 salários mínimos, exigindo renúncia ao excedente (para manter o JEF) ou ajuizamento na Vara Federal comum. A estimativa será refeita após a obtenção da carta de concessão do benefício anterior.

É o parecer, salvo melhor juízo.

{{CIDADE}}, {{DATA_PARECER}}.

_______________________________________
{{ADVOGADA_NOME}} — Advocacia e Consultoria Previdenciária
{{ADVOGADA_OAB}}

Ciente e de acordo: _______________________________________
{{CLIENTE_NOME}} — CPF {{CLIENTE_CPF}}
