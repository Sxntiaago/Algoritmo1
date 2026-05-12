# Sistema de Inventario con JSON y Categorías

## Características del Nuevo Sistema

### 1. **Persistencia en JSON**
- Los datos se guardan automáticamente en `inventario.json`
- Estructura organizada con proveedores y categorías
- Carga automática al iniciar el sistema

### 2. **Productos por Categorías**
- Cada producto pertenece a una categoría específica
- Inventario organizado y fácil de navegar
- Búsqueda por categoría disponible

### 3. **Información Completa de Proveedores**
- Cada producto muestra su proveedor
- Gestión automática de proveedores
- Evita duplicados de proveedores

## Estructura del Archivo JSON

```json
{
  "proveedores": [
    {
      "nombre": "Distribuidora Central",
      "telefono": "555-0123"
    }
  ],
  "categorias": {
    "Alimentos": [
      {
        "nombre": "Arroz",
        "precio": 3500.0,
        "cantidad": 50,
        "proveedor": "Distribuidora Central",
        "categoria": "Alimentos"
      }
    ],
    "Lácteos": [
      {
        "nombre": "Leche",
        "precio": 4200.0,
        "cantidad": 20,
        "proveedor": "Distribuidora Central",
        "categoria": "Lácteos"
      }
    ]
  }
}
```

## Nuevos Métodos de la Clase Inventario

### Métodos de Categorías
- `mostrar_categoria(categoria)` - Muestra productos de una categoría
- `obtener_categorias()` - Lista todas las categorías
- `buscar_por_categoria(nombre, categoria)` - Búsqueda filtrada

### Métodos de Persistencia
- `guardar_inventario()` - Guarda en JSON
- `cargar_inventario()` - Carga desde JSON
- Auto-guardado en cada modificación

### Gestión de Proveedores
- `agregar_proveedor(proveedor)` - Registra proveedores automáticamente
- Referencias cruzadas entre productos y proveedores

## Ejemplo de Uso

```python
from inventario import Inventario
from producto import Producto
from proveedor import Proveedor

# Crear sistema (carga automáticamente desde JSON)
sistema = Inventario()

# Agregar productos con categorías
prov = Proveedor("Proveedor XYZ", "555-0000")
sistema.agregar(Producto("Pan", 2000, 30, prov, "Panadería"))
sistema.agregar(Producto("Queso", 8000, 15, prov, "Lácteos"))

# Mostrar inventario organizado
sistema.mostrar_inventario()

# Mostrar categorías disponibles
print("Categorías:", sistema.obtener_categorias())

# Mostrar productos de una categoría
sistema.mostrar_categoria("Lácteos")
```

## Ventajas del Nuevo Sistema

✅ **Persistencia**: Datos guardados permanentemente
✅ **Organización**: Productos agrupados por categorías
✅ **Escalabilidad**: Fácil agregar nuevas categorías
✅ **Integridad**: Gestión automática de proveedores
✅ **Búsqueda**: Múltiples formas de encontrar productos
✅ **Mantenimiento**: JSON legible y editable manualmente