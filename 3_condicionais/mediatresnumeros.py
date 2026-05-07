nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3)/3

print(f"A média das notas é: {media:.2f}")

if media >= 7:
    print("Aprovado")
elif media >= 4: #elif adicionado depois. Não faz parte do exercício.
    print("Prova final")
else:
    print("Reprovado")
