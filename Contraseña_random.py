import random
import string

def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

contraseña_generada = generar_contraseña()
print("Tu contraseña generada es:", contraseña_generada)
