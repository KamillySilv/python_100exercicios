'''100 - Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados
em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma
função para gerar numeros aleatórios, simulando os lançamentos dos dados.'''

import random
def lancar_dado():
    return random.randint(1, 6)
results = []
for i in range(100):
    results.append(lancar_dado())

cont = [0, 0, 0, 0, 0, 0]
for result in results:
    cont[result-1] += 1

for i in range(6):
    print(f"O valor {i+1} foi conseguido {cont[i]} vezes.")

