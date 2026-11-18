# 02 — Contrato de honorários previdenciário (êxito, com ou sem honorários iniciais)

> **Bloco de preenchimento — não faz parte do documento.** Texto entre `INICIO_DOCUMENTO` e `FIM_DOCUMENTO`.
> **Fonte:** os dois contratos que a Dra. Faya usa ("Contrato de honorários - Êxito" e "- Êxito e Salários",
> Kit de Representação, 18/10/2026). Os dois são o mesmo texto; a variante "Salários" só acrescenta os honorários
> iniciais de análise de viabilidade. Aqui viraram um modelo só, com o bloco `{{#honorarios_iniciais}}`.

| Campo | O que é | De onde vem |
|---|---|---|
| `{{cliente_nome}}`, `{{cliente_nacionalidade}}`, `{{cliente_estado_civil}}`, `{{cliente_profissao}}` | Qualificação | Ficha de cadastro |
| `{{cliente_data_nascimento}}` | Data de nascimento | Documento de identidade |
| `{{cliente_rg}}` / `{{cliente_rg_orgao}}` / `{{cliente_cpf}}` | Documentos | Documento de identidade |
| `{{cliente_endereco}}` | Endereço completo com CEP | Comprovante de residência |
| `{{objeto}}` | O serviço, completando "consistindo no ...". Ex.: "requerimento e acompanhamento, na via administrativa e judicial, de aposentadoria por tempo de contribuição" | Triagem (POP-PREV-01) |
| Bloco `{{#honorarios_iniciais}}` | Liga a variante "Êxito e Salários" | Decisão da Dra. Faya no fechamento |
| `{{honorarios_iniciais}}` | Valor com extenso. Política atual: R$ 300,00 (trezentos reais) | Política de honorários (README, seção 4) |
| `{{honorarios_implantacao}}` | Ex.: "4 (quatro) salários de benefício" | Idem |
| `{{honorarios_exito}}` | Ex.: "30% (trinta por cento)" | Idem |
| `{{dados_bancarios_oficiais}}` | Os ÚNICOS dados para pagamento (hoje: "PIX - CNPJ (Banco C6)") | `config/escritorio.json` (não versionado) |
| `{{escritorio_*}}`, `{{titular_*}}`, `{{foro_comarca}}` | Dados fixos | README, seção 3 |
| `{{cidade_assinatura}}` / `{{data_assinatura}}` | Local e data | Gerado na emissão |

**Notas de uso**

1. Cláusula Quarta (golpe do falso advogado) é marca do escritório: não retirar. Ela se apoia no "guia de boas-vindas"
   entregue com o contrato (ver `mensagens/MSG-04`).
2. Cláusula Terceira (desconto de até 30% do líquido mensal) cita EREsp 1.874.222/DF, Súmula Vinculante 47 e art. 833, IV,
   do CPC: são as citações que ela já usa. `[CONFERIR]` vigência antes de cada revisão anual do modelo.
3. Assinatura: o escritório assina pela **Tramitação Inteligente**. Enquanto não houver integração, o contrato gerado vai
   para a plataforma à mão (`automacoes/comum/tramitacao.py` é esqueleto).
4. Os originais têm duas testemunhas sem campos: mantido.

---

<!-- INICIO_DOCUMENTO -->

# CONTRATO DE PRESTAÇÃO DE SERVIÇOS ADVOCATÍCIOS

Pelo presente instrumento particular, as partes abaixo qualificadas:

**CONTRATANTE:** {{cliente_nome}}, {{cliente_nacionalidade}}, {{cliente_estado_civil}}, {{cliente_profissao}}, nascido(a) em {{cliente_data_nascimento}}, portador(a) do RG nº {{cliente_rg}} {{cliente_rg_orgao}}, inscrito(a) no CPF sob o nº {{cliente_cpf}}, residente e domiciliado(a) à {{cliente_endereco}};

**CONTRATADA:** {{escritorio_razao_social}}, pessoa jurídica inscrita no CNPJ {{escritorio_cnpj}}, por sua representante, {{titular_nome}}, brasileira, {{titular_estado_civil}}, advogada, inscrita na {{titular_oab}}, com endereço eletrônico {{titular_email_contratos}}, e endereço comercial à {{escritorio_endereco}};

Têm entre si justo e contratado o seguinte:

## CLÁUSULA PRIMEIRA – DO OBJETO

O presente contrato tem como objeto a prestação de serviços advocatícios na área previdenciária, consistindo no {{objeto}}.

## CLÁUSULA SEGUNDA – DOS HONORÁRIOS

{{#honorarios_iniciais}}a) Honorários Iniciais: Pelos serviços ora contratados, o(a) CONTRATANTE pagará à CONTRATADA a quantia de {{honorarios_iniciais}} a título de honorários iniciais para atendimento e análise de viabilidade, devidos no ato da assinatura deste instrumento.{{/honorarios_iniciais}}

1. Honorários da Implantação: Em caso de concessão do benefício, seja na via administrativa ou na via judicial, a importância de {{honorarios_implantacao}}, assim entendidos como o valor da renda mensal inicial calculada pelo INSS.

E:

2. Honorários de êxito: {{honorarios_exito}} sobre os valores recebidos de forma retroativa, inclusive RPV ou precatório, se houver.

c) Forma de Pagamento: Os pagamentos serão realizados mediante transferência bancária ou outra forma acordada entre as partes, observado o disposto nas Cláusulas Terceira e Quarta deste instrumento.

## CLÁUSULA TERCEIRA – DA AUTORIZAÇÃO PARA DESCONTO DE HONORÁRIOS

O(A) CONTRATANTE, de forma livre, expressa e consciente, AUTORIZA o desconto dos honorários advocatícios devidos à CONTRATADA e não quitados nos respectivos vencimentos, sobre seu salário, remuneração, provento ou benefício previdenciário, limitado a 30% (trinta por cento) do valor líquido mensal por ele(a) percebido, até a integral quitação do débito.

§ 1º – Do Limite e da Preservação da Subsistência. O limite de 30% (trinta por cento) foi livremente pactuado para preservar o mínimo necessário à subsistência digna do(a) CONTRATANTE e de sua família, em consonância com o art. 833, IV, do Código de Processo Civil e com o entendimento da Corte Especial do Superior Tribunal de Justiça que admite a relativização da impenhorabilidade de verbas remuneratórias quando preservada a dignidade do devedor (EREsp 1.874.222/DF).

§ 2º – Da Natureza Alimentar. As partes reconhecem que os honorários advocatícios possuem natureza alimentar, nos termos do art. 85, § 14, do CPC e da Súmula Vinculante nº 47 do STF.

§ 3º – Da Quitação e da Cessação. A CONTRATADA fornecerá recibo de cada valor descontado e, quitado integralmente o débito, o desconto cessará de imediato, comprometendo-se a CONTRATADA a restituir, em até 10 (dez) dias, qualquer valor eventualmente recebido a maior.

§ 4º – Do Título Executivo e dos Honorários de Êxito. A presente autorização não afasta a natureza de título executivo extrajudicial deste contrato (art. 24 da Lei nº 8.906/94 e art. 784, III, do CPC), nem o direito da CONTRATADA de requerer o destaque dos honorários de êxito diretamente da RPV ou do precatório, nos termos do art. 22, § 4º, da Lei nº 8.906/94. Em eventual execução judicial, o(a) CONTRATANTE concorda que a constrição sobre verbas salariais ou previdenciárias observe o mesmo limite de 30% (trinta por cento).

## CLÁUSULA QUARTA – DA SEGURANÇA NOS PAGAMENTOS E PREVENÇÃO AO GOLPE DO FALSO ADVOGADO

Com o objetivo de proteger o CONTRATANTE contra fraudes e golpes, fica expressamente estabelecido que:

**ATENÇÃO: TODO E QUALQUER PAGAMENTO referente a este contrato somente poderá ser realizado em conta bancária de TITULARIDADE EXCLUSIVA da CONTRATADA ({{titular_nome}}).** Qualquer solicitação de pagamento em conta de terceiros deve ser imediatamente recusada e comunicada à CONTRATADA pelos canais oficiais antes de qualquer transferência.

§ 1º – Do Golpe do Falso Advogado. O(A) CONTRATANTE declara ter sido informado(a) sobre a prática criminosa conhecida como "golpe do falso advogado", na qual terceiros mal-intencionados se apresentam falsamente como advogados ou representantes da banca contratada — muitas vezes utilizando nome, foto, logotipo e dados verdadeiros do processo, obtidos em consultas públicas — solicitando pagamentos indevidos em nome da CONTRATADA, por meios como aplicativos de mensagem, e-mails ou ligações não verificadas.

§ 2º – Da Isenção de Responsabilidade. A CONTRATADA não se responsabiliza, em hipótese alguma, por pagamentos realizados pelo CONTRATANTE em contas bancárias que não sejam de sua titularidade exclusiva, ainda que o solicitante alegue ser funcionário, parceiro, estagiário ou representante do escritório. A CONTRATADA não possui prepostos autorizados a receber valores em seu nome por meios não oficiais.

§ 3º – Dos Canais Oficiais. Toda e qualquer comunicação sobre cobranças, pagamentos ou dados bancários somente terá validade se efetuada diretamente pela própria CONTRATADA por meio dos canais oficiais constantes no guia de boas-vindas, entregue junto com o presente instrumento. Em caso de dúvida sobre a autenticidade de qualquer solicitação de pagamento, o CONTRATANTE deverá entrar em contato com a CONTRATADA pelos meios acima indicados antes de realizar qualquer transferência.

§ 4º – Da Orientação Preventiva. Recomenda-se ao CONTRATANTE que nunca realize pagamentos por solicitação feita exclusivamente por aplicativos de mensagem sem confirmação por outros meios; sempre verifique o nome do titular da conta bancária antes de confirmar qualquer transferência; desconfie de cobranças inesperadas ou em valores divergentes dos estipulados neste contrato e, em caso de suspeita, registre boletim de ocorrência junto à autoridade policial competente.

§ 5º – A CONTRATADA NUNCA SOLICITA:

1. Pagamento de taxas, custas, impostos, "honorários antecipados" ou qualquer valor para "liberar" alvará, RPV, precatório, benefício ou indenização;
2. Selfies, fotos de documentos ou reconhecimento facial por aplicativo de mensagem;
3. Pagamentos via boleto ou PIX em nome de terceiros, inclusive pessoas físicas ou empresas "parceiras".

Qualquer contato com esse teor é FRAUDE e deve ser ignorado e comunicado à CONTRATADA.

§ 6º – Dos Dados Bancários Oficiais. Os únicos dados bancários válidos para pagamentos decorrentes deste contrato são: {{dados_bancarios_oficiais}}. A CONTRATADA não altera dados bancários por mensagem; eventual alteração somente terá validade mediante aditivo contratual assinado pelas partes.

§ 7º – Da Confirmação de Resultado do Processo. Notícias sobre ganho de causa, liberação de valores ou "urgências" recebidas de números ou endereços desconhecidos não devem ser consideradas antes da confirmação direta com a CONTRATADA pelos canais oficiais indicados no § 3º desta cláusula.

## CLÁUSULA QUINTA – DAS OBRIGAÇÕES DAS PARTES

À CONTRATADA compete:

a) Prestar os serviços com diligência e ética, conforme o Código de Ética da OAB;
b) Manter o(a) CONTRATANTE informado(a) sobre o andamento do processo;
c) Zelar pela confidencialidade das informações e documentos do CONTRATANTE.

Ao(À) CONTRATANTE compete:

a) Fornecer todos os documentos e informações necessários ao bom andamento da demanda;
b) Efetuar o pagamento dos honorários conforme estipulado neste contrato;
c) Não alterar a senha do MEU INSS sem prévio aviso à CONTRATADA;
d) O Contratante será informado acerca dos andamentos inerentes à contratação e avanços processuais, sendo que todo e qualquer contato será feito dentro do horário comercial (09h00 – 18h00), não havendo atendimento aos finais de semana, salvo em casos de urgência.

Parágrafo único: Os serviços profissionais ora contratados são serviços de meio, e não de resultado, razão pela qual, caso o pleito seja julgado improcedente e não comporte ou não recomende recurso, o ADVOGADO não poderá ser responsabilizado para fins indenizatórios ou criminais, salvo se agir com culpa ou dolo efetivamente comprovados.

Em assim sendo, caso os serviços aqui contratados não alcancem o sucesso desejado ou sejam julgados improcedentes e não comportem ou não recomendem recurso, os ônus decorrentes da sucumbência serão suportados integralmente pelo CONTRATANTE.

## CLÁUSULA SEXTA – DA RESCISÃO

O presente contrato poderá ser rescindido por qualquer das partes, mediante notificação por escrito, com antecedência mínima de 10 (dez) dias, sendo devidos os honorários proporcionais ao trabalho já realizado.

## CLÁUSULA SÉTIMA – DA LEI GERAL DE PROTEÇÃO DE DADOS (LGPD)

Considerando a Lei Geral de Proteção de Dados (Lei nº 13.709/2018), a CONTRATADA se obriga na observância e no cumprimento das regras quanto à proteção de dados, inclusive no tratamento de dados pessoais e sensíveis, de acordo com a necessidade e/ou obrigação legal de coleta dos dados.

Parágrafo Primeiro: A CONTRATADA executará os trabalhos a partir das premissas da LGPD, em especial os princípios da finalidade, adequação, transparência, livre acesso, segurança, prevenção e não discriminação no tratamento dos dados.

Parágrafo Segundo: A CONTRATADA esclarece que possui política interna para tratamento em caso de vazamento de dados, garantindo a confidencialidade dos dados coletados e o atendimento à finalidade do presente contrato.

## CLÁUSULA OITAVA – DA SUCESSÃO

O presente instrumento obriga as partes, seus herdeiros e sucessores, a qualquer título. O falecimento do(a) CONTRATANTE não extingue as obrigações já assumidas, em especial o pagamento dos honorários advocatícios contratados.

§ 1º – Dos Honorários em Caso de Falecimento. Ocorrendo o óbito do(a) CONTRATANTE no curso do processo administrativo ou judicial, os honorários de êxito previstos na Cláusula Segunda incidirão integralmente sobre os valores que vierem a ser recebidos por seus dependentes, herdeiros ou sucessores, inclusive valores não recebidos em vida (art. 112 da Lei nº 8.213/91) e eventual pensão por morte decorrente do benefício postulado, ficando estes solidariamente responsáveis pelo pagamento, até o limite das forças da herança e dos valores efetivamente recebidos.

§ 2º – Da Habilitação dos Sucessores. Os herdeiros e sucessores comprometem-se a comunicar o óbito à CONTRATADA em até 30 (trinta) dias e a fornecer os documentos necessários à habilitação no processo (arts. 687 a 692 do CPC), podendo, mediante novo instrumento, manter a CONTRATADA no patrocínio da causa. A recusa em fazê-lo não afasta o direito aos honorários proporcionais ao trabalho já realizado e aos de êxito sobre os valores obtidos em razão desse trabalho.

§ 3º – Do Destaque dos Honorários. Fica desde já autorizado o destaque dos honorários contratuais diretamente da RPV, do precatório ou do alvará expedido em favor dos sucessores, nos termos do art. 22, § 4º, da Lei nº 8.906/94.

§ 4º – Da Sucessão da CONTRATADA. Na hipótese de falecimento ou incapacidade civil da advogada responsável, os honorários proporcionais ao trabalho realizado serão devidos a seus sucessores ou representantes legais, nos termos do art. 24, § 2º, da Lei nº 8.906/94.

## CLÁUSULA NONA – DO FORO

Fica eleito o foro da Comarca de {{foro_comarca}}, com renúncia de qualquer outro, por mais privilegiado que seja, para dirimir quaisquer controvérsias oriundas deste contrato.

{{cidade_assinatura}}, {{data_assinatura}}.

&nbsp;

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**CONTRATANTE:** {{cliente_nome}}
CPF: {{cliente_cpf}}

&nbsp;

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**{{escritorio_razao_social}}**
CNPJ {{escritorio_cnpj}}
{{titular_nome}}
{{titular_oab}}

**TESTEMUNHAS:**

1. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ CPF:
2. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ CPF:

<!-- FIM_DOCUMENTO -->
