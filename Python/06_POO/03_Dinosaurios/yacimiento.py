class Yacimiento:

    def __init__(self, nombre):
        self.nombre = nombre
        self.dinosaurios = []

    @property
    def dinosaurios(self):
        return self.__dinosaurios

    @property
    def nombre(self):
        return self.__nombre

    @dinosaurios.setter
    def dinosaurios(self, dinosaurios):
        self.__dinosaurios = dinosaurios

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def add_dinosaurio(self, dinosaurio):
        self.__dinosaurios.append(dinosaurio)

    def hay_cazadores(self):
        hay_cazadores = False
        i = 0
        while not hay_cazadores and i < len(self.dinosaurios):
            d = self.dinosaurios[i]
            if d.vivo and type(d).__name__ in ["Rex", "Spinosaurus"]:
                hay_cazadores = True
            i += 1
        return hay_cazadores

    def ordenar_dinosaurios(self):
        self.__dinosaurios.sort(key=lambda dinosaurio: dinosaurio.pos_x)

    def __str__(self):
        self.ordenar_dinosaurios()
        clase = type(self).__name__
        msg = "{0} => Nombre: {1}\nDinosaurios: \n"
        for dino in self.dinosaurios:
            msg += dino.__str__() + "\n"
        return msg.format(clase, self.nombre)
