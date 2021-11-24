import utilidades
from triangulo import Triangulo
from cubo import Cubo
from cono import Cono
from cilindro import Cilindro
from rectangulo import Rectangulo
from circunferencia import Circunferencia

def crear_triangulo():
    base = utilidades.pedir_entero("Base: ")
    altura = utilidades.pedir_entero("Altura: ")
    print("Introduce los dos lados que faltan: ")
    lado2 = utilidades.pedir_entero("Lado2: ")
    lado3 = utilidades.pedir_entero("Lado3: ")
    return Triangulo(base, altura, base, lado2, lado3)


def crear_rectangulo():
    base = utilidades.pedir_entero("Base: ")
    altura = utilidades.pedir_entero("Altura: ")
    return Rectangulo(base, altura)


def crear_circunferencia():
    radio = utilidades.pedir_entero("Radio: ")
    return Circunferencia(radio)


def crear_cubo():
    lado = utilidades.pedir_entero("Lado: ")
    return Cubo(lado)


def crear_cono():
    radio = utilidades.pedir_entero("Radio: ")
    generatriz = utilidades.pedir_entero("Generatriz: ")
    return Cono(radio, generatriz)


def crear_cilindro():
    radio = utilidades.pedir_entero("Radio: ")
    altura = utilidades.pedir_entero("Altura: ")
    return Cilindro(radio, altura)
