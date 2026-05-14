'''
Faça um programa que recebe uma senha e enquanto ela não for igual a "12345", 
ele imprime "Tente novamente". Quando a senha estiver correta, 
o programa encerra imprimindo "Acesso liberado".
'''
import os # importa a biblioteca de acesso às funções do sistema operacional

senha = input("Senha: ") # pede a senha pela primeira vez
while senha != "12345": # enquanto a senha for diferente de 12345
    input("Tecle ENTER para tentar novamente!") # input para imprimir a mensagem de tente novamente e esperar que o usuário tecle ENTER antes de limpar a tela
    os.system("clear") #Limpa a tela do terminal
    senha = input("Senha: ")
print("Acesso liberado")