from triangulo import Triangulo


def pedir_entero(mensaje):
    correcto = False
    num = 0
    while not correcto:
        try:
            num = int(input(mensaje))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')
    return num


def crear_triangulo():
    punto1_x = pedir_entero('Introduce la coordenada x del punto 1: ')
    punto1_y = pedir_entero('Introduce la coordenada y del punto 1: ')
    punto2_x = pedir_entero('Introduce la coordenada x del punto 2: ')
    punto2_y = pedir_entero('Introduce la coordenada y del punto 2: ')
    punto3_x = pedir_entero('Introduce la coordenada x del punto 3: ')
    punto3_y = pedir_entero('Introduce la coordenada y del punto 3: ')
    return Triangulo(punto1_x, punto1_y, punto2_x, punto2_y, punto3_x, punto3_y)


def listar_triangulos(triangulos):
    for i in triangulos:
        print(i.__str__())
