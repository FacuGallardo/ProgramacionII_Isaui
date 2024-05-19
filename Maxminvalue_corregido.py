def calcularMaxMin(lista):
    max_valor = max(lista)
    min_valor = min(lista)
    return max_valor, min_valor

numeros = []
entrada = input("Ingrese números separados por comas: ")

try:
    
    numeros = [float(num) for num in entrada.split(',')]
    
    if numeros:
        maximo, minimo = calcularMaxMin(numeros)
        print(f"El valor máximo es: {maximo}")
        print(f"El valor mínimo es: {minimo}")
    else:
        print("No se ingresaron números.")
except ValueError:
    print("Por favor, ingrese solo números separados por comas.")

