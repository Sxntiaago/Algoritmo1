from producto import Producto
from inventario import Inventario
from proveedor import Proveedor
from gestion_inventario import menu_Inventario
from gestion_ventas import menu_Ventas 
from view import LoginWindow
import tkinter as tk


sistema = Inventario()


prov_general = Proveedor("Distribuidora Central", "555-0123")
sistema.agregar(Producto("Arroz", 3500.0, 50, prov_general, "Alimentos"))
sistema.agregar(Producto("Leche", 4200.0, 20, prov_general, "Lácteos"))

root = tk.Tk()
LoginWindow(root)
root.mainloop()
print("Acceso concedido")
while True:
    print("\n SISTEMA PRINCIPAL")
    print("1. Gestión inventario")
    print("2. Gestión ventas")
    print("3. Salir")
    
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        menu_Inventario() 

    elif opcion == "2":
        menu_Ventas(sistema) 

    elif opcion == "3":
        print("BAY")
        break
    else:
        print("Opción no válida.")