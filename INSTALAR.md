# INSTALAR — roteiro para o Claude executar este repositório

> **Para o Claude:** quando alguém disser "execute o repo", "instale o sistema", "rode tudo" ou `/executar-repo`,
> siga este roteiro **na ordem**. Ele liga tudo o que foi construído neste pacote. Regras:
> - **Dry-run primeiro, sempre.** Nada escreve no Notion, Asaas ou OneDrive sem a pessoa dizer "pode" depois de ver
>   o resultado do dry-run.
> - **Não invente credencial, ID, OAB, chave Pix ou dado da Dra. Faya.** Faltou: pergunte, ou deixe o módulo em modo
>   seguro e registre na lista final.
> - **Nunca** versionar `config/.env`, `config/*.json` reais, `dados/` nem documento de cliente.
> - Ao final, entregue a **tabela de status** do passo 10.

## 0. Onde estou

Descubra o ambiente e diga em uma linha: **Windows** (máquina do escritório, OneDrive sincronizado) ou **Linux/VPS**
(nuvem, OneDrive pelo rclone). O resto do roteiro tem os dois caminhos.

## 1. Python e dependências

```
python --version                      # precisa 3.10+
python -m venv venv
venv\Scripts\pip install -r requirements.txt          (Windows)
venv/bin/pip install -r requirements.txt              (Linux)
```
Use o Python do `venv` em todos os passos seguintes. LibreOffice é opcional (PDF de peça); avise se não houver.

## 2. Configuração (sem sobrescrever o que já existe)

1. `config/.env.example` → `config/.env`; cada `config/*.example.json` → o `.json` sem `.example`.
   **Se o arquivo de destino já existir, não copie por cima.**
2. Gere e grave no `.env` (e **mostre à pessoa** a senha, uma vez):
   - `PAINEL_SENHA` e `PAINEL_TOKEN_PEDIDO`: `python -c "import secrets;print(secrets.token_urlsafe(18))"`
3. Preencha em `config/escritorio.json → modelos_comuns` os dados fixos que estão em `modelos/README.md`, seção 3
   (razão social, CNPJ, endereço, OABs, e-mails, foro). O que está `[A CONFIRMAR]` lá continua vazio.
4. Pergunte à pessoa, de uma vez, o que falta (pode responder "não tenho ainda" — o módulo fica em modo seguro):

   | Variável / campo | Para quê |
   |---|---|
   | `ONEDRIVE_RAIZ` | Pasta do OneDrive/SharePoint sincronizada (Windows) ou montada pelo rclone (VPS) |
   | `NOTION_TOKEN` + ids das bases em `escritorio.json → notion` | Tarefas, prazos e processos |
   | `ASAAS_API_KEY` | Cobranças, régua e painel |
   | OABs no `escritorio.json → controladoria` | Já vêm BA 64723 e SP 308385; confirmar |
   | Estado civil da Dra. Faya, dados bancários oficiais | Contrato e procuração (`modelos/`) |

## 3. Verificação completa (obrigatória)

```
python verificar.py
```
Tem de terminar em **PACOTE OK** (automações, calculadora, painel, modelos, leis, índice). Se falhar, **pare** e
mostre a saída; não siga para os passos que escrevem em sistema externo.

## 4. Biblioteca de peças e base de leis

- `python previdenciario/pecas/gerar_peca.py listar` — confirme 41 modelos (27 iniciais + 14 relatórios).
- `python previdenciario/pecas/indice.py` — regenera `previdenciario/pecas/00_INDICE.md`. Diga quantos pontos estão na
  **pauta de revisão da Dra. Faya** (os `[CONFERIR]` herdados dos originais).
- `previdenciario/leis/banco_leis.db` tem de existir. Se não existir: `python previdenciario/leis/montar_banco_leis.py`.
- Demonstração de peça: `gerar_peca.py preencher revisao-retroacao-dib --saida teste_minuta.md` e
  `gerar_peca.py docx teste_minuta.md` — confira que o .docx sai no timbrado (cabeçalho bordô). Apague os dois
  arquivos de teste depois.

## 5. OneDrive (pastas do escritório)

Só com `ONEDRIVE_RAIZ` definido e a pasta existindo.
```
python automacoes/drive/criar_estrutura.py base            # dry-run: mostra as pastas
python automacoes/drive/criar_estrutura.py docs            # dry-run: POPs, checklists, modelos e mensagens
```
Mostre o plano. Com o "pode": repita com `--go`. VPS: o rclone tem de estar montado (`automacoes/README.md`, seção do
OneDrive) — **não grave no disco da VPS achando que é o OneDrive**.

## 6. Notion

Só com `NOTION_TOKEN`.
```
python automacoes/comum/notion.py --esquema               # lista as colunas reais das bases configuradas
```
Ajude a pessoa a mapear as colunas em `escritorio.json → notion` (não adivinhe nomes). Teste com
`--abertas`. Escrita de verdade só depois de uma tarefa de teste aprovada numa base de teste.

## 7. Controladoria e financeiro (dry-run)

```
python automacoes/controladoria/intimacoes.py             # lê o DJEN pelas OABs e mostra o que viraria tarefa
python automacoes/financeiro/regua_cobranca.py            # só com ASAAS_API_KEY
python automacoes/financeiro/relatorio_diario.py          # só com ASAAS_API_KEY
```
Mostre o resultado. Nenhum `--go` sem o "pode".

## 8. Painel das demandas externas de cálculo

Demonstração imediata (dados fictícios, nada gravado):
```
python automacoes/painel/servidor.py --exemplo            # usuário faya / senha exemplo
```
Para valer:
- **Windows**: `deploy\iniciar_painel.bat`. Para subir sozinho ao ligar o computador:
  `schtasks /Create /SC ONLOGON /TN "Faya - Painel de calculos" /TR "\"%CD%\deploy\iniciar_painel.bat\""`
  (confirme com a pessoa antes). Painel em `http://127.0.0.1:8765/painel`. Neste modo o **link dos parceiros só
  funciona dentro do escritório**: para parceiro externo, é a VPS.
- **VPS**: `deploy/painel.service` (systemd) + `deploy/Caddyfile.exemplo` (HTTPS). **Nunca exponha a porta 8765
  direto na internet.** Precisa de um subdomínio `[A CONFIRMAR]`.
- Entregue à pessoa: endereço do painel, usuário, senha e o **link dos parceiros** (`/pedido?t=<token>`).
- `PAINEL_TAREFA_NOTION=1` só depois do passo 6 aprovado; `PAINEL_PERMITE_COBRANCA=1` só com o Asaas aprovado.

## 9. Rotinas agendadas

- **VPS**: o bloco cron de `automacoes/README.md` (seção 7). Fuso: `timedatectl set-timezone America/Bahia`.
  Ligue **uma linha por vez**, cada uma depois do dry-run conferido.
- **Windows**: o equivalente no Agendador de Tarefas (`schtasks`), começando pela controladoria (dias úteis, 7h30).
  Confirme cada uma com a pessoa.

## 10. Relatório final (sempre)

Feche com esta tabela, honesta:

| Módulo | Situação | O que falta |
|---|---|---|
| Biblioteca de peças + timbrado | LIGADO / ... | revisão dos N `[CONFERIR]` pela Dra. Faya |
| Calculadora e base de leis | ... | |
| Painel de cálculos + link dos parceiros | ... | domínio/HTTPS para parceiro externo |
| OneDrive | ... | |
| Notion | MODO SEGURO se sem token | token, bases, colunas |
| Asaas (cobrança, régua, painel) | ... | |
| Controladoria (DJEN) | ... | |
| Tramitação Inteligente | ESQUELETO | documentação da API |
| Rotinas agendadas | ... | |

E a lista do que a Dra. Faya precisa mandar (está também em `PROJETO_IMPLANTACAO.md`, seção 3).
