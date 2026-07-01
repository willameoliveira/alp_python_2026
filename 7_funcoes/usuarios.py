usuarios = {"admin": 12345}

def adiciona():
    print("\033c", end="")  # Limpa a tela do terminal
    print("-- ADICIONAR USUÁRIOS ---")
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    usuarios[usuario] = senha
    input("Usuário cadastrado com sucesso! ENTER para continuar!")