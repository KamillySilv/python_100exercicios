'''87 - Crie um algoritmo para uma empresa de transportes que, a partir do peso de uma encomenda fornecida pelo
usuário, calcule o preço da remessaconforme aseguinte tabela..'''

peso = float(input("Informe o peso da encomenda (em kg): "))

if peso <= 0.5:
    valor = 1.1
elif peso <= 2:
    valor = 2.2
elif peso <= 9.9:
    valor = 3.7 * peso
else:
    valor = 5 + 3.8 * (peso - 10)

print(f"O valor da remessa é R$ {valor:.2f}")
