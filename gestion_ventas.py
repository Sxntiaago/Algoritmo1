from ventas import Venta

def menu_Ventas(sistema_inventario):
    print("\n NUEVA VENTA ")
    cliente = input("Nombre del cliente: ")
    nro_factura = input("Número de factura: ")

    nueva_venta = Venta(nro_factura, cliente)
    
    while True:
        sistema_inventario.mostrar_inventario()
        nom = input("\n¿Qué producto desea llevar? (o escribe 'fin' para terminar): ")
        
        if nom.lower() == 'fin':
            break
            
        producto = sistema_inventario.buscar_producto(nom)
        
        if producto:
            cant = int(input(f"¿Cuántas unidades de {producto.nombre}?: "))
            nueva_venta.agregar_al_carrito(producto, cant)
        else:
            print("El producto no existe.")
            
    if nueva_venta.carrito:
        nueva_venta.generar_recibo()
    else:
        print("Venta cancelada (carrito vacío).")