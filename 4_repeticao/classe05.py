'''
5. Crie um programa que recebe números inteiros positivos. Quando o usuário informar um número negativo, o programa deve parar de receber números e imprimir:    
    a) a soma de todos os números positivos informados.
    b) a média aritmética de todos os números positivos informados.
    c) o maior dos números positivos informados.
'''

soma = 0
cont = 0
maior = 0
num = 1
while num > 0:
    num = int(input("Digite um número positivo: "))
    if num > 0:
        soma += num
        cont += 1
    if num > maior:
        maior = num

print(f"A soma é: {soma}")
print(f"A média é : {soma/cont:.1f}")
print(f"O maior é: {maior}")
