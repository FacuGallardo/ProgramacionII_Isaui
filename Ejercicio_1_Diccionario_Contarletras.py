def contar_letras(cadena):
    frecuencias = {}  
    for letra in cadena:
        if letra.isalpha():  
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
    return frecuencias

cadena = "Hola, mamahuevo"
resultado = contar_letras(cadena)
print("Frecuencia de cada letra:", resultado)
