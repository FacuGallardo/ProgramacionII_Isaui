def contar_palabras (frase: str) -> int:
    palabras = frase.split()
    return len(palabras)

frase = input("Ingrese una frase:")
Numero_De_Palabras = contar_palabras(frase)
print("La frase", frase, "contiene", Numero_De_Palabras, "Palabras")
              