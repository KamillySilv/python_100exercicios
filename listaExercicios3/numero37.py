'''37 - A padaria Super Pão vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia.
Cada pãozinho custa R$ 1,00 e a broa custa R$ 3,50. Ao final do dia, o dono quer saber quanto arrecadou com a
venda dos pães e broas (juntos), e quanto deve guardar numa conta de poupança (10% do total arrecadado).
Você foi contratado para fazer os cálculos para o dono. Com base nestes fatos, faça um algoritmo para ler as
quantidades de pães e de broas, e depois calcular os dados solicitados. '''

qtd_paes = int(input("Digite a quantidade de pães vendidos: "))
qtd_broas = int(input("Digite a quantidade de broas vendidas: "))

valor_total = qtd_paes * 1.0 + qtd_broas * 3.5
valor_poupanca = valor_total * 0.1

print(f"Valor total das vendas: R$ {valor_total:.2f}")
print(f"Valor a ser guardado na conta de poupança: R$ {valor_poupanca:.2f}")
