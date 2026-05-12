class Proveedor:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def obtener_contacto(self):
        return f"{self.nombre} (Tel: {self.telefono})"