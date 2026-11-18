# -*- coding: utf-8 -*-
"""Camada comum das automacoes do escritorio Faya Barreiros Sociedade Individual de Advocacia
(Dra. Faya Barreiros, Salvador/BA - previdenciario e calculos previdenciarios).

config      -> .env, JSONs de config/, pastas de dados, --dry-run/--go
db          -> SQLite local (estado: o que ja foi enviado, emitido, agendado, arquivado)
asaas       -> API Asaas v3 (cobranca, notificacoes, NF, transferencias, extrato)
notion      -> API do Notion (processos, prazos/tarefas, clientes) - pela doc publica, NAO testado no workspace dela
tramitacao  -> Tramitacao Inteligente (assinatura e andamento) - ESQUELETO, configurado() = False
mensageria  -> modelos {{chave}} e fila de mensagens para a Barbara enviar (sem CRM de WhatsApp)
drive       -> OneDrive/SharePoint por pasta local sincronizada (ONEDRIVE_RAIZ): pastas idempotentes,
               copia de arquivo, docx->pdf pelo LibreOffice
estrutura   -> caminhos das pastas (cliente, processo, demanda externa de calculo, financeiro)
nomes       -> convencao de nomes de pasta e arquivo
cadastros   -> config/clientes.json (clientes e advogados parceiros), colaboradores, despesas
"""
