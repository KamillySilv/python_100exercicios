'''73 - Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os 
códigos utilizados são:
1 , 2, 3, 4 - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
• O total de votos para cada candidato;
• O total de votos nulos;
• O total de votos em branco;
• A percentagem de votos nulos sobre o total de votos;
• A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o 
valor zero'''

candidatos = {1: "João", 2: "Pedro", 3: "Maria", 4: "Jose"}
votos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
total_votos = 0

print("Candidatos:")
for codigo, nome in candidatos.items():
    print(f"{codigo} - {nome}")

while True:
    voto = int(input("Digite o código do seu voto ([5] para nulo, [6] para branco ou [0] para encerrar): "))

    if voto == 0:
        break

    if voto in votos:
        votos[voto] += 1
        total_votos += 1
    else:
        print("Código inválido. Voto não computado.")

print("\nResultado da eleição:")
for codigo, nome in candidatos.items():
    print(f"{nome}: {votos[codigo]} votos")

print(f"Votos nulos: {votos[5]}")
print(f"Votos em branco: {votos[6]}")

percentual_nulos = (votos[5] / total_votos) * 100
print(f"Percentual de votos nulos: {percentual_nulos:.2f}%")

percentual_brancos = (votos[6] / total_votos) * 100
print(f"Percentual de votos em branco: {percentual_brancos:.2f}%")

