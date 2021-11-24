def pedir_entero(mensaje):
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input(mensaje))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')
    return num

def es_subcadena(cad1, cad2):
    return cad1.find(cad2)>-1

def crear_lista():
    continuar = True
    lista = []
    while continuar:
        cad = input("Introduce una cadena: ")
        if cad != "":
            lista.append(cad)
        else:
            continuar = False
    return lista