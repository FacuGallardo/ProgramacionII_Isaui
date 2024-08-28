import tkinter as tk

# Funciones para manejar el contador
def incrementar():
    valor_actual = int(contador_var.get())
    contador_var.set(valor_actual + 1)

def decrementar():
    valor_actual = int(contador_var.get())
    contador_var.set(valor_actual - 1)

def resetear():
    contador_var.set(0)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Contador")

# Establecer el tamaño inicial de la ventana (ancho x alto)
ventana.geometry("300x200")

# Crear una etiqueta para el contador
etiqueta = tk.Label(ventana, text="Contador")
etiqueta.pack(pady=10)

# Crear un campo de texto no editable para mostrar el contador
contador_var = tk.StringVar(value="0")
campo_contador = tk.Entry(ventana, textvariable=contador_var, state="readonly")
campo_contador.pack(pady=10)

# Crear los botones
boton_incrementar = tk.Button(ventana, text="Count Up", command=incrementar)
boton_incrementar.pack(side=tk.LEFT, padx=10, pady=10)

boton_decrementar = tk.Button(ventana, text="Count Down", command=decrementar)
boton_decrementar.pack(side=tk.LEFT, padx=10, pady=10)

boton_reset = tk.Button(ventana, text="Reset", command=resetear)
boton_reset.pack(side=tk.LEFT, padx=10, pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
