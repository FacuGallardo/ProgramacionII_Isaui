import tkinter as tk


def incrementar_contador():
    valor_actual = int(contador_var.get())
    contador_var.set(valor_actual + 1)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("ContCreciente")


ventana.geometry("150x200")  

etiqueta = tk.Label(ventana, text="Contador")
etiqueta.pack(pady=10) 


contador_var = tk.StringVar(value="0")
campo_contador = tk.Entry(ventana, textvariable=contador_var, state="readonly")
campo_contador.pack(pady=10)


boton_incrementar = tk.Button(ventana, text="+", command=incrementar_contador)
boton_incrementar.pack(pady=10)


ventana.mainloop()

