'''
4. Imagine um sistema de caixa eletrônico. Construa um programa que receba a senha de um correntista para validar o seu acesso ao sistema. 
Considere que a senha fictícia do correntista é 123456. Considere as seguintes restrições:
• quando a senha estiver correta, mostrar a mensagem: “Olá, <SEUNOME>. Seja bem-vindo ao nosso banco!"
• quando o usuário errar a senha pela primeira vez, mostrar a mensagem: “Senha incorreta! Você ainda tem 2 tentativas.”
• se o usuário errar a senha pela segunda vez, mostrar a mensagem: “Senha incorreta! Você ainda tem 1 tentativa.”
• se o usuário errar a senha novamente, mostrar a mensagem “Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.” e o programa deve ser encerrado.
'''

usuario = input("Nome do usuário: ")
for tentativas in range(3,0,-1):
    senha = input("Senha: ")
    if senha == "123456":
        print(f"Olá, {usuario}. Seja bem vindo ao nosso banco!")
        break
    elif tentativas > 1:
        print(f"Senha incorreta! Você ainda tem {tentativas-1} tentativas.")
    else:
        print("Sua senha foi bloqueada. Por favor, dirija-se a um de nossos caixas.")