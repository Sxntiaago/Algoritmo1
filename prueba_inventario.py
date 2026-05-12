#!/usr/bin/env python3
"""
Script de prueba para el nuevo sistema de inventario con JSON y categorías
"""

from inventario import Inventario
from producto import Producto
from proveedor import Proveedor

def probar_sistema():
    print("🧪 PRUEBA DEL SISTEMA DE INVENTARIO")
    print("=" * 50)

    # Crear sistema
    sistema = Inventario("inventario_prueba.json")
    print("✅ Sistema de inventario creado")

    # Crear proveedores
    prov1 = Proveedor("Distribuidora Central", "555-0123")
    prov2 = Proveedor("Alimentos del Valle", "555-0456")

    # Agregar productos con categorías
    productos_prueba = [
        ("Arroz", 3500, 50, prov1, "Alimentos"),
        ("Leche", 4200, 20, prov1, "Lácteos"),
        ("Pan", 2000, 30, prov2, "Panadería"),
        ("Queso", 8000, 15, prov2, "Lácteos"),
        ("Manzanas", 1500, 100, prov1, "Frutas"),
        ("Naranjas", 1800, 80, prov1, "Frutas")
    ]

    print("\n📦 Agregando productos de prueba...")
    for nombre, precio, cantidad, proveedor, categoria in productos_prueba:
        producto = Producto(nombre, precio, cantidad, proveedor, categoria)
        sistema.agregar(producto)
        print(f"  ✅ {nombre} → {categoria}")

    # Mostrar inventario completo
    print("\n📋 INVENTARIO COMPLETO:")
    sistema.mostrar_inventario()

    # Probar búsqueda por categoría
    print("\n🔍 PRODUCTOS EN LÁCTEOS:")
    sistema.mostrar_categoria("Lácteos")

    # Probar búsqueda de producto
    print("\n🔎 BÚSQUEDA DE 'PAN':")
    pan = sistema.buscar_producto("pan")
    if pan:
        pan.mostrar_info()
    else:
        print("No encontrado")

    # Mostrar categorías disponibles
    print(f"\n📁 CATEGORÍAS DISPONIBLES: {sistema.obtener_categorias()}")

    # Probar edición
    print("\n✏️ EDITANDO PRODUCTO 'ARROZ'...")
    arroz = sistema.buscar_producto("arroz")
    if arroz:
        sistema.editar(arroz, 3800, 45, "Cereales")  # Cambiar precio, cantidad y categoría
        print("✅ Producto editado")

    # Mostrar inventario actualizado
    print("\n📋 INVENTARIO ACTUALIZADO:")
    sistema.mostrar_inventario()

    # Probar eliminación
    print("\n🗑️ ELIMINANDO PRODUCTO 'PAN'...")
    sistema.eliminar("pan")

    print("\n📋 INVENTARIO FINAL:")
    sistema.mostrar_inventario()

    print("\n✅ PRUEBA COMPLETADA EXITOSAMENTE")
    print("📄 Archivo guardado en: inventario_prueba.json")

if __name__ == "__main__":
    probar_sistema()