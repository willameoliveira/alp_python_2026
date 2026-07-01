nome_produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
estoque = int(input("Digite o estoque do produto: "))
promocao = input("O produto está em promoção? (s|n): ").lower() == "s"

dados_produto = [nome_produto, preco, estoque, promocao]

print("------ Dados do produto -------")
print(f"Nome.....: {dados_produto[0]}")
print(f"Preço....: {dados_produto[1]}")
print(f"Estoque..: {dados_produto[2]}")
print(f"Promoção.: {'Sim' if dados_produto[3] else 'Não'}")

