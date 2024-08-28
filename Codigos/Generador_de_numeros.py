import tkinter as tk
from tkinter import Spinbox, StringVar
import random


def generar_numero():
    numero1 = int(spin_num1.get())
    numero2 = int(spin_num2.get())
    
    if numero1 > numero2:
        numero1, numero2 = numero2, numero1  
    
    numero_aleatorio = random.randint(numero1, numero2)
    resultado_var.set(str(numero_aleatorio))


ventana = tk.Tk()
ventana.title("Generador de números")


ventana.geometry("300x200")


label_num1 = tk.Label(ventana, text="Número 1")
label_num1.pack(pady=5)

label_num2 = tk.Label(ventana, text="Número 2")
label_num2.pack(pady=5)

label_num_generado = tk.Label(ventana, text="Número Generado")
label_num_generado.pack(pady=5)


spin_num1 = Spinbox(ventana, from_=0, to=100)
spin_num1.pack(pady=5)

spin_num2 = Spinbox(ventana, from_=0, to=100)
spin_num2.pack(pady=5)


resultado_var = StringVar()
entry_resultado = tk.Entry(ventana, textvariable=resultado_var, state="readonly")
entry_resultado.pack(pady=10)


boton_generar = tk.Button(ventana, text="Generar", command=generar_numero)
boton_generar.pack(pady=10)


ventana.mainloop()

