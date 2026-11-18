# MSG-02 — Cobrança de documentos (cadência)

Versão 1 — 18/11/2026 · Usado no POP-ATD-03 (onboarding) e quando chega exigência do INSS (POP-OP-02)

| Variável | O que é |
|---|---|
| `{{nome_cliente}}` | Primeiro nome |
| `{{beneficio}}` | Ex.: "a sua aposentadoria", "o auxílio", "a revisão" |
| `{{lista_documentos}}` | Lista numerada do que falta (do checklist `CK-DIAG-PREV-*`) |
| `{{lista_recebidos}}` | O que já chegou |
| `{{data_limite}}` | Até quando precisamos |
| `{{nome_atendente}}` | Quem envia |

Cadência: D+2, D+5, D+10 depois do contrato. Exigência do INSS: no dia em que chega e 5 dias úteis antes do prazo.

## Modelo 1 — Primeira lista (D+2)

> Oi, {{nome_cliente}}! Aqui é {{nome_atendente}}, do escritório da Dra. Faya. Para darmos andamento a {{beneficio}}, precisamos destes documentos:
>
> {{lista_documentos}}
>
> Pode mandar foto legível ou PDF por aqui mesmo. O CNIS você baixa no aplicativo ou site Meu INSS, em "Extrato de Contribuição (CNIS)". Se tiver dificuldade, a gente te ajuda.

## Modelo 2 — Lembrete (D+5)

> {{nome_cliente}}, tudo bem? Já recebemos: {{lista_recebidos}}. Ainda faltam:
>
> {{lista_documentos}}
>
> Com eles completos a Dra. Faya já consegue fechar o cálculo.

## Modelo 3 — Último lembrete (D+10)

> {{nome_cliente}}, para não atrasar {{beneficio}}, precisamos dos documentos abaixo até {{data_limite}}:
>
> {{lista_documentos}}
>
> Se algum deles você não tem, me avisa que a gente vê outro caminho.

## Modelo 4 — Exigência do INSS (prazo correndo)

> {{nome_cliente}}, o INSS pediu um documento no seu processo e existe prazo para entregar: {{data_limite}}. Precisamos de:
>
> {{lista_documentos}}
>
> Consegue mandar até {{data_limite}}? Se o prazo passar, o INSS pode encerrar o pedido.

## Dicas por documento

| Documento | Onde o cliente consegue |
|---|---|
| CNIS | Meu INSS > Extrato de Contribuição (CNIS) |
| Carta de indeferimento / concessão | Meu INSS > Consultar pedidos |
| PPP | RH da empresa (obrigação dela entregar) |
| Laudos | Médico assistente; pedir com **CID e data de início** |
| HISCRE | Meu INSS > Extrato de pagamento / histórico de créditos |
