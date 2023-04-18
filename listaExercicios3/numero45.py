'''45 - Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre: a) a
idade dessa pessoa em anos; b) a idade dessa pessoa em meses; c) a idade dessa pessoa em dias; d) a idade
dessa pessoa em semanas. '''

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade_anos = ano_atual - ano_nascimento
idade_meses = idade_anos * 12
idade_dias = idade_anos * 365
idade_semanas = idade_anos * 52

print("Idade em anos:", idade_anos)
print("Idade em meses:", idade_meses)
print("Idade em dias:", idade_dias)
print("Idade em semanas:", idade_semanas)
