import utilidades as ut


class Alumno():
    def __init__(self, dni, nombre=None, apellidos=None, edad=None, genero=None, curso=None):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.genero = genero
        self.edad = edad
        self.curso = curso

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero):
        self.__genero = genero

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso):
        self.__curso = curso

    def to_dictionary(self, alumno_dict):
        character_data = {
            'nombre': self.nombre,
            'apellidos': self.apellidos,
            'genero': self.genero,
            'edad': self.edad,
            'curso': self.curso
        }

        alumno_dict.setdefault(self.dni, character_data)
        return alumno_dict