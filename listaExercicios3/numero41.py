'''41 - Três amigos, Joceyr, Thiago e Alexandre. decidiram rachar igualmente a conta de um bar. Faça um algoritmo
para ler o valor total da conta e imprimir quanto cada um deve pagar, mas faça com que Joceyr e Thiago não
paguem centavos. Ex: uma conta de R$101,53 resulta em R$33,00 para Joceyr, R$33,00 para Thiago e R$35,53
para Alexandre. '''

valor_total = float(input("Digite o valor total da conta: "))

valor_por_pessoa = valor_total / 3
valor_joceyr_thiago = round(valor_por_pessoa)
valor_alexandre = valor_total - 2*valor_joceyr_thiago

print("Joceyr e Thiago devem pagar R$ ", valor_joceyr_thiago)
print("Alexandre deve pagar R$ {:.2f}".format(valor_alexandre))
