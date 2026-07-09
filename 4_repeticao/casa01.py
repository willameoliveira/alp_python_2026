while True:
    #comando para limpar a tela do terminal
    print("\033c", end="")

    opcao = int(input("""Calculadora Simples
    1. Soma
    2. Subtração
    3. Multiplicação
    4. Divisão
    0. Sair
    Escolha a operação (0/1/2/3/4): """))

    if opcao == 0:
        print("Programa encerrado!")
        break
    elif opcao < 0 or opcao > 4:
        input("Opção inválida! ENTER para continuar...")
        continue

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        print(f"O resultado da soma é: {num1 + num2}")
    elif opcao == 2:
        print(f" o resultado da subtração é:{num1 - num2}")
    elif opcao == 3:
        print (f"o resultado da multiplicação é:{num1*num2}")
    elif opcao == 4:
        if num2 != 0:
            print(f"O resultado da divisão é: {num1 / num2}")
        else:
            print("Divisão por zero! Escolha outro número!")
    
    input("\nENTER para continuar...")