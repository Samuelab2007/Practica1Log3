from Clases.MovimientoInvalidoError import MovimientoInvalidoError


class Pieces:

    # Posición inicial de las piezas al ser puestas en juego[cuadrante, casilla dentro del bloque]

    def __init__(self, playeridentifier, pieceidentifier):
        self._coronada = False
        self._jugadorvinculado = playeridentifier
        self._id = pieceidentifier
        self._relatedtoplayer = playeridentifier
        self._position = [playeridentifier, 0 % 17]  # La progresión es: [1,0] -> [2,0] -> [3,0] -> [0,0]

    def getidentifier(self):
        return self._id

    def getposition(self):
        return self._position

    def setposition(self, cuadrante, posinterna):  # Existe con objetivos de testing, luego se debería eliminar esta funcion
        self._position = [cuadrante, posinterna]

    def moverpieza(self, numberofsquares):
        casillasposibles = self.posibles_movimientos()  # Tupla con las casillas donde me puedo mover
        if numberofsquares in casillasposibles:  # Comprueba si la cantidad seleccionada está dentro de los movimientos posibles.
            if numberofsquares == 8:
                self._coronada = True
            else:
                resultado = self._position[1] + numberofsquares  # Agrega a la posición en el bloque, si se pasa de 17 asume que pasó de cuadrante, el sobrante es la nueva subposicion.
                self._position[0] = (self._position[0] + resultado // 17) % 4
                self._position[1] = resultado % 17
        else:
            raise MovimientoInvalidoError()  # Lanza una excepción personalizada con el mensaje a mostrar en la interfaz

    def llegafasefinal(self):
        if self._position == [(self._relatedtoplayer + 3) % 4, 12]:  # Indica la posicion del ultimo seguro
            return True  # El valor a sumar y a modular se halla con el numero de jugadores que estén en juego
        else:
            return False

    def posibles_movimientos(self):  # Retorna la cantidad de casillas que se puede mover según la posición
        if self.llegafasefinal():
            return [8]
        else:
            position = self._position[1]  # Posicion dentro del bloque
            if position == 0:  # Coordenada de la casilla de salida
                return [7, 12]
            if position == 7:
                return [5, 10]
            if position == 12:
                return [5, 12]

# El proceso para moverse requiere: 1.  Un escaneo general de todos los movimientos de las fichas.
# TODO:                             2.  El jugador selecciona la ficha que quiera mover.
#                                   3.  Hace click en la cantidad que quiera mover según los dados.

#                                   4.  El sistema comprueba si la posición es posible,
#                                             En caso de que sí: (mueve la ficha y elimina el valor que movió(FALTA), continúa jugando y vuelve al paso 1)
#                                             , en caso que no lo sea: (muestra un mensaje).

#TODO: Para eliminar el valor que ya me desplazé de los dados, utilizo manejo de excepciones; si no se lanza el mensaje de movimiento ilegal supongo que me pude mover, por lo que elimino el dato que envié.
