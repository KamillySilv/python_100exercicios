'''79 - Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada
aluno, imprima o número de alunos com média maior ou igual a 7.0.'''

aprovados = 0
medias = []

for i in range(3):
    notas = []
    for j in range(2):
        nota = float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
        notas.append(nota)
    
    soma = 0
    for nota in notas:
        soma += nota
    
    media = soma / len(notas)
    medias.append(media)
    if media >= 7.0:
        aprovados += 1

print(f"O número de alunos que tem média maior ou igual a 7.0 é {aprovados}.")
