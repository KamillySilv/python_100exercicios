'''56 - O programa de fidelidade de uma determinada livraria premia seus clientes de acordo com o número de livros
compradosa cada bimestre.Os pontos são atribuídos da seguinte forma:
•Se um cliente comprar 0 livros, ele ganhará 0 pontos.
•Se um cliente comprar um livro, ele ganhará 5 pontos.
•Se um cliente comprar dois livros, ele ganhará 15 pontos.
•Se um cliente comprar 3 livros, ele ganhará 30 pontos.
•Se um cliente comprar 4 ou mais livros, ele ganhará 60 pontos.
Lista de brindes:
De 20 à 30 pontos o cliente poderá escolher entre: Uma Eco Bag OU Caneta personalizada
De 35-60 pontos o cliente poderá escolher entre: Um livro (com valor máximo de R$30,00) OU Luminária de
cabeceira.
Acima de 65 o cliente poderá escolher entre: 2 livros (com valor máximo de R$100,00)OU Power bank.'''

#livros e pontos
num_livros = int(input("Quantos livros você comprou no último bimestre? "))

if num_livros == 0:
    pontos = 0
elif num_livros == 1:
    pontos = 5
elif num_livros == 2:
    pontos = 15
elif num_livros == 3:
    pontos = 30
else:
    pontos = 60

#brindes
if pontos >= 20 and pontos <= 30:
    print("Você acumulou", pontos, "pontos e pode escolher entre uma Eco Bag ou Caneta personalizada.")
elif pontos >= 35 and pontos <= 59:
    print("Você acumulou", pontos, "pontos e pode escolher entre um livro (com valor máximo de R$30,00) ou Luminária de cabeceira.")
elif pontos == 60:
    print("Você acumulou", pontos, "pontos e pode escolher entre 2 livros (com valor máximo de R$100,00) ou Power bank.")
else:
    print("Você não acumulou pontos suficientes para escolher um brinde.")
