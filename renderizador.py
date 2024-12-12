#
# Renderizador 
#
from PIL import Image # type: ignore
from tkinter import Tk, Label
import io
from processador import Processador

class Renderizador():

    def __init__(self, cena, w, h, largura, altura):
        self.objetos = cena[0]
        self.luzes = cena[1]
        self.w = w
        self.h = h
        self.dx = w/largura
        self.dy = h/altura
        self.processador = Processador(cena)

    def renderizar(self):
        largura, altura = 500, 500
        imagem = Image.new('RGB', (largura, altura), "white")  # Fundo branco
        pixels = imagem.load()

        for l in range(altura):
            y = self.h / 2 - (self.dy / 2) - l * self.dy
            for c in range(largura):
                x = -self.w / 2 + (self.dx / 2) + c * self.dx

                direcao = [x, y, -5] 
                cor = self.processador.calculateColor([0, 0, 0], direcao)  
                pixels[c, l] = cor
    

        #imagem.save("canvas.png") use when want to save the image in a file
        #imagem.save("canvas1.png")
        img_byte_array = io.BytesIO()
        imagem.save(img_byte_array, format='PNG')  # Salva a imagem em formato PNG no buffer
        img_byte_array.seek(0)  # Volta o ponteiro para o início
        return img_byte_array.read()  # Retorna a imagem como bytes
