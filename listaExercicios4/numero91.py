'''91 - Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a
entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de
dados, faça:
• Mostre a quantidade de valores que foram lidos;
• Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
• Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
• Calcule e mostre a soma dos valores;
• Calcule e mostre a média dos valores;
• Calcule e mostre a quantidade de valores acima da média calculada;
• Calcule e mostre a quantidade de valores abaixo de sete;
• Encerre o programacom uma mensagem;'''

notas = []
nota = 0

while nota != -1:
    nota = float(input("Digite uma nota (-1 para encerrar): "))
    if nota != -1:
        notas.append(nota)

print("Quantidade de valores lidos:", len(notas))
print("Valores informados:", end=" ")
for n in notas:
    print(n, end=" ")

print("\nValores na ordem inversa:")
for i in range(len(notas) - 1, -1, -1):
    print(notas[i], end=" ")

soma = sum(notas)
print("\nSoma dos valores:", soma)

media = soma / len(notas)
print("Média dos valores:", media)

acima_media = 0
for n in notas:
    if n > media:
        acima_media += 1
print("Quantidade de valores acima da média:", acima_media)

abaixo_sete = 0
for n in notas:
    if n < 7:
        abaixo_sete += 1
print("Quantidade de valores abaixo de 7:", abaixo_sete)
print("Programa encerrado.")
