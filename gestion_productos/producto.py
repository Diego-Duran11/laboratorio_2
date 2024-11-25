class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def aumentar_stock(self, cantidad):
        self.cantidad += cantidad

    def disminuir_stock(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
        else:
            print(f"No hay suficiente stock de {self.nombre}.")