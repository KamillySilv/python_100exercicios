'''55 - Ler 20 números e exibir qual foi o menor e o maior informados.'''

numeros = []
for i in range(4):
    num = int(input("Digite um número: "))
    numeros.append(num)
menor = min(numeros)
maior = max(numeros)

print("O menor número digitado foi:", menor)
print("O maior número digitado foi:", maior)