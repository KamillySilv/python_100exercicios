'''46 - Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e estado civil
seja “CASADA”, solicitar o tempo de casada (anos).'''

nome = input("Digite o nome da pessoa: ")
sexo = input("Digite o sexo da pessoa (M/F): ")
estado_civil = input("Digite o estado civil da pessoa(se casada usar 'CASADA'): ")

if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = int(input("Digite o tempo de casamento (em anos): "))
    print("A pessoa", nome, "é casada há", tempo_casada, "anos.")
else:
    print("A pessoa", nome, "não atende aos critérios de sexo e/ou estado civil especificados.")
