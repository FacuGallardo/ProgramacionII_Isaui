def ConvertirEspaciado(texto):
    resultado = ""
    for char in texto:
        resultado += char + " "
    return resultado

if __name__ == "__main__":
    texto_usuario = input("Por favor, ingrese un texto: ")
    texto_convertido = ConvertirEspaciado(texto_usuario)
    print("Texto con espaciado adicional:")
    print(texto_convertido)
