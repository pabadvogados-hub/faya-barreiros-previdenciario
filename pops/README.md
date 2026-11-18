# POPs — Faya Barreiros Advocacia (previdenciário e cálculos)

Versão 1 — 18/11/2026. Cada POP diz **quem faz, em quanto tempo, o que a automação faz e o que a pessoa faz, o que
vira tarefa no Notion e onde o arquivo fica no OneDrive**. Onde aparecer `[A CONFIRMAR]`, a informação depende da
Dra. Faya: não preencha por conta própria.

## Índice

| Código | POP | Dono | Quem executa |
|---|---|---|---|
| ATD-01 | [Atendimento do cliente](POP-ATD-01-atendimento-cliente.md) | Dra. Faya | Bárbara |
| ATD-02 | [Lead previdenciário](POP-ATD-02-lead-previdenciario.md) | Dra. Faya | Bárbara + Dra. Faya |
| ATD-03 | [Onboarding do cliente novo](POP-ATD-03-onboarding-cliente-novo.md) | Dra. Faya | Bárbara |
| PREV-01 | [Triagem previdenciária](POP-PREV-01-triagem-previdenciaria.md) | Dra. Faya | Agente `previdenciario` + Dra. Faya |
| PREV-02 | [CNIS e cálculo](POP-PREV-02-analise-cnis-e-calculo.md) | Dra. Faya | Agente `calculista` + Dra. Faya |
| PREV-03 | [Recurso ao CRPS](POP-PREV-03-recurso-ao-crps.md) | Dra. Faya | Agente `previdenciario` + Dra. Faya |
| PREV-04 | [Petição inicial e perícia](POP-PREV-04-peticao-inicial-e-pericia.md) | Dra. Faya | Agente `previdenciario` + estagiário(a) + Dra. Faya |
| PREV-05 | [Relatórios, pareceres e planejamento](POP-PREV-05-relatorios-pareceres-e-planejamento.md) | Dra. Faya | Agente `calculista` + Dra. Faya |
| PREV-06 | [Demandas externas de cálculo](POP-PREV-06-demandas-externas-de-calculo.md) | Dra. Faya | Bárbara + agente `calculista` + Dra. Faya |
| PREV-07 | [Implantação, liquidação, RPV e honorários](POP-PREV-07-cumprimento-de-sentenca-rpv-e-honorarios.md) | Dra. Faya | Controladoria + Dra. Faya + Bárbara |
| OP-02 | [Controladoria: intimações e prazos](POP-OP-02-controladoria-intimacoes.md) | Dra. Faya | Bárbara + estagiário(a) |
| OP-05 | [Correção de peças](POP-OP-05-correcao-de-pecas.md) | Dra. Faya | IA + Dra. Faya |
| ADM-02 | [Pagamento mensal](POP-ADM-02-pagamento-mensal.md) | Dra. Faya | Agente `financeiro` + Dra. Faya |

**Checklists:** `checklists/diagnostico/CK-DIAG-PREV-01` a `06` (um por produto) e `checklists/dia-a-dia/CK-DIA-01`
(conferência antes do protocolo). **Mensagens:** `mensagens/MSG-01` a `07`.

## O caminho de um caso

```
Lead (ATD-02) → reunião → contrato (ATD-03) → triagem (PREV-01) → CNIS e cálculo (PREV-02)
   → relatório/planejamento (PREV-05)  ou  recurso CRPS (PREV-03)  ou  inicial (PREV-04)
   → correção (OP-05) → protocolo → controladoria (OP-02) → implantação/RPV/honorários (PREV-07)
Paralelo, com prazo inegociável: demandas externas de cálculo (PREV-06)
```

## Regras que valem para todos os POPs

1. **A Dra. Faya revisa tudo antes de sair.** A IA entrega minuta. A exceção do briefing (IA decide sozinha em caso
   simples e em petição de andamento) **não está ligada**.
2. **Nada inventado.** Dado que não veio de documento fica `[CONFERIR]` ou `[A CONFIRMAR]` e trava a geração.
3. **Cálculo não se estima.** Número sai do CNIS e do software, com fonte.
4. **Documento mora no OneDrive; no Notion vai o caminho.** Estrutura: `automacoes/drive/ESTRUTURA_PASTAS.md`.
5. Jurisprudência: só a que já está nos modelos dela (`previdenciario/dna/DNA_PECAS.md`), marcada para conferência.
6. Linguagem formal nas peças, sem emoji; com o cliente, simples e cordial, sem prometer data do INSS ou do juiz.

## Equipe e papéis

| Pessoa | Papel nos POPs |
|---|---|
| **Dra. Faya Milla M. M. Barreiros** (OAB/BA 64.723 e OAB/SP 308.385) | Titular. Decide, calcula, revisa e assina tudo |
| **Bárbara** (secretária) | E-mails, agenda de prazos, recibos, pastas, primeiro contato, cobrança de documentos |
| **Estagiário(a)** `[A CONFIRMAR nome]` | Minuta de petição, pushs processuais, baixa de decisões; só muda status de demanda |

O **Dr. William Ricardo Coelho** (tributário) atende à parte e não faz parte deste pacote. Lead tributário é
encaminhado a ele.

## Pendências gerais `[A CONFIRMAR]`

- Bases do Notion (clientes, processos, prazos, financeiro) e nomes das colunas, para ligar o conector.
- Se a Tramitação Inteligente tem API (assinatura e andamentos).
- Número oficial de WhatsApp de atendimento e e-mail oficial.
- Software de cálculo usado e tabela de preço das demandas externas.
- Nome do(a) estagiário(a).
