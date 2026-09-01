#Programa para calcular média de um aluno e imprimir o resultado.

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3) / 3

print(f"A média é: {media:.1f}")

if media >= 7:
    print("Aprovado!")
elif media >= 4 and media < 7:
    print("Prova final!")
else:
    print("Reprovado!")