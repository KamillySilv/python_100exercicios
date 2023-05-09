'''85 - Escrever um algoritmo para ler a quantidade de horas/aula de duas professor e o valor por hora recebido por
cada uma. Mostrar na tela qual dos professores tem salário total maior.'''

hrs_aula1 = int(input("Digite a quantidade de horas do professor 1: "))
valor_hr1 = float(input("Digite o valor por hora do professor 1: "))
hrs_aula2 = int(input("Digite a quantidade de horas do professor 2: "))
valor_hr2 = float(input("Digite o valor por hora do professor 2: "))

salario1 = hrs_aula1 * valor_hr1
salario2 = hrs_aula2 * valor_hr2
if salario1 > salario2:
    print("O professor 1 tem salário total maior.")
elif salario2 > salario1:
    print("O professor 2 tem salário total maior.")
else:
    print("Os dois professores têm salários iguais.")
