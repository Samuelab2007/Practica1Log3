from Clases.Pieces import Pieces


class Player:

    def __init__(self, playerid, color, numberofpieces):
        self._playerid = playerid
        self._color = color
        self._numberofpieces = numberofpieces
        self._piecearray = list()
        for i in range(numberofpieces):  # Creo una lista con objetos de clase Pieces(son mis fichas)
            self._piecearray.append(Pieces(self._playerid, i + 1))  # Estos objetos se identifican con números del 1 a n

    def getpiecearray(self):
        return self._piecearray

    def getid(self):
        return self._playerid
