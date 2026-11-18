# 01 — Procuração *ad judicia* previdenciária (pessoa física)

> **Bloco de preenchimento — não faz parte do documento.** O texto a gerar é só o que está entre os marcadores
> `INICIO_DOCUMENTO` e `FIM_DOCUMENTO`. Convenções: ver `README.md`.
> **Fonte:** procuração que a Dra. Faya usa hoje ("Kit de Representação", enviado em 18/10/2026), com os dados do
> cliente trocados por campos. O texto é o dela; não reescrever sem o aval dela.

| Campo | O que é | De onde vem |
|---|---|---|
| `{{cliente_nome}}` | Nome completo, sem abreviação | Documento de identidade |
| `{{cliente_nacionalidade}}`, `{{cliente_estado_civil}}`, `{{cliente_profissao}}` | Qualificação | Ficha de cadastro |
| `{{cliente_rg}}` / `{{cliente_rg_orgao}}` | RG e órgão expedidor/UF | Documento de identidade |
| `{{cliente_cpf}}` | CPF | Documento de identidade |
| `{{cliente_endereco}}` | Endereço completo com CEP | Comprovante de residência |
| `{{objeto_acao}}` | Finalidade da ação contra o INSS. Ex.: "concessão de aposentadoria especial" | Triagem (POP-PREV-01) |
| `{{escritorio_*}}`, `{{titular_*}}` | Dados fixos do escritório | `README.md`, seção 3 |
| `{{cidade_assinatura}}` / `{{data_assinatura}}` | Local e data por extenso | Gerado na emissão |

**Notas de uso**

1. Os poderes perante o INSS (Meu INSS, laudos, telas, agendamentos) são o que faz esta procuração ser previdenciária: não
   trocar pela procuração genérica.
2. Os poderes especiais incluem **levantar RPV, alvará e precatório** e **firmar declaração de isenção de IR**: conferem com o
   contrato (destaque dos honorários na RPV/precatório).
3. `[A CONFIRMAR]` Estado civil da Dra. Faya: os contratos dizem "solteira"; uma procuração antiga dizia "casada". Confirmar
   com ela antes de gerar em lote.

---

<!-- INICIO_DOCUMENTO -->

# PROCURAÇÃO "AD JUDICIA"

{{cliente_nome}}, {{cliente_nacionalidade}}, {{cliente_estado_civil}}, {{cliente_profissao}}, portador(a) do RG nº {{cliente_rg}} {{cliente_rg_orgao}}, inscrito(a) no CPF sob nº {{cliente_cpf}}, com endereço residencial na {{cliente_endereco}}, neste ato nomeia e constitui seus bastantes procuradores {{escritorio_razao_social}}, pessoa jurídica inscrita no CNPJ {{escritorio_cnpj}}, por sua representante, {{titular_nome}}, brasileira, {{titular_estado_civil}}, advogada, inscrita na {{titular_oab}}, com endereço eletrônico {{titular_email}}, e endereço comercial à {{escritorio_endereco}}, a quem confere os mais amplos e ilimitados poderes para representá-lo(a) nos órgãos públicos e privados, agências do INSS para obter cópias de expedientes e processos administrativos, acessar laudos sociais e periciais, acessar e manejar extratos, sistemas e telas do INSS, agendar serviços e atendimentos nas agências da autarquia, e ainda para o foro em geral, com cláusula "ad judicia", para funcionar em qualquer Juízo, Instância ou Tribunal, podendo propor contra quem de direito as ações competentes e defendê-lo(a) nas contrárias, seguindo umas e outras até final decisão, usando os recursos legais e acompanhando-os, conferindo-lhe ainda poderes especiais para confessar, desistir, transigir, firmar compromissos ou acordos, firmar declaração de quitação, firmar declaração de isenção de imposto de renda, receber e dar quitação, levantar RPVs, alvarás e precatórios, agindo em conjunto ou separadamente, podendo ainda substabelecer esta a outrem, com ou sem reservas de iguais poderes, dando tudo por bom, firme e valioso, em especial para propositura de ação contra o INSS para {{objeto_acao}}.

{{cidade_assinatura}}, {{data_assinatura}}.

&nbsp;

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**{{cliente_nome}}**

<!-- FIM_DOCUMENTO -->
