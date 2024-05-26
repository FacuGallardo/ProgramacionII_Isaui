def promedio_lista(lista):
    if not lista: 
        return 0  
    
    suma = sum(lista)  
    cantidad = len(lista)  
    promedio = suma / cantidad  
    return promedio  

numeros = [130, 23.2, 65.1, 64.4, 15.5, 12.2, 43.2, 65.3,87]
promedio = promedio_lista(numeros)
print("El promedio de los elementos es:", promedio)
