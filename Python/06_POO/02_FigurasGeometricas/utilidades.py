import msvcrt
import os


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


borrar_pantalla = lambda: os.system("cls")


def esperar_tecla():
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    borrar_pantalla()
