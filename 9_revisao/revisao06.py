'''
Faça um programa que recebe números inteiros positivos e, para cada um, imprime
o seu fatorial. O programa pára quando um número negativo é informado.
Para isso, importe a função fatorial criada na revisao05.

'''
from revisao05 import fatorial

num = 0
while num >= 0:
    num = int(input("Digite um número inteiro positivo: "))
    if num >= 0:
        print(f"Fatorial de {num} é {fatorial(num)}\n")