#WILLIAN RODRIGUES ALVES
"""
Um caixa de supermercado dispõe de notas de R$ 100,00 R$ 50,00, R$ 10,00, R$ 5,00 e R$ 1,00. Fazer
um programa que leia o VALOR DA MERCADORIA, o VALOR PAGO, calcular e mostrar o TROCO e
quantas notas de cada valor serão utilizadas.
"""


# Solicita o valor da mercadoria e o valor pago
valor_mercadoria = float(input("Digite o valor da mercadoria: R$ "))
valor_pago = float(input("Digite o valor pago: R$ "))

# Calcula o troco
troco = valor_pago - valor_mercadoria

# Inicializa as variáveis para contar as notas de cada valor
notas_100 = 0
notas_50 = 0
notas_10 = 0
notas_5 = 0
notas_1 = 0

# Calcula a quantidade de cada nota
while troco > 0:
    if troco >= 100:
        troco -= 100
        notas_100 += 1
    elif troco >= 50:
        troco -= 50
        notas_50 += 1
    elif troco >= 10:
        troco -= 10
        notas_10 += 1
    elif troco >= 5:
        troco -= 5
        notas_5 += 1
    else:
        troco -= 1
        notas_1 += 1

# Exibe o troco e a quantidade de cada nota
print("Troco: R$ ", valor_pago - valor_mercadoria)
print("Notas de R$ 100,00: ", notas_100)
print("Notas de R$ 50,00: ", notas_50)
print("Notas de R$ 10,00: ", notas_10)
print("Notas de R$ 5,00: ", notas_5)
print("Notas de R$ 1,00: ", notas_1)
