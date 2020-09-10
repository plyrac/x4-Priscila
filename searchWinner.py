from typing import List


def verHorizontal(matriz: List[List], player):
    winner: str = "nenhum ainda"
    sequencia: bool = False
    seqVencedora = []
    c = 0
    for i in matriz:
        while c < len(i):
            if i[c][2] != 0 and i[c][2] != 5:
                if (c + 3) < len(i):
                    if i[c][2] == i[c + 3][2]:
                        sequencia = True
                        if (c + 2) < len(i):
                            if i[c][2] == i[c + 2][2]:
                                sequencia = True
                                if (c + 1) < len(i):
                                    if i[c][2] == i[c + 1][2]:
                                        sequencia = True
                                        seqVencedora = [i[c], i[c + 1], i[c + 2], i[c + 3]]
                                        winner = player
                                        return sequencia, winner, seqVencedora
                                    else:
                                        sequencia = False
                            else:
                                sequencia = False
                    else:
                        sequencia = False
            c = c + 1
        c = 0
    return sequencia, winner, seqVencedora


def verVertical(matriz: List[List], player):
    winner: str = "nenhum ainda"
    sequencia: bool = False
    seqVencedora = []
    c = 0
    l: int = 0
    while l < len(matriz):
        i = matriz
        while c < len(i[l]):
            if i[l][c][2] != 0 and i[l][c][2] != 5:
                if (l + 3) < len(i):
                    if i[l][c][2] == i[l + 3][c][2]:
                        sequencia = True
                        if (l + 2) < len(i):
                            if i[l][c][2] == i[l + 2][c][2]:
                                sequencia = True
                                if (l + 1) < len(i):
                                    if i[l][c][2] == i[l + 1][c][2]:
                                        sequencia = True
                                        seqVencedora = [i[l][c], i[l + 1][c], i[l + 2][c], i[l + 3][c]]
                                        winner = player
                                        return sequencia, winner, seqVencedora
                                    else:
                                        sequencia = False
                            else:
                                sequencia = False
                    else:
                        sequencia = False
            c = c + 1
        l: int = l + 1
        c = 0
    return sequencia, winner, seqVencedora


def verDiagonais(matriz, player):
    sequencia = False
    seqVencedora = []
    winner = "ninguém"
    diagonais: List[List] = []
    diag: List[List] = []
    for l in range(len(matriz)):
        cDiag = 0
        lDiag: int = l
        diag.append(matriz[lDiag][cDiag])
        while lDiag < len(matriz) - 1:
            lDiag = lDiag + 1
            cDiag = cDiag + 1
            diag.append(matriz[lDiag][cDiag])
        diagonais.append(diag)
        diag = []
        lDiag = len(matriz) - 1 - l
        cDiag = len(matriz[0]) - 1
        diag.append(matriz[lDiag][cDiag])
        while lDiag < len(matriz) - 1:
            lDiag = lDiag + 1
            cDiag = cDiag - 1
            diag.append(matriz[lDiag][cDiag])
        diagonais.append(diag)
        diag = []
    for c in range(len(matriz[0])):
        cDiag = c
        lDiag = 0
        diag.append(matriz[lDiag][cDiag])
        while cDiag < len(matriz[0]):
            lDiag = lDiag + 1
            cDiag = cDiag + 1
            if lDiag < len(matriz) and cDiag < len(matriz[0]):
                diag.append(matriz[lDiag][cDiag])
        diagonais.append(diag)
        diag = []
        cDiag = len(matriz) - 1 - c
        lDiag = 0
        diag.append(matriz[lDiag][cDiag])
        while cDiag >= 0:
            lDiag = lDiag + 1
            cDiag = cDiag - 1
            if lDiag <= len(matriz) and cDiag >= 0:
                diag.append(matriz[lDiag][cDiag])
        diagonais.append(diag)
        diag = []
    diagonalVer: List[List] = []
    for x in diagonais:
        if len(x) >= 4:
            diagonalVer.append(x)
    c = 0
    for i in diagonalVer:
        while c < len(i):
            if i[c][2] != 0 and i[c][2] != 5:
                if (c + 3) < len(i):
                    if i[c][2] == i[c + 3][2]:
                        sequencia = True
                        if (c + 2) < len(i):
                            if i[c][2] == i[c + 2][2]:
                                sequencia = True
                                if (c + 1) < len(i):
                                    if i[c][2] == i[c + 1][2]:
                                        sequencia = True
                                        seqVencedora = [i[c], i[c + 1], i[c + 2], i[c + 3]]
                                        winner = player
                                        return sequencia, winner, seqVencedora
                                    else:
                                        sequencia = False
                            else:
                                sequencia = False
                    else:
                        sequencia = False
            c = c + 1
        c = 0
    return sequencia, winner, seqVencedora


def procura(matriz, player: str):
    verifica, winner, seqWin = verVertical(matriz, player)
    if not verifica:
        verifica, winner, seqWin = verDiagonais(matriz, player)
    if not verifica:
        verifica, winner, seqWin = verHorizontal(matriz, player)
    if verifica:
        winner = player
        seqWin[0][2] = 5
        seqWin[1][2] = 5
        seqWin[2][2] = 5
        seqWin[3][2] = 5

    return verifica, winner, seqWin

# print("vencedor diagonal", verDiagonais(([
# [[1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0], [1, 6, 0], [1, 7, 0]],
#                     [[2, 1, 0], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0], [2, 6, 0], [2, 7, 0]],
#                     [[3, 1, 0], [3, 2, 0], [3, 3, 0], [3, 4, 0], [3, 5, 0], [3, 6, 0], [3, 7, 9]],
#                     [[4, 1, 0], [4, 2, 0], [4, 3, 0], [4, 4, 0], [4, 5, 0], [4, 6, 9], [4, 7, 0]],
#                     [[5, 1, 0], [5, 2, 0], [5, 3, 0], [5, 4, 0], [5, 5, 9], [5, 6, 0], [5, 7, 0]],
#                     [[6, 1, 0], [6, 2, 0], [6, 3, 0], [6, 4, 9], [6, 5, 0], [6, 6, 0], [6, 7, 0]]])))
# print("")
# print("vencedor horizontal", verHorizontal([[[1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0]],
#                                            [[2, 1, 0], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0]],
#                                            [[3, 1, 0], [3, 2, 0], [3, 3, 0], [3, 4, 0], [3, 5, 0]],
#                                            [[4, 1, 0], [4, 2, 0], [4, 3, 0], [4, 4, 0], [4, 5, 0]]]))
# print("")
# print("vencedor horizontal", verHorizontal([[[1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0]],
#                                            [[2, 1, 0], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0]],
#                                            [[3, 1, 0], [3, 2, 2], [3, 3, 2], [3, 4, 2], [3, 5, 2]]]))
# print("")
# print("vencedor horizontal", verHorizontal([[[1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0]],
#                                            [[2, 1, 0], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0]],
#                                            [[3, 1, 1], [3, 2, 1], [3, 3, 0], [3, 4, 0], [3, 5, 0]],
#                                            [[4, 1, 0], [4, 2, 1], [4, 3, 1], [4, 4, 1], [4, 5, 1]]]))
# print("")
# print("vencedor horizontal", verHorizontal([[[1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0]],
#                                            [[2, 1, 0], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0]],
#                                            [[3, 1, 0], [3, 2, 2], [3, 3, 2], [3, 4, 2], [3, 5, 2]]]))
# print("")
# print("vencedor vertical", verVertical([[[1, 1, 0], [1, 2, 0], [1, 3, 1], [1, 4, 0], [1, 5, 3]],
#                                        [[2, 1, 0], [2, 2, 0], [2, 3, 1], [2, 4, 0], [2, 5, 3]],
#                                        [[3, 1, 0], [3, 2, 0], [3, 3, 2], [3, 4, 0], [3, 5, 3]],
#                                        [[4, 1, 0], [4, 2, 0], [4, 3, 1], [4, 4, 0], [4, 5, 3]]]))
# print("")
# print("vencedor vertical 6X7", verVertical([
# [[1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0], [1, 6, 0], [1, 7, 0]],
#             [[2, 1, 0], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0], [2, 6, 0], [2, 7, 0]],
#             [[3, 1, 0], [3, 2, 0], [3, 3, 0], [3, 4, 0], [3, 5, 0], [3, 6, 2], [3, 7, 0]],
#             [[4, 1, 0], [4, 2, 0], [4, 3, 0], [4, 4, 0], [4, 5, 0], [4, 6, 2], [4, 7, 0]],
#             [[5, 1, 0], [5, 2, 0], [5, 3, 0], [5, 4, 0], [5, 5, 0], [5, 6, 2], [5, 7, 0]],
#             [[6, 1, 0], [6, 2, 0], [6, 3, 0], [6, 4, 0], [6, 5, 0], [6, 6, 2], [6, 7, 0]]]))
