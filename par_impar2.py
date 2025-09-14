# JOGO DO PAR OU ÍMPAR
# GRUPO: VITOR KAUÊ, MIKAELY LUIZA, KAIQUE SOUSA
# DATA: 11/09/2025


import os                  # Importa o módulo os para comandos do sistema operacional
import random              # Importa o módulo random para gerar números aleatórios
import time                # Importa o módulo time para usar delays

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela, dependendo do sistema operacional

def linha():
    print("=" * 40)         # Imprime uma linha de 40 sinais de igual

def titulo(msg):
    linha()                 # Imprime uma linha
    print(msg.center(40))   # Centraliza e imprime a mensagem
    linha()                 # Imprime outra linha

def main():
    limpar_tela()           # Limpa a tela ao iniciar o jogo
    titulo("JOGO DO PAR OU ÍMPAR")  # Mostra o título do jogo
    print("Será que você consegue ganhar?")  # Mensagem inicial
    linha()                 # Imprime uma linha

    # Escolha do usuário
    while True:
        escolha_usuario = input("Escolha [P]ar ou [I]mpar: ").strip().lower()  # Solicita escolha e normaliza
        if escolha_usuario in ['p', 'par', 'i', 'impar', 'ímpar', 'í']:        # Verifica se é válida
            break
        print("Opção inválida. Tente novamente.")  # Mensagem de erro

    escolha_usuario = 'par' if escolha_usuario.startswith('p') else 'impar'  # Define escolha final

    # Número do usuário
    while True:
        try:
            num_usuario = int(input("Digite um número de 0 a 5: "))  # Solicita número ao usuário
            if 0 <= num_usuario <= 5:                                # Verifica se está no intervalo
                break
            else:
                print("Digite um número entre 0 e 5.")               # Mensagem de erro
        except ValueError:
            print("Por favor, digite um número válido.")             # Mensagem de erro para valor inválido

    print(f"\nSeu número foi: {num_usuario}")    # Mostra o número escolhido pelo usuário
    time.sleep(0.7)                              # Aguarda 0,7 segundos

    # Número do computador
    num_pc = random.randint(0, 5)                # Gera número aleatório para o computador
    print(f"O número do computador foi: {num_pc}")  # Mostra o número do computador
    time.sleep(0.7)                              # Aguarda 0,7 segundos

    # Soma e resultado
    soma = num_usuario + num_pc                  # Soma os dois números
    print(f"A soma dos números é: {soma}")       # Mostra a soma
    time.sleep(0.7)                              # Aguarda 0,7 segundos

    resultado = "par" if soma % 2 == 0 else "impar"  # Verifica se a soma é par ou ímpar
    print(f"O resultado deu: {resultado.upper()}")   # Mostra o resultado
    linha()                                     # Imprime uma linha

    # Verifica vencedor
    if escolha_usuario == resultado:            # Se a escolha do usuário bate com o resultado
        print("🎉 Você VENCEU! Parabéns! 🎉".center(40))  # Mensagem de vitória
    else:
        print("😢 Você PERDEU! Tente novamente. 😢".center(40))  # Mensagem de derrota
    linha()                                     # Imprime uma linha

if __name__ == "__main__":                      # Executa o main se o script for principal
    main()