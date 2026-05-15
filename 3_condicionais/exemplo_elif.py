'''
Um vendedor de camisas vende camisas a R$ 20,00 e precisa de um programa para calcular o valor total dos pedidos dos seus clientes. 
A partir de dez camisas compradas, o cliente tem 10% de desconto. 
A partir de cinco camisas, o cliente tem 5% de desconto. 
O programa deve receber a quantidade de camisas e imprimir o valor final da venda.
'''

camisas = int(input("Quantidade de camisas: "))
preco_camisa = 20.0
valor_total = camisas * preco_camisa

if camisas >= 10:
    print(f"Valor total com 10% de desconto: R$ {valor_total * 0.90}")
elif camisas >= 5:
    print(f"Valor total com 5% de desconto: R$ {valor_total * 0.95}")
else:
    print(f"Valor total sem desconto: R$ {valor_total}")