import usuarios

while True:
    print("\033c", end="")  # Limpa a tela do terminal
    opcao = input("""
    --- Cadastro de usuários ---
    1. Adicionar
    2. Pesquisar
    3. Remover
    4. Listar todos
                
    Selecione uma opção (0 para sair): """)

    if opcao == "0":
        break

    if opcao == "1":
        usuarios.adiciona()
    else:
        input("Opção inválida! ENTER para continuar!")
