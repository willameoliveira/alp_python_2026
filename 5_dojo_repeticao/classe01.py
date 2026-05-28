'''
Faça um programa que recebe uma senha e enquanto ela não for igual a "12345", 
ele imprime "Tente novamente". Quando a senha estiver correta, 
o programa encerra imprimindo "Acesso liberado".
'''
senha = int(input("digite sua senha: "))
while senha != 12345:
    print("acesso negado!")
    senha = int(input("Digite novamente a senha:"))
    if senha == 12345:
        print("acesso liberado!")


    


