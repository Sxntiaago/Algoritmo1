from producto import Producto
from proveedor import Proveedor
import json
import os
from pathlib import Path

class Inventario:
    def __init__(self, archivo_json="inventario.json"):
        self.archivo_json = Path(archivo_json)
        self.categorias = {}  # {categoria: [productos]}
        self.proveedores = []  # Lista de proveedores para referencia
        self.cargar_inventario()

    def agregar_proveedor(self, proveedor):
        """Agrega un proveedor si no existe"""
        if not any(p.nombre == proveedor.nombre for p in self.proveedores):
            self.proveedores.append(proveedor)

    def agregar(self, producto_nuevo):
        """Agrega un producto al inventario"""
        self.agregar_proveedor(producto_nuevo.proveedor)

        if producto_nuevo.categoria not in self.categorias:
            self.categorias[producto_nuevo.categoria] = []

        self.categorias[producto_nuevo.categoria].append(producto_nuevo)
        self.guardar_inventario()

    def mostrar_inventario(self):
        """Muestra todo el inventario organizado por categorías"""
        print("\n" + "="*50)
        print("           INVENTARIO ACTUAL")
        print("="*50)

        if not self.categorias:
            print("El inventario está vacío.")
            return

        total_productos = 0
        valor_total = 0

        for categoria, productos in self.categorias.items():
            print(f"\n📁 CATEGORÍA: {categoria.upper()}")
            print("-" * 40)

            for producto in productos:
                producto.mostrar_info()
                total_productos += producto.cantidad
                valor_total += producto.precio * producto.cantidad
                print()

        print("="*50)
        print(f"📊 RESUMEN:")
        print(f"   • Total de productos en stock: {total_productos}")
        print(f"   • Valor total del inventario: ${valor_total:,.0f}")
        print(f"   • Categorías: {len(self.categorias)}")
        print("="*50)

    def mostrar_categoria(self, categoria):
        """Muestra productos de una categoría específica"""
        if categoria not in self.categorias:
            print(f"No existe la categoría '{categoria}'")
            return

        print(f"\n📁 PRODUCTOS EN CATEGORÍA: {categoria.upper()}")
        print("-" * 40)

        for producto in self.categorias[categoria]:
            producto.mostrar_info()
            print()

    def obtener_categorias(self):
        """Retorna lista de categorías disponibles"""
        return list(self.categorias.keys())

    def buscar_producto(self, nombre_producto):
        """Busca un producto por nombre en todas las categorías"""
        for productos in self.categorias.values():
            for producto in productos:
                if producto.nombre.lower() == nombre_producto.lower():
                    return producto
        return None

    def buscar_por_categoria(self, nombre_producto, categoria=None):
        """Busca un producto por nombre, opcionalmente filtrando por categoría"""
        if categoria and categoria in self.categorias:
            productos = self.categorias[categoria]
        else:
            productos = [p for lista_prod in self.categorias.values() for p in lista_prod]

        for producto in productos:
            if producto.nombre.lower() == nombre_producto.lower():
                return producto
        return None

    def eliminar(self, nombre_producto, categoria=None):
        """Elimina un producto por nombre, opcionalmente de una categoría específica"""
        if categoria and categoria in self.categorias:
            productos = self.categorias[categoria]
        else:
            productos = [p for lista_prod in self.categorias.values() for p in lista_prod]

        for producto in productos:
            if producto.nombre.lower() == nombre_producto.lower():
                # Encontrar la categoría correcta si no se especificó
                if not categoria:
                    for cat, prods in self.categorias.items():
                        if producto in prods:
                            categoria = cat
                            break

                self.categorias[categoria].remove(producto)
                # Si la categoría queda vacía, la eliminamos
                if not self.categorias[categoria]:
                    del self.categorias[categoria]

                self.guardar_inventario()
                print(f"✅ '{nombre_producto}' eliminado de la categoría '{categoria}'.")
                return True

        print(f"❌ No se encontró el producto '{nombre_producto}'.")
        return False

    def editar(self, producto_objeto, nuevo_precio, nueva_cantidad, nueva_categoria=None):
        """Edita un producto existente"""
        # Buscar el producto en todas las categorías
        for categoria, productos in self.categorias.items():
            if producto_objeto in productos:
                producto_objeto.precio = nuevo_precio
                producto_objeto.cantidad = nueva_cantidad

                # Si cambia de categoría
                if nueva_categoria and nueva_categoria != categoria:
                    productos.remove(producto_objeto)
                    if not productos:  # Si la categoría queda vacía
                        del self.categorias[categoria]

                    if nueva_categoria not in self.categorias:
                        self.categorias[nueva_categoria] = []
                    self.categorias[nueva_categoria].append(producto_objeto)
                    producto_objeto.categoria = nueva_categoria

                self.guardar_inventario()
                print(f"✅ '{producto_objeto.nombre}' actualizado.")
                return True

        print(f"❌ No se encontró el producto '{producto_objeto.nombre}'.")
        return False

    def guardar_inventario(self):
        """Guarda el inventario completo en un archivo JSON"""
        try:
            # Crear directorio si no existe
            self.archivo_json.parent.mkdir(parents=True, exist_ok=True)

            # Preparar datos para JSON
            datos = {
                "proveedores": [
                    {"nombre": p.nombre, "telefono": p.telefono}
                    for p in self.proveedores
                ],
                "categorias": {}
            }

            # Organizar productos por categoría
            for categoria, productos in self.categorias.items():
                datos["categorias"][categoria] = [
                    producto.to_dict() for producto in productos
                ]

            # Guardar en JSON con indentación para legibilidad
            with open(self.archivo_json, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)

        except Exception as e:
            print(f"❌ Error al guardar inventario: {e}")

    def cargar_inventario(self):
        """Carga el inventario desde un archivo JSON"""
        try:
            if not self.archivo_json.exists():
                # Si no existe el archivo, crear uno vacío
                self.guardar_inventario()
                return

            with open(self.archivo_json, 'r', encoding='utf-8') as f:
                datos = json.load(f)

            # Cargar proveedores
            self.proveedores = []
            if "proveedores" in datos:
                for prov_data in datos["proveedores"]:
                    proveedor = Proveedor(prov_data["nombre"], prov_data["telefono"])
                    self.proveedores.append(proveedor)

            # Cargar productos por categoría
            self.categorias = {}
            if "categorias" in datos:
                for categoria, productos_data in datos["categorias"].items():
                    self.categorias[categoria] = []
                    for prod_data in productos_data:
                        producto = Producto.from_dict(prod_data, self.proveedores)
                        self.categorias[categoria].append(producto)

        except Exception as e:
            print(f"❌ Error al cargar inventario: {e}")
            # En caso de error, inicializar vacío
            self.categorias = {}
            self.proveedores = []