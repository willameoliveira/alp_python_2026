'''
Faça um programa que recebe um login e uma senha. 
Enquanto eles não forem iguais a "aluno" e "123" respectivamente,
imprima "Login/senha inválidos" e peça o login e senha novamente. 
Quando estiverem corretos, imprima "Seja bem vindo!".
'''
while True:
    login = input("Login: ")
    senha = input("Senha: ")

    if login == "aluno" and senha == "123":
        print("Seja bem vindo, aluno!")
        break
    else:
        print("Login/senha inválidos!")