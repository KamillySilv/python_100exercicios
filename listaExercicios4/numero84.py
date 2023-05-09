'''84 - Escreva um algoritmo que leia um vetor com 10 posições de números inteiros. Em seguida receba um novo
valor do usuário e verifique se este valor se encontra no vetor'''

nums = []
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    nums.append(numero)

novo_num = int(input("Digite um novo número inteiro: "))

if novo_num in nums:
    print("O valor", novo_num, "está no vetor.")
else:
    print("O valor", novo_num, "não está no vetor.")
