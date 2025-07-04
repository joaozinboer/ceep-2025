import random

def jogo_adivinhador_idade():
    """
    Um jogo onde o computador tenta adivinhar um número (idade) entre 1 e 100.
    """
    print("--- Jogo do Adivinhador de Idade ---")
    print("Pense em um número entre 1 e 100. Eu vou tentar adivinhar!")
    print("Me diga se minha tentativa é 'maior', 'menor' ou se eu 'acertou'.")

    limite_inferior = 1
    limite_superior = 100
    tentativas = 0

    while True:
        tentativas += 1
        palpite = random.randint(limite_inferior, limite_superior)

        print(f"\nMinha {tentativas}ª tentativa é: {palpite}")
        resposta_usuario = input("Sua idade é 'maior', 'menor' ou eu 'acertou'? ").lower().strip()

        if resposta_usuario == "acertou":
            print(f"\nUhu! Adivinhei sua idade em {tentativas} tentativas! Sua idade é {palpite}.")
            break
        elif resposta_usuario == "maior":
            limite_inferior = palpite + 1
        elif resposta_usuario == "menor":
            limite_superior = palpite - 1
        else:
            print("Resposta inválida. Por favor, digite 'maior', 'menor' ou 'acertou'.")

        if limite_inferior > limite_superior:
            print("\nHmm, parece que houve um engano nas suas respostas. Não consigo adivinhar!")
            break

# --- Iniciar o Jogo ---
jogo_adivinhador_idade()