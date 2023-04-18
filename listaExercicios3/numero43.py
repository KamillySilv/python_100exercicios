'''43 - Dani tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu poupar. Faça um
algoritmo para ler a quantidade de cada tipo de moeda, e imprimir o valor total economizado, em reais. Considere
que existam moedas de 1, 5, 10, 25 e 50 centavos, e ainda moedas de 1 real. Não havendo moeda de um tipo, a
quantidade respectiva é zero. '''

um_centavo = int(input("Digite a quantidade de moedas de 1 centavo: "))
cinco_centavos = int(input("Digite a quantidade de 5 centavos: "))
dez_centavos = int(input("Digite a quantidade de 10 centavos: "))
vinte_e_cinco_centavos = int(input("Digite a quantidade de 25 centavos: "))
cinquenta_centavos = int(input("Digite a quantidade de 50 centavos: "))
um_real = int(input("Digite a quantidade de 1 real: "))

total = (um_centavo * 0.01) + (cinco_centavos * 0.05) + (dez_centavos * 0.10) + (vinte_e_cinco_centavos * 0.25) + (cinquenta_centavos * 0.50) + (um_real * 1.00)

print("O valor total economizado é de R$ {:.2f}".format(total))
