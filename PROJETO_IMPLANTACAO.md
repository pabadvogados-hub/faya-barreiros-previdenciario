# Projeto de Implantação — Faya Barreiros Advocacia (previdenciário e cálculos)

Pacote no formato Casal da IA (o mesmo da Laís Torres & Alex Brunno e da SPDAG), montado em 18/11/2026 a partir do
briefing de 18/10/2026 e do material que a Dra. Faya enviou. O que já existia do sistema de outubro (repositório
`faya-barreiros-advocacia`) foi reaproveitado: timbrado, kit de representação, DNA das peças, política de honorários.

## 1. O que o escritório é e onde dói

Sociedade individual em Salvador/BA, previdenciário e **cálculos**, com a Dra. Faya fazendo quase tudo, uma
secretária e um estagiário. O que pesa:

- **Tudo passa pela Dra. Faya**: triagem, cálculo, peça, revisão, relatório. A implantação tira dela o trabalho
  repetitivo e entrega minuta pronta para revisar.
- **Cálculo** é o produto dela, para clientes e para outros advogados, com **prazo de terceiros** (inegociável).
- **CNIS lido à mão** e regras da EC 103/2019 comparadas caso a caso.
- **27 modelos de inicial e 15 de relatório** soltos em Word: viram biblioteca com campos, estrutura e citações.
- **Prazos em três fontes** (Judiciário, INSS, parceiros) num Notion sem integração.

## 2. Os módulos, na ordem de implantação

### Módulo 1 — Biblioteca de peças e relatórios no padrão dela
Os modelos dela anonimizados em `previdenciario/pecas/`, o DNA (`previdenciario/dna/`), o gerador no timbrado
(`gerar_peca.py`) e os agentes `previdenciario` e `calculista`. POPs: PREV-04, PREV-05, OP-05.
**Pronto para uso** com Claude Code; depende só da revisão dela nos `[CONFERIR]` herdados dos originais.

### Módulo 2 — Triagem e cálculo
Checklists por produto, triagem pelo agente, calculadora de apoio (`previdenciario/calculos/`) e base de leis
(`previdenciario/leis/`). POPs: PREV-01, PREV-02. **Pronto**; calibrar a calculadora contra 3 cálculos reais do
software dela.

### Módulo 3 — Demandas externas de cálculo
Entrada, prazo (parceiro − 2 dias úteis), pasta separada, entrega e cobrança. POP-PREV-06.
**Painel de cálculos pronto e testado** (`automacoes/painel/`): fila por prazo com semáforo, faturado/a receber,
ranking de parceiros, ticket e tempo médio por tipo, e o **link de pedido** para os advogados parceiros (com
protocolo e anexos direto na pasta). Para parceiro externo usar o link, precisa da VPS com HTTPS e um subdomínio.
Falta a tabela de preços.

### Módulo 4 — Controladoria
DJEN pelas duas OABs, classificação previdenciária, prazo e tarefa no Notion. POP-OP-02,
`automacoes/controladoria/`. **Depende** do token e das bases do Notion.

### Módulo 5 — Atendimento e onboarding
Kit de representação em `{{campos}}`, mensagens, pasta padrão no OneDrive. POPs ATD-01 a 03. **Pronto**; assinatura
segue manual na Tramitação Inteligente até haver API.

### Módulo 6 — Financeiro e honorários
Asaas (régua de cobrança própria, honorários iniciais, demandas externas), implantação/RPV/prestação de contas.
POP-PREV-07, POP-ADM-02, `automacoes/financeiro/`. **Depende** da chave do Asaas.

### Módulo 7 — Nuvem
VPS com o pacote, OneDrive montado por rclone, rotinas agendadas (controladoria 8h, régua de cobrança).

## 3. O que precisamos da Dra. Faya

| Item | Por quê |
|---|---|
| **Revisar os `[CONFERIR]` dos modelos** (lista em `previdenciario/pecas/00_INDICE.md`) | Alguns erros já estavam nos originais (lei citada errada, trecho de outro caso) |
| Estado civil dela (solteira x casada) | Vai na procuração e no contrato |
| Token de integração do **Notion** + quais bases (clientes, processos, prazos, financeiro) e colunas | Ligar controladoria, triagem e onboarding |
| Se a **Tramitação Inteligente** tem API | Assinatura e andamentos automáticos |
| Chave do **Asaas** | Cobrança e régua |
| Acesso ao **OneDrive** (pasta raiz) | Pastas de cliente e documentos |
| **Software de cálculo** que usa e 3 cálculos reais | Calibrar a calculadora de apoio e o agente `calculista` |
| Tabela de preços das demandas externas e prazo-padrão dos relatórios | POP-PREV-05 e 06 |
| Número oficial de WhatsApp e e-mail de atendimento | Mensagens e contrato (canais oficiais) |
| Nome do(a) estagiário(a) | POPs |
| Chave da API da Anthropic ou plano do Claude da equipe | Rodar os agentes |

## 4. Pendências abertas

- [ ] `[CONFERIR]` dos modelos revisados pela Dra. Faya
- [ ] Conector do Notion testado no workspace dela
- [ ] Tramitação Inteligente: API ou fluxo manual definitivo
- [ ] IN PRES/INSS 128/2022 consolidada (a base tem a redação original de 2022; alterações posteriores não entraram)
- [ ] Calculadora de apoio calibrada contra cálculos reais
- [ ] Feriados municipais de Salvador conferidos para o ano
- [ ] VPS e rotinas agendadas
