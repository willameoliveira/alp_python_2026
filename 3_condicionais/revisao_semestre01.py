media1 = float(input("Digite a média do B1: "))
media2 = float(input("Digite a média do B2: "))
media3 = float(input("Digite a média do B3: "))
media4 = float(input("Digite a média do B4: "))

media = (media1 + media2 + media3 + media4) / 4

print(f"A média final é: {media:.1f}")

if media >= 7:
    print("Aprovado!")
if media < 7 and media >=4:
    print("Prova final!")
if media < 4:
    print("Reprovado!")

if media >= 7:
    print("Aprovado!")
elif media >= 4:
    print("Prova final!")
else:
    print("Reprovado!")