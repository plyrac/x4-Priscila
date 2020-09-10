from typing import List
from boardCreate import *
import boardGUI as visao
from insertPiece import *
from players import *




def rodada(matriz: List[List], ordemPlay):
    verifica = False
    winner = ""
    seqWin = []
    for i in ordemPlay:
        print("Vez de", i[0])
        matriz, verifica, winner, seqWin = insertPiece(matriz, i[2], i[0], visao.getCol())
        visao.plotPieces(matriz)
        if verifica:
            break

    return matriz, verifica, winner, seqWin


def partida():
    ordemPlay = jogadores()
    j = len(ordemPlay)
    matriz = tabuleiro(j)
    visao.initGUI(len(matriz), len(matriz[0]))
    verifica = False
    winner = ""
    seqWin = []
    placar = []
    vencedores = len(ordemPlay) - 1
    while len(placar) < vencedores:
        while not verifica:
            matriz, verifica, winner, seqWin = rodada(matriz, ordemPlay)
#        print("Vencedor é", winner)
        visao.vencedor(winner)
        placar.append(winner)
        verifica = False
    print(placar)
    visao.fechar()
    return matriz


#partida()
