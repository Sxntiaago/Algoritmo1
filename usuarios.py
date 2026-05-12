class Usuarios:
    def __init__(self, nombre, contraseña, rol):
        self.nombre = nombre
        self.contraseña = contraseña
        self.rol = rol
    def mostrar_info(self):
        print(f"Usuario: {self.nombre} | Rol: {self.rol}")
class Admin(Usuarios):
    def __init__(self, nombre, contraseña):
        super().__init__(nombre, contraseña, rol="admin")
class Empleado(Usuarios):
    def __init__(self, nombre, contraseña):
        super().__init__(nombre, contraseña, rol="empleado")

