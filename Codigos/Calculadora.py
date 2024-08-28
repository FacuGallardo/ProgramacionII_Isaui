import tkinter as tk
from tkinter import messagebox


def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado_var.set(num1 + num2)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

def restar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado_var.set(num1 - num2)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

def multiplicar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado_var.set(num1 * num2)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

def dividir():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 != 0:
            resultado_var.set(num1 / num2)
        else:
            messagebox.showerror("Error", "No se puede dividir por cero.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

def modulo():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 != 0:
            resultado_var.set(num1 % num2)
        else:
            messagebox.showerror("Error", "No se puede calcular el módulo por cero.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

def limpiar():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    resultado_var.set("")


ventana = tk.Tk()
ventana.title("Calculadora")


ventana.geometry("350x250")


label_num1 = tk.Label(ventana, text="Primer número")
label_num1.grid(row=0, column=0, padx=10, pady=5)

label_num2 = tk.Label(ventana, text="Segundo número")
label_num2.grid(row=1, column=0, padx=10, pady=5)

label_resultado = tk.Label(ventana, text="Resultado")
label_resultado.grid(row=2, column=0, padx=10, pady=5)


entry_num1 = tk.Entry(ventana)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

entry_num2 = tk.Entry(ventana)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

resultado_var = tk.StringVar()
entry_resultado = tk.Entry(ventana, textvariable=resultado_var, state="readonly")
entry_resultado.grid(row=2, column=1, padx=10, pady=5)


boton_sumar = tk.Button(ventana, text="+", command=sumar)
boton_sumar.grid(row=3, column=0, padx=5, pady=5)

boton_restar = tk.Button(ventana, text="-", command=restar)
boton_restar.grid(row=3, column=1, padx=5, pady=5)

boton_multiplicar = tk.Button(ventana, text="*", command=multiplicar)
boton_multiplicar.grid(row=4, column=0, padx=5, pady=5)

boton_dividir = tk.Button(ventana, text="/", command=dividir)
boton_dividir.grid(row=4, column=1, padx=5, pady=5)

boton_modulo = tk.Button(ventana, text="%", command=modulo)
boton_modulo.grid(row=5, column=0, padx=5, pady=5)

boton_reset = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_reset.grid(row=5, column=1, padx=5, pady=5)


ventana.mainloop()
