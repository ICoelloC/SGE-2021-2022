from password import Pass

def pedir_entero(msg):
    valorcorrecto = False
    npassword = 0
    while not valorcorrecto:
        try:
            npassword = input(msg)
            npassword = int(npassword)
            valorcorrecto = True
        except ValueError:
            print("La longitud debe ser un entero")
    return npassword


def generar_passwords():
    npassword = pedir_entero("Introduce el número de password que deseas generar: ")

    listapassword = []
    long = -1
    msg = "Longitud de la contraseña {0} (-1 para longitud por defecto): "
    for i in range(npassword):
        valorcorrecto = False
        while not valorcorrecto:
            long = input(msg.format(str(i)))
            try:
                long = int(long)
                valorcorrecto = True
            except ValueError:
                print("La longitud debe ser un entero")
        if long == -1:
            listapassword.append(Pass())
        else:
            listapassword.append(Pass(long))
    return listapassword


def mostrar_lista_pass(lista_pass):
    for p in lista_pass:
        print(p)