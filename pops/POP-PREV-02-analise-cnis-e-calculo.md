# POP-PREV-02 — Análise do CNIS e cálculo (tempo, carência, RMI, valor da causa)

Versão 1 — 18/11/2026

| | |
|---|---|
| **Dono do POP** | Dra. Faya (cálculo é a especialidade do escritório) |
| **Quem executa** | Agente `calculista` (leitura do CNIS, pré-apuração, conferência) → Dra. Faya (cálculo no software e validação) |
| **Gatilho** | Caso VIÁVEL com CNIS em mãos; ou demanda externa de cálculo (POP-PREV-06) |
| **Termina quando** | Cálculo conferido e resumo pronto para a peça ou para o relatório |
| **Prazo** | 2 dias úteis a partir do CNIS completo |

## Objetivo

Transformar o CNIS em número conferível: tempo de contribuição (comum e especial convertido), carência,
qualidade de segurado, **comparativo das regras da EC 103/2019**, RMI e, quando for ação, o **valor da causa**
(e se passa de 60 salários mínimos, o que chama o termo de renúncia do JEF, `modelos/04`).

## Divisão do trabalho

| O agente faz | A Dra. Faya faz |
|---|---|
| Lê o CNIS e monta o quadro de vínculos (início, fim, categoria, indicadores) | Roda o cálculo oficial no software do escritório |
| Aponta pendências: vínculo sem fim, indicador (PEXT, PREM-EXT, IREM etc.), concomitância, CNIS x CTPS | Decide o que regularizar antes de pedir |
| Pré-apuração com `previdenciario/calculos/simular.py` (tempo, carência, período de graça, regras da EC 103) | Confere a pré-apuração contra o software |
| Confere o relatório do software contra o CNIS (período a período) e contra `FORMATO_DOS_CALCULOS.md` | Valida a regra escolhida |
| Monta o resumo de 1 página para a peça | Assina o relatório |

**A calculadora do pacote é apoio, não é o cálculo oficial.** Ela serve para conferir e para a triagem. O número
que vai para a peça é o do cálculo da Dra. Faya.

## O que a apuração tem de conter

1. **Quadro de vínculos** com início, fim, categoria e fonte (CNIS, CTPS, carnê).
2. **Pendências do CNIS**, cada uma com o documento que a resolve (e o modelo `atualizacao-de-cnis` quando for ação).
3. **Tempo especial**: só com PPP/LTCAT; conversão em comum **só até 13/11/2019** (EC 103/2019, art. 25, § 2º).
4. **Carência** e **tempo de contribuição** até a DER e até hoje.
5. **Qualidade de segurado** na DER (ou na DII, em incapacidade), com o período de graça.
6. **Comparativo das regras** (direito adquirido, pontos, idade progressiva, pedágios de 50% e 100%, idade,
   PcD, professor), com a data em que cada uma é cumprida, o coeficiente e qual é melhor **e por quê**.
7. **Valor da causa**: parcelas vencidas até o ajuizamento + 12 vincendas (Lei 10.259/2001, art. 3º, § 2º; CPC, art. 292).

## Regras de ouro

- **Cálculo não se estima.** Faltou período ou salário: o resultado sai **PROVISÓRIO**, com a lacuna em destaque.
- **Divergência CNIS x CTPS sempre aparece**, mesmo que não mude o resultado.
- Revisão: conferir a **decadência** (art. 103 da Lei 8.213/91) antes de calcular diferença.
- Arquivo na pasta do cliente, `06_CALCULOS`, com a data no nome.

## Entregável

| Arquivo | Para quê |
|---|---|
| Relatório do software (PDF) | Memória de cálculo anexável |
| Resumo de 1 página | Entra na inicial (POP-PREV-04), no recurso (POP-PREV-03) ou no relatório (POP-PREV-05) |
| Lista de pendências | O que pedir ao cliente ou ao INSS |
