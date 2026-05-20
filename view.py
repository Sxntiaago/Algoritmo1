import tkinter as tk
from tkinter import messagebox, ttk
import json
from pathlib import Path
from datetime import datetime

log = Path(r"C:\Users\santy\OneDrive\Escritorio\Algoritmo1\usuarios.json")


if not log.exists():
    with open(log, "w", encoding="utf-8") as f:
        json.dump({"admin": {"contrasena": "admin123", "rol": "admin"}}, f)


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Inventario - Login")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        self.center_window()
        
        self.crear_interfaz()
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def crear_interfaz(self):

        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        

        titulo = tk.Label(
            main_frame,
            text="SISTEMA DE INVENTARIO",
            font=("Arial", 18, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        titulo.pack(pady=(0, 10))
        
        subtitulo = tk.Label(
            main_frame,
            text="Iniciar Sesión",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#666666"
        )
        subtitulo.pack(pady=(0, 20))
        
    
        campos_frame = tk.Frame(main_frame, bg="#f0f0f0")
        campos_frame.pack(fill="both", expand=True)
        

        tk.Label(
            campos_frame,
            text="Usuario:",
            font=("Arial", 11),
            bg="#f0f0f0",
            fg="#333333"
        ).pack(anchor="w", pady=(10, 5))
        
        self.usuario_entry = tk.Entry(
            campos_frame,
            font=("Arial", 11),
            width=30,
            relief="solid",
            borderwidth=1
        )
        self.usuario_entry.pack(fill="x", pady=(0, 15))
        self.usuario_entry.focus()
        

        tk.Label(
            campos_frame,
            text="Contraseña:",
            font=("Arial", 11),
            bg="#f0f0f0",
            fg="#333333"
        ).pack(anchor="w", pady=(10, 5))
        
        self.password_entry = tk.Entry(
            campos_frame,
            font=("Arial", 11),
            width=30,
            show="*",
            relief="solid",
            borderwidth=1
        )
        self.password_entry.pack(fill="x", pady=(0, 20))
        
   
        self.password_entry.bind("<Return>", lambda e: self.verificar_login())
        

        botones_frame = tk.Frame(main_frame, bg="#f0f0f0")
        botones_frame.pack(fill="x", pady=(20, 0))
        
        btn_login = tk.Button(
            botones_frame,
            text="Iniciar Sesión",
            command=self.verificar_login,
            font=("Arial", 11, "bold"),
            bg="#4CAF50",
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10
        )
        btn_login.pack(fill="x", pady=(0, 0))
    
    def verificar_login(self):
        usuario = self.usuario_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not usuario or not password:
            messagebox.showwarning("Advertencia", "Por favor completa todos los campos")
            return
        
        try:
            with open(log, "r", encoding="utf-8") as f:
                usuarios = json.load(f)
            
            if usuario in usuarios:
                datos_usuario = usuarios[usuario]
                if isinstance(datos_usuario, dict):
                    contrasena_guardada = datos_usuario.get("contrasena")
                else:
                    contrasena_guardada = datos_usuario
                
                if contrasena_guardada == password:
                    messagebox.showinfo("Éxito", f"¡Bienvenido {usuario}!")
                    self.root.destroy()
                    self.abrir_menu_principal()
                    return True
            
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
            self.password_entry.delete(0, tk.END)
            self.usuario_entry.focus()
        except Exception as e:
            messagebox.showerror("Error", f"Error al verificar credenciales: {str(e)}")
    
    def abrir_menu_principal(self):
        from view import MainMenuWindow
        from inventario import Inventario
        
        menu_root = tk.Toplevel()
        MainMenuWindow(menu_root, Inventario())

class MainMenuWindow:
    def __init__(self, root, sistema):
        self.root = root
        self.sistema = sistema
        self.root.title("Sistema de Gestión de Inventario - Menú Principal")
        
        self.root.geometry("500x650") 
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        self.center_window()
        self.crear_interfaz()

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def crear_interfaz(self):
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        titulo = tk.Label(
            main_frame,
            text="MENÚ PRINCIPAL",
            font=("Arial", 20, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        titulo.pack(pady=(10, 5))

        subtitulo = tk.Label(
            main_frame,
            text="Selecciona una opción",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#666666"
        )
        subtitulo.pack(pady=(0, 15))

        botones_frame = tk.Frame(main_frame, bg="#f0f0f0")
        botones_frame.pack(fill="x")

        btn_inventario = tk.Button(
            botones_frame,
            text="📦 Gestión de Inventario",
            command=self.abrir_gestion_inventario,
            font=("Arial", 12, "bold"),
            bg="#2196F3",
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10, 
            width=25
        )
        btn_inventario.pack(pady=5)

        btn_ventas = tk.Button(
            botones_frame,
            text="💰 Gestión de Ventas",
            command=self.abrir_gestion_ventas,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10,
            width=25
        )
        btn_ventas.pack(pady=5)

        btn_proveedores = tk.Button(
            botones_frame,
            text="🏭 Gestión de Proveedores",
            command=self.abrir_gestion_proveedores,
            font=("Arial", 12, "bold"),
            bg="#FF9800",
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10,
            width=25
        )
        btn_proveedores.pack(pady=5)

        btn_usuarios = tk.Button(
            botones_frame,
            text="👥 Gestión de Usuarios",
            command=self.abrir_gestion_usuarios,
            font=("Arial", 12, "bold"),
            bg="#9C27B0",
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10,
            width=25
        )
        btn_usuarios.pack(pady=5)

        salir_frame = tk.Frame(main_frame, bg="#f0f0f0")
        salir_frame.pack(fill="x", pady=(20, 0))

        btn_salir = tk.Button(
            salir_frame,
            text="🚪 Salir",
            command=self.salir,
            font=("Arial", 12, "bold"),
            bg="#f44336",
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10,
            width=25
        )
        btn_salir.pack(pady=5)

    def abrir_gestion_inventario(self):
        gestion_root = tk.Toplevel(self.root)
        GestionInventarioWindow(gestion_root, self.sistema)

    def abrir_gestion_ventas(self):
        gestion_root = tk.Toplevel(self.root)
        GestionVentasWindow(gestion_root, self.sistema)

    def abrir_gestion_proveedores(self):
        gestion_root = tk.Toplevel(self.root)
        ProveedorWindow(gestion_root, self.sistema)

    def abrir_gestion_usuarios(self):
        gestion_root = tk.Toplevel(self.root)
        UsuariosWindow(gestion_root)

    def salir(self):
        if messagebox.askyesno("Confirmar salida", "¿Estás seguro de que quieres salir?"):
            self.root.quit()


class GestionInventarioWindow:
    def __init__(self, root, sistema):
        self.root = root
        self.sistema = sistema
        self.root.title("Gestión de Inventario")
        self.root.geometry("900x600")
        self.root.resizable(True, True)
        self.root.configure(bg="#f0f0f0")
        
        self.center_window()
        self.crear_interfaz()
        self.actualizar_tabla()
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def crear_interfaz(self):
        titulo_frame = tk.Frame(self.root, bg="#2196F3")
        titulo_frame.pack(fill="x", padx=0, pady=0)
        
        titulo = tk.Label(
            titulo_frame,
            text="📦 GESTIÓN DE INVENTARIO",
            font=("Arial", 18, "bold"),
            bg="#2196F3",
            fg="white"
        )
        titulo.pack(pady=10)
        
        botones_frame = tk.Frame(self.root, bg="#f0f0f0")
        botones_frame.pack(fill="x", padx=20, pady=10)
        
        btn_agregar = tk.Button(
            botones_frame,
            text="➕ Agregar Producto",
            command=self.agregar_producto,
            font=("Arial", 10, "bold"),
            bg="#4CAF50",
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        )
        btn_agregar.pack(side="left", padx=5)
        
        btn_editar = tk.Button(
            botones_frame,
            text="✏️ Editar Producto",
            command=self.editar_producto,
            font=("Arial", 10, "bold"),
            bg="#FFC107",
            fg="black",
            relief="flat",
            padx=15,
            pady=8
        )
        btn_editar.pack(side="left", padx=5)
        
        btn_eliminar = tk.Button(
            botones_frame,
            text="🗑️ Eliminar Producto",
            command=self.eliminar_producto,
            font=("Arial", 10, "bold"),
            bg="#f44336",
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        )
        btn_eliminar.pack(side="left", padx=5)
        
        btn_actualizar = tk.Button(
            botones_frame,
            text="🔄 Actualizar",
            command=self.actualizar_tabla,
            font=("Arial", 10, "bold"),
            bg="#2196F3",
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        )
        btn_actualizar.pack(side="left", padx=5)
        
        btn_salir = tk.Button(
            botones_frame,
            text="🚪 Salir",
            command=self.salir,
            font=("Arial", 10, "bold"),
            bg="#f44336",
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        )
        btn_salir.pack(side="right", padx=5)
        
        btn_volver = tk.Button(
            botones_frame,
            text="⬅️ Volver",
            command=self.root.destroy,
            font=("Arial", 10, "bold"),
            bg="#757575",
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        )
        btn_volver.pack(side="right", padx=5)
        
        tabla_frame = tk.Frame(self.root, bg="white")
        tabla_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        columns = ("Nombre", "Precio", "Cantidad", "Categoría", "Proveedor")
        self.tabla = ttk.Treeview(tabla_frame, columns=columns, height=20, show="headings")
        
        for col in columns:
            self.tabla.heading(col, text=col)
            if col == "Nombre":
                self.tabla.column(col, width=200)
            elif col == "Proveedor":
                self.tabla.column(col, width=180)
            else:
                self.tabla.column(col, width=100)
        
        scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        
        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def salir(self):
        if messagebox.askyesno("Confirmar salida", "¿Estás seguro de que quieres salir de la aplicación?"):
            if hasattr(self.root, "master") and self.root.master:
                self.root.master.destroy()
            else:
                self.root.destroy()
    
    def actualizar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        for categoria, productos in self.sistema.categorias.items():
            for producto in productos:
                self.tabla.insert("", "end", values=(
                    producto.nombre,
                    f"${producto.precio:,.0f}",
                    producto.cantidad,
                    categoria,
                    producto.proveedor.nombre
                ))
    
    def agregar_producto(self):
        ProductoWindow(tk.Toplevel(self.root), self.sistema, self.actualizar_tabla)
    
    def editar_producto(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un producto para editar")
            return
        
        item = seleccion[0]
        valores = self.tabla.item(item, "values")
        nombre_producto = valores[0]
        categoria = valores[3]
        
        producto = self.sistema.buscar_por_categoria(nombre_producto, categoria)
        if producto:
            ProductoWindow(tk.Toplevel(self.root), self.sistema, self.actualizar_tabla, producto)
    
    def eliminar_producto(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un producto para eliminar")
            return
        
        item = seleccion[0]
        valores = self.tabla.item(item, "values")
        nombre_producto = valores[0]
        categoria = valores[3]
        
        if messagebox.askyesno("Confirmar", f"¿Estás seguro de eliminar '{nombre_producto}'?"):
            self.sistema.eliminar(nombre_producto, categoria)
            self.actualizar_tabla()
            messagebox.showinfo("Éxito", f"Producto '{nombre_producto}' eliminado")


class ProductoWindow:
    def __init__(self, root, sistema, callback=None, producto=None):
        self.root = root
        self.sistema = sistema
        self.callback = callback
        self.producto = producto
        self.is_edit = producto is not None
        
        self.root.title("Editar Producto" if self.is_edit else "Agregar Producto")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        self.center_window()
        self.crear_interfaz()
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def crear_interfaz(self):
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        titulo = tk.Label(
            main_frame,
            text="Editar Producto" if self.is_edit else "Agregar Nuevo Producto",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        titulo.pack(pady=(0, 20))
        
        tk.Label(main_frame, text="Nombre:", font=("Arial", 10), bg="#f0f0f0").pack(anchor="w", pady=(10, 5))
        self.nombre_entry = tk.Entry(main_frame, font=("Arial", 10), width=40, relief="solid", borderwidth=1)
        self.nombre_entry.pack(fill="x", pady=(0, 15))
        
        tk.Label(main_frame, text="Precio:", font=("Arial", 10), bg="#f0f0f0").pack(anchor="w", pady=(10, 5))
        self.precio_entry = tk.Entry(main_frame, font=("Arial", 10), width=40, relief="solid", borderwidth=1)
        self.precio_entry.pack(fill="x", pady=(0, 15))
        
        tk.Label(main_frame, text="Cantidad:", font=("Arial", 10), bg="#f0f0f0").pack(anchor="w", pady=(10, 5))
        self.cantidad_entry = tk.Entry(main_frame, font=("Arial", 10), width=40, relief="solid", borderwidth=1)
        self.cantidad_entry.pack(fill="x", pady=(0, 15))
        
        tk.Label(main_frame, text="Categoría:", font=("Arial", 10), bg="#f0f0f0").pack(anchor="w", pady=(10, 5))
        self.categoria_entry = tk.Entry(main_frame, font=("Arial", 10), width=40, relief="solid", borderwidth=1)
        self.categoria_entry.pack(fill="x", pady=(0, 15))
        
        tk.Label(main_frame, text="Proveedor:", font=("Arial", 10), bg="#f0f0f0").pack(anchor="w", pady=(10, 5))
        self.proveedor_var = tk.StringVar()
        proveedores = [p.nombre for p in self.sistema.proveedores]
        
        self.proveedor_combo = ttk.Combobox(main_frame, textvariable=self.proveedor_var, values=proveedores, width=37, state="readonly")
        self.proveedor_combo.pack(fill="x", pady=(0, 15))
        
        tk.Label(main_frame, text="Teléfono Proveedor:", font=("Arial", 10), bg="#f0f0f0").pack(anchor="w", pady=(10, 5))
        self.telefono_entry = tk.Entry(main_frame, font=("Arial", 10), width=40, relief="solid", borderwidth=1)
        self.telefono_entry.pack(fill="x", pady=(0, 15))
        
        if self.is_edit:
            self.nombre_entry.insert(0, self.producto.nombre)
            self.precio_entry.insert(0, str(self.producto.precio))
            self.cantidad_entry.insert(0, str(self.producto.cantidad))
            self.categoria_entry.insert(0, self.producto.categoria)
            self.proveedor_var.set(self.producto.proveedor.nombre)
            self.telefono_entry.insert(0, self.producto.proveedor.telefono)
            self.nombre_entry.config(state="readonly")
            self.categoria_entry.config(state="readonly")
        
        botones_frame = tk.Frame(main_frame, bg="#f0f0f0")
        botones_frame.pack(fill="x", pady=(20, 0))
        
        btn_guardar = tk.Button(
            botones_frame,
            text="✅ Guardar",
            command=self.guardar,
            font=("Arial", 11, "bold"),
            bg="#4CAF50",
            fg="white",
            relief="flat",
            padx=20,
            pady=10
        )
        btn_guardar.pack(side="left", padx=5)
        
        btn_cancelar = tk.Button(
            botones_frame,
            text="❌ Cancelar",
            command=self.root.destroy,
            font=("Arial", 11, "bold"),
            bg="#f44336",
            fg="white",
            relief="flat",
            padx=20,
            pady=10
        )
        btn_cancelar.pack(side="right", padx=5)
    
    def guardar(self):
        from producto import Producto
        from proveedor import Proveedor
        
        try:
            nombre = self.nombre_entry.get().strip()
            precio = float(self.precio_entry.get())
            cantidad = int(self.cantidad_entry.get())
            categoria = self.categoria_entry.get().strip()
            proveedor_nombre = self.proveedor_var.get().strip()
            telefono = self.telefono_entry.get().strip()
            
            if not all([nombre, precio > 0, cantidad >= 0, categoria, proveedor_nombre]):
                messagebox.showwarning("Advertencia", "Completa todos los campos correctamente")
                return
            
            proveedor = next((p for p in self.sistema.proveedores if p.nombre == proveedor_nombre), None)
            if not proveedor:
                proveedor = Proveedor(proveedor_nombre, telefono)
                self.sistema.agregar_proveedor(proveedor)
            
            if self.is_edit:
                self.producto.precio = precio
                self.producto.cantidad = cantidad
                self.sistema.guardar_inventario()
                messagebox.showinfo("Éxito", "Producto actualizado")
            else:
                nuevo = Producto(nombre, precio, cantidad, proveedor, categoria)
                self.sistema.agregar(nuevo)
                messagebox.showinfo("Éxito", "Producto agregado")
            
            if self.callback:
                self.callback()
            self.root.destroy()
        except ValueError:
            messagebox.showerror("Error", "Precio y cantidad deben ser números")


class GestionVentasWindow:
    def __init__(self, root, sistema):
        self.root = root
        self.sistema = sistema
        self.carrito = []
        self.total = 0
        
        self.root.title("Gestión de Ventas")
        self.root.geometry("1000x650")
        self.root.resizable(True, True)
        self.root.configure(bg="#f0f0f0")
        
        self.center_window()
        self.crear_interfaz()
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def crear_interfaz(self):
        titulo_frame = tk.Frame(self.root, bg="#4CAF50")
        titulo_frame.pack(fill="x", padx=0, pady=0)
        
        titulo = tk.Label(
            titulo_frame,
            text="💰 GESTIÓN DE VENTAS",
            font=("Arial", 18, "bold"),
            bg="#4CAF50",
            fg="white"
        )
        titulo.pack(pady=10)
        
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        izq_frame = tk.Frame(main_frame, bg="white", relief="solid", borderwidth=1)
        izq_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        tk.Label(izq_frame, text="Productos Disponibles", font=("Arial", 12, "bold"), bg="white").pack(fill="x", padx=10, pady=10)
        
        tabla_frame = tk.Frame(izq_frame, bg="white")
        tabla_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        
        columns = ("Producto", "Precio", "Stock")
        self.tabla_productos = ttk.Treeview(tabla_frame, columns=columns, height=15, show="headings")
        
        for col in columns:
            self.tabla_productos.heading(col, text=col)
            if col == "Producto":
                self.tabla_productos.column(col, width=200)
            else:
                self.tabla_productos.column(col, width=100)
        
        scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=self.tabla_productos.yview)
        self.tabla_productos.configure(yscroll=scrollbar.set)
        
        self.tabla_productos.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.actualizar_productos()
        
        der_frame = tk.Frame(main_frame, bg="white", relief="solid", borderwidth=1)
        der_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))
        
        tk.Label(der_frame, text="Carrito de Compras", font=("Arial", 12, "bold"), bg="white").pack(fill="x", padx=10, pady=10)
        
        carrito_frame = tk.Frame(der_frame, bg="white")
        carrito_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        
        cols_carrito = ("Producto", "Cantidad", "Subtotal")
        self.tabla_carrito = ttk.Treeview(carrito_frame, columns=cols_carrito, height=10, show="headings")
        
        for col in cols_carrito:
            self.tabla_carrito.heading(col, text=col)
            if col == "Producto":
                self.tabla_carrito.column(col, width=150)
            else:
                self.tabla_carrito.column(col, width=100)
        
        scrollbar_carrito = ttk.Scrollbar(carrito_frame, orient="vertical", command=self.tabla_carrito.yview)
        self.tabla_carrito.configure(yscroll=scrollbar_carrito.set)
        
        self.tabla_carrito.pack(side="left", fill="both", expand=True)
        scrollbar_carrito.pack(side="right", fill="y")
        
        info_frame = tk.Frame(der_frame, bg="#f0f0f0")
        info_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Label(info_frame, text="Cliente:", font=("Arial", 10), bg="#f0f0f0").pack(anchor="w")
        self.cliente_entry = tk.Entry(info_frame, font=("Arial", 10), width=30, relief="solid", borderwidth=1)
        self.cliente_entry.pack(fill="x", pady=(0, 10))
        
        tk.Label(info_frame, text="Nro. Factura:", font=("Arial", 10), bg="#f0f0f0").pack(anchor="w")
        self.factura_entry = tk.Entry(info_frame, font=("Arial", 10), width=30, relief="solid", borderwidth=1)
        self.factura_entry.pack(fill="x", pady=(0, 10))
        
        tk.Label(info_frame, text=f"TOTAL: ${self.total:,.2f}", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#4CAF50", name="total_label")
        tk.Label(info_frame, text=f"TOTAL: ${self.total:,.2f}", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#4CAF50").pack(anchor="e", pady=10)
        
        botones_venta_frame = tk.Frame(self.root, bg="#f0f0f0")
        botones_venta_frame.pack(fill="x", padx=20, pady=10)
        
        btn_agregar = tk.Button(
            botones_venta_frame,
            text="➕ Agregar al Carrito",
            command=self.agregar_al_carrito,
            font=("Arial", 10, "bold"),
            bg="#2196F3",
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        )
        btn_agregar.pack(side="left", padx=5)
        
        btn_eliminar = tk.Button(
            botones_venta_frame,
            text="🗑️ Eliminar del Carrito",
            command=self.eliminar_del_carrito,
            font=("Arial", 10, "bold"),
            bg="#FF9800",
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        )
        btn_eliminar.pack(side="left", padx=5)
        
        btn_finalizar = tk.Button(
            botones_venta_frame,
            text="✅ Finalizar Venta",
            command=self.finalizar_venta,
            font=("Arial", 10, "bold"),
            bg="#4CAF50",
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        )
        btn_finalizar.pack(side="right", padx=5)
        
        btn_limpiar = tk.Button(
            botones_venta_frame,
            text="🧹 Limpiar Carrito",
            command=self.limpiar_carrito,
            font=("Arial", 10, "bold"),
            bg="#f44336",
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        )
        btn_limpiar.pack(side="right", padx=5)
        
        btn_salir = tk.Button(
            botones_venta_frame,
            text="🚪 Salir",
            command=self.salir,
            font=("Arial", 10, "bold"),
            bg="#f44336",
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        )
        btn_salir.pack(side="right", padx=5)
        
        btn_volver = tk.Button(
            botones_venta_frame,
            text="⬅️ Volver",
            command=self.root.destroy,
            font=("Arial", 10, "bold"),
            bg="#757575",
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        )
        btn_volver.pack(side="right", padx=5)
    
    def salir(self):
        if messagebox.askyesno("Confirmar salida", "¿Estás seguro de que quieres salir de la aplicación?"):
            if hasattr(self.root, "master") and self.root.master:
                self.root.master.destroy()
            else:
                self.root.destroy()
    
    def actualizar_productos(self):
        for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)
        
        for categoria, productos in self.sistema.categorias.items():
            for producto in productos:
                if producto.cantidad > 0:
                    self.tabla_productos.insert("", "end", values=(
                        producto.nombre,
                        f"${producto.precio:,.0f}",
                        producto.cantidad
                    ))
    
    def agregar_al_carrito(self):
        seleccion = self.tabla_productos.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un producto")
            return
        
        item = seleccion[0]
        valores = self.tabla_productos.item(item, "values")
        nombre_producto = valores[0]
        
        producto = self.sistema.buscar_producto(nombre_producto)
        if not producto:
            messagebox.showerror("Error", "Producto no encontrado")
            return
        
        cantidad_window = tk.Toplevel(self.root)
        cantidad_window.title("Cantidad")
        cantidad_window.geometry("300x150")
        cantidad_window.resizable(False, False)
        
        tk.Label(cantidad_window, text=f"¿Cuántas unidades de {nombre_producto}?", font=("Arial", 10)).pack(pady=10)
        cantidad_entry = tk.Entry(cantidad_window, font=("Arial", 10), width=20)
        cantidad_entry.pack(pady=10)
        cantidad_entry.focus()
        
        def agregar():
            try:
                cantidad = int(cantidad_entry.get())
                if cantidad <= 0:
                    messagebox.showwarning("Advertencia", "Cantidad debe ser mayor a 0")
                    return
                if cantidad > producto.cantidad:
                    messagebox.showwarning("Advertencia", f"Stock insuficiente. Disponible: {producto.cantidad}")
                    return
                
                subtotal = producto.precio * cantidad
                self.carrito.append({
                    "producto": nombre_producto,
                    "cantidad": cantidad,
                    "subtotal": subtotal,
                    "precio_unitario": producto.precio
                })
                self.total += subtotal
                
                self.actualizar_carrito()
                cantidad_window.destroy()
                messagebox.showinfo("Éxito", f"{cantidad} {nombre_producto}(s) agregado al carrito")
            except ValueError:
                messagebox.showerror("Error", "Ingresa un número válido")
        
        btn = tk.Button(cantidad_window, text="Agregar", command=agregar, bg="#4CAF50", fg="white")
        btn.pack(pady=10)
    
    def actualizar_carrito(self):
        for item in self.tabla_carrito.get_children():
            self.tabla_carrito.delete(item)
        
        for item in self.carrito:
            self.tabla_carrito.insert("", "end", values=(
                item["producto"],
                item["cantidad"],
                f"${item['subtotal']:,.2f}"
            ))
        
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label) and "TOTAL" in widget.cget("text"):
                widget.config(text=f"TOTAL: ${self.total:,.2f}")
    
    def eliminar_del_carrito(self):
        seleccion = self.tabla_carrito.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un item del carrito")
            return
        
        item_idx = self.tabla_carrito.index(seleccion[0])
        self.total -= self.carrito[item_idx]["subtotal"]
        self.carrito.pop(item_idx)
        self.actualizar_carrito()
        messagebox.showinfo("Éxito", "Item eliminado del carrito")
    
    def limpiar_carrito(self):
        if messagebox.askyesno("Confirmar", "¿Limpiar todo el carrito?"):
            self.carrito = []
            self.total = 0
            self.actualizar_carrito()
    
    def finalizar_venta(self):
        if not self.carrito:
            messagebox.showwarning("Advertencia", "El carrito está vacío")
            return
        
        cliente = self.cliente_entry.get().strip()
        factura = self.factura_entry.get().strip()
        
        if not cliente or not factura:
            messagebox.showwarning("Advertencia", "Completa cliente y nro. factura")
            return
        
        from ventas import Venta
        
        nueva_venta = Venta(factura, cliente)
        
        for item in self.carrito:
            producto = self.sistema.buscar_producto(item["producto"])
            if producto:
                nueva_venta.agregar_al_carrito(producto, item["cantidad"])
        
        self.sistema.guardar_inventario()
        
        mensaje = f"\n📄 FACTURA NRO: {factura}\n"
        mensaje += f"👤 Cliente: {cliente}\n"
        mensaje += f"📅 Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n"
        mensaje += "─" * 40 + "\n"
        for item in self.carrito:
            mensaje += f"{item['producto']} x{item['cantidad']} → ${item['subtotal']:,.2f}\n"
        mensaje += "─" * 40 + "\n"
        mensaje += f"💵 TOTAL: ${self.total:,.2f}\n"
        
        messagebox.showinfo("Venta Exitosa", mensaje)
        
        self.carrito = []
        self.total = 0
        self.cliente_entry.delete(0, tk.END)
        self.factura_entry.delete(0, tk.END)
        self.actualizar_productos()
        self.actualizar_carrito()


class ProveedorWindow:
    def __init__(self, root, sistema):
        self.root = root
        self.sistema = sistema
        
        self.root.title("Gestión de Proveedores")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.configure(bg="#f0f0f0")
        
        self.center_window()
        self.crear_interfaz()
        self.actualizar_tabla()
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def crear_interfaz(self):
        titulo_frame = tk.Frame(self.root, bg="#FF9800")
        titulo_frame.pack(fill="x", padx=0, pady=0)
        
        titulo = tk.Label(
            titulo_frame,
            text="🏭 GESTIÓN DE PROVEEDORES",
            font=("Arial", 18, "bold"),
            bg="#FF9800",
            fg="white"
        )
        titulo.pack(pady=10)
        
        botones_frame = tk.Frame(self.root, bg="#f0f0f0")
        botones_frame.pack(fill="x", padx=20, pady=10)
        
        btn_agregar = tk.Button(
            botones_frame,
            text="➕ Agregar Proveedor",
            command=self.agregar_proveedor,
            font=("Arial", 10, "bold"),
            bg="#4CAF50",
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        )
        btn_agregar.pack(side="left", padx=5)
        
        btn_eliminar = tk.Button(
            botones_frame,
            text="🗑️ Eliminar",
            command=self.eliminar_proveedor,
            font=("Arial", 10, "bold"),
            bg="#f44336",
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        )
        btn_eliminar.pack(side="left", padx=5)
        
        btn_salir = tk.Button(
            botones_frame,
            text="🚪 Salir",
            command=self.salir,
            font=("Arial", 10, "bold"),
            bg="#f44336",
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        )
        btn_salir.pack(side="right", padx=5)
        
        btn_volver = tk.Button(
            botones_frame,
            text="⬅️ Volver",
            command=self.root.destroy,
            font=("Arial", 10, "bold"),
            bg="#757575",
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        )
        btn_volver.pack(side="right", padx=5)
        
        tabla_frame = tk.Frame(self.root, bg="white")
        tabla_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        columns = ("Nombre", "Teléfono")
        self.tabla = ttk.Treeview(tabla_frame, columns=columns, height=20, show="headings")
        
        for col in columns:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=300)
        
        scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        
        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def salir(self):
        if messagebox.askyesno("Confirmar salida", "¿Estás seguro de que quieres salir de la aplicación?"):
            if hasattr(self.root, "master") and self.root.master:
                self.root.master.destroy()
            else:
                self.root.destroy()
    
    def actualizar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        for proveedor in self.sistema.proveedores:
            self.tabla.insert("", "end", values=(
                proveedor.nombre,
                proveedor.telefono
            ))
    
    def agregar_proveedor(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar Proveedor")
        ventana.geometry("400x250")
        ventana.resizable(False, False)
        
        tk.Label(ventana, text="Nombre:", font=("Arial", 10)).pack(anchor="w", padx=20, pady=(20, 5))
        nombre_entry = tk.Entry(ventana, font=("Arial", 10), width=30)
        nombre_entry.pack(padx=20, fill="x")
        
        tk.Label(ventana, text="Teléfono:", font=("Arial", 10)).pack(anchor="w", padx=20, pady=(20, 5))
        vcmd = (ventana.register(lambda P: P.isdigit() or P == ""), '%S')
        telefono_entry = tk.Entry(ventana, font=("Arial", 10), width=30, validate='key', validatecommand=vcmd)
        telefono_entry.pack(padx=20, fill="x")
        
        def guardar():
            from proveedor import Proveedor
            
            nombre = nombre_entry.get().strip()
            telefono = telefono_entry.get().strip()
            
            if not nombre or not telefono:
                messagebox.showwarning("Advertencia", "Completa todos los campos")
                return
            
            if any(p.nombre.lower() == nombre.lower() for p in self.sistema.proveedores):
                messagebox.showwarning("Advertencia", "El proveedor ya existe")
                return
            
            nuevo = Proveedor(nombre, telefono)
            self.sistema.agregar_proveedor(nuevo)
            self.actualizar_tabla()
            messagebox.showinfo("Éxito", "Proveedor agregado")
            ventana.destroy()
        
        btn_frame = tk.Frame(ventana)
        btn_frame.pack(fill="x", padx=20, pady=(30, 20))
        
        tk.Button(btn_frame, text="✅ Guardar", command=guardar, bg="#4CAF50", fg="white", relief="flat", padx=20, pady=8).pack(side="left", padx=5)
        tk.Button(btn_frame, text="❌ Cancelar", command=ventana.destroy, bg="#f44336", fg="white", relief="flat", padx=20, pady=8).pack(side="right", padx=5)
    
    def eliminar_proveedor(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un proveedor")
            return
        
        item = seleccion[0]
        valores = self.tabla.item(item, "values")
        nombre = valores[0]
        
        if messagebox.askyesno("Confirmar", f"¿Eliminar proveedor '{nombre}'?"):
            self.sistema.proveedores = [p for p in self.sistema.proveedores if p.nombre != nombre]
            self.actualizar_tabla()
            messagebox.showinfo("Éxito", "Proveedor eliminado")


class UsuariosWindow:
    def __init__(self, root):
        self.root = root
        self.archivo_usuarios = log
        
        self.root.title("Gestión de Usuarios")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.configure(bg="#f0f0f0")
        
        self.center_window()
        self.crear_interfaz()
        self.actualizar_tabla()
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def crear_interfaz(self):
        titulo_frame = tk.Frame(self.root, bg="#9C27B0")
        titulo_frame.pack(fill="x", padx=0, pady=0)
        
        titulo = tk.Label(
            titulo_frame,
            text="👥 GESTIÓN DE USUARIOS",
            font=("Arial", 18, "bold"),
            bg="#9C27B0",
            fg="white"
        )
        titulo.pack(pady=10)
        
        botones_frame = tk.Frame(self.root, bg="#f0f0f0")
        botones_frame.pack(fill="x", padx=20, pady=10)
        
        btn_agregar = tk.Button(
            botones_frame,
            text="➕ Agregar Usuario",
            command=self.agregar_usuario,
            font=("Arial", 10, "bold"),
            bg="#4CAF50",
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        )
        btn_agregar.pack(side="left", padx=5)
        
        btn_editar = tk.Button(
            botones_frame,
            text="✏️ Editar Contraseña",
            command=self.editar_usuario,
            font=("Arial", 10, "bold"),
            bg="#FFC107",
            fg="black",
            relief="flat",
            padx=15,
            pady=8
        )
        btn_editar.pack(side="left", padx=5)
        
        btn_eliminar = tk.Button(
            botones_frame,
            text="🗑️ Eliminar",
            command=self.eliminar_usuario,
            font=("Arial", 10, "bold"),
            bg="#f44336",
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        )
        btn_eliminar.pack(side="left", padx=5)
        
        btn_salir = tk.Button(
            botones_frame,
            text="🚪 Salir",
            command=self.salir,
            font=("Arial", 10, "bold"),
            bg="#f44336",
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        )
        btn_salir.pack(side="right", padx=5)
        
        btn_volver = tk.Button(
            botones_frame,
            text="⬅️ Volver",
            command=self.root.destroy,
            font=("Arial", 10, "bold"),
            bg="#757575",
            fg="white",
            relief="flat",
            padx=15,
            pady=8
        )
        btn_volver.pack(side="right", padx=5)
        
        tabla_frame = tk.Frame(self.root, bg="white")
        tabla_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        columns = ("Usuario", "Rol")
        self.tabla = ttk.Treeview(tabla_frame, columns=columns, height=20, show="headings")
        
        for col in columns:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=300)
        
        scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        
        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def salir(self):
        if messagebox.askyesno("Confirmar salida", "¿Estás seguro de que quieres salir de la aplicación?"):
            if hasattr(self.root, "master") and self.root.master:
                self.root.master.destroy()
            else:
                self.root.destroy()
    
    def actualizar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        try:
            with open(self.archivo_usuarios, "r", encoding="utf-8") as f:
                usuarios = json.load(f)
            
            for usuario, datos in usuarios.items():
                rol = datos.get("rol", "usuario") if isinstance(datos, dict) else "usuario"
                self.tabla.insert("", "end", values=(usuario, rol))
        except:
            pass
    
    def agregar_usuario(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar Usuario")
        ventana.geometry("400x350")
        ventana.resizable(False, False)
        
        tk.Label(ventana, text="Usuario:", font=("Arial", 10)).pack(anchor="w", padx=20, pady=(20, 5))
        usuario_entry = tk.Entry(ventana, font=("Arial", 10), width=30)
        usuario_entry.pack(padx=20, fill="x")
        
        tk.Label(ventana, text="Contraseña:", font=("Arial", 10)).pack(anchor="w", padx=20, pady=(20, 5))
        contraseña_entry = tk.Entry(ventana, font=("Arial", 10), width=30, show="*")
        contraseña_entry.pack(padx=20, fill="x")
        
        tk.Label(ventana, text="Rol:", font=("Arial", 10)).pack(anchor="w", padx=20, pady=(20, 5))
        rol_var = tk.StringVar(value="empleado")
        rol_combo = ttk.Combobox(ventana, textvariable=rol_var, values=["admin", "empleado"], state="readonly", width=27)
        rol_combo.pack(padx=20, fill="x")
        
        def guardar():
            usuario = usuario_entry.get().strip()
            contraseña = contraseña_entry.get()
            rol = rol_var.get()
            
            if not usuario or not contraseña:
                messagebox.showwarning("Advertencia", "Completa todos los campos")
                return
            
            try:
                with open(self.archivo_usuarios, "r", encoding="utf-8") as f:
                    usuarios = json.load(f)
                
                if usuario in usuarios:
                    messagebox.showwarning("Advertencia", "El usuario ya existe")
                    return
                
                usuarios[usuario] = {"contrasena": contraseña, "rol": rol}
                
                with open(self.archivo_usuarios, "w", encoding="utf-8") as f:
                    json.dump(usuarios, f, indent=2)
                
                self.actualizar_tabla()
                messagebox.showinfo("Éxito", "Usuario agregado")
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")
        
        btn_frame = tk.Frame(ventana)
        btn_frame.pack(fill="x", padx=20, pady=(30, 20))
        
        tk.Button(btn_frame, text="✅ Guardar", command=guardar, bg="#4CAF50", fg="white", relief="flat", padx=20, pady=8).pack(side="left", padx=5)
        tk.Button(btn_frame, text="❌ Cancelar", command=ventana.destroy, bg="#f44336", fg="white", relief="flat", padx=20, pady=8).pack(side="right", padx=5)
    
    def editar_usuario(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un usuario")
            return
        
        item = seleccion[0]
        valores = self.tabla.item(item, "values")
        usuario = valores[0]
        
        ventana = tk.Toplevel(self.root)
        ventana.title(f"Editar {usuario}")
        ventana.geometry("400x250")
        ventana.resizable(False, False)
        
        tk.Label(ventana, text="Nueva Contraseña:", font=("Arial", 10)).pack(anchor="w", padx=20, pady=(20, 5))
        contraseña_entry = tk.Entry(ventana, font=("Arial", 10), width=30, show="*")
        contraseña_entry.pack(padx=20, fill="x")
        
        def guardar():
            contraseña = contraseña_entry.get()
            
            if not contraseña:
                messagebox.showwarning("Advertencia", "Ingresa una contraseña")
                return
            
            try:
                with open(self.archivo_usuarios, "r", encoding="utf-8") as f:
                    usuarios = json.load(f)
                
                if usuario in usuarios:
                    if isinstance(usuarios[usuario], dict):
                        usuarios[usuario]["contrasena"] = contraseña
                    else:
                        usuarios[usuario] = {"contrasena": contraseña, "rol": "usuario"}
                    
                    with open(self.archivo_usuarios, "w", encoding="utf-8") as f:
                        json.dump(usuarios, f, indent=2)
                    
                    messagebox.showinfo("Éxito", "Contraseña actualizada")
                    ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")
        
        btn_frame = tk.Frame(ventana)
        btn_frame.pack(fill="x", padx=20, pady=(30, 20))
        
        tk.Button(btn_frame, text="✅ Guardar", command=guardar, bg="#4CAF50", fg="white", relief="flat", padx=20, pady=8).pack(side="left", padx=5)
        tk.Button(btn_frame, text="❌ Cancelar", command=ventana.destroy, bg="#f44336", fg="white", relief="flat", padx=20, pady=8).pack(side="right", padx=5)
    
    def eliminar_usuario(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un usuario")
            return
        
        item = seleccion[0]
        valores = self.tabla.item(item, "values")
        usuario = valores[0]
        
        if usuario == "admin":
            messagebox.showwarning("Advertencia", "No puedes eliminar el usuario admin")
            return
        
        if messagebox.askyesno("Confirmar", f"¿Eliminar usuario '{usuario}'?"):
            try:
                with open(self.archivo_usuarios, "r", encoding="utf-8") as f:
                    usuarios = json.load(f)
                
                if usuario in usuarios:
                    del usuarios[usuario]
                    
                    with open(self.archivo_usuarios, "w", encoding="utf-8") as f:
                        json.dump(usuarios, f, indent=2)
                    
                    self.actualizar_tabla()
                    messagebox.showinfo("Éxito", "Usuario eliminado")
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")
