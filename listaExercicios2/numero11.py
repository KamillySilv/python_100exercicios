'''11 - Faça um algoritmo que o usuário possa digitar o seu nome e 
a sua idade. Utilizando a tabela a baixo, verifique em qual item se 
enquadra a idade da pessoa e escreva a mensagem:
(nome) está com (idade) e pela tabela é considerado um (tipo).IDADE TIPO
0-2 anos bebê
3-11 anos Criança
12-21 anos Jovem
22-64 anos Adulto
65-100 anos Idoso
Acima de 101 anos Muito velhinho.'''

name = input("Digite o seu nome: ")
age = int(input("Digite sua idade: "))

if age >= 0  and age <= 2:
  tipo = "bebê"
elif age >= 3 and age <= 11:
  tipo = "criança"
elif age >= 12 and age <= 21:
  tipo = "joven"
elif age >= 22 and age <= 64:
      tipo = "adulto"
elif age >= 63 and age <= 100:
    tipo = "idoso"
else:
    tipo = "muito velhinho"

print (name + " está com " + str(age) + " anos e pela tabela é considerado um " + tipo)
  