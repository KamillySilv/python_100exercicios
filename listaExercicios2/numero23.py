'''23 - A granja TecFrango possui um controle automatizado de 
cada frango da sua produção. No pé direito do frango há um anel 
com um chip de identificação, no pé esquerdo são dois anéis para 
indicar o tipo de alimento que ele deve consumir. Sabendo que o 
anel com chip custa R$ 4,00 e o anel de alimento custa R$ 3,50, 
faça um algoritmo para calcular o gasto total da granja (com base 
na quantidade de frangos digitada pelo usuário) para marcar todos 
os seus frangos. '''

quant_frangos = int(input("Digite a quantidade de frangos na produção: "))
custo_anel_identificacao = 4 * quant_frangos
custo_anel_alimento = 2 * 3.5 * quant_frangos

custo_total = custo_anel_identificacao + custo_anel_alimento
print("O gasto total da granja para marcar todos os frangos é de R$", round(custo_total, 2))
