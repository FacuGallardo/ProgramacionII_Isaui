import random

def jugar_adivina_numero():
    numero_dolares = random.randint(1, 100)
    intentos = 0
    
    print("¡Bienvenido al telebingo cordobes, acerta el numero y gana dolares!")
    print("Mientras mas intentos hagas, se le restara a los dolares que ganaste")
    print("Estoy pensando en un número entre 1 y 100.")
    
    while True:
        intento = int(input("Piensa bien tu numero,¡Podrias ser el proximo ganador!: "))
        intentos += 1
        
        if intento < numero_dolares:
            print("¡Demasiado bajo! Parece que es tu dia de suerte, ¡Apunta mas alto!.")
        elif intento > numero_dolares:
            print("¡Demasiado alto! Cuidado que te quedas sin plata papa, apunta a lo humilde.")
        else:
            print(f"¡Felicidades campeon! lo adivinaste despues de {intentos} intentos.")
            numero_dolares = intento - intentos
            print(f"Sos el ganador de {numero_dolares}.")
            break

jugar_adivina_numero()
