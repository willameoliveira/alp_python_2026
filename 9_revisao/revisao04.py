'''
Faça um prgorama que guarda 10 nomes em uma lista e, ao final,
sorteia um dos nomes e o imprime.
'''

import random  # importando toda a biblioteca random
#from random import choice  # importando somente a função choice

nomes = []
for i in range(1,11):
    nomes.append(input(f"Digite o nome {i}: "))

print(f"O nome sorteado é: {random.choice(nomes)}")