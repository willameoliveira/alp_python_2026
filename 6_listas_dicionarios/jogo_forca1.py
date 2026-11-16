
# JOGO DE ADIVINHACAO DE PALAVRAS

palavra = "PYTHON"

letras_descobertas = []
letras_utilizadas = []

erros = 0
limite_erros = 6

print("=" * 35)
print("       JOGO DE ADIVINHACAO")
print("=" * 35)

while erros < limite_erros:

    # Exibe a palavra parcialmente descoberta
    print("\nPalavra: ", end="")

    for letra in palavra:
        if letra in letras_descobertas:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    print(f"\nErros: {erros}/{limite_erros}")

    # Verificar se o jogador descobriu a palavra
   
    # Pedir o palpite e guardar numa string

    # Validar a entrada (se só tem uma letra e se é letra mesmo, não número). Use a função len e a função isalpha para isso.

    # Verificar se a letra já foi utilizada

    # Adicionar a letra na lista de utilizadas

    # Verificar se a letra existe na palavra. Se sim, adicionar ela na lista de descobertas. Se não, dizer que errou e incrementar os erros.

# Resultado final
print("\n" + "=" * 35)

# Verificar se a pessoa ganhou ou perdeu e imprimir a mensagem correspondente.

print(f"A palavra secreta era: {palavra}")

print("=" * 35)
