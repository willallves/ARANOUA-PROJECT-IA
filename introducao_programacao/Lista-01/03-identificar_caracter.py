# WILLIAN RODRIGUES ALVES
"""
* Desenvolva um algoritmo para identificar letras, números, pontuações “?”, “!”, “.”, “;” e “,”. Caso não se
* encaixe em nenhum desses, informe que é um “Caractere especial”.
"""


caracter = input("Digite um caractere: ")

pontuacao = ("?", "!", ".", ";", ",")
result = 'Letras' if caracter.isalpha() else 'Numero' if caracter.isdigit() else 'Pontuacão' if caracter in pontuacao else 'caractere especial'

print(f"O caractere '{caracter}' é classificado como: {result}")
