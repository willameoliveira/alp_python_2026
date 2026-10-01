'''
7. Faça um jogo de adivinhação que recebe um número inteiro de 1 a 10, por exemplo, e 
imprime "Parabéns, você acertou!" caso o jogador acerte o número sorteado pelo programa. 
Em caso contrário, o jogo imprime "Você errou!" e "Tente um número menor" 
ou " Tente um número maior" dependendo do valor informado pelo jogador. 
O jogo deve permitir até 3 chances. Caso o jogador não acerte na terceira vez, 
o jogo deve imprimir "Você perdeu! Fim de jogo." e informar o número sorteado. 
Comece o jogo pedindo o nível de dificuldade para o usuário (adivinhar entre 1 a 10, 1 a 20 ou 1 a 30, por exemplo).
Quando o usuário vencer ou perder, o jogo pergunta se ele quer jogar novamente e reinicia.
Dica: Importe a biblioteca random para gerar número aleatório em python e use a função randint(1, 10), por exemplo. 
Assim, ela retorna um número inteiro aleatório entre 1 e 10, incluindo ambos os extremos.
'''

import random

jogar = 's'
while jogar == 's':
    print("\033c", end="") # comando para limpar a tela
    print("######## JOGO DE ADIVINHAÇÃO ########")
    print("1 - Fácil (1 a 10)")
    print("2 - Médio (1 a 20)")
    print("3 - Difícil (1 a 30)")

    dificuldade = int(input("Escolha a dificuldade: "))

    if dificuldade == 1:
        limite = 10
    elif dificuldade == 2:
        limite = 20
    elif dificuldade == 3:
        limite = 30
    else:
        input("Opção inválida! ENTER para tentar novamente.")
        continue # pula as demais linhas e vai para o próximo laço do loop, imprimindo o menu novamente.

    print("\033c", end="") # comando para limpar a tela
    print("######## JOGO DE ADIVINHAÇÃO ########")
    print("Seja bem vindo!")
    print(f"Dê seu palpite de 1 a {limite}. Você tem 3 chances!\n")

    sorteado = random.randint(1, limite)
    for tentativa in range(1, 4):
        palpite = int(input(f"Palpite 1 de {tentativa}: "))

        if palpite == sorteado:
            print("\nParabéns, você acertou!")
            break

        if tentativa < 3: # testa se não é a última tentativa.
            if palpite < sorteado:
                print("Errou! Tente um número maior!")
            else:
                print("Errou! Tente um número menor!")
        else:
            print("\nVocê perdeu! Fim de jogo!")
            print(f"O número sorteado era: {sorteado}.")
        
    jogar = input("Jogar novamente? (s/n): ").lower()