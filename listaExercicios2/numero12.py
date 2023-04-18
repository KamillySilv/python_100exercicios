'''12 - Faça um algoritmo que verifique se o número 
digitado é positivo ou negativo.'''

num = float(input("Digite o numero: "))

if num > 0:
  print("O numero digitado é positivo")
elif num < 0:
  print("O numero digitado é negativo")
else:
  print("O numero é zero")