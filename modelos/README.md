# Modelos de representação — Faya Barreiros Sociedade Individual de Advocacia

Versão 1 — 18/11/2026. Os modelos 01 a 04 são **o texto que a Dra. Faya já usa** (Kit de Representação enviado em
18/10/2026), só com os dados do cliente trocados por campos. O 05 é modelo padrão do pacote, para ela validar.

As **peças e relatórios** (petições iniciais, pareceres, planejamentos) não ficam aqui: ficam em
`previdenciario/pecas/` e saem no timbrado por `previdenciario/pecas/gerar_peca.py`.

## 1. Índice e quando usar

| Nº | Arquivo | Documento | Quando usar | Quem assina |
|---|---|---|---|---|
| 01 | `01_procuracao_previdenciaria.md` | Procuração *ad judicia* com poderes perante o INSS | Todo cliente do previdenciário | Cliente |
| 02 | `02_contrato_honorarios_previdenciario.md` | Contrato de honorários: implantação + êxito, com bloco opcional de honorários iniciais | Todo fechamento do previdenciário | Cliente + escritório + 2 testemunhas |
| 03 | `03_declaracao_hipossuficiencia.md` | Declaração de hipossuficiência | Inicial com pedido de justiça gratuita | Cliente |
| 04 | `04_termo_renuncia_jef.md` | Renúncia ao excedente de 60 salários mínimos, só para fixar o JEF | Valor da causa acima de 60 SM e estratégia de ficar no JEF | Cliente |
| 05 | `05_substabelecimento.md` | Substabelecimento com (A) ou sem (B) reserva | Correspondente, audiência, parceria, saída do processo | Dra. Faya |

**Combinação usual no fechamento:** 01 + 02 + 03, e 04 quando a conta do valor da causa pedir (POP-PREV-02).
O guia de boas-vindas com os canais oficiais (citado na Cláusula Quarta do 02) é a `mensagens/MSG-04`.

**Falta no kit** `[A CONFIRMAR com a Dra. Faya]`: contrato das **demandas externas de cálculo** (serviço que ela presta
a outros advogados, POP-PREV-06) e o recibo/prestação de contas padrão. Hoje existe só o relatório de prestação de
contas em `previdenciario/pecas/relatorios/`.

## 2. Convenções de preenchimento

- `{{chave}}` — campo simples. Dinheiro e percentual **sempre com número e extenso**.
- `{{#chave}} ... {{/chave}}` — bloco opcional: entra se a chave estiver ligada/preenchida.
- O documento é só o trecho entre `INICIO_DOCUMENTO` e `FIM_DOCUMENTO` (no 05, `_A` ou `_B`).
- `[A CONFIRMAR]` — dado do escritório que não temos. **Nunca preencher por suposição.**
- A geração recusa documento com `{{...}}` sobrando, `[A CONFIRMAR]` ou `[CONFERIR]` (`automacoes/comum/modelos.py`).

## 3. Campos fixos do escritório

Valores tirados dos contratos e procurações que a Dra. Faya enviou. Ficam em `config/escritorio.json → modelos_comuns`.

| Campo | Valor | Situação |
|---|---|---|
| `{{escritorio_razao_social}}` | FAYA BARREIROS – Sociedade Individual de Advocacia | Confirmado (contratos) |
| `{{escritorio_cnpj}}` | 67.928.823/0001-52 | Confirmado |
| `{{escritorio_endereco}}` | Avenida Tancredo Neves, 1283, Edif. Empresarial Ômega – Sala 1001, Caminho das Árvores – Salvador – Bahia – CEP 41830-021 | Confirmado (contratos) |
| `{{titular_nome}}` | FAYA MILLA M.M. BARREIROS | Confirmado |
| `{{titular_oab}}` | OAB/BA 64.723 e OAB/SP 308.385 | Confirmado |
| `{{titular_estado_civil}}` | solteira | `[A CONFIRMAR]` — uma procuração antiga dizia "casada" |
| `{{titular_email}}` | faya.calculos@gmail.com | Confirmado (briefing) |
| `{{titular_email_contratos}}` | faya.barreiros@uol.com.br | Confirmado (contratos) |
| `{{foro_comarca}}` | Salvador-BA | Confirmado (contratos) |
| `{{dados_bancarios_oficiais}}` | PIX – CNPJ (Banco C6) | Confirmado (contratos); conferir a chave no `config/escritorio.json`, nunca no repositório |
| `{{escritorio_registro_oab}}` | Registro da sociedade na OAB/BA | `[A CONFIRMAR]` |

## 4. Política de honorários (dos contratos dela)

| Item | Valor praticado |
|---|---|
| Honorários iniciais (análise de viabilidade, só na variante com bloco ligado) | R$ 300,00 (trezentos reais) |
| Implantação, se o benefício for concedido | 4 salários de benefício (sobre a RMI calculada pelo INSS) |
| Êxito | 30% (trinta por cento) sobre os retroativos, inclusive RPV e precatório |
| Desconto em benefício/salário de honorário vencido | até 30% do líquido mensal (Cláusula Terceira) |

O agente sugere; quem fixa o valor de cada contrato é a Dra. Faya.

## 5. Pontos `[CONFERIR]`

| Nº | Ponto | Onde | Como conferir |
|---|---|---|---|
| 1 | Vigência e redação do EREsp 1.874.222/DF e da SV 47 citados na Cláusula Terceira | 02 | STJ/STF, revisão anual do modelo |
| 2 | Tema Repetitivo 1.030 do STJ (renúncia no JEF): redação atual da tese | 04 | stj.jus.br > Repetitivos |
| 3 | Aceitação, pelo TRF1 e JEFs da Seção Judiciária da Bahia, de procuração assinada na Tramitação Inteligente | 01 | Prática local; na dúvida, assinatura gov.br ou ICP-Brasil |
| 4 | Estado civil da titular | 01, 02 | Perguntar à Dra. Faya |
