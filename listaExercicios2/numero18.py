'''18 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos 
são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o 
Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa 
que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa 
deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora 
é 5 e a quantidade de hora é 220.
Salário Bruto: (5 * 220) : R$ 1100,00
(-) IR (5%) : R$ 55,00 
(-) INSS ( 10%) : R$ 110,00
FGTS (11%) : R$ 121,00
Total de descontos : R$ 165,00
Salário Liquido : R$ 935,00 '''

valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas
fgts = salario_bruto * 0.11

if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.1
else:
    ir = salario_bruto * 0.2

inss = salario_bruto * 0.1
sindicato = salario_bruto * 0.03
total_descontos = ir + inss + sindicato
salario_liquido = salario_bruto - total_descontos

print("Salário Bruto: (" + str(valor_hora) + " * " + str(horas_trabalhadas) + ") : R$ " + str(round(salario_bruto, 2)))
print("(-) IR (" + str(int(ir/salario_bruto*100)) + "%) : R$ " + str(round(ir, 2)))
print("(-) INSS (10%) : R$ " + str(round(inss, 2)))
print("(-) Sindicato (3%) : R$ " + str(round(sindicato, 2)))
print("FGTS (11%) : R$ " + str(round(fgts, 2)))
print("Total de descontos : R$ " + str(round(total_descontos, 2)))
print("Salário Líquido : R$ " + str(round(salario_liquido, 2)))
