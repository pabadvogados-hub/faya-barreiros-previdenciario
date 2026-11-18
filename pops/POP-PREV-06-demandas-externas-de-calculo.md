# POP-PREV-06 — Demandas externas de cálculo e serviços avulsos (para outros advogados)

Versão 1 — 18/11/2026

| | |
|---|---|
| **Dono do POP** | Dra. Faya |
| **Quem executa** | Bárbara (entrada, prazo, cobrança); agente `calculista` (pré-apuração e conferência); Dra. Faya (cálculo e entrega) |
| **Gatilho** | Advogado parceiro pede cálculo, parecer ou serviço avulso (e-mail, WhatsApp, indicação) |
| **Termina quando** | Cálculo entregue ao parceiro **antes do prazo dele**, pago, e arquivado |
| **Prazo** | O prazo processual do parceiro menos 2 dias úteis (nunca no último dia) |

## Por que este POP existe

No briefing, a Dra. Faya declarou **inegociável o ciclo dos prazos das demandas externas de cálculos e serviços
avulsos**. Aqui o cliente é outro advogado, e o prazo é o do processo dele: atraso nosso vira prazo perdido dele.

## Ferramenta: o painel de cálculos

`automacoes/painel/` (ver `automacoes/README.md`). Tem duas portas:

- **Link de pedido** (`/pedido?t=...`), enviado aos parceiros: o advogado informa tipo, processo, **o prazo dele** e
  anexa sentença, CNIS e cálculo adverso. Recebe um protocolo `CE-AAAA-NNNN`.
- **Painel** (`/painel`, com senha): fila por prazo com semáforo, status, valor, pago/a receber, ranking de parceiros,
  ticket e tempo médio por tipo de cálculo.

## Passo a passo

1. **Entrada** — pelo link de pedido (entra sozinha) ou, se chegou por e-mail/WhatsApp, a Bárbara lança em
   "Nova demanda" no painel: parceiro, caso, tipo, **prazo processual do parceiro**, valor combinado. — *no mesmo dia*
2. **Pasta** em `DEMANDAS_EXTERNAS_CALCULO/<parceiro>/<AAAA-MM-DD - caso>` no OneDrive, separada dos clientes do
   escritório. O link de pedido já cria a pasta e guarda os anexos em `01_RECEBIDO_DO_PARCEIRO`. — *mesmo dia*
3. **Prazo**: o painel calcula o prazo interno = prazo do parceiro menos 2 dias úteis e pinta a fila (amarelo a 2
   dias úteis, vermelho depois do interno). Com `PAINEL_TAREFA_NOTION=1` vira também tarefa `[CÁLCULO EXTERNO]` no
   Notion. Pedido **sem prazo** aparece como "combinar hoje". — *mesmo dia*
4. **Conferir os documentos** em até 1 dia útil: sentença/acórdão (os critérios de correção e juros vêm do título),
   CNIS, carta de concessão, cálculo da parte contrária. Faltou: pedir ao parceiro **no mesmo dia** (o relógio é dele).
5. **Cálculo** no software, conferido pelo agente `calculista` contra o título judicial e contra
   `previdenciario/calculos/FORMATO_DOS_CALCULOS.md`. — *até o prazo interno*
6. **Entrega**: PDF do cálculo + nota técnica curta (critérios usados, divergência com o cálculo adversário). — *prazo interno*
7. **Status "ENTREGUE"** no painel (grava a data de entrega e mede a pontualidade). — *na entrega*
8. **Cobrança** pelo botão "Cobrar no Asaas" do painel (protocolo vira a referência da cobrança) e, quando pagar,
   marcar "Pago". — *na entrega*

## Regras

- Os critérios de correção e juros são **os do título** (sentença/acórdão), não os do nosso gosto. Se o título é
  omisso, a nota técnica diz qual critério foi usado e por quê.
- Demanda sem prazo informado pelo parceiro: perguntar antes de aceitar.
- Dado do cliente do parceiro tem o mesmo cuidado de LGPD que o nosso.

## Pendências

- `[A CONFIRMAR]` Tabela de preços por tipo de cálculo e se há contrato padrão com o parceiro (hoje não há modelo).
- `[A CONFIRMAR]` Qual software de cálculo o escritório usa (o formato dos relatórios está descrito em
  `previdenciario/calculos/FORMATO_DOS_CALCULOS.md`).
