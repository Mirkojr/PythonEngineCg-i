
#
# Basic CG-I python project using raycasting
#

from renderizador import Renderizador
from janela import Janela
from esfera import Esfera

def main():
    esfera = Esfera([-0.5, 0, -5], 0.2)
    esfera2 = Esfera([0.5, 0, -5], 0.2)
    esferas = [esfera, esfera2]
    cena = (esferas, []) 
    renderizador = Renderizador(cena, 2, 2, 500, 500)

    #cria a janela
    janela = Janela(500, 500)

    #gera a imagem (como bytes) e passa para a janela
    imagem_bytes = renderizador.renderizar()
    janela.atualizar_imagem(imagem_bytes)

    #abre a janela
    janela.abrir()
    

if __name__ == "__main__":
    main()
