def sumar_valores(diccionario):
    suma_total = 0  
    for valor in diccionario.values():  
        suma_total += valor  
    return suma_total  

diccionario = {'C': 1, 'D': 2, 'Z': 3, 'X': 4}
resultado = sumar_valores(diccionario)
print("La suma de todos los valores es:", resultado)