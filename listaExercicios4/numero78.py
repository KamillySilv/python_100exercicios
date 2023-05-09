'''78 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no
vetor PAR e os números IMPARES no vetor impar. Imprimaos três vetores.'''

numeros = []
pares = []
impares = []

for i in range(4):
    num = int(input(f"Digite o número {i+1}: "))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Números digitados:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)
