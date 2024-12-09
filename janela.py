#
# Janela para mostrar o canvas
#

from tkinter import Tk, Label
from PIL import Image, ImageTk # type: ignore
import io

class Janela():

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.root = Tk()
        self.root.title("Exibir Imagem")
        self.label = Label(self.root)
        self.label.pack()

    def atualizar_imagem(self, imagem_bytes):

        img = Image.open(io.BytesIO(imagem_bytes))  
        img_tk = ImageTk.PhotoImage(img)
        
        self.label.config(image=img_tk)
        self.label.image = img_tk 

    def abrir(self):
        self.root.mainloop()

    def getLargura(self):
        return self.largura
    
    def getAltura(self):
        return self.altura