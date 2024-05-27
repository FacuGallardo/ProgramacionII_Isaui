def agrupar_por_longitud(lista_palabras):
    diccionario = {}  
    for palabra in lista_palabras:  
        longitud = len(palabra)  
        if longitud not in diccionario:  
            diccionario[longitud] = [palabra]  
        else:  
            diccionario[longitud].append(palabra)
    return diccionario  

palabras = ["Hola", "Tengo", "sueño", "Hambre", "desesperacion", "ansiedad", "y", "mucho", "sueño"]
resultado = agrupar_por_longitud(palabras)
print("Palabras agrupadas por longitud:", resultado)