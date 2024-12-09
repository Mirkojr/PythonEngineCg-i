#
# Classe do objeto Esfera
#

import math

class Esfera():
    def __init__(self, centro, raio):
        self.centro = centro 
        self.raio = raio     
        self.cor = (0, 255, 255)

    def intersect(self, origem, direcao):
        oc = (origem[0] - self.centro[0], origem[1] - self.centro[1], origem[2] - self.centro[2])

        a = sum([d**2 for d in direcao])  
        b = 2 * sum([oc[i] * direcao[i] for i in range(3)])
        c = sum([o**2 for o in oc]) - self.raio**2 

        discriminante = b**2 - 4 * a * c

        if discriminante < 0:
            return None  
        
        t1 = (-b - math.sqrt(discriminante)) / (2 * a)
        t2 = (-b + math.sqrt(discriminante)) / (2 * a)
    
        if t1 > 0 and t2 > 0:
            if t1 < t2:
                return t1
            else:
                return t2
            
        if t1 > 0:
            return t1
        else:
            return t2
        
        return None