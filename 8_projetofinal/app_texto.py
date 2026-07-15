# ============================================================
# ARQUIVO: app_texto.py
# ============================================================
# Este é o arquivo PRINCIPAL da versão em modo TEXTO (terminal)
# do sistema.
#
# IMPORTANTE PARA OS ALUNOS:
# Este arquivo usa o MESMO Model (model/) e o MESMO Controller
# (controller/) da versão em Streamlit (app.py). A única coisa
# que muda é a View: em vez de telas gráficas no navegador,
# usamos input() e print() no terminal.
#
# Isso mostra na prática a vantagem do padrão MVC: como a regra
# de negócio (Controller) e os dados (Model) não conhecem
# detalhes de interface, conseguimos "trocar" a tela inteira
# sem mexer em uma linha sequer do Model ou do Controller.
# ============================================================

from view_texto.login_view_texto import tela_login_texto
from view_texto.menu_view_texto import tela_menu_texto
from view_texto.inserir_view_texto import tela_inserir_texto
from view_texto.pesquisar_view_texto import tela_pesquisar_texto
from view_texto.remover_view_texto import tela_remover_texto
from view_texto.listar_view_texto import tela_listar_texto

"""
Função que imprime o cabeçalho do programa.
"""
def exibir_cabecalho():
    print("\033c", end="")  # Limpa a tela do terminal
    print("############################################")
    print("   SISTEMA DE CADASTRO DE USUÁRIOS (TEXTO)")
    print("############################################\n")


def main():
    """
    Função principal: controla o fluxo do programa no terminal.
    Usamos um laço de repetição comum (while) para
    manter o programa rodando até o usuário escolher 'encerrar' no menu.
    """

    # Variáveis que guardam a situação do login e o usuário logado.
    autenticado = False
    usuario_logado = ""
    
    #iniciando opcao com zero para depois do login ir para o menu
    opcao = "0"
    while True:
        exibir_cabecalho()

        if not autenticado:
            autenticado, usuario_logado = tela_login_texto()
            input("ENTER para continuar...")
            """
            Usando 'continue' para pular para o próximo laço do while.
            Isso impede que o menu apareça caso o login não tenha dado certo.
            Assim, só sai do login quando o usuário loga corretamente.
            """
            continue
        
        if opcao == "0":
            opcao = tela_menu_texto(usuario_logado)
            #Usando 'continue' para pular para o próximo laço e imprimir o cabeçalho antes de entrar para outra tela
            continue

        if opcao == "1":
            tela_inserir_texto()

        elif opcao == "2":
            tela_pesquisar_texto()

        elif opcao == "3":
            tela_remover_texto()
            
        elif opcao == "4":
            tela_listar_texto()

        elif opcao == "5":
            print("Sessão encerrada. Até logo!\n")
            input("ENTER para continuar...")
            autenticado = False
            opcao = "0" #faz a tela voltar para o menu no próximo loop

        elif opcao == "6":
            print("Programa fechado. Até logo!\n")
            break

        else:
            print("Opção inválida. Digite um número de 1 a 5.\n")
            opcao = "0" #faz a tela voltar para o menu no próximo loop
            input("ENTER para voltar...")
        
        #Se a opção selecionada é 1, 2 , 3 ou 4, pergunta se o usuário quer voltar pro menu ou se quer ficar na tela em que está
        if opcao in ["1", "2", "3", "4"]:
            opcao = "0" if input("Voltar para menu? (s|n): ").lower() == 's' else opcao
        


# Só executa a função main() quando o arquivo for rodado diretamente
# (e não quando for apenas importado por outro arquivo)
if __name__ == "__main__":
    main()
