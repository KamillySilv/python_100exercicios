'''61 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a
quantidade de números impares.'''

numeros = []

for i in range(6):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

pares = 0
impares = 0

for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"A quantidade de números pares é: {pares}")
print(f"A quantidade de números ímpares é: {impares}")
