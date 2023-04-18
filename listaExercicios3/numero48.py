'''48 - Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de
etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir para ler qual condição de
pagamento escolhida e efetuar o cálculo adequado.
Código Condição de pagamento:
1 - À vista em dinheiro ou pix, recebe 10% de desconto;
2 - À vista no cartão de crédito, recebe 5% de desconto
3 - Em duas vezes, preço normal de etiqueta sem juros
4 - Em três vezes, preço normal de etiqueta mais juros de 10%. '''

print("Condições de pagamento:")
print("1 - À vista em dinheiro ou pix, recebe 10% de desconto")
print("2 - À vista no cartão de crédito, recebe 5% de desconto")
print("3 - Em duas vezes, preço normal de etiqueta sem juros")
print("4 - Em três vezes, preço normal de etiqueta mais juros de 10%")

preco_etiqueta = float(input("Digite o preço normal na etiqueta do produto: "))
condicao_pagamento = int(input("Digite o caso de apllicação da condição de pagamento: "))

if condicao_pagamento == 1:
    valor_a_pagar = preco_etiqueta * 0.1
    print("Valor a ser pago: R$ {:.2f}".format(valor_a_pagar))
elif condicao_pagamento == 2:
    valor_a_pagar = preco_etiqueta * 0.05
    print("Valor a ser pago: R$ {:.2f}".format(valor_a_pagar))
elif condicao_pagamento == 3:
    valor_a_pagar = preco_etiqueta
    print("Valor a ser pago: R$ {:.2f} em duas vezes de R$ {:.2f}".format(valor_a_pagar, valor_a_pagar/2))
elif condicao_pagamento == 4:
    valor_a_pagar = preco_etiqueta * 1.1
    print("Valor a ser pago: R$ {:.2f} em três vezes de R$ {:.2f}".format(valor_a_pagar, valor_a_pagar/3))
else:
    print("Condição de pagamento inválida. Por favor, digite um código válido.")
