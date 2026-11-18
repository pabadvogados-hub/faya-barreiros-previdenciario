# Automações do escritório Faya Barreiros Advocacia

Faya Barreiros Sociedade Individual de Advocacia (CNPJ 67.928.823/0001-52), Salvador/BA.
Previdenciário e cálculos previdenciários. Titular: Dra. Faya Barreiros (OAB/BA 64.723 e OAB/SP 308.385).

Ferramentas que o escritório já usa e que o código conversa com elas:

| Ferramenta | Para quê | Como o código fala com ela |
|---|---|---|
| **Notion** | prazos, tarefas, processos, clientes | `comum/notion.py`, API pública do Notion. Implementado pela documentação, **não testado no workspace dela** |
| **OneDrive/SharePoint** | documentos | `comum/drive.py`, por uma **pasta local sincronizada** (`ONEDRIVE_RAIZ`). Na VPS, montada pelo rclone |
| **Asaas** | cobrança, NF, Pix | `comum/asaas.py`, API v3 |
| **Tramitação Inteligente** | assinatura digital e andamento | `comum/tramitacao.py` é **só esqueleto**: a API não foi documentada para nós. A assinatura segue **manual** na plataforma |
| **PJe / DJEN** | intimações | `controladoria/djen.py`, API Comunica do CNJ (gratuita) |

Não há CRM de WhatsApp com API. Toda mensagem (régua de cobrança, avisos) vai para uma **fila**
(`dados/saida/fila_mensagens_AAAA-MM-DD.csv`), e a Bárbara envia pelo WhatsApp do escritório.

**Todo script roda em DRY-RUN por padrão**: mostra o que faria e não escreve em sistema nenhum. Só com
`--go` ele cria cobrança, Pix, nota, tarefa no Notion, pasta ou arquivo no OneDrive. Com `--go`, o
script **recusa** rodar em cima de um arquivo `*.example.json`.

```
automacoes/
├── comum/          Asaas, Notion, OneDrive (pasta local), Tramitação (esqueleto), banco local, mensagens, nomes
├── financeiro/     régua de cobrança, nova cobrança/12 boletos, NF, relatório diário, Pix da equipe
├── drive/          estrutura de pastas, documento recebido -> pasta + tarefa, demandas externas de cálculo
├── controladoria/  DJEN por OAB -> classificação -> prazo -> tarefa no Notion
├── backup/         backup semanal cifrado (banco + filas + cadastros)
├── pecas/          extração de texto para o agente revisor-pecas
├── atendimento/    andamento do processo registrado no Notion (leitura)
└── testes/         teste offline com dados fictícios
```

Os agentes do Claude Code estão em `.claude/agents/`. Os que usam estes scripts: `financeiro`,
`controladoria` e `atendimento`.

---

## 1. Instalação

### Na máquina do escritório (Windows) e na VPS (Ubuntu 22.04+)

```bash
python -m venv venv
# Windows: venv\Scripts\activate     |  Linux: source venv/bin/activate
pip install -r requirements.txt
python automacoes/testes/teste_offline.py      # tem que terminar com "TUDO OK"
```

Na VPS, além do Python: `apt install rclone libreoffice-writer openssl` (rclone para o OneDrive,
LibreOffice para converter .docx em PDF, openssl para cifrar o backup).

### Configuração

1. `config/.env.example` → `config/.env` (credenciais e a raiz do OneDrive). Chave do Asaas **entre aspas simples**.
2. `config/escritorio.example.json` → `config/escritorio.json` (OABs, bases e colunas do Notion,
   dados fiscais do contador, aprovador). Nome, CNPJ, OABs e cidade já vêm preenchidos.
3. `config/clientes.example.json` → `config/clientes.json` (cada cliente: contato financeiro, regra
   da NF, processos; e cada **advogado parceiro** com as demandas externas de cálculo).
4. `config/colaboradores.example.json` → `config/colaboradores.json` (Bárbara e o estagiário: só o
   que o Pix precisa) e `config/despesas_fixas.example.json` → `config/despesas_fixas.json`.
5. **Notion** — ver a seção 2.
6. **OneDrive** — ver a seção 3.

`.env`, tokens e os `config/*.json` reais estão no `.gitignore`. Nada disso pode ser versionado.

---

## 2. Notion (`comum/notion.py`)

> Implementado pela documentação pública do Notion (API v1, `Notion-Version: 2022-06-28`).
> **Não foi testado contra o workspace da Dra. Faya.** Antes do primeiro `--go`, fazer o roteiro abaixo.

1. Em https://www.notion.so/my-integrations, criar uma **integração interna** do workspace dela e
   copiar o token para `NOTION_TOKEN` no `config/.env`.
2. Em cada base usada (Processos, Prazos/Tarefas, Clientes e, se existir, Andamentos): **"... >
   Conexões > adicionar a integração"**. Sem isso a API responde 404.
3. Copiar o id de cada base (os 32 caracteres da URL) para `escritorio.json -> notion.databases`.
4. Rodar `python automacoes/comum/notion.py --esquema`: lista as **colunas reais** de cada base.
5. Preencher `notion.campos` com o **nome** da coluna de cada campo lógico. Não há nome de coluna no
   código: o tipo da coluna (texto, data, select, status, pessoa, relação, checkbox) é lido da API e
   o valor é montado de acordo. Campo sem coluna fica vazio e é ignorado.
6. Preencher `status_inicial`, `status_concluido`, `tipos_tarefa` (valores do select "tipo") e
   `responsaveis` (id do usuário se a coluna for Pessoa; o nome se for select/texto).
7. Testar uma tarefa: `python automacoes/controladoria/intimacoes.py --arquivo automacoes/testes/fixture_djen.json --go`
   **numa base de teste** (ou apagar as tarefas de teste depois).

O que o conector faz: `buscar_processo`, `buscar_cliente`, `listar_clientes`, `customer_id`,
`movimentacoes`/`ultimas_movimentacoes` (da base Andamentos ou, se ela não existir, dos parágrafos da
página do processo), `tarefas_abertas`, `criar_tarefa`, `concluir_tarefa`, `lancar_andamento`,
`criar_cliente`, `criar_processo`, `ids_do_escritorio`. O que ele **não faz**: baixar documento do
processo (`listar_documentos` e `url_temporaria_documento` devolvem erro `NaoSuportado`): o documento
mora no OneDrive.

Diferente do sistema do pacote de origem, o Notion **não exige processo** para criar tarefa: intimação
de processo não cadastrado vira tarefa sem vínculo + pendência "cadastrar o processo". O prazo nunca
se perde por falta de cadastro.

---

## 3. OneDrive (`comum/drive.py`, `drive/`)

Não há API da Microsoft no código. O script grava numa pasta do disco que o OneDrive sincroniza:

- **No computador do escritório**: `ONEDRIVE_RAIZ` = a pasta da biblioteca sincronizada, ex.
  `C:\Users\<usuario>\OneDrive - Faya Barreiros\ESCRITORIO`.
- **Na VPS**: a mesma biblioteca montada pelo rclone.

```bash
# 1) uma vez, na VPS (o login abre um link para autorizar com a conta Microsoft do escritório;
#    em VPS sem navegador, rodar "rclone authorize onedrive" num PC e colar o token)
rclone config            # n) new remote -> nome: onedrive -> tipo: onedrive -> conta business/SharePoint
# 2) montar (serviço systemd ou cron @reboot)
mkdir -p /mnt/onedrive
rclone mount onedrive: /mnt/onedrive --vfs-cache-mode writes --daemon
# 3) config/.env
ONEDRIVE_RAIZ=/mnt/onedrive/ESCRITORIO
```

`--vfs-cache-mode writes` é necessário para o rclone aceitar a cópia de arquivos. Use como raiz uma
**subpasta** da montagem (`/mnt/onedrive/ESCRITORIO`), nunca o próprio ponto de montagem: se o rclone
cair, `/mnt/onedrive` fica vazio, a subpasta deixa de existir e os scripts recusam o `--go` em vez de
gravar no disco da VPS. Conferir antes de ligar o cron: `ls /mnt/onedrive/ESCRITORIO`.
Alternativa sem montagem: gravar numa pasta local da VPS e sincronizar por cron com
`rclone copy /opt/escritorio/onedrive onedrive:ESCRITORIO` (nunca `sync`, que apaga do outro lado).

Regras do `drive.py`: pasta **idempotente** (existe, reusa; nunca duplica, apaga ou move); arquivo
com mesmo nome e mesmo conteúdo não é copiado de novo; mesmo nome e conteúdo diferente vira
`<nome> (2).ext` (nunca sobrescreve); o "link" que vai para o Notion é o **caminho relativo** à raiz.
`docx_para_pdf` usa o LibreOffice em modo headless; sem ele, avisa e devolve `None`.

- `ESTRUTURA_PASTAS.md`: a árvore (previdenciária, por cliente, e `DEMANDAS_EXTERNAS_CALCULO`), a
  convenção de nomes e o roteamento.
- `criar_estrutura.py`: `base`, `cliente`, `processo`, `demanda-externa` e `docs` (copia POPs,
  checklists, mensagens e modelos para `00_ESCRITORIO`). `--offline` mostra só o plano.
- `arquivar_documento.py`: a Bárbara salva o anexo recebido (e-mail/WhatsApp) e roda o script dizendo
  de quem é (`--cliente`, `--parceiro`, `--telefone`, `--email`). Ele escolhe a subpasta (CNJ,
  PPP/LTCAT, CNIS/CTPS, laudo/exame, carta do INSS, RG/CPF...), copia e cria a tarefa
  `[DOCUMENTO]` no Notion com o caminho.

### Demandas externas de cálculo (prazo inegociável)

`criar_estrutura.py demanda-externa --parceiro <id> --caso "..." --prazo AAAA-MM-DD --go` cria a
pasta em `DEMANDAS_EXTERNAS_CALCULO/<PARCEIRO>/<AAAA-MM-DD - CASO>` e a tarefa
`[CALCULO EXTERNO]` no Notion (prazo interno = entrega − 2 dias úteis; fatal = entrega). Sem `--prazo`,
sai a tarefa "DEFINIR PRAZO" para hoje. Ver `ESTRUTURA_PASTAS.md`.

### Painel das demandas externas + link de pedido dos parceiros (`painel/`)

`python automacoes/painel/servidor.py` sobe o painel em `http://127.0.0.1:8765/painel` (usuário e senha:
`PAINEL_USUARIO`/`PAINEL_SENHA`) e o formulário dos parceiros em `/pedido?t=<PAINEL_TOKEN_PEDIDO>`.

- **Fila por prazo** com semáforo: prazo interno = prazo do parceiro − 2 dias úteis (feriados nacionais, BA e
  Salvador do `controladoria/prazos.py`); atenção a 2 dias úteis; vermelho quando passa do interno ou do fatal.
- **Pedido do parceiro**: entra com protocolo `CE-AAAA-NNNN`, arquivos em
  `DEMANDAS_EXTERNAS_CALCULO/<PARCEIRO>/<AAAA-MM-DD - caso>/01_RECEBIDO_DO_PARCEIRO` e, com
  `PAINEL_TAREFA_NOTION=1`, tarefa `[CALCULO EXTERNO]` no Notion.
- **Dinheiro**: valor, pago/a receber, faturado e recebido no mês, ranking de parceiros, ticket e tempo médio por tipo.
  "Cobrar no Asaas" usa o protocolo como `externalReference`; só emite com `PAINEL_PERMITE_COBRANCA=1`.
- Banco: tabela `calculos_externos` em `dados/escritorio.db`. Demonstração sem configurar nada: `--exemplo`.
- Teste: `python automacoes/painel/teste_painel.py`.
- Na internet (VPS): sempre atrás de HTTPS (Caddy) — ver `INSTALAR.md`, passo 8.

---

## 4. Financeiro (`automacoes/financeiro/`)

| Script | O que faz |
|---|---|
| `notificacoes_asaas.py` | Desliga as notificações nativas do Asaas dos clientes que já existem (são cobradas por aviso). Rodar uma vez na implantação. |
| `nova_cobranca.py` | Cria cliente e cobrança a partir de dados mínimos. O cliente nasce com `notificationDisabled=true`. Avulso: `--parcelas N`. Mensal: `--assessoria --meses 12` registra 12 boletos. Valida CPF/CNPJ e é idempotente pela `externalReference`. |
| `regua_cobranca.py` | Lembretes **10, 5 e 3 dias antes e no dia** do vencimento, com link de pagamento, e "pagamento recebido". Textos de `mensagens/MSG-07`. Lembrete de atraso desligado até a Dra. Faya confirmar. Mensagem com dado faltando não sai: vira pendência. |
| `nota_fiscal.py` | NFS-e pelo Asaas por cliente: `nf.quando = "antes"` ou `"depois"` do pagamento. O link vai para a fila de mensagens. Travas: data de corte, idempotência e dados fiscais completos. |
| `relatorio_diario.py` | Entradas, saídas, inadimplentes, margem e custo da equipe, em `.md` e `.xlsx`. `--onedrive` copia para `FINANCEIRO/AAAA/MM/RELATORIOS`; `--avisar` põe o resumo na fila para a Dra. Faya. |
| `pagamentos.py` | Pix agendado da equipe e das despesas fixas (`agendar`), lista do dia para aprovar + tarefa no Notion (`aviso-do-dia`), alerta de saldo (`saldo`), comprovantes para `FINANCEIRO/AAAA/MM/COMPROVANTES` (`comprovantes`) e boleto de despesa (`boleto`). |

### Autorização do Pix por token no Asaas

- `POST /v3/transfers` com `scheduleDate` cria o Pix agendado. Com a **validação de eventos críticos
  por token** ligada, a transferência fica pendente (`authorized=false`) até alguém aprovar.
- Fluxo: o script agenda, a Dra. Faya recebe a lista do dia e **aprova no app ou no painel com o
  token**. Nada sai sem esse toque. Não usamos a "validação de saque via webhook" (tiraria a
  aprovação humana). Cadastrar o IP da VPS na whitelist da chave de API.
- **[A CONFERIR na conta dela]**: se o token está ligado para transferências criadas pela API e por
  qual canal chega. Homologar antes no sandbox (token `000000`).

---

## 5. Controladoria (`automacoes/controladoria/intimacoes.py`)

- **Fonte**: DJEN/Comunica do CNJ, pelas OABs de `escritorio.json -> controladoria.oabs`
  (**BA 64723 e SP 308385**). A API oscila entre "ocupado" e um falso vazio; o módulo tenta de novo.
- **Classificação** (`classificador.py`, por regras, sem IA): MERO_ANDAMENTO, EMBARGOS_DE_DECLARACAO,
  AGRAVO, APELACAO, RECURSO_ORDINARIO ou OUTROS (com subtipo; JEF → recurso inominado, 10 dias).
- **Prazo** (`prazos.py`): publicação no 1º dia útil após a disponibilização, contagem a partir do
  dia útil seguinte, dias úteis, suspensão de 20/12 a 20/01 e feriados nacionais. Interno = fatal − 2
  dias úteis; protocolo = fatal − 1.
  - `feriados_locais.json`: aplica **2 de julho (BA)**. Os municipais de Salvador (24/06 São João,
    08/12 N. Sra. da Conceição da Praia) e os de SP ficam em `_CONFERIR`, **não aplicados**, até a
    controladoria conferir no calendário do TJBA/TJSP. Na dúvida, menos feriado (prazo mais curto).
  - **Justiça Federal** (TRF1/SJBA, TRF3, JEF): os feriados da Lei 5.010/66 não são aplicados; o
    prazo sai com aviso para conferir.
- **Notion**: `[PRAZO] …` (prazo = interno, prazo fatal = fatal) e `[CONFIRMAR CLASSIFICAÇÃO] …`
  para decisão, sentença ou acórdão. Processo não cadastrado no Notion: tarefa sem vínculo + pendência.
  Tarefa que falhou no `--go` não marca a intimação como tratada: a próxima rodada tenta de novo.

---

## 6. Backup (`automacoes/backup/`)

- `backup_semanal.py` gera um `.tar.gz` com o banco local (cópia consistente do SQLite), filas,
  relatórios e cadastros. Cifrado com `openssl` AES-256 e senha guardada **também fora da VPS**, em
  rotação (8 semanas) e, com `--onedrive`, copiado para `00_ESCRITORIO/BACKUPS`.
- Sem cifra, nada vai para o OneDrive. `.env` e tokens não entram no backup.
- Os documentos dos clientes já estão no OneDrive/SharePoint (com o histórico de versões da Microsoft):
  não entram neste backup.

---

## 7. VPS: agendamentos (cron)

```cron
# m  h  dom mon dow   (horário de Brasília = Salvador: timedatectl set-timezone America/Bahia)
0   7  *   *   *     cd /opt/escritorio && venv/bin/python automacoes/financeiro/relatorio_diario.py --go --onedrive --avisar
30  7  *   *   *     cd /opt/escritorio && venv/bin/python automacoes/financeiro/nota_fiscal.py --go
30  7  *   *   1-5   cd /opt/escritorio && venv/bin/python automacoes/controladoria/intimacoes.py --go --onedrive
0   8  *   *   *     cd /opt/escritorio && venv/bin/python automacoes/financeiro/regua_cobranca.py --go
0   8  *   *   *     cd /opt/escritorio && venv/bin/python automacoes/financeiro/pagamentos.py aviso-do-dia --go
0   9  *   *   1-5   cd /opt/escritorio && venv/bin/python automacoes/financeiro/pagamentos.py saldo --dias 2 --go
0   14 *   *   *     cd /opt/escritorio && venv/bin/python automacoes/financeiro/nota_fiscal.py --go
0   18 *   *   *     cd /opt/escritorio && venv/bin/python automacoes/financeiro/pagamentos.py comprovantes --mes $(date +\%Y-\%m) --go
0   10 25  *   *     cd /opt/escritorio && venv/bin/python automacoes/financeiro/pagamentos.py agendar --go
30  3  *   *   0     /opt/escritorio/automacoes/backup/backup_semanal.sh >> /var/log/escritorio-backup.log 2>&1
```

O `backup_semanal.sh` aceita `ESCRITORIO_BASE` e `ESCRITORIO_PY` pelo ambiente (padrão
`/opt/escritorio`). **Só ligue um cron depois que o mesmo comando rodar em dry-run com resultado
conferido**, e só ligue os que usam `--onedrive` com o rclone montado.

---

## 8. Testes

`python automacoes/testes/teste_offline.py` testa, sem rede e sem credencial, com dados fictícios:
régua, relatório, 12 boletos, NF, Pix, motor de prazos (inclui 2 de julho e o aviso da Justiça
Federal), classificador com tribunais da BA, controladoria completa com o Notion **não configurado**,
o conector do Notion contra um **servidor falso** (payload, filtros, tipos de coluna, texto longo),
o esqueleto da Tramitação, o OneDrive numa **pasta temporária** (pastas idempotentes, cópia, não
sobrescrever, roteamento de documentos, demandas externas, arquivamento de ponta a ponta) e modelos.

---

## 9. Pendências `[A CONFIRMAR]`

- **Notion**: token, ids das bases, nomes das colunas, valores de status/tipo, responsáveis; teste
  com uma tarefa real numa base de teste. O conector **nunca rodou contra o workspace dela**.
- **Tramitação Inteligente**: documentação da API (ou contato do suporte) e credencial. Até lá,
  assinatura manual na plataforma.
- **OneDrive na VPS**: conta Microsoft para autorizar o rclone; qual biblioteca/pasta é a raiz.
- **Feriados**: conferir no calendário do TJBA os municipais de Salvador (24/06 e 08/12) e no do TJSP o
  9 de julho; conferir o calendário da SJBA/TRF1 (Lei 5.010/66).
- **Asaas**: token de eventos críticos para transferências pela API; se a emissão automática de NF
  já está ligada no painel (duplicaria).
- **Contador**: código do serviço municipal de Salvador, alíquotas e data de corte da NF.
- **Dra. Faya**: lista de clientes (valor, vencimento, regra da NF), advogados parceiros e demandas em
  aberto com prazo, lembretes de atraso (dias e tom), multa e juros, equipe (valor, dia, chave Pix
  informada por cada um), despesas fixas, endereço do escritório.
