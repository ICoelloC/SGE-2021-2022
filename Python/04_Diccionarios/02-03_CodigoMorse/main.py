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
            '''
            En first coge la primera palabra.
            En middle coge todas las palabras que hay entre la primera y la última.
            En last coge la última palabra.
            '''
            first, *middle, last = palabra.split()
            lista_codigos = ut.generar_lista_codigos(first)
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
