import tkinter as tk
from tkinter import messagebox
import numpy as np


def validar_input(texto):
    return texto.replace('.', '', 1).isdigit() or texto == ''


def es_incompatible(matrix):
    
    for row in matrix:
        if all([elem == 0 for elem in row[:-1]]) and row[-1] != 0:
            return True
    return False


def gauss_jordan(matrix):
    n = len(matrix)
    for i in range(n):
        if matrix[i][i] == 0:
            
            for k in range(i+1, n):
                if matrix[k][i] != 0:
                    matrix[[i, k]] = matrix[[k, i]]
                    break

        matrix[i] = matrix[i] / matrix[i][i]
        for j in range(n):
            if i != j:
                matrix[j] = matrix[j] - matrix[i] * matrix[j][i]
    
    return matrix


def calcular_matriz_3x3():
    try:
        
        a1, b1, c1, d1 = float(entry_a1.get()), float(entry_b1.get()), float(entry_c1.get()), float(entry_d1.get())
        a2, b2, c2, d2 = float(entry_a2.get()), float(entry_b2.get()), float(entry_c2.get()), float(entry_d2.get())
        a3, b3, c3, d3 = float(entry_a3.get()), float(entry_b3.get()), float(entry_c3.get()), float(entry_d3.get())

        
        matrix = np.array([[a1, b1, c1, d1],
                           [a2, b2, c2, d2],
                           [a3, b3, c3, d3]])

        
        if es_incompatible(matrix):
            messagebox.showerror("Resultado", "Sistema Incompatible: No tiene solución.")
            return

        
        resultado = gauss_jordan(matrix)

        x, y, z = resultado[0][3], resultado[1][3], resultado[2][3]
        messagebox.showinfo("Resultado", f"Sistema Compatible Determinado\nx = {x:.2f}, y = {y:.2f}, z = {z:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores válidos.")


def limpiar_campos():
    entry_a1.delete(0, tk.END)
    entry_b1.delete(0, tk.END)
    entry_c1.delete(0, tk.END)
    entry_d1.delete(0, tk.END)
    entry_a2.delete(0, tk.END)
    entry_b2.delete(0, tk.END)
    entry_c2.delete(0, tk.END)
    entry_d2.delete(0, tk.END)
    entry_a3.delete(0, tk.END)
    entry_b3.delete(0, tk.END)
    entry_c3.delete(0, tk.END)
    entry_d3.delete(0, tk.END)


def matrices_3x3():
    clear_frame()
    global entry_a1, entry_b1, entry_c1, entry_d1
    global entry_a2, entry_b2, entry_c2, entry_d2
    global entry_a3, entry_b3, entry_c3, entry_d3

    vcmd = root.register(validar_input)

    # Configura las entradas para cada ecuación
    tk.Label(frame_matrices, text="Ecuación 1:").grid(row=0, column=0)
    entry_a1 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'))
    entry_a1.grid(row=0, column=1)
    entry_a1.bind("<KeyRelease>", lambda e: next_focus(e, entry_b1))
    
    entry_b1 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'))
    entry_b1.grid(row=0, column=2)
    entry_b1.bind("<KeyRelease>", lambda e: next_focus(e, entry_c1))
    
    entry_c1 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'))
    entry_c1.grid(row=0, column=3)
    entry_c1.bind("<KeyRelease>", lambda e: next_focus(e, entry_d1))

    entry_d1 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'))
    entry_d1.grid(row=0, column=4)
    entry_d1.bind("<KeyRelease>", lambda e: next_focus(e, entry_a2))

    tk.Label(frame_matrices, text="Ecuación 2:").grid(row=1, column=0)
    entry_a2 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'))
    entry_a2.grid(row=1, column=1)
    entry_a2.bind("<KeyRelease>", lambda e: next_focus(e, entry_b2))

    entry_b2 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'))
    entry_b2.grid(row=1, column=2)
    entry_b2.bind("<KeyRelease>", lambda e: next_focus(e, entry_c2))

    entry_c2 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'))
    entry_c2.grid(row=1, column=3)
    entry_c2.bind("<KeyRelease>", lambda e: next_focus(e, entry_d2))

    entry_d2 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'))
    entry_d2.grid(row=1, column=4)
    entry_d2.bind("<KeyRelease>", lambda e: next_focus(e, entry_a3))

    tk.Label(frame_matrices, text="Ecuación 3:").grid(row=2, column=0)
    entry_a3 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'))
    entry_a3.grid(row=2, column=1)
    entry_a3.bind("<KeyRelease>", lambda e: next_focus(e, entry_b3))

    entry_b3 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'))
    entry_b3.grid(row=2, column=2)
    entry_b3.bind("<KeyRelease>", lambda e: next_focus(e, entry_c3))

    entry_c3 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'))
    entry_c3.grid(row=2, column=3)
    entry_c3.bind("<KeyRelease>", lambda e: next_focus(e, entry_d3))

    entry_d3 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'))
    entry_d3.grid(row=2, column=4)

    
    tk.Button(frame_matrices, text="Calcular", command=calcular_matriz_3x3).grid(row=3, column=0, columnspan=3)
    
    tk.Button(frame_matrices, text="Borrar", command=limpiar_campos, bg="red", fg="white").grid(row=3, column=3, columnspan=2)

def next_focus(event, next_entry):
    if len(event.widget.get()) == 1:
        next_entry.focus()

def clear_frame():
    for widget in frame_matrices.winfo_children():
        widget.destroy()

root = tk.Tk()
root.title("Calculadora de Matrices")
root.geometry("1366x765")

frame_matrices = tk.Frame(root)
frame_matrices.pack(pady=10)

matrices_3x3()

root.mainloop()
