'''58- Faça um algoritmo que mostre um Menu com opções de um cardápio de restaurante para uma pessoa
(Coloque no mínimo 5 opções e máximo 10 opções de cardápio. Ex: Bife acebolado R$15,00; Lasanha R$25,00).
A pessoa vai escolher o prato desejado e após escolher o prato, o algoritmo deverá fazer a seguinte pergunta ao
usuário, “Aceita pagar a gorjeta do garçom 10% sobre o valor do prato”. Se o usuário aceitar, mostrar o valor final
(valor do prato + 10%), caso contrário, mostrar o valor final (somente o valor do prato).'''

cardapio = {"Bife acebolado": 15.00, "Lasanha": 25.00, "Frango à parmegiana": 20.00, "Filé mignon": 30.00, "Pizza": 35.00}
print("----- Cardápio -----")
for prato, preco in cardapio.items():
    print(prato, "- R$", preco)

prato_escolhido = input("\nQual prato você deseja? ")
if prato_escolhido in cardapio:
    valor_prato = cardapio[prato_escolhido]
    print("Valor do prato:", valor_prato)

    opcao_gorjeta = input("Aceita pagar a gorjeta do garçom 10% sobre o valor do prato? (s/n) ")
    if opcao_gorjeta == "s":
        valor_final = valor_prato * 1.1
        print("Valor final com gorjeta: R$", valor_final)
    else:
        print("Valor final sem gorjeta: R$", valor_prato)

else:
    print("Prato não encontrado no cardápio.")