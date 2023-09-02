# WILLIAN RODRIGUES ALVES
"""
* Elabore um programa para ler o código de um banco e mostrar o nome, conforme a tabela abaixo
* 1     - Banco do Brasil
* 33    - Santander
* 104   - Caixa Econômica Federal
* 237   - Bradesco
* Qualquer outro código - Banco não identificado
"""

bancos = {
    1: 'Banco do Brasil',
    33: 'Santander',
    104: 'Caixa Economica Federal',
    237: 'Bradesco'
}

codigo = int(input('Digite o codigo do banco: '))
if codigo in bancos:
    print('O código pertence ao', bancos[codigo])
else:
    print("Banco não identificado!")
