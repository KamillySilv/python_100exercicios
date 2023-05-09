'''59 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo
compreendido por eles.'''

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 < num2:
    ini = num1
    fim = num2
else:
    ini = num2
    fim = num1

for i in range(ini + 1, fim):
    print(i, end=" ")
