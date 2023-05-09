'''65 - Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da
dívida, valor dos juros, quantidade de parcelas e valor da parcela. Os juros e a quantidade de parcelas seguem a
tabela abaixo:
Quantidade de Parcelas % de Juros sobre o valor inicial da dívida
1 0
3 10
6 15
9 20
12 25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da Parcela
R$ 1.000,00 0 1 R$ 1.000,00'''

divida = float(input("Digite o valor da dívida: R$ "))
print("Quantidade de Parcelas\t% de Juros\tValor da Parcela")
print("1\t\t\t0%\t\tR$ {:.2f}".format(divida))
print("3\t\t\t10%\t\tR$ {:.2f}".format((divida*1.1)/3))
print("6\t\t\t15%\t\tR$ {:.2f}".format((divida*1.15)/6))
print("9\t\t\t20%\t\tR$ {:.2f}".format((divida*1.2)/9))
print("12\t\t\t25%\t\tR$ {:.2f}".format((divida*1.25)/12))
