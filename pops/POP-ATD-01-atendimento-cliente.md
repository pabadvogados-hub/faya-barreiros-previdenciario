# POP-ATD-01 — Atendimento do cliente (andamento, documento, dúvida)

Versão 1 — 18/11/2026

| | |
|---|---|
| **Dono do POP** | Dra. Faya |
| **Quem executa** | Bárbara (secretária); estagiário(a) no andamento processual; Dra. Faya quando houver decisão jurídica |
| **Gatilho** | Cliente manda mensagem no WhatsApp do escritório, e-mail ou liga |
| **Termina quando** | O cliente recebeu resposta, a demanda está registrada no Notion e o arquivo está na pasta dele no OneDrive |
| **Prazo** | Primeira resposta no mesmo dia útil, dentro do horário comercial (9h–18h, como diz o contrato) |

## Objetivo

Cliente previdenciário pergunta sempre as mesmas três coisas: "saiu meu benefício?", "quando
recebo?" e "o que falta?". Este POP dá resposta rápida e correta sem a Dra. Faya parar o que está
fazendo, e sem prometer o que não depende do escritório (INSS, perícia, juiz).

## O que a automação faz e o que a pessoa faz

| A automação faz | A pessoa faz |
|---|---|
| Agente `atendimento` lê o andamento no Notion e o último ato do processo e propõe a resposta em linguagem simples (MSG-01) | Bárbara confere e envia |
| `automacoes/drive/arquivar_documento.py` guarda o arquivo recebido na pasta certa do cliente e abre a tarefa no Notion | Confere se o arquivo foi para a pasta certa |
| Agente `previdenciario` explica uma decisão ou exigência do INSS em rascunho | Dra. Faya aprova antes de ir ao cliente |

## Passo a passo

1. **Identificar o cliente e o caso** (nome, CPF ou nº do processo/NB) e abrir o card dele no Notion. — *na hora*
2. **Classificar o pedido:**

   | Tipo | Exemplo | Quem responde |
   |---|---|---|
   | A. Andamento | "Saiu alguma coisa?", "Como está meu processo?" | Bárbara, com o texto do agente (MSG-01). Se o ato for **decisão, sentença ou laudo pericial**, a Dra. Faya libera a explicação antes |
   | B. Perícia marcada | "Recebi a data da perícia" | Bárbara confirma data, local e o que levar (MSG-03) e lança o prazo (POP-OP-02) |
   | C. Documento | Cliente manda CNIS, laudo, carta do INSS | Bárbara arquiva (passo 4) e agradece |
   | D. Exigência do INSS | "Chegou uma carta pedindo documento" | Vira **prazo** na controladoria no mesmo dia (POP-OP-02) |
   | E. Valores | "Quando recebo?", "Quanto vou receber?" | Só a Dra. Faya fala de valor e de data de pagamento (RPV/precatório: POP-PREV-07) |
   | F. Dúvida jurídica nova | "E se eu continuar trabalhando?", "Tenho direito a outro benefício?" | Dra. Faya; pode virar caso novo (POP-PREV-01) |

3. **Responder.** Nunca prometer data do INSS, da perícia ou do juiz. Nunca falar valor de atrasados
   antes do cálculo conferido (POP-PREV-02). — *mesmo dia útil*
4. **Arquivar o que chegou** na pasta do cliente (`automacoes/drive/ESTRUTURA_PASTAS.md`): CNIS em
   `02_CNIS_E_VINCULOS`, laudo em `04_SAUDE`, carta do INSS em `05_INSS_ADMINISTRATIVO`. — *mesmo dia*
5. **Registrar no Notion** o que foi pedido, o que foi respondido e, se houver, a tarefa com prazo. — *mesmo dia*

## Regras

- **Senha do Meu INSS:** o cliente se compromete, no contrato (Cláusula Quinta, "c"), a não trocar a senha
  sem avisar. Se trocou, pedir a nova pelo canal oficial e registrar no Notion (nunca em grupo de WhatsApp).
- **Golpe do falso advogado:** se o cliente relatar cobrança ou pedido de "taxa para liberar o benefício",
  responder na hora que é fraude (Cláusula Quarta do contrato) e avisar a Dra. Faya.
- Dado de saúde do cliente não vai em mensagem para terceiros nem em grupo.

## O que vira tarefa no Notion

| Tarefa | Responsável | Prazo |
|---|---|---|
| `[RETORNO] {{cliente}} - {{assunto}}` | Quem vai responder | Mesmo dia |
| `[DOCUMENTO] Recebido - {{cliente}}` | Bárbara | Mesmo dia |
| `[EXIGÊNCIA INSS] {{cliente}} - NB {{nb}}` | Dra. Faya | Prazo da carta menos 5 dias úteis |

## Pendências deste POP

- `[A CONFIRMAR]` Número oficial de WhatsApp de atendimento (hoje o (71) 99981-1108 é o da Dra. Faya).
- `[A CONFIRMAR]` Se o estagiário responde cliente diretamente ou só a Bárbara.
