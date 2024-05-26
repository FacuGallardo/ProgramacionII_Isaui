def eliminar_duplicados(lista):
    sin_duplicados = list(set(lista)) 
    return sin_duplicados  

numeros = [1.2, 29, 32, 44, 44, 52, 126, 546, 7.8, 7.8, 7.8, 92, 103, 103]
resultado = eliminar_duplicados(numeros)
print("La lista sin duplicados es:", resultado)
