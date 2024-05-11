def factorial(n):
    factorial_n = 1
    for i in range(1, n + 1):
        factorial_n *= i
    return factorial_n

numero = int(input("Ingrese un número entero positivo para calcular su factorial: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")

