import utilidades


def menu():
    continuar = True
    while continuar:
        print("""
        1. Cadenas y Subcadenas
        2. Orden alfabetico
        3. Salir
        """)

        opcion = utilidades.pedir_entero("Elige una opción: ")

        if opcion == 1:
            cad1 = input("Cadena 1: ").lower()
            cad2 = input("Cadena 2: ").lower()
            if (cad1.find(cad2) > -1):
                print('"'+cad2+'" es subcadena de "'+cad1+'"')
            else:
                print('"'+cad2+'" no es subcadena de "'+cad1+'"')

        elif opcion == 2:
            lista = utilidades.crear_lista()
            print(min(lista))

        elif opcion == 3:
            continuar = False

        else:
            print("Opción no válida")


menu()
