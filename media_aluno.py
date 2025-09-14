# PROGRAMA QUE APROVA O ALUNO BASEADO NA MÉDIA E NA FREQUENCIA DE 75%
# GRUPO: VITOR KAUÊ, MIKAELY LUIZA, KAIQUE SOUSA
# DATA: 11/09/2025

import time  # Importa o módulo time para usar funções de tempo


print("\n" + "="*50)  # Imprime uma linha de divisão
print(" PROGRAMA QUE CALCULA A MÉDIA DO ALUNO".center(50))  # Imprime o título centralizado
print("="*50)  # Imprime outra linha de divisão
time.sleep(1)  # Aguarda 1 segundo

# Declaração de variáveis para as notas do aluno
print("\n DIGITE AS NOTAS".center(50))  # Imprime instrução centralizada
print("="*50)  # Imprime linha de divisão

# Loop para garantir que a entrada das notas seja válida
while True:
    nota1 = float(input("Digite a 1ª nota: "))  # Solicita a 1ª nota
    nota2 = float(input("Digite a 2ª nota: "))  # Solicita a 2ª nota
    nota3 = float(input("Digite a 3ª nota: "))  # Solicita a 3ª nota
    nota4 = float(input("Digite a 4ª nota: "))  # Solicita a 4ª nota
    if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10 and 0 <= nota4 <= 10:
        break  # Sai do loop se todas as notas forem válidas
    else:
        print("Notas inválidas. Por favor, digite notas entre 0 e 10.")  # Mensagem de erro

# Cálculo da média das notas
media = (nota1 + nota2 + nota3 + nota4) / 4  # Calcula a média das 4 notas

# Loop para garantir que a entrada de frequência seja válida
while True:
    frequencia_input = input("\nO aluno teve mais de 75% de frequência? (s/n): ").strip().lower()  # Solicita frequência e normaliza
    if frequencia_input == 's' or frequencia_input == 'n':
        break  # Sai do loop se a entrada for válida
    else:
        print("Entrada de frequência inválida. Por favor, digite 's' ou 'n'.")  # Mensagem de erro

# Verificação de aprovação
print("\n" + "="*50)  # Linha de divisão
print("Resultado da Avaliação".center(50))  # Título centralizado
print("="*50)  # Linha de divisão

# Condições de aprovação e reprovação
if media >= 7.0 and frequencia_input == 's':  # Média suficiente e frequência adequada
    print(f"\nMédia: {media:.2f}")  # Exibe média
    print("Frequência: Adequada (mais de 75%)")  # Exibe frequência
    print("\n" + "STATUS: APROVADO!".center(50))  # Exibe status aprovado
    print("Parabéns, o aluno foi aprovado por média e frequência.")  # Mensagem de aprovação
elif media >= 7.0 and frequencia_input == 'n':  # Média suficiente, frequência insuficiente
    print(f"\nMédia: {media:.2f}")  # Exibe média
    print("Frequência: Abaixo de 75%")  # Exibe frequência
    print("\n" + "STATUS: REPROVADO POR FALTA!".center(50))  # Exibe status reprovado por falta
    print("O aluno foi reprovado, apesar da média alta.")  # Mensagem de reprovação
elif media < 7.0 and frequencia_input == 's':  # Média insuficiente, frequência adequada
    print(f"\nMédia: {media:.2f}")  # Exibe média
    print("Frequência: Adequada (mais de 75%)")  # Exibe frequência
    print("\n" + "STATUS: REPROVADO POR MÉDIA!".center(50))  # Exibe status reprovado por média
    print("O aluno foi reprovado, apesar da frequência adequada.")  # Mensagem de reprovação
else:  # Média insuficiente e frequência insuficiente
    print(f"\nMédia: {media:.2f}")  # Exibe média
    print("Frequência: Abaixo de 75%")  # Exibe frequência
    print("\n" + "STATUS: REPROVADO POR MÉDIA E FALTA!".center(50))  # Exibe status reprovado por ambos
    print("O aluno foi reprovado por ter média e frequência insuficientes.")  # Mensagem de reprovação

print("\n" + "="*50)  # Linha de divisão final
