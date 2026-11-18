# FORMATO DOS CÁLCULOS — PADRÃO DO ESCRITÓRIO (PREVIDENCIÁRIO)

Guia para os agentes de IA **conferirem** cálculos e **montarem relatórios** no padrão da advogada calculista. Descreve só formato e método, a partir de 6 demonstrativos reais (anonimizados aqui). Não contém dados de segurado.

Tipos cobertos:

1. Apuração de tempo de contribuição (sem direito na DER)
2. Planejamento previdenciário
3. Revisão (cálculo comparativo com benefício ativo + valor da causa), no exemplo, conversão em aposentadoria da pessoa com deficiência
4. Liquidação de sentença: (a) demonstrativo de calculadora previdenciária (2 exemplos) e (b) CONTA FÁCIL PREV, da Justiça Federal

---

## 0. Origem dos PDFs (software)

| Tipo | Software indicado no texto | Observações |
|---|---|---|
| Apuração de tempo, Planejamento, Revisão | **Não aparece o nome no texto.** É uma calculadora previdenciária online que gera relatórios com quadro "Resumo dos benefícios", "Planejamento Previdenciário Inteligente", "sistema inteligente" de descartes e a mensagem "É um cálculo de revisão? ... troque a planilha para o modo de revisão". | Rodapé de cada página com o nome comercial do escritório, telefone e e-mail (dados de contato da advogada, que não se repetem aqui). |
| Liquidação (2 exemplos) | **Não aparece o nome.** Título: "Demonstrativo de Cálculo - Liquidação de Sentença". | Layout compacto: resumo, critérios, tabela mensal, honorários e quadro de RRA. |
| Liquidação (1 exemplo) | **CONTA FÁCIL PREV**, "Programa para Cálculos em Ações Previdenciárias - INSS", das Divisões de Cálculos Judiciais e de TI da Justiça Federal no Rio Grande do Sul. Versão 6.1.1 (Motor 5.19.0 Pro). | Traz "identificador" para gerar o cálculo de novo (válido por 3 anos) e aviso de que o juízo pode adotar outro critério. |

---

## 1. APURAÇÃO DE TEMPO DE CONTRIBUIÇÃO

### 1.1 Seções (na ordem)

1. **Cabeçalho**: segurado, data de nascimento, sexo, DER.
2. **Quadro-resumo por espécie de benefício**. Colunas: Benefício | Complementações ou indenizações (valor a pagar ao INSS) | Tempo de contribuição | Carência | Tem direito na DER ou direito adquirido em data anterior | Melhor RMA (Renda Mensal Atual). Linhas: aposentadoria por tempo de contribuição / por tempo e idade / por pontos; aposentadoria por idade urbana / híbrida (e outras quando houver). Situação: "Não tem direito - Cumprirá em dd/mm/aaaa" ou "Tem direito".
3. **Resumo dos benefícios** (texto): "ainda não tem direito a qualquer aposentadoria programada"; "Se continuar recolhendo mensalmente sobre o último salário R$ X, vai ter direito ... a partir de [data] (daqui a X anos, X meses e X dias), com base na regra do art. [N] da EC nº 103/2019, com uma RMI estimada de R$ X".
4. **Períodos de alíquotas reduzidas** e **períodos rurais de segurado especial após 10/1991** (informa se há ou não).
5. **CONTAGEM DE TEMPO DE CONTRIBUIÇÃO / TEMPO DE SERVIÇO COMUM**. Colunas: Nº | Nome do período (empregador + indicadores do CNIS colados, ex. IREM-INDPEND, PADM-EMPR, PEXT, IREM-ACD, PSC-MEN-SM-EC103) | Início | Fim | Fator | Tempo (anos, meses e dias; com a nota "Ajustada concomitância" quando aplicável) | Carência.
6. **Quadro de marcos temporais**. Colunas: Marco Temporal | Tempo de contribuição | Carência | Idade | Pontos (Lei 13.183/2015). Marcos: EC nº 20/98 (16/12/1998) + "Pedágio EC 20/98"; Lei 9.876/99 (28/11/1999); Reforma EC nº 103/19 (13/11/2019); 31/12 de cada ano de 2019 em diante; Lei nº 14.331/2022 (04/05/2022); data de hoje; DER. Pontos "inaplicável" antes da reforma.
7. **Competências com valor inferior ao salário mínimo**, em 4 blocos:
   - consideradas para **tempo de contribuição** (colunas: Mês | Mês consolidado com concomitantes | Salário mínimo | Diferença | Fundamento legal p/ consideração). Fundamento típico: empregado até 11/2019, **Art. 209, §2º da IN 128/2022**;
   - consideradas para **carência**, com o fundamento **Art. 189, §8º da IN 128/2022**;
   - **desconsideradas para tempo**: "Nos termos do art. 195, §14 da CF/88 (incluído pela EC 103/19) c/c arts. 209, caput e 210 da IN 128/2022";
   - **desconsideradas para carência**: "Nos termos dos arts. 189, §§7º e 9º da IN 128/2022".
8. **Recolhimentos em atraso** (contribuinte individual), com as colunas Vínculo | Competência | Observações | Contagem:
   - **considerados para carência**: recolhimento em atraso, porém posterior à primeira competência tempestiva e sem perda da qualidade de segurado (cálculo do período de graça). Fundamento: **Arts. 81, 82 e 85 da Portaria DIRBEN 991/2022**;
   - **desconsiderados para carência**: recolhido em atraso antes do primeiro recolhimento tempestivo. Fundamento: **Art. 27, inc. II, da Lei 8.213/91 c/c arts. 82 e 83 da Portaria DIRBEN/INSS Nº 991/2022 e Tema 192 TNU**.
9. **Análise do direito em cada marco** (16/12/1998, 28/11/1999, 13/11/2019, 31/12 de cada ano, 04/05/2022, DER): "Tem direito" ou "Não tem direito" por espécie.
10. **Sem cálculo de RMI**: quando não há direito em nenhuma data, o sistema não calcula RMI, valor da causa nem atrasados, e pergunta se é cálculo de revisão (modo revisão).

### 1.2 O que conferir

- Concomitâncias: o período sobreposto deve aparecer com tempo zerado ou reduzido e a nota "Ajustada concomitância". **Os salários concomitantes são somados para a RMI**, respeitado o teto.
- Cada indicador do CNIS listado no nome do período deve ser tratado no relatório (ver modelos em `pecas/relatorios/`).
- Competência abaixo do mínimo **depois de 11/2019** sai do tempo e da carência (precisa de complementação, utilização de excedente ou agrupamento, art. 29 da EC 103/2019). **Antes de 11/2019**, a de empregado continua válida.
- Recolhimento de contribuinte individual em atraso: conferir a data de pagamento contra o vencimento (dia 15 do mês seguinte, prorrogado para o primeiro dia útil) e o período de graça (12 ou 24 meses).
- Pontos = idade + tempo em anos decimais (4 casas).

---

## 2. PLANEJAMENTO PREVIDENCIÁRIO

### 2.1 Seções

1. Cabeçalho (segurado, CPF, nascimento, sexo, DER).
2. **Quadro-resumo por espécie** (mesmas colunas da apuração), incluindo: tempo de contribuição/idade/pontos; idade urbana/híbrida; idade rural; e ainda (em texto) idade internacional, aposentadoria especial, programada do professor, por tempo de contribuição da PcD e por idade da PcD.
3. **Resumo dos benefícios** (mesmo texto-padrão da apuração).
4. **Planejamento Previdenciário Inteligente**: parte da situação na data de hoje e presume recolhimento contínuo, incluindo o mês corrente.
5. **Personalização** (parâmetros escolhidos):
   - base de contribuição futura: último salário / teto do INSS / salário mínimo / valor informado; mostra a média atual dos salários de contribuição;
   - **alíquota**: 7,5% a 14% para empregado (art. 28 da EC 103/2019); 11% para contribuinte individual sócio (pró-labore) ou que presta serviço a empresa; 20% para autônomo que trabalha para pessoa física e para facultativo; **alíquotas reduzidas** (11% ou 5% sobre o salário mínimo: autônomo/facultativo com exclusão da aposentadoria por tempo, MEI, facultativo de baixa renda), que, conforme o **art. 21, §2º da Lei 8.212/91**, dão direito **só à aposentadoria por idade do art. 18 da EC 103/2019**, e não às dos arts. 15, 16, 17 e 20;
   - **periodicidade**: mensal, a cada 2, 3, 4, 5 ou 6 meses, anual (recolhendo mensalmente, mantém a qualidade de segurado);
   - **expectativa de vida**: tábua do IBGE ou idade informada.
6. **Datas do planejamento**: para cada data em que passa a cumprir uma regra, um bloco com:
   - quadro **REQUISITO | EXIGÊNCIA | CUMPRIMENTO** (tempo de contribuição + pedágio, carência de 180, idade, pontos), dizendo "Já cumprido na data de hoje" ou "cumprirá em ...";
   - data em que cumprirá todos os requisitos, idade ao se aposentar;
   - **Melhor RMI na data**, "dentre todos os artigos, considerando todos os descartes possíveis", e o percentual do salário mínimo atual;
   - recolhimento mensal (alíquota × base) e total a recolher até a data;
   - **tempo do retorno do investimento** = (valor que deixará de receber se esperar + contribuições adicionais) ÷ aumento mensal da RMI;
   - valor que deixará de receber se esperar desde a primeira data possível (meses × RMI da primeira data, com as gratificações natalinas);
   - aumento mensal da RMI em relação à primeira data;
   - valor total que receberá até a expectativa de vida (meses incluindo as gratificações natalinas × RMI).
7. **Regra inatingível** (ex.: art. 17, pedágio de 50%): exige mais de 33 anos (homem) em 13/11/2019; informa quanto faltou e quanto precisaria averbar.
8. **Lacunas contributivas**. Colunas: Lacuna | Período | Duração, com a menção à **Súmula 75 da TNU** (vínculo em CTPS não reconhecido) ou a vínculo sem registro.

### 2.2 Regras/cenários simulados

Arts. 15 (pontos progressivos), 16 (idade mínima progressiva), 17 (pedágio de 50%), 18 (idade) e 20 (pedágio de 100%) da EC 103/2019; também especial, professor, PcD, rural e internacional. Em cada data em que mais de uma regra está cumprida, a RMI é calculada por artigo e fica a maior.

### 2.3 O que conferir

- Requisitos por sexo e por ano (idade e pontos progressivos).
- Pedágio do art. 20 = tempo que faltava em 13/11/2019 para 35/30 anos; do art. 17 = 50% do que faltava (só para quem tinha mais de 33/28 anos na data).
- Retorno do investimento: se der centenas de meses, a conclusão-padrão é "não é vantajoso esperar".
- A base de contribuição escolhida (último salário, teto) e a alíquota devem bater com a categoria real do segurado. Vinculado a RPPS não pode ser facultativo, só contribuinte individual.

---

## 3. REVISÃO (benefício ativo × benefício devido)

No exemplo, revisão de aposentadoria por tempo de contribuição para **aposentadoria por tempo de contribuição da pessoa com deficiência**.

### 3.1 Seções

1. Cabeçalho e quadro-resumo por espécie, com destaque para "Benefício com a maior RMI" e "Benefício com maior valor de atrasados"; RMI válida para a DER e RMA "para hoje".
2. **Períodos de deficiência**: Início | Fim | Grau | Duração; tempo total e **deficiência preponderante**.
3. **Contagem de tempo convertido para a deficiência preponderante**. Colunas: Nº | Nome do período | Início | Fim | Deficiência (sem deficiência / leve / moderada / grave) | Multiplicador deficiência (1) | Multiplicador especial (2) | Multiplicador aplicado (3) | Tempo | Carência. Notas: (1) **art. 70-E, caput, do Decreto 3.048/99**; (2) tabela do **art. 70-F, §1º do Decreto 3.048/99**; (3) o mais favorável entre (1) e (2), **art. 70-F, §1º, parte final**.
4. Marcos temporais (Reforma, Lei 14.331/2022, DER).
5. Competências abaixo do mínimo, nos mesmos 4 blocos da apuração. Pré-07/1994: contribuinte individual/facultativo válido (**Art. 89, inc. VII, da Portaria DIRBEN/INSS Nº 991/2022**), em moedas da época (NCz$, Cr$, CR$).
6. Recolhimentos em atraso considerados para carência (período de graça de 24 meses quando já havia 120 contribuições sem perda da qualidade; vencimento conforme o **art. 99, parágrafo único, da Portaria DIRBEN/INSS Nº 991/2022** e prorrogação pelo **art. 216, inc. II, do Decreto 3.048/99**).
7. **ANÁLISE DO DIREITO** (texto): por que tem direito na DER (ex.: art. 3º da LC 142/2013, inciso conforme o grau; carência do art. 25, inc. II, da Lei 8.213/91).
8. **Salários de contribuição** (do mais recente para o mais antigo). Colunas: SEQ | DATA | SALÁRIO HISTÓRICO | (observação: "Abaixo do mínimo" / "Limitada ao teto") | ÍNDICE | SALÁRIO CORRIGIDO | TEMPO LÍQUIDO | OBSERVAÇÕES ("Descartada", "Salários concomitantes dos períodos X e Y somados").
9. **Detalhamento do cálculo da RMI** (base legal no topo; no exemplo, Art. 22 da EC 103/19), em dois blocos:
   - **Cálculo preliminar (sem descartes)**: soma dos salários, divisor, divisor mínimo (**Art. 135-A da Lei 8.213/91**, "Superado"), média, fator previdenciário (aplicado/não aplicado e por quê; expectativa de sobrevida, tempo em anos, idade em anos), coeficiente, RMI;
   - **Cálculo com descartes**: quantidade máxima de salários passíveis de descarte, quantos o sistema descartou, soma, divisor, média, fator, coeficiente, RMI;
   - Melhor RMA atualizada para hoje.
10. **Cálculo de valor da causa**:
    - data do ajuizamento (se não informada, usa a data de hoje);
    - **benefícios já recebidos** (NB, DIB, RMI, RMA). Encontro de contas; se houver mês negativo, aplica-se o **Tema 1.207 do STJ** (direito a não sofrer desconto dos meses negativos);
    - **A. Valores devidos**: início dos atrasados (DER), RMI, parcelas vencidas até o ajuizamento (atualizadas) + **12 vincendas** (mês cheio + gratificações natalinas do período);
    - **B. Valores recebidos** (mesma estrutura);
    - **C. SELIC e taxa legal previdenciária**;
    - Valor da causa = A − B − C. Teste do **teto do JEF** (60 salários mínimos vigentes no ajuizamento; competência absoluta, **art. 3º, §3º da Lei 10.259/01**).
11. **Discriminativo das parcelas vencidas**. Colunas: Data | Observações (reajuste RGPS %, gratificação natalina) | Devido | Índice CM | Devido corrigido | Recebido | Recebido corrigido | Diferença corrigida | SELIC % | SELIC R$ | Total. Linhas finais: "Até o ajuizamento", "12 vincendas", "Total".
12. **Gratificações natalinas proporcionais**: **art. 619, §§1º e 2º da IN 128/2022** (ex.: proporcional aos meses do ano após a DIB).
13. **Critérios**: início e fim dos atrasados, RMI, correção monetária, juros, ajuizamento, prescrição (parcelas anteriores a 5 anos do ajuizamento), data do cálculo.

### 3.2 Correção e juros (texto-padrão do software)

Conforme o **Manual de Cálculos da Justiça Federal (Resolução CJF nº 990/2026)**: ORTN até fev/86, OTN até dez/88, IPC até fev/89, BTN até mar/90, IPC até fev/91, INPC até dez/92, IRSM até fev/94, URV até jun/94, IPC-R até jun/95, INPC até abr/96, IGP-DI até ago/06, **INPC até 11/2021**; **de 12/2021 a 08/2025 SELIC**, sem correção monetária autônoma, porque a SELIC engloba correção e juros (**art. 3º da EC nº 113/2021**); **INPC de novo a partir de 09/2025**, com juros pela **taxa legal previdenciária** (**EC nº 136/2025** e **ARE nº 1.557.312/SP, Tema nº 1.419 do STF**), contados da data de início dos juros (em regra, a citação, que por isso normalmente não entra no valor da causa; item 4.3 do Manual). Índices negativos (deflação) entram, mas nenhuma parcela fica abaixo do valor nominal (item 4.1.2.2).

### 3.3 O que conferir

- O grau de deficiência e a data de início adotados são os do laudo usado no relatório (posição conservadora: grau mais leve).
- Multiplicador aplicado = o mais favorável entre o da deficiência e o do especial.
- Fator previdenciário na PcD só se for favorável (art. 9º, I, da LC 142/2013), coeficiente de 100%.
- Divisor com descartes: os descartes não podem baixar o tempo/carência abaixo do mínimo da regra (art. 26, §6º, da EC 103/2019).
- Encontro de contas: o recebido corrigido pelo mesmo índice do devido.
- Valor da causa ≤ 60 salários mínimos → JEF.

---

## 4. LIQUIDAÇÃO DE SENTENÇA

### 4.1 Demonstrativo da calculadora previdenciária (2 exemplos)

**Seções**

1. Dados do segurado (nome, data de nascimento).
2. **Resultado do cálculo**: Total | Parcelas vencidas | Soma dos juros | Soma SELIC | Honorários de sucumbência | Data do cálculo.
3. Benefício (espécie, NB ou "Não informado", DIB, DIP, data fim das parcelas, RMI).
4. **Critérios e parâmetros**: ajuizamento; citação (início dos juros, competência); juros de mora; correção monetária; composição da correção monetária (índice por período); honorários sucumbenciais (% sobre as parcelas vencidas até a data da sentença/acórdão).
5. **Tabela mensal**. Colunas: DATA | ÍND. REAJ. (% do reajuste em janeiro) | LÍQUIDO DEVIDO | LÍQUIDO RECEBIDO | DIFERENÇA | CORREÇÃO (coeficiente) | VLR CORRIGIDO | JUROS (% acumulado) | VLR JUROS | SELIC (% acumulado) | VLR SELIC. Linhas "13º" após agosto e dezembro (adiantamento e saldo, conforme o caso). Primeira parcela proporcional aos dias. Parcelas prescritas aparecem como "Prescrita". Diferença negativa vira 0,00.
6. Totais: soma das parcelas devidas, soma dos juros, soma SELIC, TOTAL.
7. **Demonstrativo dos honorários de sucumbência**: soma dos valores devidos até a competência-limite × percentual.
8. **Rendimentos recebidos acumuladamente (IR/RRA)**: anos anteriores × ano atual (valor e número de parcelas).

**Critérios que aparecem**

- Juros: "Poupança após 05/2012 - Lei 12.703/12 (0,5% até 01/2003, 1% até 07/2009, 0,5% até 05/2012, Poupança após)"; ou "EC 136/25 Poupança a partir de 09/2025 (Poupança até 11/2021, Selic até 08/2025, Poupança após)". Os juros decrescem para as parcelas posteriores à citação.
- Correção: "EC 113/21 - IPCA-E (IGP-DI até 08/2006, IPCA-E até 11/2021, sem correção após)"; ou "EC 136/25 - INPC (INPC até 11/2021, sem correção até 09/2025, INPC após)".
- Composição: OTN (03/1986-12/1988), BTN (01/1989-02/1991), INPC (03/1991-12/1992), IRSM (01/1993-02/1994), URV (03/1994-06/1994), IPC-r (07/1994-06/1995), INPC (07/1995-04/1996), IGP-DI (05/1996-08/2006), então IPCA-E ou INPC (09/2006-11/2021), sem correção (12/2021 em diante ou até 08/2025, conforme o critério) e INPC a partir de 09/2025 no critério da EC 136/25.
- SELIC: percentual acumulado decrescente de 12/2021 até 08/2025, 0% depois.
- Honorários sucumbenciais: percentual da sentença sobre as parcelas vencidas até a data-limite.

### 4.2 CONTA FÁCIL PREV (Justiça Federal)

**Seções**

1. **Resumo do cálculo de liquidação de sentença**: processo, autor, réu. **I - Partes**: Nome | Principal corrigido | Juros moratórios | SELIC | Total. **II - Totalização**: subtotal, total da conta na competência, "Atualizado até [mês/ano]". Local, data e "Cálculo elaborado por".
2. **Critérios e parâmetros**: data de início dos juros (decrescente para parcelas posteriores); juros de mora "6% a.a. até 12/02 + 12% a.a. até 07/09 e correspondente à Poupança (dia 1º) em diante. Atualização pela Selic a partir de 12/2021 (cfe. Manual de Cálculos da JF - Ed. 2022)"; correção "Benefícios Previdenciários - Manual de Cálculos da JF (Edição 2022) até 12/2021", composição ORTN (10/64-02/86), OTN (03/86-01/89), IPC/IBGE (01/89 42,72% e 02/89 10,14%, expurgos), BTN (03/89-03/90), IPC/IBGE (03/90-02/91), INPC (03/91-12/92), IRSM (01/93-02/94), URV (03/94-06/94), IPC-R (07/94-06/95), INPC (07/95-04/96), IGP-DI (05/96-08/06), INPC (09/2006 em diante) até 12/2021; outras sucumbências e honorários (apurados ou não); **percentual para acordo** (quando houver, ex. 95%).
3. **Demonstrativo de parcelas**. Colunas: Data | Valor (A) | Coef. Corr. Monetária (B) | Principal corrigido (C = A × B) | Juros % (D) | Juros $ (E = C × D) | SELIC % (F) | SELIC $ (G = (C + E) × F) | Total (H = C + E + G) | Obs. ("13º salário"). Totais da parte: liquidação, outros créditos/débitos, totais, **totais após acordo**.
4. **Demonstrativo para RRA (Lei 12.350/2010)**: anos-calendário anteriores × ano atual (quantidade de meses e valor).
5. **Resumo analítico**. Colunas: (A) Benefícios devidos | (B) Benefícios recebidos | (C) Outros descontos | (D = A − (B + C)) Subtotal | (E) Saldo considerado | (F) Outros créditos | (G = E + F) Valor a liquidar | Observação.
6. **Evolução da renda** (devidos e, separadamente, "Descontar" recebidos): tipo (concessão de benefício), espécie (ex.: RMI acima do salário mínimo), DIB, RMI, início e fim das parcelas. Colunas: Data | Valor | Adicional 25% | Valor final | Obs. (fração da mensalidade, ex. "19/30", fração do 13º, ex. "4/12", "Reajuste: X%").

### 4.3 O que conferir em qualquer liquidação

- Título judicial: DIB, DIP, termo final, espécie, RMI; índice de correção e juros **exatamente** como fixados na sentença/acórdão (ou Manual da JF vigente quando o título remete a ele).
- Data de início dos juros = citação.
- Prescrição quinquenal contada do ajuizamento.
- Abatimento de valores recebidos (benefício inacumulável, revisão administrativa, complemento positivo). Conferir no HISCRE se o complemento positivo foi de fato pago.
- 13º: proporcional no ano da DIB e no ano do termo final.
- Reajustes anuais aplicados em janeiro (índice do RGPS).
- Honorários de sucumbência: percentual e base (parcelas até a sentença/acórdão).
- Acordo: aplicar o percentual sobre o total.
- RRA: separar anos anteriores e ano corrente (número de meses).

---

## 5. Checklist geral do agente conferente

1. Dados do caso batem com os documentos (CNIS, carta de concessão, título judicial).
2. Concomitâncias ajustadas no tempo e somadas no salário (limitado ao teto).
3. Indicadores do CNIS listados e com tratamento no relatório.
4. Competências abaixo do mínimo tratadas conforme o período (antes ou depois de 11/2019).
5. Regra aplicada × requisitos por sexo e por ano; descartes sem quebrar o mínimo; coeficiente correto (60% + 2% por ano acima de 20/15 anos, ou 100% nas regras que o preveem).
6. Fator previdenciário só onde a regra prevê (ou só se favorável, na PcD).
7. Correção e juros conforme o período (até 11/2021, SELIC 12/2021 a 08/2025, INPC + taxa legal a partir de 09/2025) ou conforme o título.
8. Valor da causa = vencidas + 12 vincendas (encontro de contas), teste dos 60 salários mínimos.
9. Relatório final no modelo de `pecas/relatorios/` correspondente, com conclusões-modelo e anexos.
