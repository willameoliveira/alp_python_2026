'''
7. Faça um jogo de adivinhação que recebe um número inteiro de 1 a 10 e 
imprime "Parabéns, você acertou!" caso o jogador acerte o número sorteado pelo programa. 
Em caso contrário, o jogo imprime "Você errou!" e "Tente um número menor" 
ou " Tente um número maior" dependendo do valor informado pelo jogador. 
O jogo deve permitir até 3 chances. Caso o jogador não acerte na terceira vez, 
o jogo deve imprimir "Você perdeu! Fim de jogo." 
Dica: Importe a biblioteca random para gerar número aleatório em python e use a função randint(1, 10). 
Isso retorna um número aleatório entre 1 e 10.
'''

import random

num = random.randint(1,10)
for cont in range(1,4):
    esc = int(input("Digite um numero entre 1 e 10: "))

    if esc == num:
        print("Parabens, você acertou")
        break

    elif cont < 3:
        if esc < num:
            print("Digite um numero maior")
        else:
            print("Digite um numero menor")

if cont ==3:
    print("Você perdeu! Fim de jogo")