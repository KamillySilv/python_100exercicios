'''74 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.'''

numeros = []
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print("Os números digitados foram:")
for num in numeros:
    print(num)
