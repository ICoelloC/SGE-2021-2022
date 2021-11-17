import utilidades


def menu():
    continuar = True
    while continuar:
        print("""
        1. Iniciales
        2. Letras finales
        3. Capitalizar
        4. Palabras que empiezen por A
        5. Salir
        """)
        opcion = utilidades.pedir_entero("Elige una opción: ")
        if opcion == 1:
            cadena = input("Introduce una cadana para mostrar sus iniciales: ")
            print('Iniciales para la cadena "',cadena,'"->',utilidades.iniciales(cadena))
        elif opcion == 2:
            cadena = input("Introduce una cadana para mostrar sus letras del final: ")
            print('Letras finales de la cadena "',cadena,'"->',utilidades.letra_final(cadena))
        elif opcion == 3:
            cadena = input("Introduce una cadana para capitalizar sus iniciales: ")
            print('La cadena capitalizada es la siguiente -> "',utilidades.capitalizar(cadena)+'"')
        elif opcion == 4:
            cadena = input("Introduce una cadana para mostrar las palabras que empiezan por A: ")
            print(' Las palabras que empiezan por A son las siguientes ->',utilidades.palabras_comienzan_a(cadena))
        elif opcion == 5:
            continuar = False
        else:
            print("Opción no válida")

menu()
