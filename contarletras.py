def contarLetras(cadena):
    recuento = {}
    for letra in cadena:
        if letra.isalpha(): 
            if letra in recuento:
                recuento[letra] += 1
            else:
                recuento[letra] = 1
    return recuento


cadena = "Milanesa"
resultado = contarLetras(cadena)
print(f"Recuento de letras: {resultado}")
