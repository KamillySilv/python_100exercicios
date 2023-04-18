'''32 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor do saque e
depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100
reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a
quantidade de notas existentes na máquina.
• Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de
50, uma nota de 5 e uma nota de 1;
• Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de
50, quatro notas de 10, uma nota de 5 e quatro notas de 1. '''

valor = int(input("Digite o valor que deseja sacar (entre R$10 e R$600): "))

if valor < 10 or valor > 600:
    print("Valor inválido. O valor mínimo de saque é R$10 e o máximo é R$600.")
else:
    notas_100 = valor // 100
    valor = valor % 100
    
    notas_50 = valor // 50
    valor = valor % 50
    
    notas_10 = valor // 10
    valor = valor % 10
    
    notas_5 = valor // 5
    valor = valor % 5
    
    notas_1 = valor
    
    print("Notas de R$100:", notas_100)
    print("Notas de R$50:", notas_50)
    print("Notas de R$10:", notas_10)
    print("Notas de R$5:", notas_5)
    print("Notas de R$1:", notas_1)
