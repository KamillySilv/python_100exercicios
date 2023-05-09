'''92 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoasobre um crime.As perguntas são:
• "Telefonoupara a vítima?"
• "Esteve no local do crime?"
• "Mora perto da vítima?"
• "Devia para a vítima?"
• "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da
pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado
como "Inocente"'''

perguntas = ["Você telefonou para a vítima?", "Esteve no local do crime?",
             "Mora perto da vítima?", "Você devia para a vítima?",
             "Já trabalhou com a vítima?"]

respostas = []
for pergunta in perguntas:
    resposta = input(pergunta + " (s/n): ")
    if resposta.lower() == "s":
        respostas.append(True)
    else:
        respostas.append(False)

respostas_positivas = sum(respostas)
if respostas_positivas == 2:
    print("Suspeita")
elif 3 <= respostas_positivas <= 4:
    print("Cúmplice")
elif respostas_positivas == 5:
    print("Assassino")
else:
    print("Inocente")
