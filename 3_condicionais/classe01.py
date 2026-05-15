'''
1) Faça um programa que recebe um número inteiro e informa se o número é par ou ímpar.
DICA: Lembre do operador aritmético de resto da divisão: %
Ex1: 4 % 2 #resulta em 0
Ex2: 3 % 2 #resulta em 1
'''
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par!")
else:
    print("O número é ímpar!")