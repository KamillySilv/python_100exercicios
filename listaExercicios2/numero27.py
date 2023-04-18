'''27 - O departamento de Educação Física deseja informatizar este setor e 
colocou à disposição os seguintes dados de 50 alunos:
Matrícula, sexo (M, F), altura (cm) e status físico (1–bom, 2–regular, 3–ruim). Estes dados deverão ser lidos através de uma unidade de entrada qualquer. Calcular e imprimir:
a) A quantidade de alunos do sexo feminino com altura superior a 170 cm.
b) A % de alunos do sexo masculino (em relação ao total de alunos do sexo 
masculino) cujo status físico seja bom. '''

quantMulheres_altas = 0
quantAlunos_bom = 0
quantAlunos_masc_bom = 0

for i in range(50):
    matricula = int(input("Matrícula do aluno: "))
    sexo = input("Sexo do aluno (M/F): ")
    altura = float(input("Altura do aluno (em cm): "))
    status = int(input("Status físico do aluno (1-Bom, 2-Regular, 3-Ruim): "))

    if sexo == "F" and altura > 170:
        quantMulheres_altas += 1
    if status == 1:
        quantAlunos_bom+= 1
        if sexo == "M":
            quantAlunos_masc_bom += 1

porcentagem = (quantAlunos_masc_bom / (50 - quantMulheres_altas)) * 100

print(f"Quantidade de mulheres com altura superior a 170 cm: {quantMulheres_altas}")
print(f"Porcentagem de alunos do sexo masculino com status físico bom: {porcentagem:.2f}%")
