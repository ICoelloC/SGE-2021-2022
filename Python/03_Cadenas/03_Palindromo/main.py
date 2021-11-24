cadena = input("Introduce una cadena para ver si es palíndroma: ")

if cadena.lower() == cadena[::-1].lower():
    print('La cadena "'+cadena+'" es palíndromo')
else:
    print('La cadena "'+cadena+'" no es palíndromo')
