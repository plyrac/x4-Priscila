# Insert a new piece given the column number

from typing import List
from searchWinner import *


def insertPiece(matriz: List[List], cor: int, player: str, col:int):
    print("Escolha a coluna para colocar a ficha")
    cEscolhida: int = col
# cEscolhida representa a coluna em que o jogador quer colocar a ficha
    i: int = int(len(matriz)) - 1
    while i >= 0:
        if matriz[i][cEscolhida - 1][2] == 0:
            matriz[i][cEscolhida - 1][2] = cor
            break
        else:
            i = i - 1
    verifica, winner, seqWin = procura(matriz, player)

    for x in matriz:
        for y in x:
            print(y[2], end=" ")
        print("")

    return matriz, verifica, winner, seqWin


#insertPiece([[[1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0], [1, 6, 0], [1, 7, 0]],
#             [[2, 1, 0], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0], [2, 6, 0], [2, 7, 0]],
#             [[3, 1, 0], [3, 2, 0], [3, 3, 0], [3, 4, 0], [3, 5, 0], [3, 6, 0], [3, 7, 0]],
#             [[4, 1, 0], [4, 2, 0], [4, 3, 0], [4, 4, 0], [4, 5, 0], [4, 6, 0], [4, 7, 0]],
#             [[5, 1, 0], [5, 2, 0], [5, 3, 0], [5, 4, 0], [5, 5, 0], [5, 6, 0], [5, 7, 0]],
#             [[6, 1, 0], [6, 2, 0], [6, 3, 0], [6, 4, 0], [6, 5, 0], [6, 6, 0], [6, 7, 0]]], 1)
