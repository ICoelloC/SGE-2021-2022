import os
import msvcrt


def pedir_entero(mensaje):
    valido = False
    while not valido:
        try:
            numero = int(input(mensaje))
            valido = True
        except ValueError:
            print("Error. Debe introducir un número entero.")
    return numero


def borrar_pantalla(): return os.system("cls")


def esperar_tecla():
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    borrar_pantalla()


def dibujar_triangulo_iterativo(numero):
    for i in range(numero):
        print("*" * (i + 1))


def dibujar_triangulo_recursivo(numero):
    if numero > 0:
        dibujar_triangulo_recursivo(numero - 1)
        print("*" * numero)
