from poligono import Poligono


class Rectangulo(Poligono):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, base):
        if base <= 0:
            raise ValueError("La base debe ser mayor a cero")
        self.__base = base

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        if altura <= 0:
            raise ValueError("La altura debe ser mayor a cero")
        self.__altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

