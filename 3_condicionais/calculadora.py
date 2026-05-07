print("""Calculadora Simples
1. Soma
2. Subtração
3. Multiplicação
4. Divisão""")

opcao = int(input("Escolha a operação (1/2/3/4): "))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao < 1 or opcao > 4:
    print("Opção inválida!")
elif opcao == 1:
    resultado = num1 + num2
    print(f"O resultado da soma é: {resultado}")
elif opcao ==2:
    resultado = num1 - num2
    print(f" o resultado da subtração é:{resultado}")
elif opcao ==3:
    resultado = num1*num2 
    print (f"o resultado da multiplicação é:{resultado}")
elif opcao ==4:
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Divisão por zero! Escolha outro número!")
     