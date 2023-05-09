'''97 - Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL,
VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses
carros faz com um litro de combustível.Calcule e mostre:
• O modelo do carro mais econômico;
• Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000
quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela
de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios
e podem mudar a cada execução do programa.'''

carros = ['Fusca', 'Gol', 'Uno', 'Vectra']
consumos = [7, 10, 12.5, 9]

print("Comparativo de Consumo de Combustível")
for i in range(len(carros)):
    print(f"Veículo {i+1}\nNome: {carros[i]}\nKm por litro: {consumos[i]}\n")

mais_economico = consumos.index(max(consumos))
print(f"O modelo mais econômico é o {carros[mais_economico]}.")

print("Relatório final:")
for i in range(len(carros)):
    distancia = 1000
    litros = distancia / consumos[i]
    preco = litros * 2.25
    print(f"{i+1}- {carros[i]} - {distancia:.1f} km - {litros:.2f} litros - R$ {preco:.2f}")
