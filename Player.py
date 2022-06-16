class Player:

    def __init__(self, color, numberofpieces):
        self._color = color
        self._numberofpieces = numberofpieces
        self._piecearray = list()
        for i in range(numberofpieces):  # Creo una lista con objetos de clase Pieces(son mis fichas)
            self._piecearray.append(Pieces(i + 1))  # Estos objetos se identifican con números del 1 a n

    def getpiecearray(self):
        return self._piecearray


class Pieces:
    def __init__(self, identifier):
        self._id = identifier

    def getidentifier(self):
        return self._id
