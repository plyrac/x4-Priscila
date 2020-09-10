from typing import List


def verDiagonal(matriz: List[List]):
    lDiag = -1
    diag = []
    diagonais = []
    for c in range(len(matriz[0])):
        cDiag = len(matriz[0]) - c
        while (c + 1) <= len(matriz[0]):
            lDiag = lDiag + 1
            if (c + 1) < len(matriz[0]):
                cDiag = cDiag - 1
                diag.append(matriz[lDiag][cDiag])
                c = c + 1
            else:
                if lDiag < len(matriz):
                    cDiag = cDiag - 1
                    diag.append(matriz[lDiag][cDiag])
                c = c + 1
        diagonais.append(diag)
        diag = []
        lDiag = -1
    lDiag = len(matriz)
    for c in range(len(matriz[0])):
        cDiag = len(matriz[0]) - c
        while (c + 1) <= len(matriz[0]):
            lDiag = lDiag - 1
            if (c + 1) < len(matriz[0]):
                cDiag = cDiag - 1
                diag.append(matriz[lDiag][cDiag])
                c = c + 1
            else:
                if lDiag < len(matriz):
                    cDiag = cDiag - 1
                    diag.append(matriz[lDiag][cDiag])
                c = c + 1
        diagonais.append(diag)
        diag = []
        lDiag = len(matriz)
    for l in range(len(matriz)):
        lDiag = len(matriz) - l
        cDiag = len(matriz[0]) - 1
        while (lDiag + 1) >= len(matriz):
            if (lDiag + 1) > len(matriz):
                lDiag = lDiag - 1
                diag.append(matriz[lDiag][cDiag])
            else:
                if lDiag == len(matriz):
                    lDiag = lDiag - 1
                    diag.append(matriz[lDiag][cDiag])
        diagonais.append(diag)
        diag = []
        lDiag = 0
    k=0
    while k < len(diagonais):
        print(diagonais[k])
        k = k + 1
    return diagonais


matriz = [[[1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0], [1, 6, 0], [1, 7, 0]],
             [[2, 1, 0], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0], [2, 6, 0], [2, 7, 0]],
             [[3, 1, 0], [3, 2, 0], [3, 3, 0], [3, 4, 0], [3, 5, 0], [3, 6, 0], [3, 7, 0]],
             [[4, 1, 0], [4, 2, 0], [4, 3, 0], [4, 4, 0], [4, 5, 0], [4, 6, 0], [4, 7, 0]],
             [[5, 1, 0], [5, 2, 0], [5, 3, 0], [5, 4, 0], [5, 5, 0], [5, 6, 0], [5, 7, 0]],
             [[6, 1, 0], [6, 2, 0], [6, 3, 0], [6, 4, 0], [6, 5, 0], [6, 6, 0], [6, 7, 0]]]
#cEscolha = 1
#print(matriz[5])
#print(matriz[5][0])
#print(matriz[len(matriz)-1])
#print(matriz[len(matriz)-1][cEscolha-1])
#print(matriz[len(matriz)-1][cEscolha-1][2])
#print("")
#print(verDiagonal(matriz))
print("vencedor diagonal", verDiagonal([[[1, 1, 0], [1, 2, 0], [1, 3, 1], [1, 4, 0], [1, 5, 3]],
                                            [[2, 1, 0], [2, 2, 0], [2, 3, 1], [2, 4, 3], [2, 5, 3]],
                                            [[3, 1, 0], [3, 2, 0], [3, 3, 3], [3, 4, 0], [3, 5, 2]],
                                            [[4, 1, 0], [4, 2, 3], [4, 3, 1], [4, 4, 0], [4, 5, 3]]]))