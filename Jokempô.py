# UM JOGO DE JOKEMPÔ COM O USUÁRIO
# GRUPO: VITOR KAUÊ, MIKAELY LUIZA, KAIQUE SOUSA
# DATA: 11/09/2025

import random  # Importa o módulo random para gerar escolhas aleatórias
import time    # Importa o módulo time para usar delays

print("\n" + "="*50) # Imprime uma linha de divisão
print(" JOGO DE JOKEMPÔ ".center(50)) # Imprime o título centralizado
print("="*50) # Imprime outra linha de divisão
time.sleep(1)  # Aguarda 1 segundo


# Opções do jogo
opcoes = ["pedra", "papel", "tesoura"]  # Lista com as opções possíveis do jogo
jogadores = [  # Lista de dicionários com nome e pontos dos jogadores
  {"nome": "Vitor Kauê", "pontos": 0},
  {"nome": "Mikaely Luiza", "pontos": 0},
  {"nome": "Kaique Sousa", "pontos": 0},
  {"nome": "computer", "pontos": 0}
]


while True:  # Loop principal do jogo
    try: 
        print("\n" + "="*50) # Imprime uma linha de divisão
        print(" MENU PRINCIPAL ".center(50)) # Imprime o título do menu centralizado
        print("="*50) # Imprime outra linha de divisão
        
        print("\nEscolha uma opção:".center(50))  # Solicita ao usuário escolher um jogador
        print("jogadores:\n 1 - Vitor Kauê \n2 - Mikaely Luiza \n3 - Kaique Sousa \n4 - Sair do jogo".center(50))
        time.sleep(1)  # Aguarda 1 segundo
        jogador_escolhido = int(input("Digite o número do jogador que você quer ser: ")) - 1  # Recebe a escolha do jogador e ajusta o índice

        if jogador_escolhido < 0 or jogador_escolhido > 3:  # Verifica se a escolha é válida
            print("Opção inválida. Tente novamente.")  # Mensagem de erro
            continue  # Volta ao início do loop
        
        if jogador_escolhido == 3:  # Se o usuário escolher sair
            print("\n" + "="*50) # Imprime uma linha de divisão
            print(" PLACAR ATUAL ".center(50)) # Imprime o título do placar centralizado
            print("="*50) # Imprime outra linha de divisão
            time.sleep(1)  # Aguarda 1 segundo

            for jogador in jogadores:  # Itera sobre os jogadores para mostrar o placar
                print(f"{jogador['nome']}: {jogador['pontos']} pontos".center(50))  # Mostra o nome e pontos do jogador
                print("="*50)  # Imprime outra linha de divisão
            
            time.sleep(1)  # Aguarda 1 segundo
            print("Saindo do jogo. Até a próxima!")  # Mensagem de despedida
            break  # Sai do loop principal e termina o jogo

        print("\nEscolha uma opção:")  # Solicita ao usuário escolher pedra, papel ou tesoura
        time.sleep(1)  # Aguarda 1 segundo
        print("1 - Pedra \n2 - Papel \n3 - Tesoura")
        jogador = int(input("Digite o número da sua escolha: ")) - 1  # Recebe a escolha do usuário e ajusta o índice
        if jogador < 0 or jogador > 2:  # Verifica se a escolha é válida
            print("Opção inválida. Tente novamente.")  # Mensagem de erro
            continue  # Volta ao início do loop
        
        jokempô_pc = random.randint(0, 2)  # Gera a escolha aleatória do computador

        # Verifica quem ganhou
        time.sleep(1)  # Aguarda 1 segundo
        if jogador == jokempô_pc:
            print("="*50)  # Imprime outra linha de divisão
            print("Empate!".center(50))
            print(f"\nSua escolha: {opcoes[jogador]} \nEscolha do computador: {opcoes[jokempô_pc]}".center(50))  # Mostra as escolhas
            print("="*50)  # Imprime outra linha de divisão
        elif (jogador == 0 and jokempô_pc == 2) or (jogador == 1 and jokempô_pc == 0) or (jogador == 2 and jokempô_pc == 1):
            print("="*50)  # Imprime outra linha de divisão
            print(f"PARABÉNS {jogadores[jogador_escolhido]['nome'].upper()}! Você ganhou!".center(50))
            print(f"\nSua escolha: {opcoes[jogador]} \nEscolha do computador: {opcoes[jokempô_pc]}".center(50))  # Mostra as escolhas
            jogadores[jogador_escolhido]["pontos"] += 1  # Incrementa os pontos do jogador escolhido
            print("="*50)  # Imprime outra linha de divisão
        else:
            print("="*50)  # Imprime outra linha de divisão
            print(f"QUE PENA {jogadores[jogador_escolhido]['nome'].upper()}! Você perdeu!".center(50))
            print(f"\nSua escolha: {opcoes[jogador]} \nEscolha do computador: {opcoes[jokempô_pc]}".center(50))  # Mostra as escolhas
            jogadores[3]["pontos"] += 1  # Incrementa os pontos do computador
            print("="*50)  # Imprime outra linha de divisão
        continuar = input("Deseja jogar novamente? (s/n): ").strip().lower()  # Pergunta se o usuário quer continuar
        if continuar != 's':  # Se a resposta não for 's', sai do loop
            time.sleep(1)  # Aguarda 1 segundo
            print("\n" + "="*50) # Imprime uma linha de divisão
            print(" PLACAR ATUAL ".center(50)) # Imprime o título do placar centralizado
            print("="*50) # Imprime outra linha de divisão
            time.sleep(1)  # Aguarda 1 segundo
            for jogador in jogadores:  # Itera sobre os jogadores para mostrar o placar
                print(f"{jogador['nome']}: {jogador['pontos']} pontos".center(50))  # Mostra o nome e pontos do jogador
                print("="*50)  # Imprime outra linha de divisão
            print("Saindo do jogo. Até a próxima!")  # Mensagem de despedida
            break  # Sai do loop principal e termina o jogo
    except Exception as e:  # Captura qualquer erro ocorrido
        print("Ocorreu um erro:", e)  # Exibe a mensagem de erro