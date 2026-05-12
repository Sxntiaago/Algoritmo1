class Producto:
    def __init__(self, nombre, precio, cantidad, proveedor, categoria):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.proveedor = proveedor
        self.categoria = categoria

    def mostrar_info(self):
        print(f"Producto: {self.nombre} | Precio: ${self.precio:,.0f} | Stock: {self.cantidad} | Categoría: {self.categoria}")
        print(f" > Proveedor: {self.proveedor.obtener_contacto()}")

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad,
            "proveedor": self.proveedor.nombre,
            "categoria": self.categoria
        }

    @classmethod
    def from_dict(cls, data, proveedores):
        """Crea un producto desde un diccionario, buscando el proveedor por nombre"""
        proveedor = next((p for p in proveedores if p.nombre == data["proveedor"]), None)
        if not proveedor:
            # Si no encuentra el proveedor, crea uno genérico
            proveedor = Proveedor(data["proveedor"], "Sin teléfono")
        return cls(
            data["nombre"],
            data["precio"],
            data["cantidad"],
            proveedor,
            data["categoria"]
        )
