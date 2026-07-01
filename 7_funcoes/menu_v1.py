usuarios = {"admin": 12345}

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
        print("\033c", end="")  # Limpa a tela do terminal
        print("-- ADICIONAR USUÁRIOS ---")
        usuario = input("Digite o usuário: ")
        senha = input("Digite a senha: ")
        usuarios[usuario] = senha
        input("Usuário cadastrado com sucesso! ENTER para continuar!")
    elif opcao == "2":
        print("\033c", end="")  # Limpa a tela do terminal
        print("-- PESQUISAR USUÁRIOS ---")
        usuario_login = input("Digite o usuário para pesquisar: ")
        if usuario_login in usuarios:
            input(f"Usuário encontrado: {usuario_login}. ENTER para continuar!")
        else:
            input("Usuário não encontrado! ENTER para continuar!")
    elif opcao == "3":
        print("\033c", end="")  # Limpa a tela do terminal
        print("-- REMOVER USUÁRIO ---")
        usuario_remover = input("Digite o usuário para remover: ")
        if usuario_remover in usuarios:
            del usuarios[usuario_remover]
            input("Usuário removido com sucesso! ENTER para continuar!")
        else:
            input("Usuário não encontrado! ENTER para continuar!")
    elif opcao == "4":
        print("\033c", end="")  # Limpa a tela do terminal
        print("-- LISTA DE USUÁRIOS CADASTRADOS ---")
        if usuarios:
            for usuario in usuarios:
                print(usuario)
            input("ENTER para continuar!")
        else:
            input("Nenhum usuário cadastrado! ENTER para continuar!")
    else:
        input("Opção inválida! ENTER para continuar!")