'''
2) Faça um programa que cadastra usuários com suas senhas dentro de uma lista. 
Depois, faça um login que só funciona para os usuários cadastrados. 
Dica: Use duas listas, uma para cadastrar os logins e outra para cadastrar as senhas.
'''

usuarios = []
senhas = []
resp = "s"
print("\nCADASTRO DE USUÁRIOS")
while resp == "s":
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    usuarios.append(usuario)
    senhas.append(senha)
    resp = input("Cadastrar outro? s|n: ").lower()

print("\nLOGIN")

usuario_login = input("Usuário: ")
senha_login = input("Senha: ")

if usuario_login in usuarios:
    posicao = usuarios.index(usuario_login)

    if senha_login == senhas[posicao]:
        print("Login realizado com sucesso!")
    else:
        print("Senha incorreta!")
else:
    print("Usuário não cadastrado!")