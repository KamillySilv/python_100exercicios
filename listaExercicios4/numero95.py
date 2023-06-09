'''95 - A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de
arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos
usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele
conseguiugerar o seguinte arquivo, chamado "usuarios.txt":
alexandre 456123789
anderson 1245698456
antonio 123456456
carlos 91257581
cesar 987458
rosemary 789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere
um relatório, chamado "relatório.txt", no seguinte formato:ACME Inc. Uso do espaço em disco
pelos usuários'''

with open('usuarios.txt', 'r') as arq:
    dados = arq.readlines()

usuarios = {}
espaco_total = 0
for dado in dados:
    usuario, espaco = dado.split()
    espaco = int(espaco)
    usuarios[usuario] = espaco
    espaco_total += espaco

usuarios_ordenados = sorted(usuarios.items(), key=lambda x: x[1], reverse=True)
with open('relatorio.txt', 'w') as arq:
    arq.write('ACME Inc.             Uso do espaço em disco pelos usuários\n')
    arq.write('--------------------------------------------------------------\n')
    arq.write('Nr.  Usuário        Espaço utilizado     % do uso\n')
    i = 1
    for usuario, espaco in usuarios_ordenados:
        porcentagem = (espaco / espaco_total) * 100
        arq.write('{:<4} {:<15} {:>12.2f} MB {:>12.2f}%\n'.format(i, usuario, espaco/1024**2, porcentagem))
        i += 1
    arq.write('\nEspaço total ocupado: {:.2f} MB'.format(espaco_total/1024**2))
