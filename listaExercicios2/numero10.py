'''10 - Faça um algoritmo que verifique se o número 
digitado é menor, maior ou igual a 10 e apresente 
a mensagem referente ao número.'''

number = int(input("digite seu numero: "))

if number < 10:
  print("O numero é menor que 10")
elif number > 10:
  print("O numero é maior que 10")
else:
  print("O numero é igual a 10")
