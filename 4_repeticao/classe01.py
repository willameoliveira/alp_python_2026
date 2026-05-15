'''
Faça um programa que recebe uma senha e enquanto ela não for igual a "12345", 
ele imprime "Tente novamente". Quando a senha estiver correta, 
o programa encerra imprimindo "Acesso liberado".
'''

senha = input("Senha: ") # pede a senha pela primeira vez
while senha != "12345": # enquanto a senha for diferente de 12345
    print("Tente novamente!")
    senha = input("Senha: ")
print("Acesso liberado")

#Outra forma com uso de loop infinito e break
'''
while True:
    senha = input("Senha: ")
    if senha == "12345":
        print("Acesso liberado")
        break
    else:
        print("Tente novamente!")
'''