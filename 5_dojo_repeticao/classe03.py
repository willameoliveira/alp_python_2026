'''
3) Faça um programa que recebe um usuário e senha e enquanto eles não forem iguais 
ao par usuário = "aluno" e senha = "12345", o programa imprime "Tente novamente". 
Caso seja atingido o limite de três tentativas, encerre o programa imprimindo "Você tentou 3 vezes". 
Quando o usuário e senha estiverem corretos, o programa encerra imprimindo "Acesso liberado".
'''
tentativa = 3
usuario = input("Digite o usuário:")
senha = int(input("Digite a senha:"))
while (usuario != "aluno" or senha != 12345) and tentativa>1:
    print("Acesso negado,tente novamente")
    tentativa-=1
    print(f"Você ainda tem {tentativa} restantes")
    usuario=input("Digite o usuário:")
    senha=input("Digite a senha:")
if usuario == 'aluno' and senha == 12345:
        print('Acesso liberado')
else:
      print('Voce atingiu o limite de tentativas')

    

    