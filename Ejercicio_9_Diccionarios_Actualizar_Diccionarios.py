def actualizar_diccionario(diccionario, lista_tuplas):
    diccionario.update(lista_tuplas)  
    return diccionario  

diccionario = {'Y': 1, 'X': 2, 'R': 3}
lista_tuplas = [('X', 20), ('Y', 4), ('Z', 5)]
resultado = actualizar_diccionario(diccionario, lista_tuplas)
print("Diccionario actualizado:", resultado)
