---
description: Gera o SaaS da Dra. Faya - o sistema web do escritório (base white-label Casal da IA) com o pacote previdenciário dentro e o portal de cálculos para advogados parceiros
---

Monte o **SaaS da Dra. Faya Barreiros**: o sistema web do escritório na nuvem, a partir da base white-label do Casal
da IA, com tudo deste repositório dentro, mais o **portal de cálculos para advogados parceiros** como produto.

## Regras
- Trabalhe numa pasta **nova, ao lado** desta: `../FAYA_BARREIROS_SAAS`. Não misture com este repositório.
- Não invente dado da Dra. Faya (CNPJ, OAB, endereço e e-mails estão no `CLAUDE.md`; o resto fica `[A CONFIRMAR]`).
- Nada de nome, CPF, processo ou texto de cliente real de outro escritório. Ao terminar, faça uma varredura de
  vazamento (nomes do PAB e de outros clientes, CPF, CNJ) no projeto inteiro.
- Não publique, não suba em VPS e não exponha porta sem o "pode" de quem pediu. Repositório novo: pergunte se é
  público ou privado antes do push.

## Passos
1. **Base:** `git clone https://github.com/pabadvogados-hub/sistema-base-virgem ../FAYA_BARREIROS_SAAS`. Leia o
   README da base inteiro e siga o roteiro "montar cliente novo" (`deploy/personalizar.py --nome "Faya Barreiros
   Advocacia" --curto "Faya" --cidade "Salvador" --uf "BA"`, equipe, `.env`, `escritorio-config.js`).
2. **Identidade:** bordô `#4E151C` e dourado `#B8955A` do timbrado (`previdenciario/timbrado/timbrado_faya.docx`);
   equipe = Dra. Faya (titular/admin, assina e revisa), Bárbara (secretária) e estagiário(a) `[A CONFIRMAR nome]`.
   Só previdenciário e cálculos: desligue ou esconda os módulos de outras áreas (trabalhista, tributário, cível).
3. **Pacote previdenciário dentro do sistema** (fonte: este repositório):
   - DNA e modelos de peça: `previdenciario/dna/DNA_PECAS.md` e os 41 modelos de `previdenciario/pecas/` no módulo
     de peças do sistema, no timbrado dela, com a mesma trava de pendência (`{{campo}}`, `[CONFERIR]`).
   - Kit de representação (`modelos/01` a `05`) como modelos de contratação.
   - Base de leis (`previdenciario/leis/banco_leis.db`) consultável pela IA do sistema.
   - Calculadora EC 103 (`previdenciario/calculos/`) como tela de simulação, com o aviso de que é apoio.
   - POPs, checklists e mensagens (`pops/`, `checklists/`, `mensagens/`) onde a base tiver lugar para eles.
4. **Portal de cálculos para parceiros (o produto SaaS):** leve `automacoes/painel/` para dentro do sistema web:
   - área interna = o painel (fila por prazo com semáforo, status, faturamento, ranking de parceiros);
   - área do parceiro com **cadastro e login próprios**: o advogado pede o cálculo, anexa documentos, acompanha o
     status, baixa o cálculo entregue e paga (Asaas, `externalReference` = protocolo);
   - regra do prazo: interno = prazo do parceiro − 2 dias úteis (POP-PREV-06); cada parceiro só vê o que é dele.
5. **Integrações dela:** Asaas, Notion, OneDrive e DJEN pelas OABs BA 64723 e SP 308385, aproveitando
   `automacoes/comum/`. Não use ADVBOX. Tramitação Inteligente continua esqueleto.
6. **Teste:** suba o sistema localmente e confira todos os módulos. Teste a instalação a partir de um `git clone`
   limpo, não da pasta de trabalho. Crie testes do portal de parceiros (login, isolamento entre parceiros, pedido
   com anexo, prazo, cobrança simulada).
7. **Entrega:** commit local e um `SAAS.md` com o que foi feito, como subir na VPS (domínio e HTTPS `[A CONFIRMAR]`),
   o que ficou em modo seguro e o que falta da Dra. Faya. Pergunte antes de criar o repositório e de qualquer deploy.

$ARGUMENTS
