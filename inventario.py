from producto import Producto

class Inventario:
    def __init__(self):
        self.lista_productos = []

    def agregar(self, producto_nuevo):
        self.lista_productos.append(producto_nuevo)

    def mostrar_inventario(self):
        print("\n INVENTARIO ACTUAL ")
        if not self.lista_productos:
            print("El inventario está vacío.")
        for p in self.lista_productos:
            p.mostrar_info()

    def buscar_producto(self, nombre_producto):
        for p in self.lista_productos:
            if p.nombre.lower() == nombre_producto.lower():
                return p
        return None

    def eliminar(self, nombre_producto):
        p = self.buscar_producto(nombre_producto)
        if p:
            self.lista_productos.remove(p)
            print(f" '{nombre_producto}' eliminado.")
        else:
            print(" No se encontró el producto.")

    def editar(self, producto_objeto, nuevo_precio, nueva_cantidad):
        producto_objeto.precio = nuevo_precio
        producto_objeto.cantidad = nueva_cantidad
        print(f"'{producto_objeto.nombre}' actualizado.")