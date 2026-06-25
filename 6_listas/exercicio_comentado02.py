produtos = []
resposta = "s"

while resposta == "s":
    produto = input("Informe o nome do produto: ")
    produtos.append(produto)
    resposta = input("Deseja adicionar outro? (s|n): ").lower()

print(produtos)