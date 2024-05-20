import string

def Palindromo(palabra):
    palabra_procesada = ''.join(caracter for caracter in palabra.lower() if caracter not in string.punctuation + ' ')
    izquierda = 0
    derecha = len(palabra_procesada) - 1
    
    while izquierda < derecha:
        if palabra_procesada[izquierda] != palabra_procesada[derecha]:
            return False
        izquierda += 1
        derecha -= 1
    
    return True

# Ejemplo de uso:
palabra = "Anita, la gorda lagartona, no traga la droga latina."
resultado = Palindromo(palabra)
print(f"¿'{palabra}' es un palíndromo?: {resultado}")
      