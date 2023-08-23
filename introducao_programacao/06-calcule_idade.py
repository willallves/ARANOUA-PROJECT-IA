# WILLIAN RODRIGUES ALVES
"""
* Faça um programa que leia o ano de nascimento de nascimento de uma pessoa, calcule e mostre sua idade em relação ao
ano corrente (2023) e, também, verifique e mostre se a ela já tem idade para votar e para tirar
a carteira de habilitação.
"""


ano_nascimento = int(input("Informe o ano de seu nascimento: "))

ano_atual = int(input("Informe o ano atual: "))

idade_anos = ano_atual - ano_nascimento
print("A idade em anos é: ", idade_anos)

if 16 > idade_anos:
    print('Náo pode votar')
elif 16 < idade_anos < 18:
    print("Pode votar mas náo pode tirar habilitacao")
else:
    print("Pode votar e pode tirar habilitacao")