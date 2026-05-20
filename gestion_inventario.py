from producto import Producto
from inventario import Inventario
from proveedor import Proveedor

sistema = Inventario()
prov_general = Proveedor("Proveedor General", "555-0000")
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
            mostrar_por_categoria()

        elif opcion == "4":
            editar_producto_interactivo()

        elif opcion == "5":
            eliminar_producto_interactivo()

        elif opcion == "6":
            mostrar_categorias()

        elif opcion == "7":
            print("👋 Regresando al menú principal...")
            break

        else:
            print("❌ Opción no válida. Intente nuevamente.")

        input("\nPresione Enter para continuar...")

def agregar_producto_interactivo():
    print("\n➕ AGREGAR NUEVO PRODUCTO")
    print("-" * 30)

    try:
        nombre = input("Nombre del producto: ").strip()
        if not nombre:
            print("❌ El nombre no puede estar vacío.")
            return

        precio = float(input("Precio: "))
        if precio <= 0:
            print("❌ El precio debe ser mayor a 0.")
            return

        cantidad = int(input("Cantidad en stock: "))
        if cantidad < 0:
            print("❌ La cantidad no puede ser negativa.")
            return

        categoria = input("Categoría: ").strip()
        if not categoria:
            print("❌ La categoría no puede estar vacía.")
            return

        nombre_proveedor = input("Nombre del proveedor: ").strip()
        telefono_proveedor = input("Teléfono del proveedor: ").strip()

        proveedor = None
        for p in sistema.proveedores:
            if p.nombre.lower() == nombre_proveedor.lower():
                proveedor = p
                break

        if not proveedor:
            proveedor = Proveedor(nombre_proveedor, telefono_proveedor)
            print(f"✅ Nuevo proveedor '{nombre_proveedor}' registrado.")

        nuevo_producto = Producto(nombre, precio, cantidad, proveedor, categoria)
        sistema.agregar(nuevo_producto)

        print(f"✅ Producto '{nombre}' agregado exitosamente en categoría '{categoria}'.")

    except ValueError as e:
        print(f"❌ Error en los datos ingresados: {e}")
    except Exception as e:
        print(f"❌ Error al agregar producto: {e}")

def mostrar_por_categoria():
    categorias = sistema.obtener_categorias()

    if not categorias:
        print("📭 No hay categorías disponibles.")
        return

    print("\n📁 CATEGORÍAS DISPONIBLES:")
    for i, cat in enumerate(categorias, 1):
        print(f"{i}. {cat}")

    try:
        opcion = int(input("\nSeleccione categoría (número): "))
        if 1 <= opcion <= len(categorias):
            categoria_seleccionada = categorias[opcion - 1]
            sistema.mostrar_categoria(categoria_seleccionada)
        else:
            print("❌ Opción no válida.")
    except ValueError:
        print("❌ Ingrese un número válido.")

def editar_producto_interactivo():
    print("\n✏️ EDITAR PRODUCTO")
    print("-" * 20)

    sistema.mostrar_inventario()
    nombre = input("\nNombre del producto a editar: ").strip()

    producto = sistema.buscar_producto(nombre)
    if not producto:
        print(f"❌ No se encontró el producto '{nombre}'.")
        return

    print(f"\nProducto encontrado: {producto.nombre}")
    print(f"Categoría actual: {producto.categoria}")
    print(f"Precio actual: ${producto.precio:,.0f}")
    print(f"Stock actual: {producto.cantidad}")

    try:
        nuevo_precio = float(input("Nuevo precio (Enter para mantener actual): ") or producto.precio)
        nueva_cantidad = int(input("Nueva cantidad (Enter para mantener actual): ") or producto.cantidad)
        nueva_categoria = input(f"Nueva categoría (Enter para mantener '{producto.categoria}'): ").strip() or producto.categoria

        if nuevo_precio <= 0:
            print("❌ El precio debe ser mayor a 0.")
            return

        if nueva_cantidad < 0:
            print("❌ La cantidad no puede ser negativa.")
            return

        sistema.editar(producto, nuevo_precio, nueva_cantidad, nueva_categoria)
        print("✅ Producto actualizado exitosamente.")

    except ValueError as e:
        print(f"❌ Error en los datos: {e}")

def eliminar_producto_interactivo():
    print("\n🗑️ ELIMINAR PRODUCTO")
    print("-" * 20)

    sistema.mostrar_inventario()
    nombre = input("\nNombre del producto a eliminar: ").strip()

    confirmar = input(f"¿Está seguro de eliminar '{nombre}'? (s/n): ").strip().lower()
    if confirmar == 's':
        sistema.eliminar(nombre)
    else:
        print("❌ Operación cancelada.")

def mostrar_categorias():
    categorias = sistema.obtener_categorias()

    if not categorias:
        print("📭 No hay categorías registradas.")
        return

    print("\n📁 CATEGORÍAS DISPONIBLES:")
    print("=" * 30)
    for i, categoria in enumerate(categorias, 1):
        productos_en_cat = len(sistema.categorias[categoria])
        print(f"{i}. {categoria} ({productos_en_cat} productos)")

        print(f"\n📊 Total de categorías: {len(categorias)}")
        break