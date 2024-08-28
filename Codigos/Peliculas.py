import tkinter as tk
from tkinter import Listbox, END


def anadir_pelicula():
    pelicula = entry_pelicula.get()
    if pelicula:
        list_peliculas.insert(END, pelicula)
        entry_pelicula.delete(0, tk.END)


ventana = tk.Tk()
ventana.title("Películas")


ventana.geometry("400x300")


label_escribir = tk.Label(ventana, text="Escribe el título de una película")
label_escribir.pack(pady=10)

label_peliculas = tk.Label(ventana, text="Películas")
label_peliculas.pack(pady=10)


entry_pelicula = tk.Entry(ventana, width=50)
entry_pelicula.pack(pady=5)


list_peliculas = Listbox(ventana, width=50, height=10)
list_peliculas.pack(pady=10)


boton_anadir = tk.Button(ventana, text="Añadir", command=anadir_pelicula)
boton_anadir.pack(pady=10)


ventana.mainloop()

