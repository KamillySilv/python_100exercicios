'''99 - Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos
valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.'''

vtr1 = []
vtr2 = []
for i in range(10):
    vlr1 = int(input(f"Digite o {i+1}º valor do primeiro vetor: "))
    vtr1.append(vlr1)
    vlr2 = int(input(f"Digite o {i+1}º valor do segundo vetor: "))
    vtr2.append(vlr2)

vtr3 = []
for i in range(10):
    vtr3.append(vtr1[i])
    vtr3.append(vtr2[i])

print("Terceiro vetor:", vtr3)
