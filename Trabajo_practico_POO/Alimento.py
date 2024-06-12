#definiendo el alimento alimenticio

from Producto import Producto

class Alimento(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_expiracion):
        super().__init__(nombre, precio, cantidad)
        self.fecha_expiracion = fecha_expiracion

    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"{info_base}, Fecha de Expiración: {self.fecha_expiracion}"
