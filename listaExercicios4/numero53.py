'''53 - Ler diversos números e exibir quantos números ímpares foram digitados. Considere o valor - 999 como
código fim de entrada.'''

contador = 0
num = int(input("Digite um número (ou -999 para parar): "))
while num != -999:
    if num % 2 == 1:
        contador += 1
    num = int(input("Digite um número (ou -999 para parar): "))
print("Foram digitados", contador, "números ímpares")