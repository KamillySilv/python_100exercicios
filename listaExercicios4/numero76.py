'''76 - Faça um Programaque leia 4 notas, mostre as notas e a médiana tela.'''

notas = []

for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("Notas: ", notas)
print(f"Média: {media:.2f}")
