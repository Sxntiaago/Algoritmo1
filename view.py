import tkinter as tk
from tkinter import messagebox
import json
from pathlib import Path

log = Path(r"C:\Users\santy\OneDrive\Escritorio\Algoritmo1\usuarios.json")


if not log.exists():
    with open(log, "w", encoding="utf-8") as f:
        json.dump({"admin": "admin123"}, f)


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
        
        # Botón Login
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
            
            if usuario in usuarios and usuarios[usuario].get("contrasena") == password:
                messagebox.showinfo("Éxito", f"¡Bienvenido {usuario}!")
                self.root.destroy()
                # Abrir menú principal después del login exitoso
                self.abrir_menu_principal()
                return True
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")
                self.password_entry.delete(0, tk.END)
                self.usuario_entry.focus()
        except Exception as e:
            messagebox.showerror("Error", f"Error al verificar credenciales: {str(e)}")
    
    def abrir_menu_principal(self):
        from menu_view import MainMenuWindow
        from inventario import Inventario
        from producto import Producto
        from proveedor import Proveedor
        
        # Crear instancia del sistema
        sistema = Inventario()
        prov_general = Proveedor("Distribuidora Central", "555-0123")
        sistema.agregar(Producto("Arroz", 3500.0, 50, prov_general, "Alimentos"))
        sistema.agregar(Producto("Leche", 4200.0, 20, prov_general, "Lácteos"))
        
        # Abrir ventana del menú principal
        menu_root = tk.Tk()
        MainMenuWindow(menu_root, sistema)
        menu_root.mainloop()


root = tk.Tk()
LoginWindow(root)
root.mainloop()
