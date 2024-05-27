def combinar_diccionario_listas(diccionario):
    return [elemento for lista in diccionario.values() for elemento in lista]

diccionario = {'a': [10, 20, 30], 'b': [40, 50, 60], 'c': [70, 80, 9.9]}
resultado = combinar_diccionario_listas(diccionario)
print("Lista combinada:", resultado)