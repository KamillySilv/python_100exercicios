'''75 - Faça um Programaque leia um vetor de 10 números reais e mostre-os na ordem inversa.'''

numeros = [0] * 10

for i in range(10):
    numeros[i] = float(input(f"Digite o {i+1}º número: "))

print("Valores na ordem inversa:")
for i in range(9, -1, -1):
    print(numeros[i])
