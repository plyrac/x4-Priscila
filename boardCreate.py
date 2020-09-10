#Create a board given a size parameter

from typing import List


def numJogadores() -> int:
    print("Número de jogadores")
    j = int(input())
    return j


def tabuleiro(j: int) -> List[List]:
    ncolunas: int = 5+j
    nlinhas: int = 4+j
    matriz: List = []
    linhasMatriz: List = []
    n = 1
    c = 1
    i = 0
    l = 1
    while n < (nlinhas + 1):
        matriz.append([])
        n = n + 1
    while i < len(matriz):
        while l < (nlinhas + 1):
            while c < (ncolunas + 1):
                linhasMatriz.append([l, c, 0])
                c = c + 1
            l = l + 1
            c = 1
            matriz[i] = linhasMatriz
            i = i + 1
            linhasMatriz = []
#    x = 0
#    while x < len(matriz):
#        print(matriz[x])
#        x = x + 1
    return matriz


#tabuleiro(numJogadores())
