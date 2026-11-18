# MSG-03 — Perícia médica ou avaliação social marcada

Versão 1 — 18/11/2026 · Usado no POP-ATD-01 e no POP-OP-02 · Enviar no dia em que a perícia é marcada e de novo 2 dias antes

| Variável | O que é |
|---|---|
| `{{nome_cliente}}` | Primeiro nome |
| `{{tipo_pericia}}` | "perícia médica do INSS", "perícia médica judicial", "avaliação social" |
| `{{data_hora}}`, `{{local}}` | Data, hora e endereço |
| `{{lista_levar}}` | Documentos a levar (padrão abaixo) |

## Modelo 1 — Aviso

> Oi, {{nome_cliente}}! Foi marcada a sua {{tipo_pericia}}: {{data_hora}}, em {{local}}. Chegue com 30 minutos de antecedência e leve:
>
> {{lista_levar}}
>
> Na perícia, conte com sinceridade o que você sente no dia a dia e o que deixou de conseguir fazer no trabalho e em casa. Não aumente nem diminua. Qualquer dúvida, fale com a gente antes.

## Modelo 2 — Lembrete (2 dias antes)

> {{nome_cliente}}, lembrete: sua {{tipo_pericia}} é {{data_hora}}, em {{local}}. Separou os documentos? Se não puder ir, avise a gente **antes**, porque faltar sem justificativa pode encerrar o pedido.

## O que levar (padrão)

1. Documento com foto
2. Todos os laudos, exames e receitas, **originais**, em ordem de data
3. Relatório do médico assistente dizendo desde quando não pode trabalhar
4. CTPS
5. Na avaliação social (BPC): comprovantes de renda e de despesas da casa, e a folha-resumo do CadÚnico
