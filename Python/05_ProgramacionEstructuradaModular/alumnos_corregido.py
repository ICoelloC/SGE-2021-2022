def agregarAlumno(dicc, nombre, apellidos, dni):
    alumno = {"nombre": nombre, "apellidos": apellidos }
    """Si el dni existía en el almacén será sobreescrito"""
    dicc[dni]=alumno

def mostrarAlumnos(dicc):
    for dni,alumno in dicc.items():
        print("DNI:", dni, alumno)

def buscarAlumnos(dicc, **kwargs):
    resultados_busqueda = [];
    if "dni" in kwargs.keys():
        alumno = dicc[dni];
        resultados_busqueda.append(alumno);
    else:
        almacen_filtrado = dicc.values();
        alumno_buscado = True
        for alumno in almacen_filtrado:
            for name,value in kwargs.items():
                if alumno_buscado and alumno[name] != value: alumno_buscado = False
            if alumno_buscado: resultados_busqueda.append(alumno)
            else: alumno_buscado = True

    return resultados_busqueda;

if __name__ == '__main__':
    almacenAlumnos = {}
    parar = False
    nombre = ""
    apellidos = ""
    dni = ""
    while not parar:
        print("Introduzca los datos del alumno (S para salir)")
        nombre = input("Nombre: ")
        if(nombre != "S"):
            apellidos = input("Apellidos: ")
            if (apellidos != "S"):
                dni = input("DNI: ")
            else: parar = True
        else: parar = True
        if (not parar):
            agregarAlumno(almacenAlumnos, nombre, apellidos, dni)

    print(buscarAlumnos(almacenAlumnos, nombre="Marta", apellidos="Gómez"))