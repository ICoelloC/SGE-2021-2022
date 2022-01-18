from alumno import Alumno


def is_dni_valido(dni):
    return dni.isdigit() and len(dni) == 8


def pedir_entero(mensaje):
    correcto = False
    num = 0
    while not correcto:
        try:
            num = int(input(mensaje))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num


def pedir_datos_alumno():
    dni = input('Introduce el DNI del alumno: ')
    nombre = input("Introduce el nombre del alumno: ")
    apellidos = input("Introduce los apellidos del alumno: ")
    edad = pedir_entero("Introduce la edad del alumno: ")
    genero = input("Introduce el genero del alumno: ")
    curso = input("Introduce el curso del alumno: ")
    return Alumno(dni, nombre, apellidos, edad, genero, curso)


def mostrar_alumnos(dicc):
    for alumno in dicc:
        print(alumno, '-->', dicc[alumno])


def buscar_alumno(dicc, **kwargs):
    resultado_busqueda = []
    if "dni" in kwargs.keys() and kwargs["dni"] != "":
        dni_alumno_busq = kwargs["dni"]
        alumno = dicc[dni_alumno_busq]
        resultado_busqueda.append(alumno)
    else:
        alumno_buscado = True
        for dni, alumno_dict in dicc.items():
            for name, value in kwargs.items():
                if alumno_buscado and value != "" and str(alumno_dict[name]) != value:
                    alumno_buscado = False
            if alumno_buscado:
                resultado_busqueda.append({dni: alumno_dict})
            else:
                alumno_buscado = True
    return resultado_busqueda


def borrar_alumno(dicc, dni):
    if dni in dicc:
        del dicc[dni]
    else:
        print("Alumno no encontrado")


def buscar(dicc):
    dni = input('Buscar por DNI: ')
    nombre = input("Buscar por nombre: ")
    apellidos = input("Buscar por apellidos: ")
    edad = input("Buscar por edad: ")
    genero = input("Buscar por genero: ")
    curso = input("Buscar por curso: ")
    resultado = buscar_alumno(dicc, dni=dni, nombre=nombre, apellidos=apellidos, edad=edad, genero=genero, curso=curso)
    print("El resultado de la búsqueda es: ")
    for alumno in resultado:
        print(alumno)
