'''26 - Um brechó revende produtos usados, e fixa o preço de 
venda de cada produto conforme o valor de sua aquisição: Se o 
preço de aquisição de um produto é menor que R$ 50,00, ele 
deve ser vendido por um preço 45% maior, caso contrário o lucro 
será de 30%. Sabendo disso, faça um algoritmo que leia o valor 
de aquisição de um produto e mostre o seu valor de venda. '''

valor_primario = float(input("Valor de aquisição do produto: "))

if valor_primario < 50:
    valor_venda = valor_primario * 1.45
else:
    valor_venda = valor_primario * 1.3

print(f"Valor de venda do produto: R${valor_venda:.2f}")
