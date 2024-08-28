import tkinter as tk
from math import factorial

# Función para calcular y mostrar el factorial
def calcular_factorial():
    global n
    # Calcular el factorial del número actual
    resultado = factorial(n)
    # Mostrar el resultado en el segundo campo
    factorial_var.set(str(resultado))
    # Incrementar el número
    n += 1

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Factorial")

# Establecer el tamaño inicial de la ventana (ancho x alto)
ventana.geometry("300x200")

# Crear una etiqueta para el número
etiqueta_n = tk.Label(ventana, text="n")
etiqueta_n.pack(pady=10)

# Crear un campo de texto no editable para mostrar el número
n = 2  # Número inicial
n_var = tk.StringVar(value=str(n))
campo_n = tk.Entry(ventana, textvariable=n_var, state="readonly")
campo_n.pack(pady=10)

# Crear una etiqueta para el factorial
etiqueta_factorial = tk.Label(ventana, text="Factorial(n)")
etiqueta_factorial.pack(pady=10)

# Crear un campo de texto no editable para mostrar el factorial
factorial_var = tk.StringVar(value="1")
campo_factorial = tk.Entry(ventana, textvariable=factorial_var, state="readonly")
campo_factorial.pack(pady=10)

# Crear un botón para calcular el factorial y avanzar al siguiente número
boton_siguiente = tk.Button(ventana, text="Siguiente", command=calcular_factorial)
boton_siguiente.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
