def juego_adivina_numero():
    print("Piensa en un número entre 1 y 100, y yo intentaré adivinarlo con mi super inteligencia.")
    input("Presiona Enter para cuando estes listo... Pero no tengo todo el dia asi que dale.")
    
    limite_inferior = 1
    limite_superior = 100
    adivinado = False
    
    while not adivinado:
        numero_propuesto = (limite_inferior + limite_superior) // 2
        
        respuesta = input(f"¿Es {numero_propuesto} tu número? (responde 'menor', 'mayor', o 'igual'): ").lower()
        
        if respuesta == "igual":
            print(f"¡Genial! He adivinado tu número. Es {numero_propuesto}.")
            adivinado = True
        elif respuesta == "menor":
            limite_superior = numero_propuesto - 1
        elif respuesta == "mayor":
            limite_inferior = numero_propuesto + 1
        else:
            print("Por favor, ingresa una respuesta válida ('menor', 'mayor', o 'igual').")

juego_adivina_numero()
