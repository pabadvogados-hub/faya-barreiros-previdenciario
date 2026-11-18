# 03 — Declaração de hipossuficiência econômica

> **Bloco de preenchimento — não faz parte do documento.** Texto entre `INICIO_DOCUMENTO` e `FIM_DOCUMENTO`.
> **Fonte:** declaração do "Kit de Representação" da Dra. Faya (18/10/2026), com os dados do cliente em campos.

| Campo | O que é | De onde vem |
|---|---|---|
| `{{cliente_nome}}`, `{{cliente_nacionalidade}}` | Nome e nacionalidade | Documento de identidade |
| `{{cliente_cpf}}`, `{{cliente_rg}}`, `{{cliente_rg_orgao}}` | Documentos | Documento de identidade |
| `{{cliente_endereco}}` | Endereço completo com CEP | Comprovante de residência |
| `{{cidade_assinatura}}` / `{{data_assinatura}}` | Local e data | Gerado na emissão |

**Notas de uso**

1. Acompanha a inicial quando a peça pede justiça gratuita (Lei 1.060/50 e art. 98 e seguintes do CPC): é o caso da maioria
   dos modelos em `previdenciario/pecas/iniciais/`.
2. Quem assina é o cliente. Se a renda dele for incompatível com a gratuidade, a advogada decide antes de juntar.

---

<!-- INICIO_DOCUMENTO -->

# DECLARAÇÃO DE HIPOSSUFICIÊNCIA ECONÔMICA

{{cliente_nome}}, {{cliente_nacionalidade}}, inscrito(a) no CPF nº {{cliente_cpf}}, portador(a) da cédula de identidade nº {{cliente_rg}}-{{cliente_rg_orgao}}, residente e domiciliado(a) na {{cliente_endereco}},

DECLARO, sob as penas da lei, que sou pobre no sentido legal do termo, não tendo condições para prover as despesas do processo sem privar-me dos recursos indispensáveis ao próprio sustento e da família.

Responsabiliza-se o(a) infra-assinado(a) pelo teor da presente declaração, ciente de que sujeitar-se-á às sanções civis e criminais em caso de falsidade.

Para clareza e os devidos fins de direito, firmo a presente declaração.

{{cidade_assinatura}}, {{data_assinatura}}.

&nbsp;

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**{{cliente_nome}}**

<!-- FIM_DOCUMENTO -->
