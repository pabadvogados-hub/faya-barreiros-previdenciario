# POP-PREV-04 — Petição inicial previdenciária e quesitos de perícia

Versão 1 — 18/11/2026

| | |
|---|---|
| **Dono do POP** | Dra. Faya |
| **Quem executa** | Agente `previdenciario` (minuta a partir do modelo dela) → estagiário(a) (anexos e índice) → Dra. Faya (revisão e protocolo) |
| **Gatilho** | Caso VIÁVEL com a via administrativa esgotada (indeferimento, cessação, recurso negado ou mora do INSS) |
| **Termina quando** | Inicial protocolada no PJe, com quesitos quando houver perícia |
| **Prazo** | Minuta em 3 dias úteis a partir do cálculo conferido |

## Pré-requisito

**Prévio requerimento administrativo** (sem indeferimento, cessação ou mora não há interesse de agir). O NB, a
DER e o motivo do indeferimento entram na inicial. Exceção: revisão de matéria só de direito, quando o modelo dela
já trata disso.

## Como a minuta nasce

1. Escolher o modelo na triagem (POP-PREV-01): `python previdenciario/pecas/gerar_peca.py listar`.
2. Ver os campos e os documentos que o modelo usa: `gerar_peca.py campos <tipo>`.
3. O agente `previdenciario` escreve a minuta **a partir do texto do modelo**, mantendo a estrutura da Dra. Faya
   (`previdenciario/dna/DNA_PECAS.md`): narra os fatos com os documentos do cliente, põe o quadro de vínculos e o
   resumo do cálculo, e deixa `[CONFERIR]` onde faltar dado. **Não acrescenta tese nem jurisprudência que o
   modelo não tenha.**
4. `gerar_peca.py conferir minuta.md` lista o que ainda falta; `gerar_peca.py docx minuta.md` põe no timbrado.
   Enquanto houver pendência, o arquivo sai com "MINUTA - NÃO PROTOCOLAR".
5. Correção pela IA (POP-OP-05) e revisão final da Dra. Faya.

## A estrutura dela (não mudar a ordem)

Endereçamento e qualificação → nome da ação → justiça gratuita → tramitação preferencial (só se cabe) →
audiência de conciliação (art. 334 do CPC) → esgotamento da via administrativa → fatos (com quadro de vínculos
e recortes do CNIS/PPP/laudos) → direito → tutela de urgência (só se houver) → valor da causa (com a conta) →
pedidos → autenticidade dos documentos → índice da instrução.

## Anexos que acompanham

- Procuração, declaração de hipossuficiência (`modelos/01` e `03`)
- **Termo de renúncia do JEF** (`modelos/04`) quando o valor da causa passar de 60 salários mínimos e a estratégia for o JEF
- Documentos na ordem do índice da instrução, com o nome do arquivo igual ao do índice

## Quesitos de perícia (incapacidade, BPC, PcD, adicional de 25%)

- Diagnóstico, data de início da doença (DID) e **data de início da incapacidade (DII)**
- Incapacidade **total ou parcial**, **temporária ou permanente**, para a **atividade habitual**
- Possibilidade de **reabilitação**, considerando idade e escolaridade
- Necessidade de **assistência permanente de terceiro** (acréscimo de 25%, art. 45 da Lei 8.213/91)
- BPC e PcD: impedimento de **longo prazo** (2 anos ou mais) e grau da deficiência (LC 142/2013)
- Acidente: **redução da capacidade** para o trabalho que exercia (auxílio-acidente)

⚠ **A DII decide os atrasados.** Quesito mal feito sobre DII custa dinheiro do cliente.

## Regra

Linguagem formal, sem emoji, no timbrado bordô da Dra. Faya. **Nenhuma inicial é protocolada sem a revisão dela.**
