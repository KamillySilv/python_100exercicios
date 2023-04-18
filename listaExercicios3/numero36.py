'''36 - O cardápio da lanchonete Burgão é o seguinte:
ESPECIFICAÇÃO CÓDIGO PREÇO
Cachorro Quente 100 R$ 11,20
Ovo Simples 101 R$ 8,30
Bauru com Ovo 102 R$ 11,50
Hambúrguer 103 R$ 16,20
Refrigerante 201 R$ 6,00
Suco 202 R$ 7,50
Água Mineral 203 R$ 4,70
Escreva um algoritmo que leia o código de um sanduíche e de uma bebida, e mostre o valor a pagar pelo cliente.
Assuma as entradas corretas:'''

precos = {
    100: 11.20,
    101: 8.30,
    102: 11.50,
    103: 16.20,
    201: 6.00,
    202: 7.50,
    203: 4.70
}

codigo_sanduiche = int(input("Digite o código do sanduíche: "))
codigo_bebida = int(input("Digite o código da bebida: "))

valor_sanduiche = precos[codigo_sanduiche]
valor_bebida = precos[codigo_bebida]
valor_total = valor_sanduiche + valor_bebida

print("Valor total a pagar: R$ {:.2f}".format(valor_total))
