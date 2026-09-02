'''
Crie uma função que recebe um número inteiro positivo e retorna o fatorial desse número.
Considere que o número recebido sempre será um inteiro positivo.
OBS: Não utilize a biblioteca math do python
'''
def fatorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado