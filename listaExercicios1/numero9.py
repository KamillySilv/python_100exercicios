'''9 - Faça um algoritmo que leia o nome de um
aluno, o nome da disciplina, nota de 3 provas e
calcule a média desse aluno e verifique se o
aluno foi aprovado. Sabendo que para ser
aprovado a média deverá ser maior ou igual a
6,0.
Posteriormente imprima o resultado de cada
variável linha abaixo de linha. '''

nome_aluno = input("Digite o nome do aluno: ")
nome_disciplina = input("Digite o nome da disciplina: ")
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))

media = (nota1 + nota2 + nota3) / 3
aprovado = media >= 6

print("Nome do aluno:", nome_aluno)
print("Nome da disciplina:", nome_disciplina)
print("Nota da primeira prova:", nota1)
print("Nota da segunda prova:", nota2)
print("Nota da terceira prova:", nota3)
print("Média do aluno:", media)

if aprovado:
    print("O aluno foi aprovado!")
else:
    print("O aluno foi reprovado.")
