#Definiendo al electro y al medico

from Producto import Producto

class Electronico(Producto):
    def __init__(self, nombre, precio, cantidad, marca, modelo, garantia):
        super().__init__(nombre, precio, cantidad)
        self.marca = marca
        self.modelo = modelo
        self.garantia = garantia

    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"{info_base}, Marca: {self.marca}, Modelo: {self.modelo}, Garantía: {self.garantia} años"
