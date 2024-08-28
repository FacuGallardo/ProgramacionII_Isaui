import tkinter as tk


def decrementar_contador():
    valor_actual = int(contador_var.get())
    contador_var.set(valor_actual - 1)


ventana = tk.Tk()
ventana.title("ContDecreciente")


ventana.geometry("150x200")  


etiqueta = tk.Label(ventana, text="Contador")
etiqueta.pack(pady=10)  


contador_var = tk.StringVar(value="88")  
campo_contador = tk.Entry(ventana, textvariable=contador_var, state="readonly")
campo_contador.pack(pady=10)


boton_decrementar = tk.Button(ventana, text="-", command=decrementar_contador)
boton_decrementar.pack(pady=10)


ventana.mainloop()
