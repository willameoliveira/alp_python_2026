'''
1. Construa um programa que receba um número inteiro positivo informado pelo usuário. 
Caso ele seja par, o programa deve calcular o seu quadrado. 
Mas, se ele for ímpar, deve ser calculado o seu cubo. 
Ao fim, o programa deve imprimir o valor calculado. 
'''

num = int(input("Digite seu número inteiro"))

if num % 2 == 0:
    resultado = num **2
    print(f"O seu numero é par. E o quadrado do numero é {resultado:.2f}")
else: 
    resultado =num **3 
    print(f"o numero e impar. E o cubo do numero é {resultado:.2f}")
   
    