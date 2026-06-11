'''
6. Um professor de Matemática deseja construir um programa para imprimir uma Progressão Aritmética (PA). 
Para isso, devem ser informados 3 argumentos: a) primeiro termo, b) quantidade de termos e c) razão.
'''
pt = int(input("Digite o primeiro termo: "))
qt = int(input("Digite a quantidade d termos: "))
raz = int(input("Digite a razão: "))

termo = pt

for cont in range(qt):
    print(termo)
    termo += raz