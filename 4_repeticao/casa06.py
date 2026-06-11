'''
6. Um professor de Matemática deseja construir um programa 
para imprimir uma Progressão Aritmética (PA). 
Para isso, devem ser informados 3 argumentos: 
a) primeiro termo, b) quantidade de termos e c) razão.
'''
primeiro_termo = int(input("Digite o primeiro termo: "))
qtde_termos = int(input("Digite a quantidade de termos: "))
razao = int(input("Digite a razão: "))

termo = primeiro_termo

for cont in range(qtde_termos):
    print(termo)
    termo += razao