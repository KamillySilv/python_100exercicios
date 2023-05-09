'''51- Ler diversos números e exibir qual foi a soma. O valor -999 é o código de fim da entrada.'''

soma = 0
num = int(input("Digite um número (-999 para parar): "))
while num != -999:
    soma += num
    num = int(input("Digite um número (-999 para parar): "))
print("A soma dos números digitados é", soma)