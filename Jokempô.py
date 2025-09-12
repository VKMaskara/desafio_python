# UM JOGO DE JOKEMPÔ COM O USUÁRIO
# GRUPO: VITOR KAUÊ, MIKAELY LUIZA, KAIQUE SOUSA
# DATA: 11/09/2025

import random

print("\n" + "="*50) # divisão
print(" JOGO DE JOKEMPÔ ".center(50))
print("="*50) # divisão

# Opções do jogo
opcoes = ["pedra", "papel", "tesoura"]
jogadores = [{nome: "Vitor Kauê", pontos: 0}, {nome: "Mikaely Luiza", pontos: 0}, {nome: "Kaique Sousa", pontos: 0}]

while True:
   try: 
     print("\n" + "="*50) # divisão
     print(" MENU PRINCIPAL ".center(50))
     print("="*50) # divisão

     print("\nEscolha uma opção:")
     print("jogadores: 1 - Vitor Kauê \n2 - Mikaely Luiza \n3 - Kaique Sousa \n4 - Sair do jogo")
     jogador_escolhido = int(input("Digite o número do jogador que você quer ser: ")) - 1  

     print("\nEscolha uma opção:")
     print("1 - Pedra \n2 - Papel \n3 - Tesoura")
     jogador = int(input("Digite o número da sua escolha: ")) - 1
     break
    