'''21 -Um funcionário recebe um salário fixo mais 
4% de comissão sobre vendas. Faça um 
algoritmo que receba o salário fixo de um 
funcionário e o valor de suas vendas, calcule e 
mostre o valor da comissão e o salário final do 
funcionário. '''

salario_fixo = float(input("Digite o salário fixo do funcionário: "))
vendas = float(input("Digite o valor das vendas do funcionário: "))

comissao = vendas * 0.04
salario_final = salario_fixo + comissao

print(f"O valor da comissão é R$ {comissao:.2f}")
print(f"O salário final do funcionário é R$ {salario_final:.2f}")
