'''83 - Escreva um algoritmo que solicite ao usuário a entrada de 5 números, e que exiba o somatório desses
números na tela. Após exibir a soma, o programa deve mostrar também os números que o usuário digitou, um por
linha.'''

numeros = []

for i in range(5):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

soma = 0
for numero in numeros:
    soma += numero
print("A soma dos números  digitados é:", soma)

print("Os números digitados foram:")
for numero in numeros:
    print(numero)
