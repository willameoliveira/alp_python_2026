'''
1) (Questão 3 do capítulo 5) Uma turma de formandos está vendendo rifas para angariar 
recursos financeiros para sua cerimônia de formatura. 
Construa um programa para cadastrar os nomes das pessoas que compraram a rifa. 
Ao fim, o programa deve sortear o ganhador do prêmio e imprimir o seu nome.
'''

import random

rifa = []
while True:
    nome = input("Informe um nome: ")
    rifa.append(nome)
    resp = input("Deseja continuar [S|N]? ")
    if resp.upper() == "N":
        break

sorteado = random.choice(rifa)  # Sorteia aleatoriamente um elemento
print(f"{sorteado} foi o(a) sorteado(a)!")