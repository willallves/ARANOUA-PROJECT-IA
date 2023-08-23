##WILLIAN RODRIGUES ALVES
"""
* O IMC – Indice de Massa Corporal é um critério da Organização Mundial de Saúde para dar uma indicação sobre a condição
* de peso de uma pessoa adulta. A fórmula é IMC = peso / (altura) 2 Elabore um algoritmo que leia o peso e a altura de
* um adulto e mostre sua condição de acordo com a tabela abaixo:.
* <18.5         - Abaixo do Peso
* >=18.5 e <=25 - Peso Normal
* >25 e <=30    - Acima do Pe
* >30           - Obeso
"""


peso = float(input('Qual seu peso (Kg): '))
altura = float(input('Qual sua altura (m): '))

imc = peso / (altura ** 2)

print('O IMC dessa pessoa é: ', imc)

if (imc < 18.5):
    print("Abaixo de peso")
elif (18.5 <= imc < 25):
    print("Peso Normal")
elif (25 < imc <= 30):
    print("Acima do Peso")
elif imc > 30:
    print("Obeso")
