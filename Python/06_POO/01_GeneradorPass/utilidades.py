from password import Pass


def pedir_entero(msg):
    valor_correcto = False
    numero = 0
    while not valor_correcto:
        try:
            numero = input(msg)
            numero = int(numero)
            valor_correcto = True
        except ValueError:
            print("La longitud debe ser un entero")
    return numero


def generar_passwords():
    num_pass = pedir_entero("Introduce el número de password que deseas generar: ")
    lista_pass = []
    long = -1
    msg = "Longitud de la contraseña {0} (-1 para longitud por defecto): "
    for i in range(num_pass):
        valido = False
        while not valido:
            long = input(msg.format(str(i)))
            try:
                long = int(long)
                valido = True
            except ValueError:
                print("La longitud debe ser un entero")
        if long == -1:
            lista_pass.append(Pass())
        else:
            lista_pass.append(Pass(long))
    return lista_pass


def mostrar_lista_pass(lista_pass):
    for p in lista_pass:
        print(p)
