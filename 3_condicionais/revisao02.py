#Questão 4 do capítulo 3
usuario = input("Usuário: ")
senha = input("Senha: ")

if (usuario == "procopio" and senha == "12345") or (usuario == "paiva" and senha == "54321"):
    print("Seja bem vindo!")
else:
    print("Usuário/Senha não conferem!")