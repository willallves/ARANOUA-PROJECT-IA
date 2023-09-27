# WILLIAN RODRIGUES ALVES
"""
Criar uma agenda de contatos com o nome e o telefone no Python, armazenando os dados em arquivo .txt.
O programa deverá apresentar:

- Um menu com as opções de
   1. Cadastrar um contato
   2. Consultar um contato
   3. Listar todos contatos em ordem alfabética. Dica: pesquisar o método sort().
   4. Sair do Programa.
"""

import unicodedata
import os


file = 'contatos.txt'
arquivo = open(file, "w")
arquivo.close()

def cadastrar_contato():
    try:
        print("Cadastro de Contatos")
        nome = input("Informe o nome do contato\n")
        telefone = int(input("Digite o número do telefone\n"))
        nome_normalizado = unicodedata.normalize('NFKC', nome)

        arquivo = open(file, "a")
        arquivo.write(f"{nome_normalizado.encode('utf-8')} - {str(telefone)}\n")
        arquivo.close()
    except:
        print("Erro!!!!!(:")


def consultar_contato(nome):
    arquivo = open(file, "r")
    contatos = arquivo.readlines()

    contato_existe = False

    for contato in contatos:
        nome_normalizado = unicodedata.normalize('NFKC', nome)
        if nome_normalizado.upper().encode('utf-8') in contato.upper().encode('utf-8'):
            print(contato.strip())
            contato_existe = True

    if not contato_existe:
        print((f"Contato com o nome '{nome}' não encontrado."))

    print("\nFim do arquivo")
    arquivo.close()


def listar_contato():
    arquivo = open("contatos.txt", "r")
    contatos = arquivo.readlines()

    if not contatos:
        print("Agenda Vazia!")
        return

    contatos.sort()

    for contato in contatos:
        print(contato.strip())

    print("\nFim do arquivo")
    arquivo.close()


while True:
    try:
        print("---------------Menu-----------------")
        escolha = (int(input(
            " 1 - Para cadastrar um contanto\n 2 - Para consultar um Contato\n 3 - Para listar os contatos\n 4 - Sair\n")))

        if escolha == 4:
            break
        elif escolha == 1:
            cadastrar_contato()
        elif escolha == 2:
            if os.stat('contatos.txt').st_size != 0:
                contato = input("Digite o nome do contato que deseja buscar: \n")
            else:
                print("agenda vazia!")

            consultar_contato(contato)
        elif escolha == 3:
            listar_contato()
    except:
        print("_/\_Error_/\_(ôô) as Opções:")
