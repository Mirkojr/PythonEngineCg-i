
class Light(object):

    __position = list[3]
    __intensity = list[3]

    def __init__(self, position, intensity):
        self.__position = position
        self.__intensity = intensity
        self.__on = True

    def toggle(self):
        self.on = not self.__on

    def is_on(self):
        return self.__on
    
    def get_position(self):
        return self.__position

    def getIntensity(self):
        return self.__intensity   
    
    def set_position(self, position):
        self.__position = position

    def set_intensity(self, intensity):
        self.__intensity = intensity
    
    def __str__(self):
        return f'position: {self.position}, intensity: {self.intensity}'