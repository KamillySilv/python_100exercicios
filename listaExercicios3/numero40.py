'''40 - João recebeu seu salário de R$ 1200,00 e precisa pagar duas contas (C1=R$ 200,00 e C2=R$120,00) que
estão atrasadas. Como as contas estão atrasadas, João terá de pagar multa de 2% sobre cada conta. Faça um
algoritmo que calcule e mostre quanto restará do salário do João. '''

salario = 1200.0
multa = 0.02

conta1 = 200.0
conta2 = 120.0

total_contas = conta1*(1+multa) + conta2*(1+multa)
restante_salario = salario - total_contas

print("Restará R$ {:.2f} do salário do João após o pagamento das contas.".format(restante_salario))
