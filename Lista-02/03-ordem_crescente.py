#WILLIAN RODRIGUES ALVES
"""
* Construa um algoritmo que leia 5 números inteiros e escreva os números em ordem crescente. (Dica:
* pesquisar método de Ordenação Bolha)
"""


def bolhaSort(list):
    for passnum in range(len(list)-1, 0, -1):
        for i in range(passnum):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

for i in range(5):
    a = int(input(f"Digite o {i + 1}º número inteiro: "))
    list.append(a)

bolhaSort(list)

print(list)
