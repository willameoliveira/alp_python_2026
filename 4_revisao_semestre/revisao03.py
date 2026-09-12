'''
Faça um programa que recebe 10 números inteiros positivos e, ao final, imprime
o resultado do somatório deles.
'''
soma = 0

for i in range(1,11):
    num = int(input(f"Digite o número {i}: "))
    soma += num #  soma = soma + num

print(f"A soma é: {soma}")