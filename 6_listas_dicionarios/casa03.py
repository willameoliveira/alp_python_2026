'''
3) Pesquise no capítulo 6 do livro sobre Dicionários e 
refaça a questão 2 usando essa outra estrutura de dados.
'''

usuarios = {}
resp = "s"
print("\nCADASTRO DE USUÁRIOS")
while resp == "s":
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    usuarios[usuario] = senha
    resp = input("Cadastrar outro? s|n: ").lower()

print("\nLOGIN")

usuario_login = input("Usuário: ")
senha_login = input("Senha: ")

if usuario_login in usuarios:
    if senha_login == usuarios[usuario_login]:
        print("Login realizado com sucesso!")
    else:
        print("Senha incorreta!")
else:
    print("Usuário não cadastrado!")