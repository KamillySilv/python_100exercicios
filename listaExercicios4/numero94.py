'''94 - Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais
de 13 anos possuem altura inferior à média de altura desses alunos.'''

idades = []
alturas = []
for i in range(3):
    idade = int(input(f"Digite a idade do {i+1}º aluno: "))
    altura = float(input(f"Digite a altura do {i+1}º aluno (em metros): "))
    idades.append(idade)
    alturas.append(altura)

media_altura = sum(alturas) / len(alturas)
count = 0
for i in range(3):
    if idades[i] > 13 and alturas[i] < media_altura:
        count += 1

print(f"Há {count} alunos com altura inferior a media entre os alunos")

