import utilidades as ut


def menu_principal(lst_triangulos):
    salir = False
    while not salir:
        print("""
        1. Crear Triángulo
        2. Listar Triángulos
        3. Salir
        """)
        opcion = ut.pedir_entero("Ingrese una opción: ")
        if opcion == 1:
            lst_triangulos.append(ut.crear_triangulo())
        elif opcion == 2:
            ut.listar_triangulos(lst_triangulos)
        elif opcion == 3:
            print("Saliendo...")
            salir = True
        else:
            print("Opción inválida")


triangulos = []
menu_principal(triangulos)
