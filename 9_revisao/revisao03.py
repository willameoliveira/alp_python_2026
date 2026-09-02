'''
Faça um programa que recebe 10 números inteiros e, ao final, imprime
o resultado da soma de todos eles.
'''
soma = 0

for i in range(1,11):
    num = int(input(f"Digite o número {i}: "))
    soma += num

print(f"A soma é: {soma}")