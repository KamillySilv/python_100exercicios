'''19 -Faça um Programa que peça os 3 lados de 
um triângulo. Indique, caso os lados formem um 
triângulo, se o mesmo é: equilátero, isósceles ou 
escaleno.  '''

lado1 = float(input("Digite o primeiro lado do seu triângulo: "))
lado2 = float(input("Digite o segundo lado do seu triângulo: "))
lado3 = float(input("Digite o terceiro lado do seu triângulo: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print("O seu triângulo é equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O seu triângulo é isósceles.")
    else:
        print("O seu triângulo é escaleno.")
else:
    print("Os lados informados não formam um triângulo.")
