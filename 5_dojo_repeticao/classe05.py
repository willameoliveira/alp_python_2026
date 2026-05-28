'''
5. Crie um programa que recebe números inteiros positivos. 
Quando o usuário informar um número negativo, o programa deve parar de receber números e imprimir:    
    a) a soma de todos os números positivos informados.
    b) a média aritmética de todos os números positivos informados.
    c) o maior dos números positivos informados.
'''
soma = 0
media = 0
numero = int(input("Digite um numero"))
while numero >= 0:
    soma += numero


print(f"A soma é {soma}")


