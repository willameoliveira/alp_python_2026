'''Programa que recebe o preço de um produto, 
a quantidade comprada 
e imprime o valor total da compra'''

# recebendo o preço pelo teclado
preco = float(input("Digite o preço do produto: "))
quantidade_comprada = int(input("Digite a quantidade comprada: "))

valor_total = preco * quantidade_comprada

print(f"O valor total é : R$ {valor_total:.2f}")