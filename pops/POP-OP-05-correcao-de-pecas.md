# POP-OP-05 — Correção de peças (primeira correção pela IA, revisão final da Dra. Faya)

Versão 1 — 16/11/2026

| | |
|---|---|
| **Dono do POP** | Dra. Faya |
| **Quem executa** | IA (primeira correção); Dra. Faya (revisão final) |
| **Gatilho** | Minuta de peça pronta (feita pelo estagiário, pela Dra. Faya ou pela IA) |
| **Termina quando** | Peça com parecer **APROVADA** do revisor(a), salva no OneDrive e protocolada |
| **Prazo** | Primeira correção pela IA: no mesmo dia útil. Revisão final: até 1 dia útil antes do protocolo |

## Objetivo

Tirar da Dra. Faya a correção do que é objetivo (prazo, número, endereçamento, cálculo que não fecha). A IA faz a
primeira correção com critérios objetivos; a Dra. Faya faz a **revisão final**, já com os problemas apontados.

## Quem faz a revisão final

**A Dra. Faya revisa toda peça e todo cálculo antes de sair do escritório.** É regra do briefing: a IA
só poderia decidir sozinha em caso simples e padronizado ou em petição de andamento, e isso **não está
ligado** (precisa de decisão dela).

| Produto | O que a revisão final olha primeiro |
|---|---|
| Petição inicial (concessão) | Prévio requerimento, qualidade de segurado, carência, valor da causa x 60 SM (termo de renúncia) |
| Revisão de benefício | Decadência (art. 103 da Lei 8.213/91) e a conta da diferença de RMI |
| Incapacidade e BPC | DII ancorada em documento e quesitos de perícia |
| Relatório, parecer e planejamento | Cada número com a fonte (CNIS, carta de concessão, planilha) e as regras da EC 103/2019 comparadas |
| Cálculo para advogado parceiro (POP-PREV-06) | Memória de cálculo, índices e prazo do parceiro |

## Fluxo

```
Minuta → 1ª correção pela IA → autor(a) ajusta → revisão final da Dra. Faya → protocolo
              (mesmo dia)        (até 1 dia útil)    (até 1 dia útil antes)
```

## Passo a passo

1. **Autor(a) da minuta** salva a peça em `07_PECAS` com o nome `MINUTA - TIPO - CLIENTE - Nº DO PROCESSO - AAAA-MM-DD.docx`
   e junta, na mesma pasta ou em link, **o que a peça enfrenta** (inicial, decisão, sentença) e os documentos que ela cita. — *prazo interno da peça*
2. **Rodar a primeira correção pela IA** com o checklist abaixo. A IA devolve um parecer com status
   **APROVADA**, **APROVADA COM RESSALVAS** ou **NÃO APROVADA**, e a lista numerada de ajustes (onde
   está o problema e qual a correção sugerida). — *mesmo dia útil*
3. **Autor(a) faz os ajustes** e marca no parecer o que foi corrigido. — *até 1 dia útil*
4. **Revisão final** pelo Dra. Faya: lê a peça inteira, confere o parecer da IA e os pontos
   que a IA não confere (item "O que a IA não faz"). Devolve com OK ou com ajustes. — *até 1 dia útil antes do protocolo*
5. **Versão final** salva como `TIPO - CLIENTE - Nº DO PROCESSO - AAAA-MM-DD.docx` e em PDF, e protocolada.
6. **Registrar no Notion** o protocolo e concluir a tarefa.

## Checklist da primeira correção (critérios objetivos)

A IA percorre as camadas na ordem: o que é eliminatório primeiro.

**Camada 1 — Admissibilidade (eliminatória: qualquer falha = NÃO APROVADA)**
1. Tempestividade: prazo conferido em dias úteis, data da publicação e contagem (POP-OP-02).
2. Endereçamento ao juízo ou tribunal certo.
3. Número do processo conferido dígito a dígito; nomes das partes certos.
4. Procuração e, se for o caso, substabelecimento nos autos; advogado(a) que assina está habilitado(a).
5. Custas e preparo quando exigidos (no JEF não há custas no 1º grau; recurso inominado tem preparo, salvo gratuidade).
6. Cabimento: é a peça certa para o ato atacado (POP-OP-02, árvore de decisão).

**Camada 2 — Estrutura e conformidade jurídica**
7. Estrutura completa da peça (fatos, direito, pedidos ou a estrutura padrão do tipo de peça).
8. Artigos de lei citados existem e correspondem ao que a peça afirma.
9. Toda jurisprudência, súmula, tema e enunciado citado está marcada para conferência humana (ver "O que a IA não faz").
10. Recurso: cada fundamento da decisão atacada foi impugnado especificamente.
11. Defesa ou réplica: todas as preliminares e todos os pedidos da outra parte foram enfrentados.
12. Todo pedido tem fundamento, e todo fundamento tem pedido correspondente.

**Camada 3 — Tese e prova**
13. Cada tese está amarrada a documento ou prova dos autos (ID, folha ou anexo).
14. Não há fato que não esteja nos autos ou nos documentos do cliente.
15. Não há teses contraditórias entre si.
16. O ônus da prova está corretamente distribuído (CPC, art. 373; CLT, art. 818).

**Camada 4 — Riscos**
17. Pontos fracos que a outra parte vai explorar, e se a peça já se antecipa a eles.
18. Risco de preclusão, inovação recursal, litigância de má-fé.

**Camada 5 — Linguagem e formatação**
19. Linguagem formal, técnica, objetiva, sem gíria, sem primeira pessoa no corpo técnico.
20. Ortografia, concordância, repetição de palavras e parágrafos longos demais.
21. Padrão visual do escritório: timbrado, fonte, espaçamento, títulos `[A CONFIRMAR padrão do escritório]`.
22. Fecho, local, data, nome e OAB de quem assina.
23. Nome do arquivo no padrão.

## O que a IA não faz (é do revisor humano)

- **Não confirma vigência** de lei, súmula, tema ou tese: o revisor confere em fonte oficial.
- **Não confirma que a jurisprudência existe**: toda decisão citada é conferida no site do tribunal
  ou em repositório confiável. Precedente não localizado sai da peça.
- **Não inventa** fato, documento, argumento ou precedente para "completar" a peça.
- **Não substitui** a revisão final nem a assinatura do advogado(a).

## O que vira tarefa no Notion

| Tarefa | Responsável | Prazo |
|---|---|---|
| `[CORREÇÃO IA] {{tipo}} - {{cliente}} - {{processo}}` | Autor(a) da minuta | Mesmo dia útil da minuta |
| `[REVISÃO FINAL] {{tipo}} - {{cliente}} - {{processo}}` | Dra. Faya | Prazo fatal menos 1 dia útil |
| `[PROTOCOLO] {{tipo}} - {{cliente}} - {{processo}}` | Quem assina | Prazo fatal menos 1 dia útil |

## Onde salva no OneDrive

`CLIENTES/{{cliente}}/02_JUDICIAL/{{nº do processo}} - .../02_PECAS/`
- `MINUTA - ...docx` (versões de trabalho)
- `PARECER IA - ...md` (parecer da primeira correção)
- `TIPO - CLIENTE - Nº - AAAA-MM-DD.docx` e `.pdf` (versão protocolada)

## Pendências `[A CONFIRMAR]`
- Padrão visual das peças do escritório (timbrado, fonte, espaçamento, recuo).
- Já calibrado com as 27 iniciais e 14 relatórios da Dra. Faya (`previdenciario/dna/DNA_PECAS.md`); novas peças entram por lá.
