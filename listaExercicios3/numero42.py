'''42 - A fábrica de refrigerantes Gui-Cola vende seu produto em três formatos:
Lata de 350 ml; Garrafa de 600 ml; Garrafa de 2 litros. Se um comerciante compra uma determinada quantidade de cada formato, faça um algoritmo para calcular
quantos litros de refrigerante ele comprou.'''

qtd_lata = int(input("Digite a quantidade de latas de 350ml: "))
qtd_garrafa_600 = int(input("Digite a quantidade de garrafas de 600ml: "))
qtd_garrafa_2l = int(input("Digite a quantidade de garrafas de 2 litros: "))

total_litros = (qtd_lata * 0.35) + (qtd_garrafa_600 * 0.6) + (qtd_garrafa_2l * 2)
print("O total de litros de refrigerante comprado é de", total_litros, "litros.")
