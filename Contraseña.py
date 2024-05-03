import re

def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres de longitud."
    
    if not re.search("[A-Z]", contrasena):
        return False, "La contraseña debe tener al menos una letra mayúscula."
    
    if not re.search("[a-z]", contrasena):
        return False, "La contraseña debe contener al menos una letra minúscula."
    
    if not re.search("[0-9]", contrasena):
        return False, "La contraseña debe contener al menos un número."
    
    if not re.search("[!@#\$%\^&\*\(\)\-_+=<>\?¿ªº/']", contrasena):
        return False, "La contraseña debe contener al menos un carácter especial."
    
    return True, "La contraseña cumple los requisitos."






    
      
    