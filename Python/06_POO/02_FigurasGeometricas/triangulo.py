from poligono import Poligono


class Triangulo(Poligono):
    def __init__(self, base, altura, *args):
        if len(args) != 3:
            raise ValueError("Un triángulo tiene 3 lados")
        super().__init__(*args)
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        if base <= 0:
            raise ValueError("La base debe ser mayor que cero")
        self._base = base

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        if altura <= 0:
            raise ValueError("La altura debe ser mayor que cero")
        self._altura = altura

    def area(self):
        return self.base * self.altura / 2
