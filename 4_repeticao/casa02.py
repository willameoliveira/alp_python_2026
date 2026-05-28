print('\033c', end='') #limpa a tela sem quebrar a linha
opcao = 1
while opcao != 0:
    valor = float(input("Digite o valor da compra: "))
    print('-' * 50)
    opcao = int(input(f"""[0]Encerrar programa
[1] A vista 15% de desconto 
[2] Cartão de debito 10% de desconto
[3] Cartão de credito 5% de desconto
Selecione a opçao desejada: """))
    print('-' * 50)

    if opcao == 1:
        print(f"O valor do desconto é de R${valor * 0.15:.2f} e o valor final a ser pago é de R${valor * 0.85:.2f}")
    elif opcao == 2:
        print(f"O valor do desconto é de R${valor * 0.10:.2f} e o valor final a ser pago é de R${valor * 0.90:.2f}")
    elif opcao == 3:
        print(f"O valor do desconto é de R${valor * 0.05:.2f} e o valor final a ser pago é de R${valor * 0.95:.2f}")
    elif opcao == 0: 
        print("Programa encerrado!")
    else:
        print("Opção inválida!")