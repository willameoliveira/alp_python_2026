print("""Calculadora Simples
1. Soma
2. Subtração
3. Multiplicação
4. Divisão""")

opcao = int(input("Escolha a operação (1/2/3/4): "))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
 
if opcao == 1:
    print(f"O resultado da soma é: {num1 + num2}")
elif opcao == 2:
    print(f"O resultado da subtração é: {num1 - num2}")
elif opcao == 3:
    print (f"O resultado da multiplicação é: {num1 * num2}")
elif opcao == 4:
    if num2 != 0:
        print(f"O resultado da divisão é: {num1 / num2:.2f}")
    else:
        print("Divisão por zero! Escolha outro número!")
else:
    print("Opção inválida!")