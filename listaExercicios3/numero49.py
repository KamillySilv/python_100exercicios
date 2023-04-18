'''49 - Elaborar um programa que apresente o valor da conversão em real (R$) de um valor lido em dólar (US$). O
programa deve solicitar o valor da cotação do dólar. '''

cotacao_dolar = float(input("Digite a cotação atual do dólar: "))
valor_dolar = float(input("Digite o valor em dólar: "))

valor_real = valor_dolar * cotacao_dolar
print("Valor em real: R$ {:.2f}".format(valor_real))
