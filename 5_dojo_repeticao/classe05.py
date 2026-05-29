'''
5. Crie um programa que recebe números inteiros positivos. 
Quando o usuário informar um número negativo, o programa deve parar de receber números e imprimir:    
    a) a soma de todos os números positivos informados.
    b) a média aritmética de todos os números positivos informados.
    c) o maior dos números positivos informados.
'''
soma = 0
cont = 0
numero = 1
maior = 0
while numero > 0:
    numero = int(input("Digite um numero: "))
    if numero > 0:
        soma += numero
        cont += 1
    if numero > maior:
        maior = numero
print(f"a soma é :{soma}")
print(f"a media é :{soma/cont}")
print(f"o maior é:{maior}")  





