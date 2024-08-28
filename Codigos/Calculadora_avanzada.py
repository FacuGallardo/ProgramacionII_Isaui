import tkinter as tk
from tkinter import StringVar, Radiobutton


def calcular():
    valor1 = float(entry_valor1.get())
    valor2 = float(entry_valor2.get())
    operacion = operacion_var.get()
    
    if operacion == "Sumar":
        resultado = valor1 + valor2
    elif operacion == "Restar":
        resultado = valor1 - valor2
    elif operacion == "Multiplicar":
        resultado = valor1 * valor2
    elif operacion == "Dividir":
        if valor2 != 0:
            resultado = valor1 / valor2
        else:
            resultado_var.set("Error")
            return
    
    resultado_var.set(str(resultado))


ventana = tk.Tk()
ventana.title("Calculadora 2")


ventana.geometry("350x300")


label_valor1 = tk.Label(ventana, text="Valor 1")
label_valor1.pack(pady=5)

label_valor2 = tk.Label(ventana, text="Valor 2")
label_valor2.pack(pady=5)

label_resultado = tk.Label(ventana, text="Resultado")
label_resultado.pack(pady=5)

label_operaciones = tk.Label(ventana, text="Operaciones")
label_operaciones.pack(pady=5)


entry_valor1 = tk.Entry(ventana)
entry_valor1.pack(pady=5)

entry_valor2 = tk.Entry(ventana)
entry_valor2.pack(pady=5)

resultado_var = StringVar()
entry_resultado = tk.Entry(ventana, textvariable=resultado_var, state="readonly")
entry_resultado.pack(pady=5)


operacion_var = StringVar(value="Sumar")

radio_suma = Radiobutton(ventana, text="Sumar", variable=operacion_var, value="Sumar")
radio_suma.pack(anchor="w", padx=20)

radio_resta = Radiobutton(ventana, text="Restar", variable=operacion_var, value="Restar")
radio_resta.pack(anchor="w", padx=20)

radio_multiplicar = Radiobutton(ventana, text="Multiplicar", variable=operacion_var, value="Multiplicar")
radio_multiplicar.pack(anchor="w", padx=20)

radio_dividir = Radiobutton(ventana, text="Dividir", variable=operacion_var, value="Dividir")
radio_dividir.pack(anchor="w", padx=20)


boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.pack(pady=10)


ventana.mainloop()


