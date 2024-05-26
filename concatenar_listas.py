def concatenar_listas_en_sitio(lista1, lista2):
    lista1.extend(lista2)  
    return lista1  

lista1 = [0, 20, 31,32,33]
lista2 = [64, 55, 64]
resultado = concatenar_listas_en_sitio(lista1, lista2)
print("La lista concatenada es:", resultado)
