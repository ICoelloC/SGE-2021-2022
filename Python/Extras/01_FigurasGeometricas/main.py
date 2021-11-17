import utilidades
import factorias


def menu():
    salir = False

    while not salir:
        print("Qué desea introducir:")
        print("1. Triángulo")
        print("2. Rectángulo")
        print("3. Circunferencia")
        print("4. Cubo") # no funciona
        print("5. Cono")
        print("6. Cilindro")# no funciona
        print("0. Salir")
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
