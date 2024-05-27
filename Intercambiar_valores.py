def intercambiar_valores(diccionario, clave1, clave2):
    if clave1 in diccionario and clave2 in diccionario:  
        
        diccionario[clave1], diccionario[clave2] = diccionario[clave2], diccionario[clave1]
    return diccionario  

diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
clave1 = 'b'
clave2 = 'd'
resultado = intercambiar_valores(diccionario, clave1, clave2)
print("Diccionario después de intercambiar los valores:", resultado)