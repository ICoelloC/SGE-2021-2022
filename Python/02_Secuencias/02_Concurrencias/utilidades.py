def is_in_lista(lista, cadena):
    if cadena in lista:
        print("La cadena %s está en la lista" % cadena)
    else:
        print("La cadena no está en la lista")

def sustituir_valor(lista, apariciones, valor_a_sutituir, valor_sustitutivo):
    pos = 0
    for _ in range(apariciones):
        pos = lista.index(valor_a_sutituir, pos)
        lista[pos] = valor_sustitutivo
    return lista
