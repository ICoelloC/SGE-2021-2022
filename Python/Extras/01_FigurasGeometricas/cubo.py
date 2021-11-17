from rectangulo import Rectangulo


class Cubo():
    def __init__(self, lado):
        self.cara = Rectangulo(lado, lado)

    @property
    def cara(self):
        return self.__cara

    @cara.setter
    def cara(self, cara):
        self.__cara = cara

    def area(self):
        return 6 * self.cara.area()

    def perimetro(self):
        return 12 * self.cara.perimetro()

    def __str__(self):
        clase = type(self).__name__
        msg = '{0} de lado {1}'
        return msg.format(clase, self.cara.lado)
