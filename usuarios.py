class Usuarios:
    def __init__(self, nombre, user, contraseña, rol):
        self.nombre = nombre
        self.user = user
        self.contraseña = contraseña
        self.rol = rol
    def mostrar_info(self):
        print(f"Usuario: {self.nombre} | User: {self.user} | Rol: {self.rol}")
class Admin(Usuarios):
    def __init__(self, nombre, contraseña, user):
        super().__init__(nombre, user, contraseña, rol="admin")
class Empleado(Usuarios):
    def __init__(self, nombre, contraseña, user):
        super().__init__(nombre, user, contraseña, rol="empleado")

