'''15 -Faça um Programa que verifique se uma letra 
digitada é "F" ou "M". Conforme a letra escreva: F 
- Feminino, M – Masculino ou Sexo Inválido.'''

letra = input("Digite uma letra: ")

if letra == "F" or letra == "f":
  print("Feminino")
elif letra == "M" or letra == "m":
  print("Masculino")

else:
  print("Sexo Inválido")