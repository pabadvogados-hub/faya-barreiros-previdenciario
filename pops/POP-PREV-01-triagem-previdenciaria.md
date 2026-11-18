# POP-PREV-01 — Triagem previdenciária do caso novo

Versão 1 — 18/11/2026

| | |
|---|---|
| **Dono do POP** | Dra. Faya |
| **Quem executa** | Bárbara (coleta) → agente `previdenciario` (triagem) → Dra. Faya (decisão) |
| **Gatilho** | Caso novo chega pelo WhatsApp, Instagram, indicação ou na reunião |
| **Termina quando** | Caso classificado como **VIÁVEL**, **PENDENTE DE DOCUMENTO** ou **SEM TESE**, com a decisão registrada no Notion |
| **Prazo** | Triagem no mesmo dia útil em que o CNIS chega; decisão em até 1 dia útil |

## Objetivo

Separar cedo o caso que tem tese do que não tem, e já escolher **o modelo de peça certo** entre os 27 que a
Dra. Faya usa (`previdenciario/pecas/iniciais/`). A carta de indeferimento do INSS quase sempre diz onde está
o problema: ela é lida antes de qualquer opinião.

## Passo 1 — Perguntas de entrada (sem exceção)

1. Qual benefício quer, perdeu ou quer revisar?
2. **Já pediu no INSS?** Número (NB/protocolo) e data (DER)?
3. **Foi negado ou cessado?** Qual o motivo escrito na carta?
4. Tem o **CNIS** e acesso ao Meu INSS?
5. Já teve advogado neste caso? Há processo em andamento?
6. Idade, cidade e profissão (atividade habitual).

> Sem 1, 2 e 3 a triagem não começa: são elas que dizem se o caminho é novo pedido, recurso ao CRPS ou ação.
> Em **revisão**, a pergunta 2 vira "qual a data do **primeiro pagamento**?" (decadência de 10 anos, art. 103 da Lei 8.213/91).

## Passo 2 — Documentos por produto

| Produto | Checklist | Modelos de inicial ligados |
|---|---|---|
| BPC/LOAS | `CK-DIAG-PREV-01-bpc-loas.md` | `bpc-deficiente` |
| Incapacidade (auxílio, aposentadoria, adicional de 25%, auxílio-acidente) | `CK-DIAG-PREV-02-incapacidade.md` | `auxilio-doenca`, `auxilio-doenca-fibromialgia`, `aposentadoria-por-incapacidade-*`, `auxilio-acidente` |
| Aposentadorias programadas (tempo, pontos, especial, PcD, professor) | `CK-DIAG-PREV-03-aposentadorias.md` | `aposentadoria-especial-ruido`, `aposentadoria-por-tempo-com-conversao`, `aposentadoria-por-pontos-*`, `aposentadoria-pessoa-com-deficiencia-*`, `atualizacao-de-cnis` |
| Pensão por morte | `CK-DIAG-PREV-04-pensao-por-morte.md` | `pensao-por-morte-uniao-estavel`, `pensao-por-morte-filho-maior-invalido` |
| Revisão de benefício | `CK-DIAG-PREV-05-revisao.md` | os 9 modelos `revisao-*` |
| Descontos, RMC, IR, contribuição acima do teto | `CK-DIAG-PREV-06-descontos-e-restituicoes.md` | `devolucao-rmc`, `suspensao-descontos-indevidos`, `isencao-de-ir`, `devolucao-de-inss-acima-do-teto` |

Os nomes exatos dos modelos: `python previdenciario/pecas/gerar_peca.py listar`.

## Passo 3 — O que o agente devolve

- Benefício pretendido e **requisitos** (qualidade de segurado, carência, idade, tempo, incapacidade,
  deficiência, miserabilidade, dependência, conforme o caso), com o artigo de lei (base em `previdenciario/leis/`)
- O que **já está provado** e o que **falta**, com o documento que resolve cada lacuna
- Se houve indeferimento: o motivo do INSS e se ele se sustenta
- **Simulação de apoio** quando for aposentadoria: `python previdenciario/calculos/simular.py caso.json`
  (regras da EC 103/2019; não substitui o cálculo do POP-PREV-02)
- Caminho sugerido: **novo requerimento**, **recurso ao CRPS** (POP-PREV-03), **ação** (POP-PREV-04) ou
  **planejamento** (POP-PREV-05), e o **modelo de peça** que se aplica
- Classificação: VIÁVEL · PENDENTE DE DOCUMENTO · SEM TESE

⚠ **O agente não decide o caso.** Quem decide é a Dra. Faya.

## Passo 4 — Registro

| Onde | O quê |
|---|---|
| Notion | Cliente e caso, com produto, classificação e modelo sugerido |
| OneDrive | Pasta do cliente com o que chegou (`automacoes/drive/ESTRUTURA_PASTAS.md`) |
| Tarefa | `[TRIAGEM] Decidir caso - {{cliente}} - {{produto}}`, Dra. Faya, D+1 |

## Erros que este POP existe para evitar

- Abrir caso sem ler a carta de indeferimento e descobrir depois que faltava um documento simples.
- Revisão proposta depois de passados os 10 anos do primeiro pagamento.
- Calcular RMI antes de saber se há qualidade de segurado.
- Prometer prazo ou valor na triagem.
