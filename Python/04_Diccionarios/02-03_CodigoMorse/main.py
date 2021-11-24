import utilidades as ut


def menu():
    salir = False
    while not salir:
        print("""
        1. Generar morse a partir de una cadena
        2. Generar cadena a partir de código morse
        3. Salir
        """)
        opcion = ut.pedir_entero("Elige una opción: ")
        if opcion == 1:
            palabra = input("Palabra:")
            lista_codigos = ut.generar_lista_codigos(palabra)
            print(" ".join(lista_codigos))

        elif opcion == 2:
            morse = input("Morse:")
            lista_morse = morse.split(" ")
            palabra = ut.generar_palabra(lista_morse)
            print(palabra)

        elif opcion == 3:
            salir = True

        else:
            print("Opción no válida")


menu()
