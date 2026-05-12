# Sistema de Gestión de Inventario

## Estructura Modular del Proyecto

### Archivos de Vista (Interfaz Gráfica)
- **`view.py`** - Contiene la ventana de login (`LoginWindow`)
- **`menu_view.py`** - Contiene el menú principal (`MainMenuWindow`)

### Archivos de Lógica de Negocio
- **`inventario.py`** - Gestión del inventario
- **`producto.py`** - Clase Producto
- **`proveedor.py`** - Clase Proveedor
- **`ventas.py`** - Clase Venta
- **`gestion_inventario.py`** - Funciones para gestionar inventario
- **`gestion_ventas.py`** - Funciones para gestionar ventas

### Archivos de Usuario (Módulos Separados)
- **`usuario.py`** - Clase base Usuario
- **`admin.py`** - Clase Admin (hereda de Usuario)
- **`empleado.py`** - Clase Empleado (hereda de Usuario)

### Archivo Principal
- **`main.py`** - Punto de entrada que inicia la interfaz gráfica

## Flujo de la Aplicación

1. **`main.py`** ejecuta `LoginWindow` desde `view.py`
2. Después del login exitoso, `view.py` abre `MainMenuWindow` desde `menu_view.py`
3. El menú principal permite acceder a gestión de inventario y ventas
4. Las funciones de gestión usan los módulos de lógica de negocio

## Beneficios de la Separación

- **Modularidad**: Cada componente en su propio archivo
- **Mantenibilidad**: Fácil modificar vistas sin afectar lógica
- **Reutilización**: Clases pueden importarse independientemente
- **Claridad**: Código organizado y fácil de entender

## Ejecución

```bash
python main.py
```

Esto iniciará la interfaz gráfica completa del sistema.