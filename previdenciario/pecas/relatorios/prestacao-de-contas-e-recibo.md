---
tipo: prestacao-de-contas-e-recibo
titulo: RELATÓRIO - PRESTAÇÃO DE CONTAS E RECIBO
grupo: relatorio
objetivo: Prestar contas ao cliente após a concessão do benefício (protocolo, carta de concessão, honorários contratados, forma de pagamento), encerrar o contrato e emitir o recibo de honorários
documentos_necessarios:
  - Comprovante de protocolo do requerimento no INSS
  - Carta de concessão do benefício
  - Contrato de prestação de serviços (cláusula de honorários)
  - Dados bancários/chave PIX da contratada
campos:
  - CLIENTE_NOME
  - CONTRATADA_NOME
  - ESPECIE_BENEFICIO
  - DATA_PROTOCOLO
  - DATA_CONCESSAO
  - CLAUSULA_HONORARIOS
  - HONORARIOS
  - HONORARIOS_EXTENSO
  - BASE_HONORARIOS
  - TIPO_CHAVE_PIX
  - CHAVE_PIX
  - BANCO
  - TITULAR_CONTA
  - ADVOGADA_NOME
  - ADVOGADA_QUALIFICACAO
  - ADVOGADA_OAB
  - CIDADE
  - DATA_RECIBO
citacoes:
  - nenhuma citação legal no modelo original
---

# PRESTAÇÃO DE CONTAS

**CLIENTE:** {{CLIENTE_NOME}}
**CONTRATADA:** {{CONTRATADA_NOME}}

## RESUMO:

Trata-se de contratação para pedido administrativo de concessão de {{ESPECIE_BENEFICIO}}, em favor do(a) segurado(a) {{CLIENTE_NOME}}.

O pedido foi realizado junto ao INSS em {{DATA_PROTOCOLO}}, conforme protocolo abaixo:

[INSERIR IMAGEM: comprovante de protocolo do requerimento no INSS]

E foi concedido em {{DATA_CONCESSAO}} conforme carta de concessão abaixo:

[INSERIR IMAGEM: carta de concessão do benefício]

## DOS HONORÁRIOS

Os honorários que foram firmados entre as partes em contrato de prestação de serviço, na {{CLAUSULA_HONORARIOS}}, acordados da seguinte forma:

[INSERIR IMAGEM: recorte da cláusula de honorários do contrato]

Assim, o valor TOTAL devido será de:

R$ {{HONORARIOS}} – {{HONORARIOS_EXTENSO}} - Referente {{BASE_HONORARIOS}} [no original: "ao valor de uma mensalidade da Renda Mensal Inicial"].

[INSERIR IMAGEM: comprovante do valor que serve de base aos honorários (ex.: RMI na carta de concessão)]

## DA FORMA DE PAGAMENTO

O valor será pago através de transferência via PIX para a chave abaixo:

**CHAVE PIX PARA PAGAMENTO**
{{TIPO_CHAVE_PIX}}: {{CHAVE_PIX}}
{{BANCO}}
{{TITULAR_CONTA}}

## ENCERRAMENTO

Assim, diante da concessão do benefício e liberação do pagamento, dá se por encerrada a prestação de serviços contratada, sendo o objeto do contrato adimplido em sua totalidade.

---

# RECIBO DE PAGAMENTO

Eu, {{ADVOGADA_NOME}}, {{ADVOGADA_QUALIFICACAO}}, advogada inscrita na {{ADVOGADA_OAB}}, declaro que recebi de {{CLIENTE_NOME}} a quantia de R$ {{HONORARIOS}} – {{HONORARIOS_EXTENSO}}, referente à HONORÁRIOS ADVOCATÍCIOS, sob a prestação de serviços junto ao INSS para concessão de benefício de {{ESPECIE_BENEFICIO}}.

{{CIDADE}}, {{DATA_RECIBO}}.

{{ADVOGADA_NOME}}
{{ADVOGADA_OAB}}
