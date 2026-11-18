# POP-PREV-05 — Relatórios, pareceres e planejamento previdenciário

Versão 1 — 18/11/2026

| | |
|---|---|
| **Dono do POP** | Dra. Faya |
| **Quem executa** | Agente `calculista` (minuta do relatório no modelo dela) → Dra. Faya (cálculo oficial, revisão e assinatura) |
| **Gatilho** | Cliente contratou análise, parecer ou planejamento; ou a triagem pediu parecer antes de decidir a ação |
| **Termina quando** | Relatório assinado entregue ao cliente (e, se houver proposta, honorários registrados) |
| **Prazo** | `[A CONFIRMAR com a Dra. Faya]` — sugestão: 5 dias úteis a partir dos documentos completos |

## Objetivo

O relatório é produto do escritório, não só documento interno: é o que o cliente leva para casa e o que
justifica a contratação da ação. A Dra. Faya tem **14 modelos** prontos (`previdenciario/pecas/relatorios/`),
todos com a mesma espinha: dados do segurado → metodologia → vínculos → indicadores do CNIS → conferência de
tempo → RMI/coeficiente/fator → conclusão → honorários.

## Qual modelo usar

| Situação do cliente | Modelo |
|---|---|
| "Quando posso me aposentar e com quanto?" | `planejamento-previdenciario` (com conversões, se tem tempo especial; `planejamento-professor` para professor) |
| "Vale a pena entrar com a ação?" | `parecer-viabilidade` |
| Análise geral do histórico | `analise-previdenciaria` |
| Já aposentado: dá para revisar? | `parecer-analise-de-revisao`, `parecer-revisao-tempo-especial`, `parecer-revisao-pcd`, `parecer-recalculo-de-rmi` |
| Auxílio com RMI suspeita | `conferencia-rmi-auxilio` |
| Contribuiu acima do teto | `contribuicoes-acima-do-teto` |
| Ganhou trabalhista e o salário mudou | `recalculo-rmi-verba-trabalhista` |
| Fase de execução | `parecer-liquidacao` (POP-PREV-07) |
| Pagamento recebido | `prestacao-de-contas-e-recibo` (POP-PREV-07) |

Nomes exatos: `python previdenciario/pecas/gerar_peca.py listar`.

## Passo a passo

1. **Documentos completos** (checklist do produto) e **cálculo oficial** feito (POP-PREV-02). — *antes de escrever*
2. O agente `calculista` preenche o modelo: dados, quadro de vínculos, indicadores, conferência de tempo
   (INSS x escritório) e o texto técnico que o modelo já traz. Números só do cálculo oficial; o que faltar,
   `[CONFERIR]`. — *1 dia útil*
3. Cenários do planejamento: a tabela regra x data x coeficiente pode ser **pré-montada** com
   `previdenciario/calculos/simular.py` e conferida contra o software. — *junto com o passo 2*
4. `gerar_peca.py conferir` e `gerar_peca.py docx` (timbrado). — *mesmo dia*
5. **Revisão e assinatura** da Dra. Faya. — *até o prazo*
6. Entrega ao cliente com explicação simples (reunião ou áudio), e registro no Notion. Se o relatório traz
   proposta de honorários, ela entra no contrato (`modelos/02`). — *na entrega*

## Regras

- **Todo número com fonte** (CNIS, carta de concessão, PPP, planilha).
- Planejamento fala em **cenários**, nunca em garantia: a lei pode mudar e o INSS pode divergir.
- Divergência entre o tempo do INSS e o do escritório **é o coração do relatório**: sempre em quadro.
