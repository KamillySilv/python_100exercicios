''''64 - Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram
obtidos os seguintes dados:
• Código da cidade;
• Número de veículos de passeio (em 1999);
• Número de acidentes de trânsito com vítimas (em 1999).
Deseja-se saber:
• Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
• Qual a média de veículos nas cinco cidades juntas;
• Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.'''

cidades = {}

soma_veiculos = 0
soma_acidentes = 0
qtd_cidades_menos_2000_veiculos = 0

for i in range(5):
    codigo = input("Digite o código da cidade (duas letras maiúsculas): ")
    veiculos = int(input("Digite o número de veículos de passeio em 1999: "))
    acidentes = int(input("Digite o número de acidentes de trânsito com vítimas em 1999: "))
    
    cidades[codigo] = {'veiculos': veiculos, 'acidentes': acidentes}
    
    soma_veiculos += veiculos
    soma_acidentes += acidentes
    
    if veiculos < 2000:
        qtd_cidades_menos_2000_veiculos += 1
media_veiculos = soma_veiculos / 5
media_acidentes_menos_2000 = soma_acidentes / qtd_cidades_menos_2000_veiculos

maior_indice = 0
menor_indice = float('inf')
cidade_maior_indice = ''
cidade_menor_indice = ''

for codigo, dados in cidades.items():
    indice = dados['acidentes'] / dados['veiculos']
    
    if indice > maior_indice:
        maior_indice = indice
        cidade_maior_indice = codigo
    if indice < menor_indice:
        menor_indice = indice
        cidade_menor_indice = codigo

print("Maior índice de acidentes de trânsito: {:.2f}, na cidade {}".format(maior_indice, cidade_maior_indice))
print("Menor índice de acidentes de trânsito: {:.2f}, na cidade {}".format(menor_indice, cidade_menor_indice))
print("Média de veículos de passeio nas cidades: {:.2f}".format(media_veiculos))
print("Média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio: {:.2f}".format(media_acidentes_menos_2000))
