# Sistema de Gestión de Inventario 📦

Un sistema profesional de gestión de inventario y ventas con interfaz gráfica en Tkinter. Permite administrar productos, categorías, proveedores y realizar transacciones de venta con persistencia de datos en JSON.

## ✨ Características

- **Interfaz Gráfica**: Interfaz moderna y amigable con Tkinter
- **Gestión de Inventario**: Agregar, editar, eliminar y buscar productos
- **Organización por Categorías**: Productos clasificados automáticamente por categoría
- **Gestión de Proveedores**: Registrar y vincular proveedores a productos
- **Sistema de Ventas**: Crear facturas con múltiples productos
- **Persistencia JSON**: Todos los datos se guardan en formato JSON
- **Login Seguro**: Sistema de autenticación de usuarios
- **Reportes**: Ver inventario total, cantidad de productos, valor del inventario

## 📋 Requisitos

- Python 3.8+
- Tkinter (incluido en Python por defecto)

## 🚀 Instalación

1. Clona o descarga el repositorio:
```bash
git clone <url-del-repositorio>
cd Algoritmo1
```

2. Verifica que tengas Python instalado:
```bash
python --version
```

3. ¡Listo! No hay dependencias adicionales que instalar.

## 💻 Uso

### Iniciar la Aplicación

```bash
python main.py
```

### Credenciales de Prueba

**Usuario**: `admin`  
**Contraseña**: `admin123`

### Flujo de la Aplicación

1. **Login**: Inicia sesión con tus credenciales
2. **Menú Principal**: Accede a las opciones principales
3. **Gestión Inventario**: 
   - Ver todos los productos organizados por categoría
   - Agregar nuevos productos
   - Editar productos existentes
   - Eliminar productos
4. **Gestión Ventas**:
   - Crear nuevas ventas
   - Seleccionar productos y cantidades
   - Generar facturas

## 📁 Estructura del Proyecto

### Vistas (Interfaz Gráfica)
- **`view.py`** - Ventana de login con validación de usuarios
- **`menu_view.py`** - Menú principal con opciones de navegación

### Lógica de Negocio
- **`inventario.py`** - Gestión del inventario y persistencia JSON
- **`producto.py`** - Clase Producto con atributos y métodos
- **`proveedor.py`** - Clase Proveedor para gestionar contactos
- **`ventas.py`** - Clase Venta para registrar transacciones
- **`gestion_inventario.py`** - Funciones CLI para operaciones del inventario
- **`gestion_ventas.py`** - Funciones CLI para operaciones de ventas

### Seguridad y Usuarios
- **`login.py`** - Sistema de login (heredado)
- **`usuario.py`** - Clase base Usuario (modelo de usuarios)
- **`admin.py`** - Clase Admin con permisos elevados
- **`empleado.py`** - Clase Empleado con permisos limitados

### Datos y Configuración
- **`usuarios.json`** - Almacena usuarios registrados
- **`inventario.json`** - Almacena productos por categoría

### Punto de Entrada
- **`main.py`** - Script principal que inicia la aplicación

## 📊 Estructura de Datos JSON

### Inventario (inventario.json)
```json
{
  "Alimentos": [
    {
      "nombre": "Arroz",
      "precio": 3500,
      "cantidad": 50,
      "proveedor": "Distribuidora Central",
      "categoria": "Alimentos"
    }
  ],
  "Lácteos": [
    {
      "nombre": "Leche",
      "precio": 4200,
      "cantidad": 20,
      "proveedor": "Distribuidora Central",
      "categoria": "Lácteos"
    }
  ]
}
```

### Usuarios (usuarios.json)
```json
{
  "admin": "admin123",
  "empleado": "emp123"
}
```

## 🔑 Funcionalidades Principales

### Gestión de Inventario

| Operación | Descripción |
|-----------|------------|
| Agregar Producto | Crear nuevo producto con categoría y proveedor |
| Ver Inventario | Listar todos los productos por categoría |
| Editar Producto | Modificar precio y cantidad de productos |
| Eliminar Producto | Remover productos del inventario |
| Buscar Producto | Encontrar productos por nombre |

### Gestión de Ventas

| Operación | Descripción |
|-----------|------------|
| Nueva Venta | Iniciar transacción con cliente |
| Agregar Items | Seleccionar productos y cantidades |
| Generar Recibo | Crear factura con detalles de venta |

## 🎯 Ejemplos de Uso

### Agregar un Producto
```
1. Selecciona "Gestión Inventario"
2. Selecciona "Agregar Producto"
3. Ingresa: Nombre, Precio, Cantidad, Categoría
4. El producto se guarda automáticamente en JSON
```

### Realizar una Venta
```
1. Selecciona "Gestión Ventas"
2. Ingresa nombre del cliente y número de factura
3. Selecciona productos disponibles
4. Ingresa cantidad de unidades
5. Completa la venta - se genera el recibo
```

## 🔐 Sistema de Seguridad

- **Autenticación**: Login con usuario y contraseña
- **Persistencia Segura**: Los datos se guardan en JSON local
- **Roles de Usuario**: Admin y Empleado con diferentes permisos

## 📈 Datos Guardados

Todos los datos se persisten automáticamente en formato JSON:
- ✅ Productos y categorías
- ✅ Información de proveedores
- ✅ Historial de ventas
- ✅ Credenciales de usuarios

## 🐛 Solución de Problemas

### "Python no se encuentra"
```bash
# Intenta con python3
python3 main.py
```

### "Módulo no encontrado"
Asegúrate de estar en el directorio correcto:
```bash
cd c:\Users\santy\OneDrive\Escritorio\Algoritmo1
```

### Los datos no se guardan
Verifica que tengas permisos de escritura en la carpeta del proyecto.

## 🤝 Contribuciones

Las sugerencias y mejoras son bienvenidas. Siéntete libre de:
- Reportar bugs
- Sugerir nuevas características
- Mejorar la documentación

## 📝 Licencia

Este proyecto es de código abierto y puede ser utilizado libremente.

## 👨‍💻 Autor

Proyecto desarrollado como sistema de gestión de inventario educativo.

---

**Última actualización**: Mayo 2026  
**Versión**: 1.0