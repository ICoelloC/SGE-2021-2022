import utilidades as ut


def menu_principal():
    salir = False
    dicc = {}
    while not salir:
        print("""
        1. Añadir nuevo alumno
        2. Mostrar lista de alumnos
        3. Buscar alumno
        4. Borrar alumno
        5. Salir
        """)
        opcion = ut.pedir_entero("Elige una opción: ")

        if opcion == 1:
            alumno = ut.pedir_datos_alumno()
            dicc = alumno.to_dictionary(dicc)

        elif opcion == 2:
            ut.mostrar_alumnos(dicc)

        elif opcion == 3:
            """ dni = input("Introduce el DNI del alumno: ")
            alumno = ut.buscar_alumno(dicc, dni = dni) """
            alumno = ut.buscar(dicc)
            if alumno:
                print(alumno)
            else:
                print("Alumno no encontrado")

        elif opcion == 4:
            dni = input("Introduce el DNI del alumno: ")
            ut.borrar_alumno(dicc, dni)

        elif opcion == 5:
            salir = True

        else:
            print("Opción incorrecta")

menu_principal()
