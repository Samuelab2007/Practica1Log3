from Player import *
from tkinter import *


# raiz = Tk()
rojo = Player("rojo", 4)
print(rojo.__getattribute__("_color"), rojo.getpiecearray())
print(rojo.__getattribute__("_piecearray")[3].getidentifier())


# raiz.title("Ventana inicial")

# raiz.geometry("450x300")

# raiz.mainloop()
