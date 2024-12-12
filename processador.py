#
# Processador de interseccoes 
#
import math


class Processador():

    def __init__(self, cena):
        self.objetos = cena[0]
        self.luzes = cena[1]
        self.DOUBLE_MAX = 1.7976931348623158E+308 
        self.bgColor = (100, 100, 100)
        self.ambientIntensity = [0.6, 0.6, 0.6]
        
    def calculateColor(self, origem, direcao):
        objeto, distancia = self.intersectObjects(origem, direcao)
        if objeto == None:
            return self.bgColor
        else:
            ponto = [origem[i] + direcao[i] * distancia for i in range(3)]
            normal = objeto.getNormal(ponto)
            view_dir = [-direcao[i] for i in range(3)]
            return self.calcularIluminacaoPhong(ponto, normal, view_dir, objeto.getMaterial(), self.luzes)

    def intersectObjects(self, origem, direcao):
        menorDistancia = self.DOUBLE_MAX
        objetoMaisProximo = None
        for objeto in self.objetos:
            resultado = objeto.intersect(origem, direcao)
            if(resultado != None) and (resultado < menorDistancia):
                objetoMaisProximo = objeto
                menorDistancia = resultado
        return (objetoMaisProximo, menorDistancia)

    def calcularIluminacaoPhong(self, ponto, normal, view_dir, material, luzes):
        ambient_color = [0, 0, 0]
        difuse_color = [0, 0, 0]
        specular_color = [0, 0, 0]

        view_dir = self.normalize(view_dir)
        normal = self.normalize(normal)

        # Ambient component
        for i in range(3):
            ambient_color[i] += self.ambientIntensity[i] * material.getAmbient()[i]

        for luz in luzes:
            if not luz.is_on():
                continue


            # Diffuse component
            light_dir = [luz.get_position()[i] - ponto[i] for i in range(3)]
            light_dir_mag = math.sqrt(sum([d**2 for d in light_dir]))
            light_dir = [d / light_dir_mag for d in light_dir]

            dot_nl = max(0, sum([normal[i] * light_dir[i] for i in range(3)]))
            for i in range(3):
                difuse_color[i] += luz.getIntensity()[i] * material.getDifuse()[i] * dot_nl

            # Specular component
            reflect_dir = [2 * dot_nl * normal[i] - light_dir[i] for i in range(3)]
            reflect_dir_mag = math.sqrt(sum([r**2 for r in reflect_dir]))
            reflect_dir = [r / reflect_dir_mag for r in reflect_dir]

            dot_rv = max(0, sum([reflect_dir[i] * view_dir[i] for i in range(3)]))
            spec = dot_rv ** material.getShininess()
            for i in range(3):
                specular_color[i] += luz.getIntensity()[i] * material.getSpecular()[i] * spec

        # Combine all components
        cor_final = [0, 0, 0]
        for i in range(3):
            cor_final[i] = min(255, int((ambient_color[i] + difuse_color[i] + specular_color[i]) * 255))

        return tuple(cor_final)
    
    def normalize(self, v):
        norm = math.sqrt(sum([d**2 for d in v]))
        return [d / norm for d in v]
        
    