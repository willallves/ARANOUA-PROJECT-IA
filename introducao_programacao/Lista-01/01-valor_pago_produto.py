#WILLIAN RODRIGUES ALVES
"""
* Elabore um programa que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a
* escolha da condição de pagamento. Utilize os códigos da tabela a seguir para ler qual a condição de pagamento
* escolhida e efetuar o cálculo adequado.
* 1 - À vista em dinheiro ou cheque, recebe 10% de desconto
* 2 - À vista no cartão de crédito, recebe 15% de desconto
* 3 - Em duas vezes, preço normal de etiqueta sem juros
* 4 - Em tres vezes, preço normal de etiqueta mais juros de 10%
"""

preco = float(input('Pre;o normal da etiqueta: '))
cod = int(input('Código de 1 a 4: '))
if cod < 1 or cod > 4:
    print("Código inválido.")
else:
    if cod == 1:
        print("À vista em dinheiro ou cheque, recebe 10% de desconto: R$ ", preco * 0.9)
    elif cod == 2:
        print("À vista no cartão de crédito, recebe 15% de desconto: R$ ", preco * 0.85)
    elif cod == 3:
        print("Em duas vezes, preço normal de etiqueta sem juros: parcelas de R$ ", preco / 2)
    else:
        print("Em duas vezes, preço normal de etiqueta mais juros de 10%: parcelas de R$ ", preco * 1.1 / 3)
