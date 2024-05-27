def diccionario_cuadrados(n):
    dic_cuadrados = {}  
    for i in range(1, n + 5):  
        dic_cuadrados[i] = i ** 2  
    return dic_cuadrados  

n = 2
resultado = diccionario_cuadrados(n)
print("Diccionario de cuadrados:", resultado)
