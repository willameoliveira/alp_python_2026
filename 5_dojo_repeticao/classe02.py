'''
Faça um programa que recebe dez números inteiros positivos 
e diz quantos números pares foram informados.
'''
num = 0
pares = 0
for cont in range(10):
    num = int(input("Digite dez números positivos inteiros: "))
    if num % 2 == 0:
        pares += 1

print(f"Números pares digitados: {pares}")