'''98 - Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de
organizações:"Qual o melhor Sistema Operacional para uso em servidores?"
As possíveis respostas são:
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da
mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não
deverão ser aceitos valores além dos válidos para o programa (0 a 6).'''

votos = [0, 0, 0, 0, 0, 0]

print("1- Windows Server \n2- Unix \n3- Linux \n4- Netware \n5- Mac OS \n6- Outro")

while True:
    voto = int(input("Digite o seu voto (0 para encerrar): "))
    if voto == 0:
        break
    elif voto < 1 or voto > 6:
        print("Voto inválido! Digite novamente")
    else:
        votos[voto-1] += 1

total_votos = sum(votos)

print("Sistema Operacional\tVotos\t%")
print("-------------------\t-----\t---")
print(f"Windows Server\t\t{votos[0]}\t{(votos[0]/total_votos)*100:.2f}%")
print(f"Unix\t\t\t{votos[1]}\t{(votos[1]/total_votos)*100:.2f}%")
print(f"Linux\t\t\t{votos[2]}\t{(votos[2]/total_votos)*100:.2f}%")
print(f"Netware\t\t\t{votos[3]}\t{(votos[3]/total_votos)*100:.2f}%")
print(f"Mac OS\t\t\t{votos[4]}\t{(votos[4]/total_votos)*100:.2f}%")
print(f"Outro\t\t\t{votos[5]}\t{(votos[5]/total_votos)*100:.2f}%")
print("-------------------\t-----\t---")
print(f"Total\t\t\t{total_votos}")

mr_voto = max(votos)
if votos.count(mr_voto) == 1:
    so_vencedor = votos.index(mr_voto)
    if so_vencedor == 0:
        print("O Sistema Operacional vencedor foi: Windows Server")
    elif so_vencedor == 1:
        print("O Sistema Operacional vencedor foi: Unix")
    elif so_vencedor == 2:
        print("O Sistema Operacional vencedor foi: Linux")
    elif so_vencedor == 3:
        print("O Sistema Operacional vencedor foi: Netware")
    elif so_vencedor == 4:
        print("O Sistema Operacional vencedor foi: Mac OS")
    else:
        print("O Sistema Operacional vencedor foi: Outro")
else:
    print("Não houve um Sistema Operacional vencedor.")
