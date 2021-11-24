def pedir_entero(mensaje):
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input(mensaje))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num


def es_bisiesto(anio):
    return not anio % 4 and (anio % 100 or not anio % 400)
