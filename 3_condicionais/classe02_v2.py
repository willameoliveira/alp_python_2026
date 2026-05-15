'''
2) Faça um programa que recebe três notas e calcula a média imprimindo:
a) "Aprovado", caso a média seja maior ou igual a 7,
b) "Prova final", caso a média seja menor que 7 e maior ou igual a 4 e
c) "Reprovado" em caso contrário.
'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado")
if media >= 4 and media < 7:
    print("Prova final")
if media < 4:
    print("Reprovado")