# Programa que guarda uma lista de compras

lista = []  # criando lista vazia
item = input("Digite um item da lista (ENTER para parar): ")
while item:  # similar a escrever: item != ""
    lista.append(item)
    item = input("Digite um item da lista (ENTER para parar): ")

print(lista)