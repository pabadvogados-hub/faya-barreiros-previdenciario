# MSG-06 — Benefício concedido, implantado e pagamento (RPV/precatório)

Versão 1 — 18/11/2026 · Usado no POP-PREV-07 · Só sai depois de a Dra. Faya conferir a implantação ou o cálculo

| Variável | O que é |
|---|---|
| `{{nome_cliente}}` | Primeiro nome |
| `{{beneficio}}` | O benefício concedido |
| `{{rmi}}` | Valor mensal conferido |
| `{{data_primeiro_pagamento}}` | Data informada pelo INSS |
| `{{valor_bruto}}`, `{{honorarios}}`, `{{valor_liquido}}` | Da prestação de contas (modelo `prestacao-de-contas-e-recibo`) |

## Modelo 1 — Concedido

> {{nome_cliente}}, que notícia boa: o seu {{beneficio}} foi concedido! A Dra. Faya conferiu e o valor mensal ficou em R$ {{rmi}}. O primeiro pagamento está previsto para {{data_primeiro_pagamento}}. Sobre os valores atrasados, vamos te explicar o próximo passo assim que o cálculo for conferido.

## Modelo 2 — RPV/precatório pago

> {{nome_cliente}}, o valor do seu processo foi pago. Segue a prestação de contas: valor bruto R$ {{valor_bruto}}, honorários conforme o contrato R$ {{honorarios}}, valor que fica com você R$ {{valor_liquido}}. O recibo completo vai em PDF. Qualquer dúvida, a Dra. Faya explica por ligação.

## Lembrete fixo (acrescentar nos dois)

> Lembrando: nós nunca pedimos taxa para liberar valor. Pagamento só na conta oficial do escritório.
