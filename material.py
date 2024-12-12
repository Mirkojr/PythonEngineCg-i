
class Material():

    __k_ambient = list[3]
    __k_specular = list[3]
    __k_difuse = list[3]
    __k_shininess = float

    def __init__(self, k_ambient, k_specular, k_difuse, k_shininess):
        self.__k_ambient = k_ambient
        self.__k_specular = k_specular
        self.__k_difuse = k_difuse
        self.__k_shininess = k_shininess
    
    def getAmbient(self):
        return self.__k_ambient
    
    def getSpecular(self):
        return self.__k_specular
    
    def getDifuse(self):
        return self.__k_difuse
    
    def getShininess(self):
        return self.__k_shininess
    
    def setK_ambient(self, k_ambient):
        self.__k_ambient = k_ambient

    def setK_specular(self, k_specular):
        self.__k_specular = k_specular
    
    def setK_difuse(self, k_difuse):
        self.__k_difuse = k_difuse

    def setK_shininess(self, k_shininess):
        self.__k_shininess = k_shininess
    
    def __str__(self):
        return f'k_ambient: {self.k_ambient}, k_specular: {self.k_specular}, k_difuse: {self.k_difuse}, k_shininess: {self.k_shininess}'