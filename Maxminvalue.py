def calcularMaxMin(lista):
    max_valor = max(lista)
    min_valor = min(lista)
    return max_valor, min_valor

if __name__ == "__main__":
    numeros = []
    print("Ingrese números (escriba 'fin' para terminar):")
    
    while True:
        entrada = input()
        if entrada.lower() == 'fin':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor, ingrese un número válido.")

    if numeros:
        maximo, minimo = calcularMaxMin(numeros)
        print(f"El valor máximo es: {maximo}")
        print(f"El valor mínimo es: {minimo}")
    else:
        print("No se ingresaron números.")

        