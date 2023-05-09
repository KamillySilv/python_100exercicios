'''86 - Faça um algoritmo que receba o valor do salário de uma pessoa e o valor de um financiamento pretendido.
Caso o financiamento seja menor ou igual a 5 vezes o salário da pessoa, o algoritmo deverá escrever
“Financiamento Concedido"; senão, ele deverá escrever "Financiamento Negado". Independente de conceder ou
não o financiamento, o algoritmo escreverá depois a frase "Obrigado por Consultar"'''

salario = float(input("Digite o valor do seu salário: "))
financiamento = float(input("Digite o valor do financiamento pretendido: "))

if financiamento <= 5 * salario:
    print("Financiamento Concedido")
else:
    print("Financiamento Negado")
print("Obrigado por Consultar")
