'''93 - Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após
isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês
elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).'''

meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

temperaturas = []
soma_temperaturas = 0
for i in range(12):
    temperatura = float(input(f"Digite a temperatura média de {meses[i+1]}: "))
    temperaturas.append(temperatura)
    soma_temperaturas += temperatura

media_anual = soma_temperaturas / 12
print("Meses com temperaturas acima da média anual:")
for i, temperatura in enumerate(temperaturas):
    if temperatura > media_anual:
        print(f"{meses[i+1]}: {temperatura:.2f}°C")
