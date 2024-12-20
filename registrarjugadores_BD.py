from tkinter import ttk, messagebox, filedialog
import tkinter as tk
from tkcalendar import DateEntry  
from PIL import Image, ImageTk
import re
import mysql.connector

directorio_imagenes = r"C:\Users\Usuario\Downloads\visual code\matematica\Liga de Handball Punilla"
jugadores = []

# Conexión a la base de datos
def conectar_db():
    try:
        return mysql.connector.connect(
            host="localhost",  # Cambia esto si es necesario
            user="tu_usuario",  # Cambia esto por tu usuario de MySQL
            password="tu_contraseña",  # Cambia esto por tu contraseña de MySQL
            database="tu_base_de_datos"  # Cambia esto por tu nombre de base de datos
        )
    except mysql.connector.Error as err:
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {err}")
        return None

# Función para agregar jugador a la base de datos
def alta_jugador():
    jugador = {
        "nombre": entry_nombre.get(),
        "apellido": entry_apellido.get(),
        "dni": entry_dni.get(),
        "domicilio": entry_domicilio.get(),
        "telefono": entry_telefono.get(),
        "correo": entry_correo.get(),
        "fecha_nacimiento": entry_fecha_nacimiento.get_date(),
        "localidad": localidad_combo.get(),
        "club": club_combo.get(),
        "categoria": tipo_combo.get(),
        "ficha_medica": ficha_medica_img_label.image,
        "carnet": carnet_img_label.image,
    }
    
    if not validar_campos():  # Asegúrate de validar los campos antes de agregar
        return

    # Conectar a la base de datos y agregar jugador
    db = conectar_db()
    if db:
        cursor = db.cursor()
        sql = ("INSERT INTO jugadores (nombre, apellido, dni, domicilio, telefono, correo, fecha_nacimiento, localidad, club, categoria) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        values = (jugador["nombre"], jugador["apellido"], jugador["dni"], jugador["domicilio"],
                  jugador["telefono"], jugador["correo"], jugador["fecha_nacimiento"],
                  jugador["localidad"], jugador["club"], jugador["categoria"])
        try:
            cursor.execute(sql, values)
            db.commit()
            messagebox.showinfo("Guardado exitoso", "Jugador agregado exitosamente ⚽")
            borrar_datos()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo guardar el jugador: {err}")
        finally:
            cursor.close()
            db.close()

directorio_imagenes = r"C:\Users\Usuario\Downloads\visual code\matematica\Liga de Handball Punilla"
jugadores = []

def cargar_imagen(label):
    archivo = filedialog.askopenfilename(initialdir=directorio_imagenes, filetypes=[("Imágenes", ".png;.jpg;*.jpeg")])
    if archivo:
        # Carga la imagen
        img = Image.open(archivo)

        # Obtén el tamaño actual del label
        label_width = label.winfo_width()
        label_height = label.winfo_height()

        # Redimensiona la imagen manteniendo la relación de aspecto
        img.thumbnail((label_width, label_height), Image.LANCZOS)
        
        # Calcula el nuevo tamaño de la imagen para el label
        img = img.resize((label_width, label_height), Image.LANCZOS)

        img = ImageTk.PhotoImage(img)

        # Actualiza la imagen del label
        label.config(image=img)
        label.image = img  # Guarda la referencia para evitar recolección de basura

def verificar_correo(correo):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(patron, correo):
        messagebox.showerror("Error", f"{correo} : no es una dirección de correo válida.")
        return False
    return True

def validar_dni(dni):
    if not dni.isdigit():
        messagebox.showerror("Error", "El DNI debe contener solo dígitos.")
        return False
    elif len(dni) < 7 or len(dni) > 8:
        messagebox.showerror("Error", "El número del DNI debe tener 7 u 8 dígitos.")
        return False
    return True

def validar_telefono(telefono):
    if not telefono.isdigit():
        messagebox.showerror("Error", "El teléfono debe contener solo dígitos.")
        return False
    elif len(telefono) < 6 or len(telefono) > 10:
        messagebox.showerror("Error", "El número de teléfono debe tener entre 6 y 10 dígitos.")
        return False
    return True

def validar_campos_obligatorios(entries):
    if any(entry.get().strip() == "" for entry in entries):
        messagebox.showerror("Error", "Todos los campos obligatorios deben completarse.")
        return False
    return True

def validar_campos():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    dni = entry_dni.get()
    domicilio = entry_domicilio.get()
    telefono = entry_telefono.get()
    fecha_nacimiento = entry_fecha_nacimiento.get_date()
    correo = entry_correo.get()
    localidad = localidad_combo.get()
    club = club_combo.get()
    tipo = tipo_combo.get()

    # Validación de campos obligatorios
    if not validar_campos_obligatorios([entry_nombre, entry_apellido, entry_dni, entry_correo]):
        return False

    # Validación de nombre y apellido
    if not re.match("^[A-Za-z ]+$", nombre):
        messagebox.showerror("Error", "El nombre solo debe contener letras y espacios.")
        return False
    if not re.match("^[A-Za-z ]+$", apellido):
        messagebox.showerror("Error", "El apellido solo debe contener letras y espacios.")
        return False

    # Validación de DNI y teléfono
    if not validar_dni(dni) or not validar_telefono(telefono):
        return False

    # Validación de correo electrónico
    if not verificar_correo(correo):
        return False

    # Validación de selección de categoría, localidad y club
    if tipo == 'Categoría':
        messagebox.showerror("Error", "Debe seleccionar una categoría válida.")
        return False
    if localidad == 'Ninguna':
        messagebox.showerror("Error", "Debe seleccionar una localidad.")
        return False
    if club == 'Cualquiera':
        messagebox.showerror("Error", "Debe seleccionar un club.")
        return False

    # Validación de carga de imágenes
    if not hasattr(ficha_medica_img_label, 'image') or not hasattr(carnet_img_label, 'image'):
        messagebox.showerror("Error", "Es obligatorio cargar el Carnet y la Ficha Médica.")
        return False

    # Confirmación de guardado
    if messagebox.askyesno("Confirmación", "¿Está seguro que desea guardar los datos?"):
        messagebox.showinfo("Guardado exitoso", "Jugador agregado exitosamente ⚽")
        borrar_datos()
        return True  # Devuelve True si todo es válido y el usuario confirma guardar
    return False  # Devuelve False si no se confirma guardar


def borrar_datos():
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_dni.delete(0, tk.END)
    entry_domicilio.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_fecha_nacimiento.set_date('23-10-2024')  
    entry_correo.delete(0, tk.END)
    tipo_combo.set('Categoría')
    localidad_combo.set('Ninguna')
    club_combo.set('Cualquiera')
    ficha_medica_img_label.config(image='', text="Sin Imagen")
    ficha_medica_img_label.image = None
    carnet_img_label.config(image='', text="Sin Imagen")
    carnet_img_label.image = None

def confirmar_borrado():
    if messagebox.askyesno("Confirmación", "¿Está seguro que desea borrar todos los datos?"):
        borrar_datos()

def volver_menu():
    root.destroy()

def solo_letras(char):
    return char.isalpha() or char == " "

def solo_numeros(char):
    return char.isdigit()

def alta_jugador():
    jugador = {
        "nombre": entry_nombre.get(),
        "apellido": entry_apellido.get(),
        "dni": entry_dni.get(),
        "domicilio": entry_domicilio.get(),
        "telefono": entry_telefono.get(),
        "correo": entry_correo.get(),
        "fecha_nacimiento": entry_fecha_nacimiento.get_date(),
        "localidad": localidad_combo.get(),
        "club": club_combo.get(),
        "categoria": tipo_combo.get(),
        "ficha_medica": ficha_medica_img_label.image,
        "carnet": carnet_img_label.image,
    }
    jugadores.append(jugador)  
    borrar_datos()  
    
def baja_jugador():
    dni = entry_dni.get()
    for jugador in jugadores:
        if jugador["dni"] == dni:
            jugadores.remove(jugador)
            messagebox.showinfo("Éxito", "Jugador eliminado exitosamente ⚽")
            borrar_datos()  
            return
    messagebox.showerror("Error", "No se encontró un jugador con ese DNI.")

def modificar_jugador():
    dni = entry_dni.get()
    for jugador in jugadores:
        if jugador["dni"] == dni:
            # Cargamos los datos en los campos
            entry_nombre.delete(0, tk.END)
            entry_nombre.insert(0, jugador["nombre"])
            entry_apellido.delete(0, tk.END)
            entry_apellido.insert(0, jugador["apellido"])
            entry_domicilio.delete(0, tk.END)
            entry_domicilio.insert(0, jugador["domicilio"])
            entry_telefono.delete(0, tk.END)
            entry_telefono.insert(0, jugador["telefono"])
            entry_correo.delete(0, tk.END)
            entry_correo.insert(0, jugador["correo"])
            entry_fecha_nacimiento.set_date(jugador["fecha_nacimiento"])
            localidad_combo.set(jugador["localidad"])
            club_combo.set(jugador["club"])
            tipo_combo.set(jugador["categoria"])
            return
    messagebox.showerror("Error", "No se encontró un jugador con ese DNI.")

root = tk.Tk()
root.title("Alta/Modificación de Jugadores")
root.geometry("1366x765")
root.configure(bg="#ff7f00")
root.resizable(False, False)


frame_datos = tk.Frame(root, bg="#ff7f00")
frame_datos.grid(row=0, column=0, padx=50, pady=20, sticky="n")

frame_imagenes = tk.Frame(root, bg="#ff7f00")
frame_imagenes.grid(row=0, column=1, padx=200, pady=20, sticky="n")

frame_botones = tk.Frame(root, bg="#ff7f00")
frame_botones.grid(row=1, column=0, columnspan=1, padx=20, pady=40, sticky="n")

tk.Label(frame_datos, text="nombre (Obligatorio)", bg="#ff7f00", fg="black").grid(row=1, column=0, sticky="e", padx=10, pady=5)
entry_nombre = tk.Entry(frame_datos, width=30, validate="key")
entry_nombre['validatecommand'] = (root.register(solo_letras), '%S')
entry_nombre.grid(row=1, column=1, pady=5)

tk.Label(frame_datos, text="apellido (Obligatorio)", bg="#ff7f00", fg="black").grid(row=2, column=0, sticky="e", padx=10, pady=5)
entry_apellido = tk.Entry(frame_datos, width=30, validate="key")
entry_apellido['validatecommand'] = (root.register(solo_letras), '%S')
entry_apellido.grid(row=2, column=1, pady=5)

tk.Label(frame_datos, text="d.n.i (Obligatorio)", bg="#ff7f00", fg="black").grid(row=3, column=0, sticky="e", padx=10, pady=5)
entry_dni = tk.Entry(frame_datos, width=30, validate="key")
entry_dni['validatecommand'] = (root.register(solo_numeros), '%S')
entry_dni.grid(row=3, column=1, pady=5)

tk.Label(frame_datos, text="domicilio", bg="#ff7f00", fg="black").grid(row=4, column=0, sticky="e", padx=10, pady=5)
entry_domicilio = tk.Entry(frame_datos, width=30)
entry_domicilio.grid(row=4, column=1, pady=5)

tk.Label(frame_datos, text="teléfono", bg="#ff7f00", fg="black").grid(row=5, column=0, sticky="e", padx=10, pady=5)
entry_telefono = tk.Entry(frame_datos, width=30, validate="key")
entry_telefono['validatecommand'] = (root.register(solo_numeros), '%S')
entry_telefono.grid(row=5, column=1, pady=5)

tk.Label(frame_datos, text="correo (obligatorio)", bg="#ff7f00", fg="black").grid(row=6, column=0, sticky="e", padx=10, pady=5)
entry_correo = tk.Entry(frame_datos, width=30)
entry_correo.grid(row=6, column=1, pady=5)

tk.Label(frame_datos, text="fecha de Nacimiento", bg="#ff7f00", fg="black").grid(row=7, column=0, sticky="e", padx=10, pady=5)
entry_fecha_nacimiento = DateEntry(frame_datos, width=27, background="orange", foreground="black", date_pattern="dd-mm-yyyy", state="readonly")  
entry_fecha_nacimiento.set_date('23-10-2024')
entry_fecha_nacimiento.grid(row=7, column=1, pady=5)


tk.Label(frame_datos, text="localidad", bg="#ff7f00", fg="black").grid(row=8, column=0, sticky="e", padx=10, pady=5)
localidad_combo = ttk.Combobox(frame_datos, values=["Ninguna", "Villa Carlos Paz", "Cosquín", "La Falda", "Huerta Grande"], state='readonly')
localidad_combo.set("ninguna")
localidad_combo.grid(row=8, column=1, pady=5)

tk.Label(frame_datos, text="club", bg="#ff7f00", fg="black").grid(row=9, column=0, sticky="e", padx=10, pady=5)
club_combo = ttk.Combobox(frame_datos, values=["cualquiera", "club 1", "club 2", "club 3"], state='readonly')
club_combo.set("cualquiera")
club_combo.grid(row=9, column=1, pady=5)

tk.Label(frame_datos, text="Categoría", bg="#ff7f00", fg="black").grid(row=10, column=0, sticky="e", padx=10, pady=5)
tipo_combo = ttk.Combobox(frame_datos, values=["categoría", "femenino", "masculino"], state='readonly')
tipo_combo.set("categoría")
tipo_combo.grid(row=10, column=1, pady=5)

ficha_medica_img_label = tk.Label(frame_imagenes, text="sin Imagen", width=40, height=20, bg="lightgrey")
ficha_medica_img_label.grid(row=0, column=0, padx=10, pady=10)
btn_cargar_ficha = tk.Button(frame_imagenes, text="cargar Ficha Médica", command=lambda: cargar_imagen(ficha_medica_img_label), bg="lightgrey")
btn_cargar_ficha.grid(row=1, column=0)

carnet_img_label = tk.Label(frame_imagenes, text="sin Imagen", width=40, height=20, bg="lightgrey")
carnet_img_label.grid(row=0, column=1, padx=10, pady=10)
btn_cargar_carnet = tk.Button(frame_imagenes, text="cargar Carnet", command=lambda: cargar_imagen(carnet_img_label), bg="lightgrey")
btn_cargar_carnet.grid(row=1, column=1)

tk.Button(frame_botones, text="agregar jugador", command=validar_campos, bg="gray").grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_botones, text="eliminar jugador", command=confirmar_borrado, bg="gray").grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_botones, text="modificar jugador", command=validar_campos, bg="gray").grid(row=0, column=2, padx=5, pady=5)
tk.Button(frame_botones, text="borrar datos", command=confirmar_borrado, bg="gray").grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_botones, text="volver al menú", command=volver_menu, bg="gray").grid(row=1, column=1, padx=5, pady=5)

root.mainloop()