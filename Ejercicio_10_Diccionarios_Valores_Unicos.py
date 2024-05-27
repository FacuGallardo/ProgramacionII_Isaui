def valores_unicos(diccionario):
    return list(set(diccionario.values())) 

diccionario = {'a': 20, 'b': 2.2, 'c': 2.2, 'd': 2, 'e': 1}
resultado = valores_unicos(diccionario)
print("Lista de valores únicos:", resultado)

