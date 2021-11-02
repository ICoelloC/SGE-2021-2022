import utilidades
import operaciones


def menu_operaciones():
    salir = False
    while not salir:
        print('\nEjercicio 2.\n')
        print('1.Sumar.\n2.Restar.\n3.Multiplicar.\n4.Dividir.\n5.Potencia\n6.Salir')
        opc = utilidades.pedir_entero('Escoja la opción: ')

        if opc == 1:
            print('\n')
            print('La suma es -->', operaciones.sumar())
        elif opc == 2:
            print('\n')
            print('La resta es -->', operaciones.restar())

        elif opc == 3:
            print('\n')
            print('La multiplicación es -->', operaciones.multiplicar())

        elif opc == 4:
            print('\n')
            print('La división es -->', operaciones.dividir())

        elif opc == 5:
            print('\n')
            print('La potencia es -->', operaciones.potencia())

        elif opc == 6:
            salir = True


menu_operaciones()
