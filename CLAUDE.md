# Faya Barreiros Advocacia — previdenciário e cálculos — contexto para o Claude

> **"Execute o repo" / "instale" / "rode tudo" / `/executar-repo`** → siga o **`INSTALAR.md`** do passo 0 ao 10.
> Ele instala, roda `python verificar.py` (tem de dar PACOTE OK), configura sem inventar dado e liga, em dry-run
> primeiro: biblioteca de peças, calculadora, base de leis, **painel de cálculos com o link dos parceiros**, OneDrive,
> Notion, Asaas, controladoria e rotinas. Termina com a tabela de status.
>
> **"Gere o SaaS" / `/gerar-saas`** → `.claude/commands/gerar-saas.md`: sistema web do escritório a partir da base
> white-label (`sistema-base-virgem`), com este pacote dentro e o portal de cálculos para advogados parceiros.

Pacote de implantação Casal da IA, no mesmo formato dos pacotes da Laís Torres & Alex Brunno e da SPDAG:
POPs, checklists, mensagens, modelos, agentes Claude e automações. Este repositório é **só o previdenciário**
da Dra. Faya. O tributário do Dr. William fica no repositório anterior (`faya-barreiros-advocacia`, que juntava as
duas áreas num sistema Python) e não entra aqui.

Fontes: briefing do Casal da IA preenchido em **18/10/2026**; material que a Dra. Faya enviou em **18/10/2026**
(Kit de Representação, 27 modelos de petição inicial, 15 relatórios, cálculos de exemplo, timbrado); sistema montado
em 22–23/10/2026. Pacote previdenciário montado em **18/11/2026**.

## Quem é quem

| Pessoa | Papel |
|---|---|
| **Dra. Faya Milla Magalhães Mascarenhas Barreiros** — OAB/BA 64.723 e OAB/SP 308.385 | Titular da sociedade individual. Previdenciário, **cálculos** e serviços avulsos (inclusive para outros advogados). Decide, calcula, revisa e assina tudo. |
| **Bárbara** | Secretária: e-mails, prazos, recibos, pastas, primeiro contato com cliente e lead |
| **Estagiário(a)** `[A CONFIRMAR nome]` | Elabora petições, confere pushs processuais, baixa decisões; só muda status das demandas |
| Dr. William Ricardo Coelho (OAB/BA 64.518) | Tributário, **fora deste pacote**. Lead tributário é encaminhado a ele |

Pessoa jurídica: **FAYA BARREIROS – Sociedade Individual de Advocacia**, CNPJ **67.928.823/0001-52**, Av. Tancredo
Neves, 1283, Edif. Empresarial Ômega, Sala 1001, Caminho das Árvores, Salvador/BA, CEP 41830-021. Atendimento
presencial em Salvador e online para todo o Brasil. E-mail de trabalho `faya.calculos@gmail.com`; nos contratos,
`faya.barreiros@uol.com.br`.

## O que o escritório faz

- **Concessão**: aposentadoria especial, por tempo (com conversão), por pontos/direito adquirido, da pessoa com
  deficiência (inclusive visão monocular), por incapacidade (com e sem adicional de 25%), auxílio por incapacidade,
  auxílio-acidente, BPC, pensão por morte.
- **Revisão**: retroação da DIB, atividade concomitante, inclusão de verbas de reclamatória trabalhista, conversão de
  tempo especial, pós-reforma → pré-reforma, aposentadoria por incapacidade (regra pré-reforma), adicional de 25%.
- **Outras**: suspensão de descontos indevidos, RMC, isenção de IR, restituição de contribuição acima do teto,
  atualização de CNIS, cobrança de licença-prêmio e de honorários.
- **Relatórios e cálculos** (o diferencial dela): análise previdenciária, planejamento (com conversões, professor),
  pareceres de viabilidade, revisão, liquidação, recálculo de RMI, conferência de RMI, prestação de contas.
- **Demandas externas de cálculo** para advogados parceiros — o **ciclo de prazos** dessas demandas é
  **inegociável** para ela (briefing).

## Mapa do pacote

| Pasta | O que tem |
|---|---|
| `pops/` | 13 POPs (atendimento, triagem, CNIS e cálculo, CRPS, inicial e perícia, relatórios, demandas externas, RPV e honorários, controladoria, correção de peças, pagamentos). Comece pelo `pops/README.md` |
| `checklists/` | `CK-DIAG-PREV-01` a `06` por produto; `CK-DIA-01` conferência antes do protocolo |
| `mensagens/` | MSG-01 a 07 (andamento, documentos, perícia, boas-vindas, lead, benefício concedido/RPV, cobrança) |
| `modelos/` | Kit de representação dela em `{{campos}}`: procuração, contrato, declaração, termo de renúncia do JEF, substabelecimento |
| `previdenciario/pecas/` | **27 iniciais e 14 relatórios da Dra. Faya**, anonimizados, + `gerar_peca.py` (preenche e põe no timbrado) |
| `previdenciario/dna/` | `DNA_PECAS.md`: estilo, estrutura e citações das peças dela |
| `previdenciario/leis/` | Base de leis por artigo (Lei 8.213, 8.212, LOAS, Decreto 3.048, EC 103, LC 142, IN 128 e outras) com `buscar_lei.py` |
| `previdenciario/calculos/` | Calculadora de apoio (tempo, carência, período de graça, regras da EC 103/2019) com testes, e o formato dos cálculos dela |
| `previdenciario/timbrado/` | Timbrado oficial dela (bordô) |
| `automacoes/` | Python: Asaas (real), Notion, OneDrive, DJEN/controladoria, financeiro. Ver `automacoes/README.md` |
| `automacoes/painel/` | **Painel das demandas externas de cálculo** (fila por prazo, semáforo, faturamento, parceiros) e o **link de pedido para advogados parceiros**. `servidor.py --exemplo` para demonstrar |
| `INSTALAR.md`, `verificar.py`, `deploy/` | Roteiro de execução, verificação completa e arquivos de implantação (Windows e VPS) |
| `.claude/agents/` | `previdenciario`, `calculista`, `revisor-pecas`, `atendimento`, `controladoria`, `financeiro` |
| `.claude/skills/` | `triagem-previdenciaria` |

## Ferramentas do escritório

- **Notion** — prazos, financeiro e processos. Conector `automacoes/comum/notion.py` feito pela documentação pública
  da API, **não testado no Notion dela**: falta o token de integração e os IDs/colunas das bases.
- **Tramitação Inteligente** — assinatura digital e andamento. `automacoes/comum/tramitacao.py` é **esqueleto**
  (sem documentação da API do nosso lado). Não inventar endpoint.
- **OneDrive/SharePoint** — documentos. As automações trabalham na pasta sincronizada (ou montada por rclone na VPS).
- **Asaas** — cobrança (`automacoes/comum/asaas.py`, conector real).
- **PJe** (TRF1/JEF da Bahia; TJBA nas acidentárias) e DJEN pelas duas OABs.
- Ela quer rodar **na nuvem**. Não usa ADVBOX, Google Workspace nem CRM de WhatsApp.

## Regras de trabalho neste projeto

- **Revisão humana obrigatória.** A Dra. Faya revisa toda peça, cálculo e relatório. A exceção do briefing (IA define
  a estratégia sozinha em caso simples/padronizado e em petição de andamento) **não está ligada**: ligar exige
  decisão dela.
- **Nada inventado.** O que não veio de documento fica `[CONFERIR]` / `[A CONFIRMAR]` e trava a geração. Nunca
  preencher NB, DER, CPF, OAB, chave Pix ou valor por suposição.
- **Jurisprudência**: só a que já está nos modelos dela (`previdenciario/dna/DNA_PECAS.md`, seção de citações),
  sempre marcada para conferência de vigência. Artigo de lei: conferir em `previdenciario/leis/`.
- **Cálculo não se estima.** A calculadora do pacote é apoio; o número oficial é o do software dela.
- **Dado de cliente nunca entra no repositório.** Os modelos foram anonimizados; os originais dela (com nome, CPF,
  dados de saúde) ficam só em `C:\AUTOMAÇÕES CLIENTES\FAYA BARREIROS\MATERIAL_FAYA` (fora do git). Antes de
  qualquer commit de modelo novo: varrer CPF, NB, nº CNJ, nomes.
- Peça: formal, sem emoji, no timbrado dela. Cliente: linguagem simples, cordial, sem prometer data do INSS ou do juiz.
- **Menor custo de manutenção**: usar o que ela já tem (Notion, Tramitação, OneDrive, Asaas). Ferramenta paga nova
  só com o custo na mesa.
