def producto_elementos(lista):
    producto = 1  
    for numero in lista:  
        producto *= numero  
    return producto  

numeros = [1, 2, 2, 54]
resultado = producto_elementos(numeros)
print("El producto de los elementos es:", resultado)
