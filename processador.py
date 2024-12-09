#
# Processador de interseccoes 
#
class Processador():

    def __init__(self, cena):
        self.objetos = cena[0]
        self.luzes = cena[1]
        self.DOUBLE_MAX = 1.7976931348623158E+308 
        self.bgColor = (100, 100, 100)

    def intersectObjects(self, origem, direcao):
        menorDistancia = self.DOUBLE_MAX
        objetoMaisProximo = None
        for objeto in self.objetos:
            resultado = objeto.intersect(origem, direcao)
            if(resultado != None) and (resultado < menorDistancia):
                objetoMaisProximo = objeto
                menorDistancia = resultado
        return (objetoMaisProximo, menorDistancia)