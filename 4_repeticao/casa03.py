'''
3. Construa um programa que receba o nome e o preço de 5 medicamentos de uma drogaria 
(considere que o usuário informou cinco medicamentos distintos). 
O programa deve informar o nome e o preço do medicamento mais barato, bem como a média aritmética
 dos preços informados.
'''
soma = 0
nome_mais_barato = ""
preco_mais_barato = 0
for cont in range(5):
    nome = input("Nome do medicamento: ")
    preco = float(input("Preço do medicamento: "))
    soma += preco
    if cont == 0 or preco < preco_mais_barato:
        nome_mais_barato = nome
        preco_mais_barato = preco

print(f"A média dos preços é: R$ {soma/5:.2f}")
print(f"O remédio mais barato é: {nome_mais_barato} e seu preço é R$ {preco_mais_barato}")