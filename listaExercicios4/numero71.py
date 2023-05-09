'''71 - Faça um programaque peça um numero inteiro positivo e em seguidamostre este numero invertido.
Exemplo: 12376489 => 98467321'''

num = int(input("Digite um número inteiro positivo: "))
num_invertido = int(str(num)[::-1])
print("O número invertido é:", num_invertido)