'''96 - Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de
fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200
mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode
aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um
número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
• necessitada esfera;
• necessita de limpeza; a. necessita troca do cabo ou conector; a. quebrado ou inutilizado Uma
identificação igual a zero encerra o programa.Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100
Situação Quantidade Percentual
1- necessita da esfera 40 40%
2- necessita de limpeza 30 30%
3- necessita troca do cabo ou conector 15 15%'''

mouses = {"necessita da esfera": 0, "necessita de limpeza": 0, 
          "necessita troca do cabo ou conector": 0, "quebrado ou inutilizado": 0}

while True:
    identificacao = int(input("Digite o número de identificação do mouse (0 para sair): "))
    if identificacao == 0:
        break
    elif identificacao < 0 or identificacao > 200:
        print("Identificação inválida. Digite um número entre 1 e 200.")
        continue
    estado = int(input("Digite o estado do mouse (1 - necessita da esfera, 2 - necessita de limpeza, 3 - necessita troca do cabo ou conector, 4 - quebrado ou inutilizado): "))
    if estado < 1 or estado > 4:
        print("Estado inválido. Digite um número entre 1 e 4.")
        continue
    if estado == 1:
        mouses["necessita da esfera"] += 1
    elif estado == 2:
        mouses["necessita de limpeza"] += 1
    elif estado == 3:
        mouses["necessita troca do cabo ou conector"] += 1
    elif estado == 4:
        mouses["quebrado ou inutilizado"] += 1

quantidade_total = sum(mouses.values())
print("Quantidade de mouses:", quantidade_total)
print("Situação", " " * 10, "Quantidade", "Percentual")
print("1- necessita da esfera", " " * 2, mouses["necessita da esfera"], "{:.0%}".format(mouses["necessita da esfera"]/quantidade_total))
print("2- necessita de limpeza", " " * 2, mouses["necessita de limpeza"], "{:.0%}".format(mouses["necessita de limpeza"]/quantidade_total))
print("3- necessita troca do cabo ou conector", mouses["necessita troca do cabo ou conector"], "{:.0%}".format(mouses["necessita troca do cabo ou conector"]/quantidade_total))
print("4- quebrado ou inutilizado", " " * 2, mouses["quebrado ou inutilizado"], "{:.0%}".format(mouses["quebrado ou inutilizado"]/quantidade_total))
