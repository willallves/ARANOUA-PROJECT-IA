# WILLIAN RODRIGUES ALVES
"""
* Elabore um programa para ler um número Natural (0 a 9) e mostrar o número por extenso.
"""


cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')

while True:
    num = int(input('Digite um numero entre 0 e 9: '))
    if 0 <= num <= 9:
        break
    print('Tente novamente!')
print('Vocë digitou o numero: ', cont[num])
