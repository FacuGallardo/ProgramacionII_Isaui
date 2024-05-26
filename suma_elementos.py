def suma_elementos(lista):
    suma = 0  
    for numero in lista:  
        suma += numero  
    return suma  

numeros = [132, 22, 35, 41, 56,12,76,23,76]
resultado = suma_elementos(numeros)
print("La suma de los elementos es:", resultado)


