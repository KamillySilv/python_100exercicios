'''28 - Faça um Programa que peça 2 números inteiros e um número
real. Calcule e mostre:
•o produto do dobro do primeiro com metade do segundo .
•a soma do triplo do primeiro com o terceiro.
•o terceiro elevado ao cubo. '''

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = float(input("Digite o número real: "))

calculo1 = (2 * num1) * (num2 / 2)
calculo2 = (3 * num1) + num3
calculo3 = num3 ** 3

print("O produto do dobro do primeiro com metade do segundo é:", calculo1)
print("A soma do triplo do primeiro com o terceiro é:", calculo2)
print("O terceiro elevado ao cubo é:", calculo3)
