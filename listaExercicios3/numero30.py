'''30 - João Papo-de-Pescador, homem de bem, comprou um
microcomputador para controlar o rendimento diário de seu
trabalho. Toda vez que ele traz um peso de peixes maior que o
estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a
variável peso (peso de peixes) e calcule o excesso. Gravar na
variável excesso a quantidade de quilos além do limite e na
variável multa o valor da multa que João deverá pagar. Imprima os
dados do programa com as mensagens adequadas. '''

peso = float(input("Digite o peso dos peixes: "))
limite = 50.0
excesso = max(peso - limite, 0.0)
multa = excesso * 4.0

if excesso == 0:
    print("Não houve excesso de peso.")
else:
    print(f"Houve um excesso de {excesso:.2f} kg de peixes.")
    print(f"A multa a ser paga é de R$ {multa:.2f}.")