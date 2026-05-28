'''
4) Faça um programa que recebe 10 números inteiros positivos e ao 
final imprime o resultado do somatório de todos eles.
'''
soma = 0

for cont in range (10):
    num = int(input("Digite um número positivo: "))
    soma = soma + num
print(f"O resultado da soma de todos os números é: {soma}")