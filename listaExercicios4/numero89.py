'''89 - Fatura da Águas Guariroba –as regras que a Águas Guariroba utiliza para cobrar a fatura de água e esgoto de
clientes residenciais estão expressas na tabela abaixo. Repare que existem 6 faixas de consumo e que cada uma
possui uma franquia de consumo e um valor diferente para cada metro cúbico (m³) consumido.'''

consumo = float(input("Informe o consumo de água em m³: "))

faixas = [(5, 37.47), (5, 1.16), (5, 6.46), (5, 6.49), (10, 6.55), (0, 11.08)]

fatura = 0.0
for i, faixa in enumerate(faixas):
    if consumo <= 0:
        break
    elif consumo <= faixa[0]:
        fatura += consumo * faixa[1]
        consumo = 0
    else:
        fatura += faixa[0] * faixa[1]
        consumo -= faixa[0]
        
agua = fatura
esgoto = 0.8 * agua

total = agua + esgoto
print(f"Valor da água consumida: R$ {agua:.2f}")
print(f"Valor do esgoto: R$ {esgoto:.2f}")
print(f"Valor total da fatura: R$ {total:.2f}")
