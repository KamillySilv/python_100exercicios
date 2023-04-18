'''38 - O restaurante a quilo Sabor em Quilo cobra R$59,00 por cada quilo de refeição. Escreva um algoritmo que
leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar. Assuma que a balança já
desconte o peso do prato. '''

peso_prato = float(input("Digite o peso do prato (em kg): "))

valor_pagar = peso_prato * 59
print("O valor a pagar é R$ {:.2f}".format(valor_pagar))
