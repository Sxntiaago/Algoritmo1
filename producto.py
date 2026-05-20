from proveedor import Proveedor
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
        proveedor = next((p for p in proveedores if p.nombre == data["proveedor"]), None)
        if not proveedor:
            proveedor = Proveedor(data["proveedor"], "Sin teléfono")
        return cls(
            data["nombre"],
            data["precio"],
            data["cantidad"],
            proveedor,
            data["categoria"]
        )
