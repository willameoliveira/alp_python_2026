'''
5. Crie um programa no qual o usuário informe 2 números inteiros: a e b. 
Para que o programa continue sua execução, verifique se a < b. 
Se sim, calcule a soma dos números inteiros no intervalo [a, b]. 
Caso contrário, informe uma mensagem de erro.
'''

a = int(input("Informe o primeiro número: "))
b = int(input("Informe o segundo número: "))
soma = 0

for num in range(a, b + 1):
    soma = soma + num

if (soma == 0):
    print("Erro. O primeiro deve ser menor que o segundo!")
else:
    print(f"A soma de todos os números entre {a} e {b} é {soma}.")