# Faya Barreiros Advocacia — previdenciário e cálculos

Pacote de implantação Casal da IA para o escritório da Dra. Faya Barreiros (Salvador/BA).

- **Comece por aqui:** abra a pasta no Claude Code e diga **"execute o repo"** (ou `/executar-repo`). O roteiro está
  em `INSTALAR.md`.
- **Contexto completo:** `CLAUDE.md`. **Plano e pendências:** `PROJETO_IMPLANTACAO.md`.
- **Conferir que está tudo de pé:** `python verificar.py` → `PACOTE OK`.
- **Ver o painel de cálculos agora, com dados fictícios:** `python automacoes/painel/servidor.py --exemplo` e abrir
  `http://127.0.0.1:8765/painel` (usuário `faya`, senha `exemplo`).

Nenhum dado de cliente está neste repositório: os modelos de peça foram anonimizados e as credenciais ficam em
`config/.env` (fora do git).
