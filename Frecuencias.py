def diccionario_frecuencias(lista_palabras):
    frecuencias = {}  
    for palabra in lista_palabras:  
        if palabra in frecuencias:
            frecuencias[palabra] += 1  
        else:
            frecuencias[palabra] = 1  
    return frecuencias  

lista_palabras = ['Hola', 'Tengo', 'Hambre', 'Sueño', 'Cansancio', 'Cansancio', 'Sueño']
resultado = diccionario_frecuencias(lista_palabras)
print("Frecuencia de cada palabra:", resultado)