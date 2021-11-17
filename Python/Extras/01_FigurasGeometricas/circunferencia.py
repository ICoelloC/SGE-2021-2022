import math


class Circunferencia():
    def __init__(self, radio):
        self.radio = radio

    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser mayor que 0")
        self.__radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio
    
    def __str__(self):
        clase = type(self).__name__
        msg = "{0} de radio {1}"
        return msg.format(clase, self.radio)
