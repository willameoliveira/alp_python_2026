numero = int(input("Digite um número inteiro positivo: "))
if numero <= 0:
    print("Informe um número maior que zero!")
elif numero % 2 == 0:
    print(f"O número é par, seu quadrado é: {numero**2}")
else:
    print(f"O número é ímpar, seu cubo é: {numero**3}")