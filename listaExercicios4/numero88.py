'''88 - Máquina de café
Uma máquina de vender café funciona da seguinte forma: o usuário seleciona um tipo de café, insere algumas
notas ou moedas na máquina e, se a quantia paga for suficiente para pagar o café desejado, a máquina enche um
copo descartável com o tipo de café selecionado e dá o troco em moedas. Faça um programa para imitar esse
comportamento: o usuário informa qual é o tipo de café desejado e o valor pago, e o seu programa deve dizer qual
deve ser o valor do troco e quantas moedas são necessárias para pagar esse troco. Considere a existência de
moedas com os seguintes valores: R$ 1.00, R$ 0.50, R$ 0.25, R$ 0.10, R$ 0.05 e R$ 0.01.A tabela de preços é
dada abaixo...'''

moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
precos = {"Cafe normal": 1.05, "Cafe expresso": 1.52, "Capuccino": 2.17, "Mocaccino": 2.36}

cafe = input("Digite o tipo de café desejado: ")
valor_pago = float(input("Digite o valor pago: "))

if valor_pago >= precos[cafe]:
    troco = valor_pago - precos[cafe]
    print("O troco a ser devolvido é de R$ {:.2f}".format(troco))
    for moeda in moedas:
        quantidade = int(troco // moeda)
        if quantidade > 0:
            print("Quantidade de moedas de R$ {:.2f}: {}".format(moeda, quantidade))
            troco = round(troco % moeda, 2)
            if troco == 0:
                break
else:
    print("Valor pago insuficiente para o café desejado!")
