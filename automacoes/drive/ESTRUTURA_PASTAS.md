# Estrutura de pastas do escritório no OneDrive

Versão 1 (18/11/2026). Quem cria as pastas é o script `automacoes/drive/criar_estrutura.py`. Os
nomes vêm de um arquivo só, `automacoes/drive/estrutura_pastas.json`: se um nome mudar lá, muda em
todos os scripts.

**Regra de ouro:** o documento fica no OneDrive/SharePoint; no Notion vai só o caminho do arquivo
(relativo à raiz). Se o Notion mudar, o acervo continua inteiro no OneDrive.

**Como o script chega ao OneDrive:** não há API da Microsoft. O script grava numa pasta local que o
OneDrive sincroniza (`ONEDRIVE_RAIZ` em `config/.env`). No computador do escritório é a pasta do
OneDrive/SharePoint; na VPS, a mesma biblioteca montada pelo rclone (`automacoes/README.md`).

## A árvore

```
ONEDRIVE_RAIZ (pasta do escritório no OneDrive/SharePoint)
├── 00_ESCRITORIO
│   ├── POPS                 cópia dos POPs (pops/*.md)
│   ├── CHECKLISTS           checklists de diagnóstico e do dia a dia
│   ├── MODELOS              procuração, contrato, declaração, termo de renúncia, peças-modelo
│   ├── MENSAGENS            modelos de mensagem (MSG-01 a MSG-07)
│   ├── CONTROLADORIA/AAAA/MM   relatório diário da controladoria
│   ├── ENTRADA_DOCUMENTOS   documento de remetente sem cadastro (a triagem decide o destino)
│   └── BACKUPS              backup semanal da VPS (cifrado)
├── FINANCEIRO
│   └── AAAA
│       └── MM
│           ├── RELATORIOS        relatório diário (.md e .xlsx)
│           ├── COMPROVANTES      comprovantes de Pix da equipe e das despesas fixas
│           └── NOTAS_FISCAIS
├── CLIENTES
│   └── NOME COMPLETO DO CLIENTE (em maiúsculas)
│       ├── 00_CONTRATACAO           contrato de honorários, procuração, declaração de hipossuficiência,
│       │                            termo de renúncia (assinados na Tramitação Inteligente)
│       ├── 01_DOCUMENTOS_PESSOAIS   RG, CPF, CNH, certidões, comprovante de residência
│       ├── 02_CNIS_E_VINCULOS       CNIS, CTPS, carnês/GPS, contracheques, ficha de registro
│       ├── 03_PROVAS_ESPECIAIS      PPP, LTCAT, laudos técnicos de insalubridade/periculosidade
│       ├── 04_SAUDE                 laudos médicos, exames, atestados, receitas, prontuário
│       ├── 05_INSS_ADMINISTRATIVO   requerimento, carta de indeferimento/concessão, exigências,
│       │                            processo administrativo, recurso ao CRPS
│       ├── 06_CALCULOS              contagem de tempo, carência, RMI, comparativo EC 103/2019
│       ├── 07_PECAS                 minutas, parecer da revisão, versão protocolada
│       ├── 08_PROCESSO_JUDICIAL
│       │   └── 1001234-56.2026.4.01.3300 - INSS - TIPO DE AÇÃO     uma pasta por processo
│       ├── 09_FINANCEIRO            boletos, comprovantes, recibos do cliente
│       └── 99_A_CLASSIFICAR         o que chegou e o robô não soube onde pôr
└── DEMANDAS_EXTERNAS_CALCULO        cálculos e serviços avulsos para OUTROS advogados
    └── NOME DO ADVOGADO PARCEIRO
        ├── AAAA-MM-DD - CASO                 uma pasta por demanda (data de recebimento na frente)
        │   ├── 01_RECEBIDO_DO_PARCEIRO
        │   ├── 02_CALCULO_EM_ELABORACAO
        │   ├── 03_ENTREGUE                   versão final enviada ao parceiro
        │   └── 04_FINANCEIRO                 cobrança e comprovante do serviço
        └── 99_A_CLASSIFICAR                  documento do parceiro sem demanda identificada
```

## Demandas externas de cálculo: o prazo é inegociável

A Dra. Faya faz cálculos e serviços avulsos para outros advogados. Isso fica **separado dos
clientes** (o cliente final é do parceiro, não do escritório) e o ciclo de prazo é tratado como
prazo processual:

1. Recebeu a demanda: `criar_estrutura.py demanda-externa --parceiro <id ou nome> --caso "<caso>" --prazo AAAA-MM-DD --go`.
   - Cria a pasta e as 4 subpastas.
   - Cria no Notion a tarefa `[CALCULO EXTERNO] <caso> - <parceiro> - entrega dd/mm/aaaa`, com prazo
     interno = entrega − 2 dias úteis e prazo fatal = data de entrega.
   - **Sem `--prazo`**, a tarefa sai para HOJE como `DEFINIR PRAZO`: nenhuma demanda fica sem data.
   - Idempotente: rodar de novo não duplica a tarefa (tabela `demandas_externas` do banco local).
2. Registrar a demanda em `config/clientes.json -> parceiros[].demandas` (caso, recebida_em,
   prazo_entrega, palavras_chave). É isso que faz o documento do parceiro cair na pasta certa.
3. Entregou: arquivo final em `03_ENTREGUE` e `entregue_em` preenchido no cadastro (a demanda deixa
   de receber documentos automáticos).

## Convenção de nomes de arquivo

| O quê | Padrão | Exemplo |
|---|---|---|
| Documento em geral | `AAAA-MM-DD_TIPO_descricao-curta.ext` | `2026-11-18_CNIS-E-VINCULOS_extrato-cnis.pdf` |
| Documento sem pasta definida | `AAAA-MM-DD_DOC-CLIENTE_<legenda>.ext` | `2026-11-18_DOC-CLIENTE_foto-documento.jpg` |
| Documento do parceiro | `AAAA-MM-DD_DOC-PARCEIRO_<legenda>.ext` | |
| Peça (minuta) | `MINUTA - TIPO - CLIENTE - Nº DO PROCESSO - AAAA-MM-DD.docx` | `MINUTA - PETICAO INICIAL - MARIA DA SILVA - 1001234-56.2026.4.01.3300 - 2026-11-18.docx` |
| Peça protocolada | `TIPO - CLIENTE - Nº DO PROCESSO - AAAA-MM-DD.docx/.pdf` | |
| Comprovante de Pix | `AAAA-MM-DD_COMPROVANTE_<favorecido>.pdf` | `2026-12-05_COMPROVANTE_equipe-barbara.pdf` |
| Relatório financeiro | `AAAA-MM-DD_relatorio_financeiro.md/.xlsx` | |
| Relatório da controladoria | `AAAA-MM-DD_relatorio-controladoria.md` | |

Regras: data sempre `AAAA-MM-DD` na frente (ordena sozinho); sem `/ \ : * ? " < > |`; descrição
curta, sem acento, com hífen (o script faz isso). Arquivo com o mesmo nome e conteúdo diferente
nunca é sobrescrito: o novo vira `<nome> (2).ext`.

## Como o documento recebido chega à pasta (`arquivar_documento.py`)

O escritório não tem CRM de WhatsApp com API: a Bárbara salva o anexo (do e-mail ou do WhatsApp)
e roda o script dizendo de quem é (`--cliente`, `--parceiro`, `--telefone` ou `--email`).

1. Remetente sem cadastro → `00_ESCRITORIO/ENTRADA_DOCUMENTOS`.
2. Advogado parceiro → pasta da demanda (palavra-chave ou única demanda aberta) ou `99_A_CLASSIFICAR` do parceiro.
3. Nº de processo (CNJ) na legenda ou no nome do arquivo → `08_PROCESSO_JUDICIAL/<processo>`.
4. Palavra-chave do tipo de documento → subpasta (`estrutura_pastas.json -> palavras_chave`, na
   ordem: PPP/LTCAT antes de "laudo"; CNIS/CTPS/"contrato de trabalho" antes de "contrato").
5. Fora disso → `99_A_CLASSIFICAR`, com tarefa no Notion para alguém classificar.

Em todos os casos sai a tarefa `[DOCUMENTO] Documento recebido - <cliente> - <pasta>` (ou
`[CALCULO EXTERNO] ...` para parceiro), com o caminho no OneDrive e prazo de 1 dia útil.

## POPs e checklists

Os POPs e checklists citam estes nomes de pasta. Se um nome mudar no `estrutura_pastas.json`,
atualize também `pops/README.md`.
