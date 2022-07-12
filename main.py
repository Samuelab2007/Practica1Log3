from Clases.Player import *

# raiz = Tk()
rojo = Player(1, "rojo", 4)
verde = Player(2, "verde", 4)

result = (6, 6)
print(result)

listafichasenjuego = dict()  # contiene los array de las fichas de todos los jugadores.

rojo.getpiecearray()[0].moverpieza(12, listafichasenjuego)
rojo.getpiecearray()[0].moverpieza(5, listafichasenjuego)
rojo.getpiecearray()[0].moverpieza(7, listafichasenjuego)
verde.getpiecearray()[0].moverpieza(7, listafichasenjuego)
rojo.getpiecearray()[1].moverpieza(7, listafichasenjuego)
print(listafichasenjuego)
# raiz.title("Ventana inicial")

# raiz.geometry("450x300")

# raiz.mainloop()
