from usuarios import usuarios
from menu import mostrarMenu

usuario_logado = None # inicializa a variável com "nada"

while True:
    print("\033c", end="")  # Limpa a tela do terminal
    print("------ BEM VINDO ------")
    usuario = input("Informe seu usuário..: ")
    senha = input("Informe sua senha....: ")
    
    if usuario in usuarios and usuarios[usuario] == senha:
        usuario_logado = usuario
        break
    else:
        print("\nUsuário e/ou senha não conferem!")
        input("ENTER para tentar novamente.")

mostrarMenu(usuario_logado)