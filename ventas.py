class Venta:
    def __init__(self, nro_factura,  cliente):
        self.nro_factura = nro_factura
        self.cliente = cliente
        self.carrito = [] 
        self.total = 0

    def agregar_al_carrito(self, producto, cantidad_vendida):
        if producto.cantidad >= cantidad_vendida:
            producto.cantidad -= cantidad_vendida
            
            item = {
                "producto": producto.nombre,
                "cantidad": cantidad_vendida,
                "subtotal": producto.precio * cantidad_vendida
            }
            self.carrito.append(item)
            self.total += item["subtotal"]
            print(f"{producto.nombre} agregado a la factura.")
        else:
            print(f"Stock insuficiente para {producto.nombre}.")

    def generar_recibo(self):

        print(f" FACTURA NRO: {self.nro_factura}")
        print(f" Cliente: {self.cliente}")

        for item in self.carrito:
            print(f"{item['producto']} x{item['cantidad']}  ${item['subtotal']}")

        print(f" TOTAL A PAGAR: ${self.total}")
