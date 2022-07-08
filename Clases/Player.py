import random

from Clases.Pieces import Pieces


def throwdices():  # Retorna una tupla con int aleatorios del 1 al 6, correspondientes a los dados
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2


def salepar(datadices):  # Verifica si el resultado es el mismo en ambos dados
    dado1, dado2 = datadices
    return dado1 == dado2


class Player:

    def __init__(self, playerid, color, numberofpieces):
        self._playerid = playerid
        self._color = color
        self._numberofpieces = numberofpieces
        self._piecearray = list()
        for i in range(numberofpieces):  # Creo una lista con objetos de clase Pieces(son mis fichas)
            self._piecearray.append(Pieces(self._playerid, i))  # Estos objetos se identifican con números del 1 a n

    def getpiecearray(self):
        return self._piecearray

    def getid(self):
        return self._playerid

    def algunafichamueve(self, datadices):  # Averigua si alguna pieza se puede mover, en ese caso retorna True
        dado1, dado2 = datadices
        sumadados = dado1 + dado2
        for element in self._piecearray:
            movimientos = element.posibles_movimientos()
            if (dado1 in movimientos) or (dado2 in movimientos) or (sumadados in movimientos):
                return True
        return False

