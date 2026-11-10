produtos = []
resposta = "s"

while resposta == "s":
    produto = input("Informe o nome do produto: ")
    produtos.append(produto)
    resposta = input("Deseja adicionar outro? (s|n): ").lower()

# Maneira melhor de imprimir a lista
print("Produtos cadastrados:")
for nome in produtos:
    print(nome)