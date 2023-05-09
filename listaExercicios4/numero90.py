'''90 - Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em
comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por
exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000,
ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos
vendedores receberam salários nos seguintes intervalos de valores:
• $200 - $299
• $300 - $399
• $400 - $499
• $500 - $599
• $600 - $699
• $700 - $799
• $800 - $899
• $900 - $999
• $1000 em diante.'''

salarios = [0] * 10
vendas = [2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000]

for venda in vendas:
    salario = 200 + venda * 0.09
    if salario >= 1000:
        salarios[-1] += 1
    else:
        posicao = int(salario / 100) - 1
        salarios[posicao] += 1

for i in range(len(salarios)):
    if i == 0:
        print("$200 - $299: ", salarios[i])
    elif i == 9:
        print("$1000 em diante: ", salarios[i])
    else:
        print("$" + str((i+1)*100) + " - $" + str((i+2)*100 - 1) + ": ", salarios[i])
