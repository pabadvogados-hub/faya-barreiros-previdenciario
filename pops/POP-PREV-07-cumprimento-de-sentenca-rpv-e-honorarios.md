# POP-PREV-07 — Implantação, liquidação, RPV/precatório e honorários

Versão 1 — 18/11/2026

| | |
|---|---|
| **Dono do POP** | Dra. Faya |
| **Quem executa** | Controladoria (prazos); Dra. Faya (conferência do cálculo); Bárbara (aviso ao cliente, recibo, cobrança) |
| **Gatilho** | Benefício concedido (administrativo ou judicial), sentença transitada, cálculo do INSS/contadoria juntado, RPV ou precatório expedido |
| **Termina quando** | Benefício implantado, valores levantados, honorários recebidos e prestação de contas entregue ao cliente |

## As quatro etapas

| Etapa | O que fazer | Quem |
|---|---|---|
| **1. Implantação** | Conferir no Meu INSS se o benefício foi implantado com a DIB e a RMI certas. RMI menor que a calculada: modelo `conferencia-rmi-auxilio` ou impugnação | Dra. Faya |
| **2. Liquidação** | Conferir o cálculo do INSS ou da contadoria contra o título e o nosso cálculo (modelo `parecer-liquidacao`); impugnar no prazo (POP-OP-02) | Dra. Faya + agente `calculista` |
| **3. RPV/precatório** | Pedir o **destaque dos honorários contratuais** (art. 22, § 4º, da Lei 8.906/94, autorizado na Cláusula Oitava, § 3º, do contrato), acompanhar a expedição e o pagamento | Dra. Faya |
| **4. Prestação de contas** | Recibo e demonstrativo ao cliente (modelo `prestacao-de-contas-e-recibo`): valor bruto, honorários de êxito, implantação, valor líquido | Bárbara prepara, Dra. Faya assina |

## Honorários (contrato `modelos/02`)

- **Implantação:** o número de salários de benefício do contrato (política atual: 4), sobre a RMI calculada pelo INSS.
- **Êxito:** o percentual do contrato (política atual: 30%) sobre os retroativos, inclusive RPV e precatório.
- **Não pagos no vencimento:** desconto autorizado de até 30% do líquido mensal (Cláusula Terceira). Usar com
  parcimônia e sempre com recibo de cada desconto (§ 3º).
- Cobrança do saldo: Asaas (`automacoes/financeiro/`), régua da MSG-07.

## Avisos ao cliente

- Benefício concedido / implantado: MSG-06, **sem falar valor de atrasado antes da conferência**.
- RPV paga: MSG-06 com a prestação de contas anexa.
- Lembrar sempre: o escritório **nunca pede taxa para liberar valor** (Cláusula Quarta do contrato).

## Regras

- O cálculo do INSS **sempre** é conferido. Aceitar sem conferir é perder dinheiro do cliente e honorário.
- Renúncia ao excedente da RPV (para receber mais rápido) é decisão do cliente, por escrito, **separada** do
  termo de renúncia do JEF (`modelos/04` diz isso expressamente).
