print("Apenas números positivos")
num1 = int(input("Dígite o primeiro número: "))
num2 = int(input("Dígite o segundo número: "))
print("Menu")
print("-"*50)
print("""1 - Média ponderada de pesos 2 e 3
2 - Quadrado da soma dos 2 números
3 - Cubo do menor número""")
print("-"*50)
opcao = int(input("escolha a opção: "))
if opcao == 1:
    resultado = (num1*2+num2*3)/5
    print(f"A média ponderada destes números é {resultado} ")
elif opcao == 2:
    resultado = (num1 + num2)**2
    print(f"O quadrado da soma dos dois números é {resultado} ")
elif opcao == 3:
    if num1 > num2:
        resultado = num2**3
        print(f"O cubo do menor número é {resultado}")
    else:
        resultado = num1**3
        print(f"O cubo do menor número é {resultado}")
else:
    print("Opção invalida")
