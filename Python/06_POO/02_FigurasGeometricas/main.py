import utilidades
import factorias


def menu():
    salir = False

    while not salir:
        print("""
        1. Triángulo
        2. Rectángulo
        3. Circunferencia
        4. Cubo #TODO solucionar errores
        5. Cono
        6. Cilindro #TODO solucionar errores
        0. Salir
        """)
        opcion = utilidades.pedir_entero("Introduzca una opción: ")

        if opcion == 0:
            salir = True
        elif opcion == 1:
            figura = factorias.crear_triangulo()
        elif opcion == 2:
            figura = factorias.crear_rectangulo()
        elif opcion == 3:
            figura = factorias.crear_circunferencia()
        elif opcion == 4:
            figura = factorias.crear_cubo()
        elif opcion == 5:
            figura = factorias.crear_cono()
        elif opcion == 6:
            figura = factorias.crear_cilindro()
        else:
            print("Opción incorrecta.")

        if not salir:
            print(figura)
            print("Perímetro: {0}\nArea: {1}".format(figura.perimetro(), figura.area()))
            utilidades.esperar_tecla()

menu()
