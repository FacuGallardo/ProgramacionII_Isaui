def filtrar_diccionario(diccionario, claves):
    dic_filtrado = {}  
    for clave in claves:  
        if clave in diccionario:   
            dic_filtrado[clave] = diccionario[clave]  
    return dic_filtrado  

diccionario = {'F': 1, 'bq': 2, 'cd': 3, 'dx': 4, 'cd': 5}
claves = ['F', 'cd', 'l']
resultado = filtrar_diccionario(diccionario, claves)
print("Diccionario filtrado:", resultado)
