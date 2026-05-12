class Producto:
    def __init__(self, nombre, precio, cantidad, proveedor):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.proveedor = proveedor

    def mostrar_info(self):
        print(f"Producto: {self.nombre} | Precio: {self.precio} | Stock: {self.cantidad}")
        print(f" > Proveedor: {self.proveedor.obtener_contacto()}")
