'''63 - Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma
dos valores.'''
n = int(input("Quantidade de números: "))

numeros = []
for i in range(n):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

maior = menor = numeros[0]
soma = 0

for num in numeros:
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Soma dos valores: {soma}")
