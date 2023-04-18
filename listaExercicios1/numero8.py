'''8 - Faça um algoritmo que calcule o custo
estimado de uma viagem de carro.
Posteriormente imprima o resultado. '''

distancia = float(input("Digite a distância a ser percorrida (em km): "))
consumo = float(input("Digite o consumo médio do carro (em km/l): "))
preco = float(input("Digite o preço do combustível (em R$/litro): "))
litros = distancia / consumo
custo = litros * preco

print("O gasto estimado com a viagem é de R$", custo)