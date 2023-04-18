'''25 - Uma fábrica de camisetas produz os tamanhos pequeno, 
médio e grande, cada uma sendo vendida respectivamente por 
R$10,00, R$12,00 e R$15,00. Faça um algoritmo em que o 
usuário forneça a quantidade de camisetas pequenas, médias e 
grandes referentes a uma venda, o algoritmo informe qual o valor 
total da compra. '''

qtd_pequenas = int(input("Quantidade de camisetas pequenas: "))
qtd_medias = int(input("Quantidade de camisetas médias: "))
qtd_grandes = int(input("Quantidade de camisetas grandes: "))

valor_total = qtd_pequenas * 10 + qtd_medias * 12 + qtd_grandes * 15

print(f"Valor total da compra: R${valor_total:.2f}")
