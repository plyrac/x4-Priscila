from typing import List


def verDiagonal(matriz: List[List]):
    winner: str = "ninguém"
    l = 0
    c = 0
    n = 0
    diagonais = []
    diagonalVer: List = []
    diag = []
    while (l + n) < len(matriz):
        while n < len(matriz[0]):
            if not(((c + n) >= len(matriz[0])) or ((l+n) >= len(matriz))):
                diag.append(matriz[l + n][c + n])
            else:
                if diag != []:
                    diagonais.append(diag)
                diag = []
            n = n + 1
        if diag != []:
            diagonais.append(diag)
        l = l + 1
        diag = []
        n = 0
    while (c + n) < len(matriz):
        l = 0
        while n < len(matriz[0]):
            if not(((c + n) >= len(matriz[0])) or ((l+n) >= len(matriz))):
                diag.append(matriz[l + n][c + n])
            else:
                if diag != []:
                    diagonais.append(diag)
                diag = []
            n = n + 1
        if diag != []:
            diagonais.append(diag)
        c = c + 1
        diag = []
        n = 0
    ç = 0
    while ç < len(diagonais):
        print("matriz diagonais", diagonais[ç])
        ç = ç + 1
#    print("matriz diagonais", diagonais)
    e = 0
    for x in diagonais:
        if diagonalVer != []:
            for y in diagonalVer:
                if x == y:
                    break
                elif x != y:
                    if len(x) >= 4:
                        diagonalVer.append(x)
                else:
                    break
        else:
            if len(x) >= 4:
                diagonalVer.append(x)
    ç = 0
    while ç < len(diagonalVer):
        print("diagonal verificada", diagonalVer[ç])
        ç = ç + 1
#    print("diagonal verificada", diagonalVer)
    if winner == "ninguém":
        return False, winner
    else:
        return True, winner



# print("vencedor diagonal", verDiagonal([[1, 2, 3, 0], [5, 6, 0, 8], [9, 0, 11, 12], [0, 14, 15, 16]]))
print("vencedor diagonal", verDiagonal([[[1, 1, 0], [1, 2, 0], [1, 3, 1], [1, 4, 0], [1, 5, 3]],
                                        [[2, 1, 0], [2, 2, 0], [2, 3, 1], [2, 4, 3], [2, 5, 3]],
                                        [[3, 1, 0], [3, 2, 0], [3, 3, 3], [3, 4, 0], [3, 5, 2]],
                                        [[4, 1, 0], [4, 2, 3], [4, 3, 1], [4, 4, 0], [4, 5, 3]]]))
