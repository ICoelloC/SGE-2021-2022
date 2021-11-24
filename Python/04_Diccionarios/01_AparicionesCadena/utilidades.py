def generar_diccionario(lista_palabras):
    dic = {}
    for palabra in lista_palabras:
        if palabra in dic:
            dic[palabra]+=1
        else:
            dic[palabra]=1
    return dic

