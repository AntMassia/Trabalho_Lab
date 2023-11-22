import random
import sys

# List of words
def palavras():
    return ["viola", "tempo", "tenis", "amigo", "cacau"]

# List of words already used
registro = []

# Dictionary of words already typed
palavras_digitadas = {}

# Function to choose a random word
def escolher_palavra():
    global palavras
    palavra = random.choice(palavras())
    palavras().remove(palavra)
    return palavra

# Function to validate a word
def validar_palavra(palavra):
    return palavra.isalpha()

# Function to display the board
def exibir_tabuleiro(palavra, palpite):
    if len(palavra) != len(palpite):
        raise ValueError("As palavras devem ter o mesmo tamanho.")
    for i in range(len(palavra)):
        if palavra[i] == palpite[i]:
            print("🟩", end="")
        elif palavra[i] in palpite:
            print("🟨", end="")
        else:
            print("⬛", end="")
    print()


# Function to process a guess
def processar_palpite(palpite):
    global palavras_digitadas
    if palpite in palavras_digitadas:
        print("Você já digitou essa palavra.")
        return
    palavras_digitadas[palpite] = True
    if not validar_palavra(palpite):
        print("A palavra deve ser composta apenas de letras.")
        return
    return palpite

# Main function
def main():
    # Choose a random word
    palavra_secreta = escolher_palavra()

    # Start the game
    tentativas = 5
    while tentativas > 0:
        # Ask the player for a guess
        palpite = input("Digite uma palavra (5 letras): ").lower()

        # Process the guess
        palpite = processar_palpite(palpite)

        # Check if the guess is correct
        if palpite == palavra_secreta:
            print("Parabéns! Você acertou a palavra.")
            break
        else:
            # Display the board
            exibir_tabuleiro(palavra_secreta, palpite)
            tentativas -= 1

    # Check if the player lost
    if tentativas == 0:
        print("Você perdeu! A palavra secreta era:", palavra_secreta)

if __name__ == "__main__":
    main()
