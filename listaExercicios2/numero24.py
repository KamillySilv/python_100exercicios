'''24 - A lanchonete GostoSoft vende apenas um tipo de sanduíche, 
cujo recheio inclui duas fatias de queijo, uma fatia de presunto e 
uma rodela de hambúrguer. Sabendo que cada fatia de queijo ou 
presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 
100 gramas, faça um algoritmo em que o dono forneça a 
quantidade de sanduíches a fazer, e a máquina informe as 
quantidades (em quilos) de queijo, presunto e carne necessários 
para compra. '''

quant_sanduiches = int(input("Quantidade de sanduíches a fazer: "))
quant_queijo = quant_sanduiches * 2 * 50 / 1000
quant_presunto = quant_sanduiches * 1 * 50 / 1000
quant_carne = quant_sanduiches * 1 * 100 / 1000

print(f"Quantidade de queijo necessário: {quant_queijo:.2f} kg")
print(f"Quantidade de presunto necessário: {quant_presunto:.2f} kg")
print(f"Quantidade de carne necessário: {quant_carne:.2f} kg")
