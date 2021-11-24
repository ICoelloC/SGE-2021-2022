import utilidades as ut
frase = input("Frase:")
lista_palabras=frase.split(" ")

dicc = ut.generar_diccionario(lista_palabras)

print ('\nLISTADO DE PALABRAS')
for campo,valor in dicc.items():
    print (campo+":",valor)