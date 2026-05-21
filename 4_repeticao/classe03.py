'''
3) Faça um programa que recebe um usuário e senha e enquanto eles não forem iguais 
ao par usuário = "aluno" e senha = "12345", o programa imprime "Tente novamente". 
Caso seja atingido o limite de três tentativas, encerre o programa imprimindo "Você tentou 3 vezes". 
Quando o usuário e senha estiverem corretos, o programa encerra imprimindo "Acesso liberado".
'''

for tentativa in range(1,4): # for tentativa de 1 até 3
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario == "aluno" and senha == "12345":
        print("Acesso liberado!")
        break
    else:
        print("Usuário e/ou senha inválidos! Tente novamente!")

if tentativa == 3:
    print("Você tentou 3 vezes!")