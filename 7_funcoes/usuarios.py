usuarios = {"admin": 12345}

def adicionar():
    print("\033c", end="")  # Limpa a tela do terminal
    print("-- ADICIONAR USUÁRIOS ---")
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    usuarios[usuario] = senha
    print("Usuário cadastrado com sucesso!")
    input("ENTER para continuar!")

def pesquisar():
    print("\033c", end="")  # Limpa a tela do terminal
    print("-- PESQUISAR USUÁRIOS ---")
    usuario_login = input("Digite o usuário para pesquisar: ")
    if usuario_login in usuarios:
        input(f"Usuário encontrado: {usuario_login}. ENTER para continuar!")
    else:
        input("Usuário não encontrado! ENTER para continuar!")    

def remover():
    print("\033c", end="")  # Limpa a tela do terminal
    print("-- REMOVER USUÁRIO ---")
    usuario_remover = input("Digite o usuário para remover: ")
    if usuario_remover in usuarios:
        del usuarios[usuario_remover]
        input("Usuário removido com sucesso! ENTER para continuar!")
    else:
        input("Usuário não encontrado! ENTER para continuar!")

def listarTodos():
    print("\033c", end="")  # Limpa a tela do terminal
    print("-- LISTA DE USUÁRIOS CADASTRADOS ---")
    if usuarios:
        for usuario in usuarios:
            print(usuario)
        input("ENTER para continuar!")
    else:
        input("Nenhum usuário cadastrado! ENTER para continuar!")