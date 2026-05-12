from producto import Producto
from inventario import Inventario
from proveedor import Proveedor

sistema = Inventario()

prov_general = Proveedor("Distribuidora Central", "555-0123")
sistema.agregar(Producto("Arroz", 3500.0, 50, prov_general))
sistema.agregar(Producto("Leche", 4200.0, 20, prov_general))

def menu_Inventario():
    while True:
        print("\n GESTION DE INVENTARIO")
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Editar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nom = input("Nombre: ")
            pre = float(input("Precio: "))
            cant = int(input("Cantidad: "))
            nuevo = Producto(nom, pre, cant, prov_general)
            sistema.agregar(nuevo)
            print("Producto agregado.")

        elif opcion == "2":
            sistema.mostrar_inventario()

        elif opcion == "3":
            sistema.mostrar_inventario()
            nom = input("\n¿Qué producto quieres editar?: ")
            encontrado = sistema.buscar_producto(nom)
            
            if encontrado:
                pre = float(input("Nuevo precio: "))
                cant = int(input("Nueva cantidad: "))
                sistema.editar(encontrado, pre, cant)
            else:
                print("No existe.")

        elif opcion == "4":
            sistema.mostrar_inventario()
            nom = input("\nNombre a eliminar: ")
            sistema.eliminar(nom)

        elif opcion == "5":
            break