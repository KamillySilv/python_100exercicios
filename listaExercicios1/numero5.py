'''5 - Faça um algoritmo que leia o nome do aluno,
o nome da disciplina, notas de 3 provas e calcule
a média desse aluno.
Posteriormente imprima o resultado de cada
variável linha abaixo de linha. '''

nome = input("Digite o nome do aluno: ")
disciplina = input("Digite o nome da disciplina: ")
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))
media = (nota1 + nota2 + nota3) / 3

print("Nome do aluno:", nome)
print("Disciplina:", disciplina)
print("Notas das provas:", nota1, nota2, nota3)
print("Média do aluno:", media)