'''69 - Faça um programa que leia 5 números e informe a soma e a média dos números'''

soma = 0
for i in range(5):
    num = float(input("Digite um número: "))
    soma += num

media = soma / 5

print("A soma dos números é:", soma)
print("A média dos números é:", media)
