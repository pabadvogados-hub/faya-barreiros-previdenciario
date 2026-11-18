# POP-ATD-03 — Onboarding do cliente novo (contrato, pasta, documentos)

Versão 1 — 18/11/2026

| | |
|---|---|
| **Dono do POP** | Dra. Faya |
| **Quem executa** | Bárbara; Dra. Faya assina e define honorários |
| **Gatilho** | Cliente fechou na reunião |
| **Termina quando** | Kit assinado, pasta criada no OneDrive, card no Notion, cobrança no Asaas (se houver honorário inicial) e documentos mínimos recebidos |
| **Prazo** | Kit enviado no mesmo dia; documentos cobrados até ficarem completos (MSG-02) |

## Passo a passo

1. **Gerar o kit de representação** com os dados do cliente (`modelos/`): — *mesmo dia*
   - `01` procuração previdenciária (com o objeto da ação);
   - `02` contrato de honorários (ligar `{{#honorarios_iniciais}}` se ela cobrou a análise);
   - `03` declaração de hipossuficiência, se a inicial vai pedir gratuidade;
   - `04` termo de renúncia do JEF, **só** depois da conta do valor da causa (POP-PREV-02).
   A geração recusa documento com campo vazio ou `[A CONFIRMAR]`: corrigir antes de mandar.
2. **Assinatura** pela Tramitação Inteligente (como o escritório já faz). Integração: `automacoes/comum/tramitacao.py`
   é esqueleto; até lá, sobe à mão. — *mesmo dia*
3. **Boas-vindas** com a MSG-04: canais oficiais, o que esperar e o alerta do golpe do falso advogado. — *depois da assinatura*
4. **Pasta no OneDrive** em `CLIENTES/<NOME>` com as subpastas padrão (`automacoes/drive/criar_estrutura.py`). — *mesmo dia*
5. **Card no Notion** (cliente + caso): benefício, NB, DER, classificação da triagem, responsável. — *mesmo dia*
6. **Asaas**: só se houver honorário inicial ou parcelado (`automacoes/financeiro/nova_cobranca.py`). Honorário de
   implantação e de êxito só se cobra quando o benefício sai (POP-PREV-07). — *mesmo dia*
7. **Cobrar os documentos** do checklist do produto (`checklists/diagnostico/CK-DIAG-PREV-*`) com a MSG-02, até completar. — *D+2, D+5, D+10*

## O que vira tarefa no Notion

| Tarefa | Responsável | Prazo |
|---|---|---|
| `[ASSINATURA] Kit - {{cliente}}` | Bárbara | D+1 |
| `[DOCUMENTOS] Cobrar - {{cliente}}` | Bárbara | D+2, D+5, D+10 |
| `[CÁLCULO] {{cliente}} - {{produto}}` | Dra. Faya | 2 dias úteis após CNIS completo (POP-PREV-02) |

## Pendências

- `[A CONFIRMAR]` Se a Tramitação Inteligente tem API e como o escritório recebe o documento assinado de volta.
- `[A CONFIRMAR]` Estrutura das bases do Notion (clientes, processos, prazos, financeiro) para o conector.
