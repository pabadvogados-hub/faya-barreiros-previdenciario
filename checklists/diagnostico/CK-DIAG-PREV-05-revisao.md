# CK-DIAG-PREV-05 — Revisão de benefício

Versão 1 — 18/11/2026 · Dono: Dra. Faya · Usado no POP-PREV-01 e no POP-PREV-05

**Quando usar**: aposentado ou pensionista acha que o benefício está errado. Modelos: os 9 `revisao-*`, e os
relatórios `parecer-analise-de-revisao`, `parecer-recalculo-de-rmi`, `parecer-revisao-*`, `recalculo-rmi-verba-trabalhista`.

## A. Primeiro filtro: decadência

| Pergunta | OK |
|---|---|
| Data do **primeiro pagamento** do benefício (não da concessão) | ☐ |
| Já passaram **10 anos** do dia 1º do mês seguinte ao primeiro pagamento? (art. 103 da Lei 8.213/91) | ☐ |
| Houve pedido de revisão administrativa antes (interrompe/conta de outra data)? `[CONFERIR caso a caso]` | ☐ |

> Passou dos 10 anos e não há exceção: **SEM TESE** de revisão do ato de concessão. Não seguir.

## B. Qual revisão

| Sinal no caso | Revisão possível | Modelo |
|---|---|---|
| Ganhou ação trabalhista com reflexo em salário | Inclusão de salários da RT | `revisao-inclusao-periodo-rt`, relatório `recalculo-rmi-verba-trabalhista` |
| Trabalhou em dois lugares ao mesmo tempo | Atividade concomitante (soma dos salários) | `revisao-atividade-concomitante` |
| Tinha direito a benefício melhor antes | Retroação da DIB / melhor benefício | `revisao-retroacao-dib` |
| Tempo especial não reconhecido | Conversão em especial | `revisao-conversao-aposentadoria-tempo-em-especial` |
| Aposentou depois da EC 103 mas tinha direito antes | Pós-reforma → pré-reforma | `revisao-conversao-aposentadoria-tempo-pos-reforma-para-pre-reforma` |
| Aposentadoria por incapacidade calculada pela regra nova | Regra/cálculo pré-reforma | `revisao-aposentadoria-incapacidade-*` |
| Precisa de cuidador permanente | Acréscimo de 25% | `revisao-acrescimo-adicional-25` |

## C. Documentos

- ☐ **Carta de concessão com memória de cálculo**
- ☐ CNIS com remunerações e CTPS
- ☐ Processo administrativo da concessão (cópia integral)
- ☐ Sentença e cálculos da ação trabalhista, se for o caso
- ☐ PPP/LTCAT, se a revisão envolve tempo especial
- ☐ Histórico de créditos (HISCRE)

## D. Classificação

- **VIÁVEL**: dentro do prazo, com diferença de RMI **calculada** (POP-PREV-02) que justifica a ação
- **PENDENTE DE DOCUMENTO**: falta carta de concessão, processo administrativo ou documento da tese
- **SEM TESE**: decadência, ou diferença irrelevante depois do cálculo
