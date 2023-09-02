#WILLIAN RODRIGUES ALVES
"""
* Crie um programa que leia um número inteiro e positivo e verifique se ele é primo ou não. (Dica: os
* números primos são os números que só podem ser divididos por eles mesmos e por 1).
"""


n = int(input("Verificar numeros primos ate: "))
mult = 0

for count in range(2, n):
    if n % count == 0:
        print("Múltiplo de", count)
        mult += 1

if mult == 0 and n >= 2:
    print("É primo")
else:
    print("Não é primo")
