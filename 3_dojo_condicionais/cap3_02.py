'''
2. Construa um programa que solicite ao usuário dois números 
positivos. Em seguida, o programa deve apresentar o seguinte 
menu:
    1. Média ponderada, com pesos 2 e 3, respectivamente
    2. Quadrado da soma dos 2 números
    3. Cubo do menor número
    Escolha uma opção:
De acordo com a opção informada, o programa deve calcular a 
operação apresentada no menu. 
Se a opção escolhida for inválida, o programa deve mostrar a 
mensagem “Opção inválida” e ser encerrado.
'''
print("Menu")
print("1.Média ponderada,com 2  3 pesos respectivamente")
print("2.Quadrado da soma dos 2 números")
print("3.Cubo do menor numero")

opçao = int(input("qual a sua opçao: "))

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

if opçao == 1:
    media = (numero1 * 2 + numero2 * 3)/5
    print(f"Resultado:{media:.2f}" )
elif opçao == 2:
    media = (numero1 + numero2)**2
    print(f"Resultado:{media}")
elif opçao == 3:
    if numero1 < numero2: 
     numero1 ** 3
     print(f"o cubo do menor número é: {cubo do menor}"
 elif opcao == 3:
    if numero2 < numero1
    else:
     numero2 ** 3

    

