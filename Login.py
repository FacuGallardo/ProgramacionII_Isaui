def Login(usuario, contraseña):
    return usuario == "fernetks1" and contraseña == "taieres31"

def validar_intentos(intentos):
    return intentos < 3

intentos = 0
max_intentos = 3

while intentos < max_intentos:
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if Login(usuario, contraseña):
        print("adentrooo")
        break
    else:
        intentos += 1
        print(f"Login fallido :c. Intento {intentos} de {max_intentos}.")

    if intentos >= max_intentos:
        print("Usted a excedido el numero de intentos.")
        print("Se olvido la contraseña?. Haga click aqui.")
        print("Se olvido el usuario?. Haga click aqui.")
        break