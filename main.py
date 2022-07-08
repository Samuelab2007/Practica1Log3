from Clases.Player import *

# raiz = Tk()
rojo = Player(1, "rojo", 4)
verde = Player(2, "verde", 4)


print(rojo.__getattribute__("_piecearray")[3].getidentifier())
result = (6, 6)
print(result)

rojo.getpiecearray()[0].moverpieza(12)
verde.getpiecearray()[0].moverpieza(7)




# raiz.title("Ventana inicial")

# raiz.geometry("450x300")

# raiz.mainloop()
