---
name: triagem-previdenciaria
description: Triagem rápida de um caso previdenciário novo no padrão da Dra. Faya Barreiros. Use quando alguém colar um CNIS, uma carta do INSS ou descrever um caso e perguntar "tem direito?", "qual ação?", "vale a pena?". Devolve requisitos, o que falta, o caminho, o modelo de peça e a classificação VIÁVEL / PENDENTE DE DOCUMENTO / SEM TESE.
---

# Triagem previdenciária (POP-PREV-01)

1. **Identifique o produto** e abra o checklist certo em `checklists/diagnostico/`:
   01 BPC · 02 incapacidade · 03 aposentadorias · 04 pensão por morte · 05 revisão · 06 descontos/RMC/IR/teto.
2. **Leia a carta do INSS** (se houver) e transcreva o motivo do indeferimento.
3. **Filtros que encerram cedo:**
   - Revisão: passou 10 anos do 1º dia do mês seguinte ao 1º pagamento? (art. 103 da Lei 8.213/91) → SEM TESE.
   - Incapacidade/pensão: havia qualidade de segurado na DII/óbito? (art. 15 da Lei 8.213/91; rode
     `previdenciario/calculos/periodo_graca.py` pelo `simular.py`).
   - Ação judicial sem prévio requerimento → primeiro o pedido no INSS.
4. **Requisitos com artigo**, conferidos no texto da lei: `python previdenciario/leis/buscar_lei.py --lei 8213 --art N`.
5. Aposentadoria: rode `python previdenciario/calculos/simular.py caso.json` para a tabela de regras (apoio; o
   cálculo oficial é o POP-PREV-02).
6. **Modelo de peça**: `python previdenciario/pecas/gerar_peca.py listar` e escolha o que casa com o caso.

## Formato da resposta

```
CASO: <nome ou iniciais> — <produto>
CARTA DO INSS: <motivo transcrito, ou "não há pedido">
REQUISITOS: <requisito — artigo — provado / falta (documento que resolve)>
FILTROS: decadência <ok/não se aplica/estourou> · qualidade de segurado <ok/perdida em dd/mm/aaaa/a conferir>
CAMINHO: novo pedido | recurso CRPS | ação (JEF/Vara) | planejamento — porque <motivo>
MODELO: <tipo do modelo>
CLASSIFICAÇÃO (sugestão): VIÁVEL | PENDENTE DE DOCUMENTO | SEM TESE
PEDIR AO CLIENTE: <lista para a MSG-02>
```

Nada inventado: o que não está em documento vai como "a conferir". Quem decide é a Dra. Faya.
