'''66 - Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de
crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.'''

populacao_a = 80000
populacao_b = 200000
taxa_cresc_a = 0.03
taxa_cresc_b = 0.015
anos = 0

while populacao_a < populacao_b:
    populacao_a += int(populacao_a * taxa_cresc_a)
    populacao_b += int(populacao_b * taxa_cresc_b)
    anos += 1

print(f"Serão necessários {anos} anos para a população do país A ultrapassar ou igualar a população de B.")
