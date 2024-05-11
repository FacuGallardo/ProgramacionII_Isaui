import random

print("Bienvenido al ahorcado joven duelista.")
print("Veremos que tan experto en el reino de los duelos eres. ¡Es hora del Du Du Duelo!!!")

def obtener_palabra_aleatoria():
    palabras = ["yugioh", "kaiba", "yubel", "polimerizacion", "dragon blanco de ojos azules", "kuriboh", "dragon arcoiris,neos"]
    return random.choice(palabras)

def jugar_ahorcado():
    palabra_secreta = obtener_palabra_aleatoria()
    letras_adivinadas = []
    turnos_restantes = 5

    print("Bienvenido al ahorcado joven duelista.")
    print("Veremos que tan experto en el reino de los duelos eres. Tu alma esta en juego... ¡Es hora del Du Du Duelo!!!")

    while turnos_restantes > 0:
        palabra_mostrada = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_mostrada += letra
            else:
                palabra_mostrada += "_"
        
        print("\nPalabra:", palabra_mostrada)
        print("turnos restantes:", turnos_restantes)
        
        if palabra_mostrada == palabra_secreta:
            print("¡Felicidades duelista! ¡Tu alma de guerrero a salido victoriosa...por ahora!")
            break
        
        letra_ingresada = input("Ingresa una letra: ").lower()
        
        if letra_ingresada in letras_adivinadas:
            print("Ya has ingresado esa letra. Intenta con otra.")
            continue
        
        letras_adivinadas.append(letra_ingresada)
        
        if letra_ingresada not in palabra_secreta:
            print("La letra es incorrecta, tu alma esta en peligro.")
            turnos_restantes -= 1

    if turnos_restantes == 0:
        print("\nHas perdido el combate. La palabra secreta era:", palabra_secreta)

jugar_ahorcado()
