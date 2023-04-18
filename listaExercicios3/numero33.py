'''33 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
• par ou ímpar;
• positivo ou negativo;
• inteiro ou decimal.'''

num1 = float(input("Digite o seu primeiro número: "))
num2 = float(input("Digite o seu segundo número: "))

operacao = input("Qual operação matemática deseja realizar? Digite + para soma, - para subtração, * para multiplicação ou / para divisão: ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2
else:
    print("Operação inválida.")
    exit()

if resultado % 2 == 0:
    tipo_num = "par"
else:
    tipo_num = "ímpar"

if resultado >= 0:
    sinal_num = "positivo"
else:
    sinal_num = "negativo"

if resultado.is_integer():
    tipo_valor = "inteiro"
else:
    tipo_valor = "decimal"

print("O resultado da sua operação é:", resultado)
print("O número é ", tipo_num)
print("O número é ", sinal_num)
print("O número é ", tipo_valor)