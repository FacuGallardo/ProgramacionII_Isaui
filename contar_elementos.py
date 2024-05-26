def contar_elementos(lista, valor):
    contador = 0  
    for elemento in lista: 
        if elemento == valor:  
            contador += 1  
    return contador 

numeros = [13, 21, 21, 3.2, 4.9, 21, 6, 61, 2, 7, 8, 20, 9, 10, 23]
valor = 21
resultado = contar_elementos(numeros, valor)
print(f"El valor {valor} aparece {resultado} veces en la lista.")
