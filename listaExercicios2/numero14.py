'''14 - Faça um algoritmo para ler: número da conta 
do cliente, saldo, débito e crédito. Após, calcule e 
escreva o saldo atual (saldo atual = saldo - débito 
+ crédito). Também teste se saldo atual for maior 
ou igual a zero. Em seguida escreva a mensagem 
'Saldo Positivo', senão, escrever a mensagem 
'Saldo Negativo'. '''

numCon = input("Digite o numero da conta: ")
saldo = float(input("Digite o saldo atual: "))
debito = float(input("Digite o valor do debito: "))
credito = float(input("Digite o valor do credito: "))

saldoAtual = saldo - debito + credito

if saldoAtual >= 0:
  print("Saldo positivo")
else:
  print("Saldo negativo")

print ("O saldo atual é: R$", saldoAtual)