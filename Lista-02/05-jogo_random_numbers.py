#WILLIAN RODRIGUES ALVES
"""
Desenvolva o programa de um jogo que gere um número aleatório entre 0 e 9. Dê 3 chances para o
jogador descobrir qual o número gerado. A cada tentativa errada, mostrar se o número informado é maior
ou menor que o número gerado. Se for igual, parar o loop e informar que o jogador acertou. Ao final de
3 tentativas erradas, informar que o jogador não conseguiu acertar e mostrar qual era o número gerado.
"""

import random

# Gera um número aleatório entre 0 e 9
numero_gerado = random.randint(0, 9)

# Inicializa o número de tentativas
tentativas = 0

# Número máximo de tentativas permitidas
max_tentativas = 3

while tentativas < max_tentativas:
    # Solicita ao jogador que adivinhe o número
    try:
        palpite = int(input("Tente adivinhar o número entre 0 e 9: "))
    except ValueError:
        print("Por favor, insira um número válido.")
        continue

    # Verifica se o palpite do jogador é maior, menor ou igual ao número gerado
    if palpite < numero_gerado:
        print("O número é maior.")
    elif palpite > numero_gerado:
        print("O número é menor.")
    else:
        print("Parabéns! Você acertou o número ", numero_gerado)
        break

    tentativas += 1

# Se o jogador não acertar após 3 tentativas, mostra o número gerado
if tentativas == max_tentativas:
    print("Você não conseguiu acertar. O número gerado era ", numero_gerado)
