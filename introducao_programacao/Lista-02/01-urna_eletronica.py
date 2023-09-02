#WILLIAN RODRIGUES ALVES
"""
* Em uma determinada escola, 3 candidatos (D, G, X) concorrem ao cargo de Diretor Geral. A urna
* eletrônica elaborada para essa eleição, aceita os votos conforme a legenda abaixo:
*
* Legenda                Voto
* “A” Candidato           A
* “B” Candidato           B
* “C” Candidato           C
* “O”                     Voto em Branco
* “N”                     Voto Nulo
* “F”                     Finaliza a eleição
*
* Elabore um programa para ler todos os votos, contabilizando os votos para cada candidato. Ao final, o
* algoritmo deverá mostrar:
*
*     • O candidato vencedor
*     • O número de votos de cada candidato e de votos brancos e nulos
*     • O total de votos válidos da eleição
*     • O percentual de cada legenda sobre o total de votos (exceto “F”)
*
"""

votos_candidato_D = 0
votos_candidato_G = 0
votos_candidato_X = 0

votos_branco = 0
votos_nulo = 0

total_votos_validos = 0

votos_total = 0
voto = "voto invalido"
while voto != "F":
    voto = input(
        "Dígite seu voto \n CANDIDATO (A)\n CANDIDATO (B)\n CANDIDATO (C)\n BRANCO (O)\n NULO (N)\n PARA FINALIZAR (F)\n").upper()

    if voto == "A":
        votos_candidato_D += 1
    elif voto == "B":
        votos_candidato_G += 1
    elif voto == "C":
        votos_candidato_X += 1
    elif voto == "O":
        votos_branco += 1
    elif voto == "N":
        votos_nulo += 1

    votos_total += 1

print("Vota;ó finalizada")

total_votos_validos = votos_candidato_D + votos_candidato_G + votos_candidato_X

percentual_D = (votos_candidato_D / total_votos_validos) * 100 if votos_candidato_D > 0 else 0
percentual_G = (votos_candidato_G / total_votos_validos) * 100 if votos_candidato_G > 0 else 0
percentual_X = (votos_candidato_X / total_votos_validos) * 100 if votos_candidato_X > 0 else 0

vencedor = ""

if votos_candidato_D == votos_candidato_G == votos_candidato_X:
    vencedor = "Empate entre Candidatos D, G e X"
elif votos_candidato_D >= votos_candidato_G and votos_candidato_D >= votos_candidato_X:
    vencedor = "Candidato D"
elif votos_candidato_G >= votos_candidato_D and votos_candidato_G >= votos_candidato_X:
    vencedor = "Candidato G"
else:
    vencedor = "Candidato X"

print("Candidato vencedor: ", vencedor)
print("Votos para Candidato D: ", votos_candidato_D)
print("Votos para Candidato G: ", votos_candidato_G)
print("Votos para Candidato X: ", votos_candidato_X)
print("Votos em Branco: ", votos_branco)
print("Votos Nulos: ", votos_nulo)
print("Total de votos válidos: ", total_votos_validos)
print("Percentual de votos para Candidato D: ", percentual_D)
print("Percentual de votos para Candidato G: ", percentual_G)
print("Percentual de votos para Candidato X: ", percentual_X)
