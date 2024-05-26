def maximo_minimo(lista):
    if not lista:  
        return None, None  

    maximo = lista[0]  
    minimo = lista[0]  

    for numero in lista[1:]:
        if numero > maximo:  
            maximo = numero 
        if numero < minimo:  
            minimo = numero  

    return maximo, minimo            

           
numeros = [15.1, 123, 114, 216, 515, 296, 632, 126, 542, 332, 15.2]
maximo, minimo = maximo_minimo(numeros)
print("El valor máximo es:", maximo)
print("El valor mínimo es:", minimo)