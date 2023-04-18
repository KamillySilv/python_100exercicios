'''22 -Faça um algoritmo que receba o preço de um 
produto, calcule e mostre o novo preço, sabendo-se que este sofreu um desconto de 10%. '''

preco = float(input("Digite o preço do produto: "))

novo_preco = preco * 0.9

print(f"O novo preço do produto com desconto é R$ {novo_preco:.2f}")
