from usuarios import usuarios
from menu import mostrarMenu

while True:
    print("\033c", end="")  # Limpa a tela do terminal
    print("------ BEM VINDO ------")
    usuario = input("Informe seu usuário..: ")
    senha = input("Informe sua senha....: ")
    
    if usuario in usuarios and usuarios[usuario] == senha:
        break
    else:
        print("Usuário e/ou senha não conferem!")
        input("ENTER para tentar novamente.")

mostrarMenu()