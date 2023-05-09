'''77 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as
consoantes.'''

letras = []
consoantes = []

for i in range(10):
    letra = input(f"Digite a letra {i+1}: ")
    letras.append(letra.lower())

for letra in letras:
    if letra.isalpha() and letra not in "aeiou":
        consoantes.append(letra)

print(f"Foram lidas {len(consoantes)} consoantes.")
print("As consoantes lidas foram:", ", ".join(consoantes))
