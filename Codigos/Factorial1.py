import tkinter as tk
from math import factorial


def calcular_factorial():
    global n
    
    resultado = factorial(n)
    
    factorial_var.set(str(resultado))
    
    n += 1


ventana = tk.Tk()
ventana.title("Factorial")


ventana.geometry("300x200")


etiqueta_n = tk.Label(ventana, text="n")
etiqueta_n.pack(pady=10)


n = 2  
n_var = tk.StringVar(value=str(n))
campo_n = tk.Entry(ventana, textvariable=n_var, state="readonly")
campo_n.pack(pady=10)


etiqueta_factorial = tk.Label(ventana, text="Factorial(n)")
etiqueta_factorial.pack(pady=10)


factorial_var = tk.StringVar(value="1")
campo_factorial = tk.Entry(ventana, textvariable=factorial_var, state="readonly")
campo_factorial.pack(pady=10)


boton_siguiente = tk.Button(ventana, text="Siguiente", command=calcular_factorial)
boton_siguiente.pack(pady=10)


ventana.mainloop()
