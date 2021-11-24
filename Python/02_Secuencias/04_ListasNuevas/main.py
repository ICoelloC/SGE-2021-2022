import utilidades

lista1 = utilidades.crear_lista()
lista1 = utilidades.borrar_repetidos(lista1)
print("Lista 1 sin repetidos: ", lista1,'\n')

lista2 = utilidades.crear_lista()
lista2 = utilidades.borrar_repetidos(lista2)
print("Lista 2 sin repetidos: ", lista2,'\n')

comunes = utilidades.elementos_comunes(lista1, lista2)
print("Palabras que aparecen en las dos listas: ", comunes,'\n')

elementosSoloPrimera = utilidades.elementos_solo_una_lista(lista1, lista2)
print("Palabras que aparecen sólo en la primera: ", elementosSoloPrimera,'\n')

elementosSoloSegunda = utilidades.elementos_solo_una_lista(lista2, lista1)
print("Palabras que aparecen sólo en la segunda: ", elementosSoloSegunda)
