def elementos_mayores(lista, n):
    mayores = []
    for numero in lista:
        if numero > n:
            mayores.append(numero)
    return mayores

numeros = [21, 4, 6, 12, 76, 32, 54, 25, 45, 1]
valor_n = 55
resultado = elementos_mayores(numeros, valor_n)
print(f"Los numeros que superan a este", valor_n, "son:", resultado)
