def indice_primera_aparicion(lista, valor):
    try:
        indice = lista.index(valor)  
        return indice  
    except ValueError:
        return -1  

numeros = [2, 2, 5, 4, 6, 6, 5, 8, 97, 10]
valor = 5
resultado = indice_primera_aparicion(numeros, valor)
print("El índice de la primera aparición de", valor, "es:", resultado)
