def Login(usuario, contraseña, usuario_actual, contraseña_actual):
    return usuario == usuario_actual and contraseña == contraseña_actual

def validarIntentos(intentos):
    return intentos < 3

def crearCuenta():
    nuevo_usuario = input("Ingrese un nuevo nombre de usuario: ")
    nueva_contraseña = input("Ingrese una nueva contraseña: ")
    return nuevo_usuario, nueva_contraseña

def restablecerCredenciales(usuario_actual, contraseña_actual):
    print("Seleccione una opción:")
    print("1. Crear una nueva cuenta")
    print("2. Restablecer nombre de usuario o contraseña")
    opcion = input("Ingrese el número de la opción: ")

    if opcion == '1':
        nuevo_usuario, nueva_contraseña = crearCuenta()
        print(f"Cuenta creada exitosamente. Usuario: {nuevo_usuario}")
        return nuevo_usuario, nueva_contraseña
    elif opcion == '2':
        nuevo_usuario = input(f"Ingrese su nuevo nombre de usuario (o presione Enter para mantener {usuario_actual}): ")
        nueva_contraseña = input(f"Ingrese su nueva contraseña (o presione Enter para mantener la actual): ")
        return nuevo_usuario or usuario_actual, nueva_contraseña or contraseña_actual
    else:
        print("Opción no válida.")
        return usuario_actual, contraseña_actual

# Programa principal
usuario_actual = "usuario1"
contraseña_actual = "asdasd"
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if Login(usuario, contraseña, usuario_actual, contraseña_actual):
        print("Login exitoso")
        break
    else:
        intentos += 1
        print(f"Login fallido. Intento {intentos} de {max_intentos}.")

    if intentos >= max_intentos:
        print("Has excedido el número de intentos permitidos.")
        opcion = input("¿Olvidó su nombre de usuario o contraseña? (s/n): ")
        if opcion.lower() == 's':
            usuario_actual, contraseña_actual = restablecerCredenciales(usuario_actual, contraseña_actual)
            intentos = 0  # Resetear intentos después de restablecer credenciales
        else:
            break

