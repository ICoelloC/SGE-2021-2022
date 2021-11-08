import utilidades


def menu():
    salir = False
    while not salir:
        print("1. Dibujar triángulo iterativo")
        print("2. Dibujar triángulo recursivo")
        print("3. Salir")
        opc = utilidades.pedir_entero("Elige una opción: ")
        if opc == 1:
            altura = utilidades.pedir_entero(
                'Introduce la altura del tríangulo: ')
            utilidades.dibujar_triangulo_iterativo(altura)
            utilidades.esperar_tecla()
        elif opc == 2:
            altura = utilidades.pedir_entero(
                'Introduce la altura del tríangulo: ')
            utilidades.dibujar_triangulo_recursivo(altura)
            utilidades.esperar_tecla()
        elif opc == 3:
            print("Adiós")
            salir = True


menu()
