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
    print(f"Aluno aprovado com média: {media:.1f}")
elif media >= 4: # mesmo que dizer senao se media >= 4 e media < 7
    print(f"Aluno de prova final com média: {media:.1f}")
else:
    print(f"Aluno reprovado com média: {media:.1f}")
