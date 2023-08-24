# WILLIAN RODRIGUES ALVES
"""
* A Alíquota do cálculo mensal do imposto de renda 2023 é baseada na tabela abaixo:
*
* Até R$ 1.903,98               - 0,0
* De R$ 1.903,99 a R$ 2.826,65  - 7,5
* De R$ 2.826,66 a R$ 3.751,05  - 15,0
* De R$ 3.751,06 a R$ 4.664,68  - 22,5
* Acima de R$ 4.664,68          - 27,5
*
* Crie um algoritmo para ler o salário, calcular a alíquota e mostrar o valor do Imposto de Renda mensal.
"""

salario = float(input("Digite o salário em R$: "))

aliquota = 0.0 if salario <= 1903.98 else 7.5 if salario <= 2826.65 else 15.0 if salario <= 3751.05 else 22.5 if salario <= 4664.68 else 27.5

imposto_renda = salario * (aliquota / 100)

print('A aliquota é: ' + str(aliquota) + ' e o imposto a pagar é: ' + str(imposto_renda) + ' salario liquido: ' + str(salario - imposto_renda))
