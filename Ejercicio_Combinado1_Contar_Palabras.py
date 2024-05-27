def contar_palabras(lista_frases):
    frecuencias = {}  
    for frase in lista_frases:  
        palabras = frase.split()  
        for palabra in palabras:  
            if palabra in frecuencias:  
                frecuencias[palabra] += 1
            else:  
                frecuencias[palabra] = 1
    return frecuencias  

frases = [
    "Hola, hola que tal",
    "Carta trampa seteada",
    "Invoco a Exodia",
    "Tengo sueño"
]
resultado = contar_palabras(frases)
print("Frecuencias de palabras:", resultado)
