# PROGRAMA QUE APROVA O ALUNO BASEADO NA MÉDIA E NA FREQUENCIA DE 75%
# GRUPO: VITOR KAUÊ, MIKAELY LUIZA, KAIQUE SOUSA
# DATA: 11/09/2025

import time
import math

print("\n" + "="*50) # divisão
print(" PROGRAMA QUE CALCULA A MÉDIA DO ALUNO".center(50))
print("="*50) # divisão
time.sleep(1) # Tempo de espera

# Declaração de variáveis para as notas do aluno
print("\n DIGITE AS NOTAS".center(50))
print("="*50)# divisão

# Loop para garantir que a entrada das notas seja válida

while True:
    nota1 = float(input("Digite a 1ª nota: "))
    nota2 = float(input("Digite a 2ª nota: "))
    nota3 = float(input("Digite a 3ª nota: "))
    nota4 = float(input("Digite a 4ª nota: "))
    if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10 and 0 <= nota4 <= 10:
        break # Sai do loop se todas as notas forem válidas
    else:
        print("Notas inválidas. Por favor, digite notas entre 0 e 10.")


# Cálculo da média das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

# Loop para garantir que a entrada de frequência seja válida
while True:
    frequencia_input = input("\nO aluno teve mais de 75% de frequência? (s/n): ").strip().lower() # Remove espaços e converte para minúsculas
    
    # Se a entrada for válida, saímos do loop
    if frequencia_input == 's' or frequencia_input == 'n':
        break # O comando `break` sai do loop `while`
    
    # Se a entrada for inválida, mostramos a mensagem de erro e o loop continua
    else:
        print("Entrada de frequência inválida. Por favor, digite 's' ou 'n'.")

# Verificação de aprovação
print("\n" + "="*50)
print("Resultado da Avaliação".center(50))
print("="*50)


# Condições de aprovação e reprovação
if media >= 7.0 and frequencia_input == 's': # Se a média for maior ou igual a 7.0 e a frequência for adequada
    print(f"\nMédia: {media:.2f}")
    print("Frequência: Adequada (mais de 75%)")
    print("\n" + "STATUS: APROVADO!".center(50))
    print("Parabéns, o aluno foi aprovado por média e frequência.")
elif media >= 7.0 and frequencia_input == 'n': # Se a média for maior ou igual a 7.0 e a frequência for inadequada
    print(f"\nMédia: {media:.2f}")
    print("Frequência: Abaixo de 75%")
    print("\n" + "STATUS: REPROVADO POR FALTA!".center(50))
    print("O aluno foi reprovado, apesar da média alta.")
elif media < 7.0 and frequencia_input == 's': # Se a média for menor que 7.0 e a frequência for adequada
    print(f"\nMédia: {media:.2f}")
    print("Frequência: Adequada (mais de 75%)")
    print("\n" + "STATUS: REPROVADO POR MÉDIA!".center(50))
    print("O aluno foi reprovado, apesar da frequência adequada.")
else: # Se a média for menor que 7.0 e a frequência for inadequada
    print(f"\nMédia: {media:.2f}")
    print("Frequência: Abaixo de 75%")
    print("\n" + "STATUS: REPROVADO POR MÉDIA E FALTA!".center(50))
    print("O aluno foi reprovado por ter média e frequência insuficientes.")

print("\n" + "="*50)