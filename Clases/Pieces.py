class Pieces:

    # Posición inicial de las piezas al ser puestas en juego[cuadrante, casilla dentro del bloque]

    def __init__(self, playeridentifier, pieceidentifier):
        self._jugadorvinculado = playeridentifier
        self._id = pieceidentifier
        self._relatedtoplayer = playeridentifier
        self._position = [playeridentifier, 0 % 17]  # El mínimo en la tupla es [1, 0], el máximo es [4, 16]

    def getidentifier(self):
        return self._id

    def setposition(self, cuadrante, posinterna):
        self._position = [cuadrante, posinterna]

    def moverpieza(self, numberofpieces):
        resultado = self._position[1] + numberofpieces
        self._position[0] += resultado // 17
        self._position[1] += resultado % 17

    def llegafasefinal(self):
        if self._position == [(self._relatedtoplayer + 3) % 4, 12]:  # Indica la posicion del ultimo seguro
            return True  # El valor a sumar y a modular se halla con el numero de jugadores que estén en juego
        else:
            return False
