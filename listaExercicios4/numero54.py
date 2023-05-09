'''54- Ler diversos números inteiros e exibir quantas vezes o número 50 foi informado. O valor 0 é o código de fim
de entrada.'''

contador = 0
num = int(input("Digite um número (ou 0 para parar): "))
while num != 0:
    if num == 50:
        contador += 1
    num = int(input("Digite um número (ou 0 para parar): "))
print("O número 50 foi digitado", contador, "vezes")