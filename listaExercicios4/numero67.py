'''67 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do
usuário, mostrando uma mensagem de erro e voltando a pedir as informações.'''

while True:
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    if nome_usuario != senha:
        print("Usuário e senha cadastrados com sucesso!")
        break
    else:
        print("ERRO: a senha não pode ser igual ao nome de usuário.")
