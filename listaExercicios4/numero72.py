'''72 - Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo
a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta
em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a
média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo
abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7
Resultado final:'''

nome = input("Digite o nome do atleta: ")
notas = []

for i in range(7):
    notas.append(float(input("Digite a nota do jurado %d: " % (i+1))))
notas.sort()

notas = notas[1:-1]
media = sum(notas) / len(notas)

print("\nResultado final:")
print("Atleta: %s" % nome)
print("Melhor nota: %.1f" % max(notas))
print("Pior nota: %.1f" % min(notas))
print("Média: %.2f" % media)
