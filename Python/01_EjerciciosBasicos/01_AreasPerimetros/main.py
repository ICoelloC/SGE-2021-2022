import areas
import perimetros
import utilidades


def menu_principal():
    salir = False

    while not salir:

        print('Ejercicio 1.\n')
        print('1.Calcular perímetros.\n2.Calcular áreas.\n3.Salir')
        opc = utilidades.pedir_entero('Escoja la opción: ')

        if opc == 1:

            menu_perimetros(salir)

        elif opc == 2:
            menu_areas(salir)

        elif opc == 3:
            salir = True


def menu_areas(salir):
    while not salir:
        print("Calcular Áreas de figuras Geométricas.\n")
        print("1.Cuadrado.\n2.Cubo.\n3.Círculo.\n4.Salir.\n")
        x = utilidades.pedir_entero('Escoja la figura: ')

        if x == 1:
            L = utilidades.pedir_entero('Ingrese la longitud del lado: ')
            print('el area del cuadrado es: ', areas.area_cuadrado(L))

        elif x == 2:
            L = utilidades.pedir_entero('Ingrese la longitud de la cara: ')
            print('el area del cubo es: %.3f ' % areas.area_cubo(L))

        elif x == 3:
            R = utilidades.pedir_entero(
                'Ingrese el radio de la circunferencia: ')
            print('el area del círculo es %.3f ' % areas.area_circulo(R))

        elif x == 4:
            salir = True


def menu_perimetros(salir):
    while not salir:
        print("Calcular Perímetros de figuras Geométricas.\n")
        print("1.Cuadrado.\n2.Cubo.\n3.Círculo.\n4.Salir\n")
        x = utilidades.pedir_entero('Escoja la figura: ')

        if x == 1:
            L = utilidades.pedir_entero('Ingrese la longitud del lado: ')
            print('el perímetro del cuadrado es: ',
                  perimetros.perimetro_cuadrado(L))

        elif x == 2:
            L = utilidades.pedir_entero('Ingrese la longitud de la cara: ')
            print('el perímetro del cubo es: %.3f ' %
                  perimetros.perimetro_cubo(L))

        elif x == 3:
            R = utilidades.pedir_entero(
                'Ingrese el radio de la circunferencia: ')
            print('el perímetro de la circunferencia es %.3f ' %
                  perimetros.perimetro_circulo(R))

        elif x == 4:
            salir = True


menu_principal()
