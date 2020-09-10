from typing import List
from typing import Dict
from boardCreate import *

class Data:
    def __init__(self, niver: str):
        niver = niver.split("/")
        self.diaN = int(niver[0])
        self.mesN = int(niver[1])
        self.anoN = int(niver[2])

    def idade(self):
        anoidade = 2100
        mesidade = 1
        diaidade = 30
        if self.diaN < 30:
            diaidade = diaidade - self.diaN
        elif self.diaN >= 30:
            diaidade = self.diaN
        if self.mesN == 1:
            mesidade = 0
            anoidade = anoidade - self.anoN
        elif self.mesN > 1 and self.mesN <= 12:
            mesidade = 13 - self.mesN
            anoidade = 2099 - self.anoN
        idadePlayer = [anoidade, mesidade, diaidade]
        return idadePlayer

    def dia_aniversario(self):
        return self.diaN

    def mes_aniversario(self):
        return self.mesN

    def ano_aniversario(self):
        return self.anoN


class Player:
    def __init__(self, n: str, d: Data, p: int, c: int):
        self.nome = n
        self.aniversario: List[int] = [d.dia_aniversario(), d.mes_aniversario(), d.ano_aniversario()]
        self.idade = d.idade()
        self.points = p
        self.cor = c

    def jogador(self):
        return self.nome

    def corPartida(self):
        return self.cor

    def aniversario(self):
        return self.aniversario

    def idadeP(self):
        return self.idade


def jogadores():
    j = numJogadores()
    i = 1
    players = []
    while i <= j:
        print("Nome do jogador:")
        n = input()
        print("Data de nascimento (no formato dd/mm/aaaa)")
        data = input()
        d: Data = Data(data)
        print("Escolha a cor da ficha (números de 1 a 4)")
        c = int(input())
        p_i: Player = Player(n, d, 0, c)
        p_i_dados = [p_i.jogador(), p_i.idadeP(), p_i.corPartida()]
        players.append(p_i_dados)
        i = i + 1
    ordemPlay = ordemRodada(players)
    print("Ordem de jogada")
    x=0
    for x in ordemPlay:
        print(x)

    return ordemPlay


def ordenar(p:List, q:List):
    player1 = []
    player2 = []
    anos_p1 = p[1][0]
    anos_p2 = q[1][0]
    if anos_p1 < anos_p2:
        player1 = q
        player2 = p
    elif anos_p1 == anos_p2:
        mes_p1 = p[1][1]
        mes_p2 = q[1][1]
        if mes_p1 < mes_p2:
            player1 = q
            player2 = p
        elif mes_p1 == mes_p2:
            dia_p1 = p[1][1]
            dia_p2 = q[1][1]
            if dia_p1 < dia_p2:
                player1 = q
                player2 = p
            else:
                player1 = p
                player2 = q
        else:
            player1 = p
            player2 = q
    else:
        player1 = p
        player2 = q

    return player1, player2



def ordemRodada(players: List[List]):
    ordemPlay: List = []
    p1 = players[0]
    p2 = players[1]
    player3 = []
    player4 = []
    player1, player2 = ordenar(p1, p2)
    playAux = [player1, player2, player3, player4]
    if len(players) > 2:
        p3 = players[2]
        player2, player3 = ordenar(player2, p3)
        playAux = [player1, player2, player3, player4]
        if len(players) == 4:
            p4 = players[3]
            player3, player4 = ordenar(player3, p4)
            playAux = [player1, player2, player3, player4]
    for i in playAux:
        if i != []:
            ordemPlay.insert(0, i)

    return ordemPlay


#print(jogadores())