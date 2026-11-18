# POP-OP-02 — Controladoria: intimações, prazos do INSS e do Judiciário

Versão 1 — 18/11/2026

| | |
|---|---|
| **Dono do POP** | Dra. Faya |
| **Quem executa** | Bárbara (agenda de prazos); estagiário(a) (pushs processuais e baixa de decisões); Dra. Faya confirma a classificação de decisão, sentença e laudo |
| **Gatilho** | Todo dia útil, 8h (publicações do DJEN, pushs do PJe, Meu INSS, e-mail) |
| **Termina quando** | Toda intimação do dia classificada, com prazo e tarefa no Notion e o cliente avisado quando for o caso |
| **Prazo** | Leitura até 9h30; tarefas criadas até 12h |

## Objetivo

Nenhum prazo perdido — nem do processo judicial, nem das **demandas externas de cálculo**, cujo ciclo de prazos a
Dra. Faya declarou **inegociável**. Em previdenciário há três fontes de prazo, e as três entram aqui.

## As três fontes

| Fonte | Onde aparece | Exemplos |
|---|---|---|
| **Judicial** | DJEN (OAB/BA 64.723 e OAB/SP 308.385), pushs do PJe (TRF1 / JEF da Seção Judiciária da Bahia; Justiça Estadual nas acidentárias) | Perícia designada, laudo juntado, sentença, cálculo do INSS para impugnar, RPV expedida |
| **Administrativa (INSS)** | Meu INSS do cliente, carta pelos Correios | Carta de exigência, indeferimento, cessação, convocação para perícia, decisão da Junta de Recursos |
| **Demandas externas de cálculo** | E-mail/WhatsApp do advogado parceiro | Prazo que o parceiro tem no processo dele (POP-PREV-06) |

## O que a automação faz e o que a pessoa faz

| A automação faz (`automacoes/controladoria/`) | A pessoa faz |
|---|---|
| Lê o DJEN pelas OABs do `config/escritorio.json` e classifica cada publicação | Confere se não sobrou publicação sem classificação |
| Calcula o prazo e propõe a tarefa no Notion (dry-run; `--go` só com o "pode") | Confere responsável e data |
| Gera o relatório do dia | Lê e fecha o dia |

O INSS e as demandas externas **não** chegam pelo DJEN: Bárbara lança à mão no Notion, no mesmo dia em que chegam.

## Classificação e prazo — previdenciário

| O que chegou | Prazo | Quem |
|---|---|---|
| **Carta de exigência do INSS** | O prazo da própria carta (em regra 30 dias) `[CONFERIR na carta]` | Bárbara pede o documento ao cliente (MSG-02); Dra. Faya responde |
| **Indeferimento ou cessação** | Recurso à Junta de Recursos (CRPS): **30 dias** da ciência | Dra. Faya decide: recurso (POP-PREV-03), novo pedido ou ação (POP-PREV-04) |
| **Perícia médica ou social designada** (INSS ou judicial) | Data da perícia | Avisar o cliente (MSG-03); quesitos e assistente técnico, se houver prazo aberto |
| **Laudo pericial juntado** | Manifestação: prazo do despacho (no JEF costuma ser 5 a 10 dias) `[CONFERIR no despacho]` | Dra. Faya |
| **Sentença no JEF** | Recurso inominado: **10 dias úteis** (Lei 9.099/95, arts. 42 e 12-A, c/c Lei 10.259/2001, art. 1º); embargos de declaração: **5 dias** | Dra. Faya |
| **Acórdão da Turma Recursal** | Pedido de uniformização (Lei 10.259/2001, art. 14) e recurso extraordinário: **15 dias** `[CONFERIR regimento da TNU/TRU]` | Dra. Faya |
| **Sentença na Vara Federal / Estadual** | Apelação: **15 dias úteis** (CPC, arts. 1.003, § 5º, e 219); embargos: 5 dias úteis | Dra. Faya |
| **Decisão interlocutória (Vara)** | Agravo de instrumento: 15 dias úteis, se no rol do art. 1.015 do CPC | Dra. Faya |
| **Cálculo do INSS / contadoria para manifestar** | Prazo do despacho | Dra. Faya confere com o cálculo do escritório (POP-PREV-07) |
| **RPV/precatório expedido ou pago** | Sem prazo processual; aviso ao cliente e cobrança dos honorários | POP-PREV-07 |
| **Mero andamento** (conclusão, remessa, juntada) | Sem prazo | Só registra |

Na dúvida sobre a classificação: **tratar como prazo** e pedir a confirmação da Dra. Faya no mesmo dia.

## Como contar

1. Judicial: **dias úteis** (CPC, art. 219; no JEF, Lei 9.099/95, art. 12-A). Exclui o dia do começo, inclui o do vencimento (CPC, art. 224).
2. DJEN: publicação no 1º dia útil seguinte à disponibilização; o prazo começa no 1º dia útil seguinte à publicação (CPC, art. 224, §§ 2º e 3º).
3. Intimação pelo sistema: no dia da consulta; sem consulta, 10 dias corridos após o envio (Lei 11.419/2006, art. 5º, § 3º).
4. **O INSS tem prazo em dobro** (CPC, art. 183); **o segurado não**. No JEF não há prazo diferenciado para a Fazenda (Lei 10.259/2001, art. 9º).
5. Recesso de 20/12 a 20/01 suspende os prazos judiciais (CPC, art. 220). **Não suspende** prazo administrativo do INSS.
6. Feriados: calendário do TRF1 e da Justiça Federal na Bahia; 2 de julho (Independência da Bahia) e feriados municipais de Salvador `[CONFERIR lista do ano em automacoes/controladoria/feriados_locais.json]`.
7. Registrar no Notion **o prazo fatal e o prazo interno** (fatal menos 2 dias úteis para a peça pronta).

## O que vira tarefa no Notion

| Tarefa | Responsável | Prazo |
|---|---|---|
| `[PRAZO] {{peça}} - {{cliente}} - {{processo}}` | Dra. Faya | Prazo interno (fatal anotado) |
| `[EXIGÊNCIA INSS] {{cliente}} - NB {{nb}}` | Dra. Faya | Prazo da carta menos 5 dias úteis |
| `[PERÍCIA] {{cliente}} - {{data}}` | Bárbara avisa o cliente | 5 dias úteis antes da perícia |
| `[CÁLCULO EXTERNO] {{parceiro}} - {{caso}}` | Dra. Faya | Prazo do parceiro menos 2 dias úteis |
| `[AVISAR CLIENTE] {{assunto}}` | Bárbara | 1 dia útil |

## Onde salva

- Ato processual: `CLIENTES/{{cliente}}/08_PROCESSO_JUDICIAL/AAAA-MM-DD_{{tipo}}.pdf`
- Carta do INSS: `CLIENTES/{{cliente}}/05_INSS_ADMINISTRATIVO/AAAA-MM-DD_{{tipo}}.pdf`
- Relatório do dia: `00_ESCRITORIO/CONTROLADORIA/AAAA-MM/AAAA-MM-DD_relatorio.md`

## Pendências

- `[A CONFIRMAR]` Se a Tramitação Inteligente já entrega os andamentos (aí ela vira a fonte principal e o DJEN a conferência).
- `[A CONFIRMAR]` Quantos processos ativos e em quais tribunais (TRF1, TJBA, TRF3 pela OAB/SP).
