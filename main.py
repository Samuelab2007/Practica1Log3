from Clases.Player import *

# raiz = Tk()
rojo = Player(4, "rojo", 4)
print(rojo.__getattribute__("_color"), rojo.getpiecearray())
print(rojo.__getattribute__("_piecearray")[3].getidentifier())
result = throwdices()

# raiz.title("Ventana inicial")

# raiz.geometry("450x300")

# raiz.mainloop()
