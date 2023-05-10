'''81 - Considere os cenários de problemas a serem resolvidos:
1- Um berçário desejainformatizar suas operações.
Quando um bebê nasce, algumas informações são armazenadas sobre ele, tais como: nome, data do nascimento,
peso do nascimento, altura, a mãe deste bebê e o médico que fez seu parto. Para as mães, o berçário também
deseja manter um controle, guardando informações como: nome, endereço, telefone e data de nascimento. Para
os médicos, é importante saber: CRM, nome, telefone celular e especialidade.
Para resolver o cenário 1 faça:
A) Levantamento de requisitos (funcionais e não funcionais);
B) Diagramas UML (Caso de Uso);
C) Documento com levantamento de requisitos e diagramas UML;
D) Algoritmo em python.
E) Apresentação da atividade (Em slides)
F) Ao finalizar a atividade coloque na pasta compartilhada no Microsoft Teams (crie uma pasta com a descrição
“AtivAva1DevAlg”dentro de ambas as pastas dos membros da dupla).'''

nomeBebe = input("Qual o nome da criança? ")
dnBebe = input("Qual a dada de nascimento da criança? ")
pesoNasci = float(input("Qual o peso em KG que a criança nasceu? "))
altura = float(input("Qual a altura em metros da criança "))
nomeMae = input("Qual o nome da mãe? ")
nomeMedico = input("Qual o nome do medico que realizou o parto? ")

endereço = input("Qual o endereço da mãe? ")
telefoneMae = int(input("Qual numero de telefone da mãe"))
dnMae = input("Qual a data de nascimento da mãe? ")
 

crm = int(input("Qual o CRM do medico? "))
telefoneMedico = int(input("Qual o telefone do medico que realizou o parto? "))
especializacao= input("Qual o especialização do medico que fez o parto? ")

print("Dados registrados com sucesso!")