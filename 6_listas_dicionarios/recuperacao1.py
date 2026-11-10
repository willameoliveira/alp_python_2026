nome = input("Nome: ")
senha = input("Senha: ")
tentativa = 3

while tentativa > 1 and senha != "12345":
    tentativa -= 1
    print(f"Senha incorreta! Você ainda tem {tentativa} tentativa(s).")
    senha = input("Senha: ")

if senha == "12345":
    print(f"Olá {nome}, seja bem vindo ao nosso banco.")
else:
    print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")