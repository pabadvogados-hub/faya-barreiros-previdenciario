---
tipo: contribuicoes-acima-do-teto
titulo: RELATÓRIO DE ANÁLISE PREVIDENCIÁRIA - Recolhimentos Concomitantes e Restituição de Valores Pagos Acima do Teto do INSS
grupo: relatorio
objetivo: Apurar, no período não prescrito, as competências com recolhimentos concomitantes cuja soma superou o teto do RGPS e calcular o valor a restituir corrigido pela SELIC
documentos_necessarios:
  - CNIS completo com remunerações por vínculo e valores consolidados por ano civil
  - Tabelas de faixas e teto de contribuição do INSS de cada ano do período
  - Tabela da taxa SELIC mensal divulgada pela Receita Federal
  - Planilha mês a mês do cálculo (anexo)
campos:
  - SEGURADO_NOME
  - SEGURADO_CPF
  - SEGURADO_DATA_NASCIMENTO
  - SEGURADO_SEXO
  - COMPETENCIA_PRESCRICAO
  - DATA_BASE
  - DATA_RELATORIO
  - QTD_COMPETENCIAS_CONCOMITANTES
  - PERIODO
  - VINCULOS_CONCORRENTES
  - NUMERO_MESES
  - TOTAL_RECOLHIDO
  - TOTAL_DEVIDO
  - VALOR_RESTITUIR
  - VALOR_CORRIGIDO_SELIC
  - ANOS_TABELAS
  - COMPETENCIAS_SEM_RESTITUICAO
  - CIDADE
  - ADVOGADA_NOME
  - ADVOGADA_OAB
citacoes:
  - nenhuma citação legal no modelo original (só menciona a tabela progressiva do INSS e a taxa SELIC não capitalizada)
---

# RELATÓRIO DE ANÁLISE PREVIDENCIÁRIA

**Recolhimentos Concomitantes e Restituição de Valores Pagos Acima do Teto do INSS**

**Dados do(a) Contribuinte:**

| Segurado(a): | {{SEGURADO_NOME}} | CPF: | {{SEGURADO_CPF}} |
|---|---|---|---|
| Data de nascimento: | {{SEGURADO_DATA_NASCIMENTO}} | Sexo: | {{SEGURADO_SEXO}} |
| Prescrição (base): | {{COMPETENCIA_PRESCRICAO}} | Data base: | {{DATA_BASE}} |
| Data do relatório: | {{DATA_RELATORIO}} |  |  |

## 1. Objeto da Análise

Analisando o CNIS de {{SEGURADO_NOME}}, verificou-se, no período não prescrito compreendido entre {{COMPETENCIA_PRESCRICAO}} e a data-base de {{DATA_BASE}}, a ocorrência de recolhimentos previdenciários simultâneos em mais de um vínculo/fonte pagadora em uma mesma competência, situação que pode configurar contribuição acima do teto do RGPS e ensejar direito à restituição.

## 2. Períodos de Concomitância Identificados

Foram identificadas {{QTD_COMPETENCIAS_CONCOMITANTES}} competências com contribuições concomitantes, distribuídas nos seguintes períodos:

| Período | Vínculos concorrentes | Nº de meses |
|---|---|---|
| {{PERIODO}} | {{VINCULOS_CONCORRENTES}} [ex.: "Empregador A (empregada) + Empregador B (empregada)" ou "Empregador A (empregada) + Recolhimento CI (MEI/LC123)"] | {{NUMERO_MESES}} |

Nos meses em que a soma dos salários de contribuição superou o teto previdenciário vigente na competência, houve recolhimento acima do limite legal, dando origem ao valor a restituir apurado no item 3.

## 3. Metodologia de Cálculo

Para cada competência concomitante, calculou-se a contribuição efetivamente paga em cada fonte pagadora, aplicando a tabela progressiva do INSS (alíquotas de 7,5%, 9%, 12% e 14%) vigente no respectivo ano.

Em seguida, apurou-se a contribuição correta devida sobre a soma dos salários de contribuição, limitada ao teto do INSS de cada competência.

O valor a restituir corresponde à diferença entre o total efetivamente pago e o valor correto (contribuição no teto), quando positiva.

Para a correção monetária, aplicou-se a taxa SELIC de forma não capitalizada (soma simples das taxas mensais divulgadas pela Receita Federal, do mês seguinte ao pagamento até o mês anterior à data-base, acrescida de 1% referente ao mês-base de {{DATA_BASE}}).

[INSERIR IMAGEM: logotipo/cabeçalho ou recorte da planilha de cálculo, conforme o original]

## 4. Resultado Consolidado

| Indicador | Valor (R$) |
|---|---|
| Total recolhido nos meses concorrentes | R$ {{TOTAL_RECOLHIDO}} |
| Total devido (limitado ao teto, cálculo progressivo) | R$ {{TOTAL_DEVIDO}} |
| Valor a restituir (sem correção monetária) | R$ {{VALOR_RESTITUIR}} |
| Valor total corrigido pela SELIC (não capitalizada, base {{DATA_BASE}}) | R$ {{VALOR_CORRIGIDO_SELIC}} |

O detalhamento mês a mês (salários de contribuição, contribuições pagas, alíquotas, soma das contribuições, contribuição no teto, valor a restituir e valor corrigido pela SELIC) consta da planilha, que acompanha este relatório.

## 5. Ressalvas

Os coeficientes de faixa e teto utilizados ({{ANOS_TABELAS}}) foram obtidos de fontes públicas e conferidos contra os valores "Consolidados por Ano Civil" do próprio extrato CNIS, com integral coincidência.

Em competências nas quais a soma paga foi inferior à contribuição corretamente devida ({{COMPETENCIAS_SEM_RESTITUICAO}}), não há valor a restituir para o período.

{{CIDADE}}, {{DATA_RELATORIO}}

{{ADVOGADA_NOME}}
{{ADVOGADA_OAB}}
Especialista em Cálculos
