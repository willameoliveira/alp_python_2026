#Exemplo de comentário de uma linha.

'''
Faça um programa que recebe três notas, imprime a média e exibe o resultado
do aluno de acordo com as seguintes regras:
- Se a média for maior ou igual a 7, imprime "Aprovado".
- Se a média for menor que 7 e maior ou igual a 4, imprime "Prova final".
- Se a média for menor que 4, imprime "Reprovado!".
'''

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3) / 3

print(f"A média é: {media:.1f}")

if media >= 7:
    print("Aprovado!")
elif media >= 4:
    print("Prova Final!")
else:
    print("Reprovado!")