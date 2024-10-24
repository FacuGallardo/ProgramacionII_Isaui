import tkinter as tk
import numpy as np


def validar_input(texto):
    return texto.replace('.', '', 1).replace('-', '', 1).isdigit() or texto == ''


def es_incompatible(matrix):
    for row in matrix:
        
        if all([elem == 0 for elem in row[:-1]]) and row[-1] != 0:
            return True
        
        for other_row in matrix:
            if np.allclose(row[:-1], other_row[:-1]) and not np.isclose(row[-1], other_row[-1]):
                return True
    return False


def es_indeterminado(matrix):
    for row in matrix:
        if all([elem == 0 for elem in row[:-1]]) and row[-1 == 0]:
            return True
    return False


def gauss_jordan(matrix):
    n = len(matrix)
    for i in range(n):
        if matrix[i][i] == 0:
            for k in range(i + 1, n):
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

        # Comprobación de compatibilidad
        if es_incompatible(matrix):
            resultado_var.set("Sistema Incompatible: No tiene solución.")
            return
        elif es_indeterminado(matrix):
            resultado_var.set("Sistema Compatible Indeterminado: Infinitas soluciones.")
            return

        resultado = gauss_jordan(matrix)

        # Mostrar el resultado para sistemas compatibles determinados
        x, y, z = resultado[0][3], resultado[1][3], resultado[2][3]
        resultado_var.set(f"Sistema Compatible Determinado:\n x = {x:.2f}\n y = {y:.2f}\n z = {z:.2f}")

    except ValueError:
        resultado_var.set("Error: Por favor ingresa valores válidos.")



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
    resultado_var.set("")  # Limpia el resultado al borrar campos


def matrices_3x3():
    global entry_a1, entry_b1, entry_c1, entry_d1
    global entry_a2, entry_b2, entry_c2, entry_d2
    global entry_a3, entry_b3, entry_c3, entry_d3

    vcmd = root.register(validar_input)

    # Configura las entradas para cada ecuación
    tk.Label(frame_matrices, text="Ecuación 1:", font=("Arial", 16), bg="#1E3A60", fg="white").grid(row=0, column=0, sticky="nsew")
    entry_a1 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'), font=("Arial", 14))
    entry_a1.grid(row=0, column=1)

    entry_b1 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'), font=("Arial", 14))
    entry_b1.grid(row=0, column=2)

    entry_c1 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'), font=("Arial", 14))
    entry_c1.grid(row=0, column=3)

    entry_d1 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'), font=("Arial", 14))
    entry_d1.grid(row=0, column=4)

    tk.Label(frame_matrices, text="Ecuación 2:", font=("Arial", 16), bg="#1E3A60", fg="white").grid(row=1, column=0, sticky="nsew")
    entry_a2 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'), font=("Arial", 14))
    entry_a2.grid(row=1, column=1)

    entry_b2 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'), font=("Arial", 14))
    entry_b2.grid(row=1, column=2)

    entry_c2 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'), font=("Arial", 14))
    entry_c2.grid(row=1, column=3)

    entry_d2 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'), font=("Arial", 14))
    entry_d2.grid(row=1, column=4)

    tk.Label(frame_matrices, text="Ecuación 3:", font=("Arial", 16), bg="#1E3A60", fg="white").grid(row=2, column=0, sticky="nsew")
    entry_a3 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'), font=("Arial", 14))
    entry_a3.grid(row=2, column=1)

    entry_b3 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'), font=("Arial", 14))
    entry_b3.grid(row=2, column=2)

    entry_c3 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'), font=("Arial", 14))
    entry_c3.grid(row=2, column=3)

    entry_d3 = tk.Entry(frame_matrices, validate='key', validatecommand=(vcmd, '%P'), font=("Arial", 14))
    entry_d3.grid(row=2, column=4)

    # Encabezados de columnas
    tk.Label(frame_matrices, text="x", font=("Arial", 16), bg="#1E3A60", fg="white").grid(row=3, column=1, sticky="nsew")
    tk.Label(frame_matrices, text="y", font=("Arial", 16), bg="#1E3A60", fg="white").grid(row=3, column=2, sticky="nsew")
    tk.Label(frame_matrices, text="z", font=("Arial", 16), bg="#1E3A60", fg="white").grid(row=3, column=3, sticky="nsew")
    tk.Label(frame_matrices, text="Igualdad", font=("Arial", 16), bg="#1E3A60", fg="white").grid(row=3, column=4, sticky="nsew")

    # Recuadro para mostrar el resultado
    global resultado_var
    resultado_var = tk.StringVar()
    resultado_frame = tk.Frame(frame_matrices, bg="white", bd=2, relief="groove")
    resultado_frame.grid(row=4, column=0, columnspan=5, pady=10)

    resultado_label = tk.Label(resultado_frame, textvariable=resultado_var, font=("Arial", 14), bg="white")
    resultado_label.pack(padx=10, pady=10)

    tk.Button(frame_matrices, text="Calcular", command=calcular_matriz_3x3, font=("Arial", 14)).grid(row=5, column=0, columnspan=3)
    tk.Button(frame_matrices, text="Borrar", command=limpiar_campos, bg="red", fg="white", font=("Arial", 14)).grid(row=5, column=3, columnspan=2)

    # Explicación sobre NaN, inf y -inf
    explicacion = (
        "NaN: No es un número.\n"
        "inf: Infinito, ocurre cuando el resultado supera el límite.\n"
        "-inf: Infinito negativo, ocurre con valores que tienden a negativo infinito."
    )
    tk.Label(frame_matrices, text=explicacion, justify=tk.LEFT, bg="#1E3A60", fg="white", font=("Arial", 14)).grid(row=6, column=0, columnspan=5, sticky="w", pady=10)

# Configura la ventana principal
root = tk.Tk()
root.title("Resolución de Sistemas de Ecuaciones Lineales")
root.geometry("1366x786")
root.configure(bg="#1E3A60")

frame_matrices = tk.Frame(root, bg="#1E3A60")
frame_matrices.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

matrices_3x3()

root.mainloop()
