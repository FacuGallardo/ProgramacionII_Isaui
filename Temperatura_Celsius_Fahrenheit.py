def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    print("1. Convertir de Celsius a Fahrenheit")
    print("2. Convertir de Fahrenheit a Celsius")
    print("3. Salir")

    choice = input("Selecciona una opción (1, 2 o 3): ")

    if choice == '1':
        celsius = float(input("Ingresa la temperatura en grados Celsius: "))
        print("La temperatura en grados Fahrenheit es:", celsius_a_fahrenheit(celsius))
    elif choice == '2':
        fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
        print("La temperatura en grados Celsius es:", fahrenheit_a_celsius(fahrenheit))
    elif choice == '3':
        print("¡Y no vuelva sin mas datos del clima!")
        break
    else:
        print("Opción no válida. Por favor solo seleccione 1, 2 o 3.")

