# CK-DIAG-PREV-03 — Aposentadorias programadas (tempo, pontos, idade, especial, PcD, professor)

Versão 1 — 18/11/2026 · Dono: Dra. Faya · Usado no POP-PREV-01 e no POP-PREV-05 (planejamento)

**Quando usar**: segurado quer saber quando e como se aposenta, teve aposentadoria negada, ou quer converter tempo
especial. Modelos ligados: `aposentadoria-especial-ruido`, `aposentadoria-por-tempo-com-conversao`,
`aposentadoria-por-pontos-direito-adquirido`, `aposentadoria-pessoa-com-deficiencia-monocular`, `atualizacao-de-cnis`;
relatórios `planejamento-*`.

## A. Requisitos a conferir

| Requisito | Como se prova | OK |
|---|---|---|
| Data de filiação (antes ou depois de 13/11/2019 muda as regras disponíveis) | CNIS | ☐ |
| Tempo de contribuição e carência (180 meses) | CNIS, CTPS, carnês, CTC de regime próprio | ☐ |
| Direito adquirido até 13/11/2019 (tempo 30/35 ou 86/96 pontos) | Simulação `previdenciario/calculos/simular.py` + software | ☐ |
| Regras de transição da EC 103/2019 (arts. 15, 16, 17, 18, 20) e permanente | Idem | ☐ |
| **Tempo especial**: agente nocivo, intensidade e período | **PPP** e **LTCAT**; para ruído, o nível em dB e a técnica de medição | ☐ |
| Conversão especial → comum só **até 13/11/2019** | Quadro de períodos | ☐ |
| Deficiência (LC 142/2013): grau e período | Laudos; avaliação biopsicossocial; visão monocular = Lei 14.126/2021 | ☐ |
| Professor: tempo exclusivo de magistério na educação infantil, fundamental ou médio | CTPS, declaração da escola | ☐ |
| Pendências do CNIS (vínculo sem fim, remuneração faltando, indicadores) | CNIS; CTPS e holerites para corrigir | ☐ |

## B. Documentos a pedir ao cliente

- ☐ RG, CPF, comprovante de residência
- ☐ **CNIS completo** (com remunerações) e **todas as CTPS**
- ☐ Carnês e guias de contribuinte individual, se houver
- ☐ **PPP** de cada empresa com atividade especial (e LTCAT quando o PPP for omisso)
- ☐ CTC de regime próprio, se trabalhou no serviço público
- ☐ Laudos e relatórios médicos (PcD)
- ☐ Carta de indeferimento e cópia do processo administrativo, se já pediu
- ☐ Sentença trabalhista que reconheceu vínculo ou salário, se houver

## C. Pontos que derrubam o caso

- PPP sem responsável técnico pelos registros ambientais ou sem o nível do agente: não prova a especialidade.
- EPI eficaz informado no PPP (exceto ruído): discussão do Tema 555 do STF / RE 664.335 `[CONFERIR alcance atual]`.
- Contar conversão de período especial **depois** de 13/11/2019.
- Vínculo só na CTPS e fora do CNIS sem prova complementar: vira pedido de averbação, não conta direto.

## D. Classificação

- **VIÁVEL**: requisitos de alguma regra cumpridos e provados
- **PENDENTE DE DOCUMENTO**: falta PPP, CTPS ou acerto de CNIS que muda o resultado
- **SEM TESE (por ora)**: nenhuma regra cumprida → oferecer **planejamento** (POP-PREV-05) com a data provável
