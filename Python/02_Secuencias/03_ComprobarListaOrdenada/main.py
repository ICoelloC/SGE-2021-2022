import utilidades

lista = []
salir = False

while not salir:
    num = utilidades.pedir_entero("Introduce un número: ")
    lista.append(num)
    continuar = input("Deseas continuar (x para salir)")
    if continuar in ["X", "x"]:
        salir = True

lista2=lista[:]

lista2.sort()
print(lista2)

if (utilidades.son_iguales(lista, lista2)):
    print("La lista está ordenada")
else:
    print("La lista no está ordenada")
