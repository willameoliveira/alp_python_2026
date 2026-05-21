print("Informe apenas números inteiros positivos!")
soma = 0
for cont in range(1,11):
    num = int(input(f"Digite o número {cont}: "))
    soma += num

print(f"A soma é {soma}")