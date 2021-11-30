from circunferencia import Circunferencia
from rectangulo import Rectangulo
import math


class Cilindro():
    def __init__(self, radio, altura):
        self.circunferencia = Circunferencia(radio)
        self.rectangulo = Rectangulo(2 * math.pi * radio, altura)

    @property
    def circunferencia(self):
        return self.__circunferencia

    @circunferencia.setter
    def circunferencia(self, circunferencia):
        self.__circunferencia = circunferencia

    @property
    def rectangulo(self):
        return self.__rectangulo

    @rectangulo.setter
    def rectangulo(self, rectangulo):
        self.__rectangulo = rectangulo

    def perimetro(self):
        return self.circunferencia.perimetro() * 2 + self.rectangulo.altura()

    def area(self):
        return self.circunferencia.area() * 2 + self.rectangulo.area()

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} de radio {1} y altura {2}"
        return msg.format(clase, self.circunferencia.radio, self.rectangulo.altura)
