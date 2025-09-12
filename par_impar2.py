import os
import random
import time

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def linha():
    print("=" * 40)

def titulo(msg):
    linha()
    print(msg.center(40))
    linha()

def main():
    limpar_tela()
    titulo("JOGO DO PAR OU ÍMPAR")
    print("Será que você consegue ganhar?")
    linha()

    # Escolha do usuário
    while True:
        escolha_usuario = input("Escolha [P]ar ou [I]mpar: ").strip().lower()
        if escolha_usuario in ['p', 'par', 'i', 'impar', 'ímpar', 'í']:
            break
        print("Opção inválida. Tente novamente.")

    escolha_usuario = 'par' if escolha_usuario.startswith('p') else 'impar'

    # Número do usuário
    while True:
        try:
            num_usuario = int(input("Digite um número de 0 a 5: "))
            if 0 <= num_usuario <= 5:
                break
            else:
                print("Digite um número entre 0 e 5.")
        except ValueError:
            print("Por favor, digite um número válido.")

    print(f"\nSeu número foi: {num_usuario}")
    time.sleep(0.7)

    # Número do computador
    num_pc = random.randint(0, 5)
    print(f"O número do computador foi: {num_pc}")
    time.sleep(0.7)

    # Soma e resultado
    soma = num_usuario + num_pc
    print(f"A soma dos números é: {soma}")
    time.sleep(0.7)

    resultado = "par" if soma % 2 == 0 else "impar"
    print(f"O resultado deu: {resultado.upper()}")
    linha()

    # Verifica vencedor
    if escolha_usuario == resultado:
        print("🎉 Você VENCEU! Parabéns! 🎉".center(40))
    else:
        print("😢 Você PERDEU! Tente novamente. 😢".center(40))
    linha()

if __name__ == "__main__":
    main()