
#
# Basic CG-I python project using raycasting
#

from renderizador import Renderizador
from janela import Janela
from esfera import Esfera
from material import Material
from light import Light

def main():
    k_ambient = [0.5, 0, 0]
    k_specular = [0.1, 0.1, 0.1]
    k_difuse = [0.7, 0, 0]
    k_shininess = 5
    material = Material(k_ambient, k_specular, k_difuse, k_shininess)

    esfera = Esfera([-0.5, 0, -5], 0.2, material)
    esfera2 = Esfera([0.5, 0, -5], 0.2, material)
    esferas = [esfera, esfera2]

    light = Light([0, 1, -4], [0.7, 0.7, 0.7])
    lights = [light]

    cena = (esferas, lights) 
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
