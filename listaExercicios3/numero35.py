'''35 - O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
Até 5 Kg Acima de 5 Kg
File Duplo R$ 34,90 por Kg R$ 35,80 por Kg
Alcatra R$ 44,90 por Kg R$ 46,80 por Kg
Picanha R$ 66,90 por Kg R$ 67,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente
receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a
quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar. '''

print("Promoção de Carnes\n")
print("Tipo de carne disponível:\n[1] - Filé Duplo\n[2] - Alcatra\n[3] - Picanha\n")

tipo_carne = int(input("Digite o número correspondente ao tipo de carne desejado: "))
quantidade = float(input("Digite a quantidade desejada em Kg: "))
cartao_tabajara = input("Pagamento com cartão Tabajara? (S/N): ")

if tipo_carne == 1:
    preco_kg = 34.90
    if quantidade > 5:
        preco_kg = 35.80
    tipo = "Filé Duplo"
elif tipo_carne == 2:
    preco_kg = 44.90
    if quantidade > 5:
        preco_kg = 46.80
    tipo = "Alcatra"
elif tipo_carne == 3:
    preco_kg = 66.90
    if quantidade > 5:
        preco_kg = 67.80
    tipo = "Picanha"
else:
    print("Opção inválida de tipo de carne. Tente novamente.")
    exit()

preco_total = preco_kg * quantidade

if cartao_tabajara.upper() == "S":
    desconto = 0.05 * preco_total
    tipo_pagamento = "Cartão Tabajara"
else:
    desconto = 0
    tipo_pagamento = "Outro cartão / dinheiro"

valor_a_pagar = preco_total - desconto

print("\nCUPOM FISCAL\n")
print(f"Tipo de carne: {tipo}")
print(f"Quantidade: {quantidade:.2f} Kg")
print(f"Preço total: R$ {preco_total:.2f}")
print(f"Tipo de pagamento: {tipo_pagamento}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")
