'''
Faça um programa que recebe dez números inteiros positivos 
e diz quantos números pares foram informados.
'''
quant_pares = 0
for cont in range(1,11):
    num = int(input(f"Digite o {cont}º número: "))
    if num % 2 == 0: # verifica se é par
        quant_pares += 1

print(f"Tem {quant_pares} números pares.")