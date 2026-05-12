import tkinter as tk
from tkinter import messagebox

class MainMenuWindow:
    def __init__(self, root, sistema):
        self.root = root
        self.sistema = sistema
        self.root.title("Sistema de Gestión de Inventario - Menú Principal")
        self.root.geometry("500x400")
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
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Título
        titulo = tk.Label(
            main_frame,
            text="MENÚ PRINCIPAL",
            font=("Arial", 20, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        titulo.pack(pady=(0, 10))

        subtitulo = tk.Label(
            main_frame,
            text="Selecciona una opción",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#666666"
        )
        subtitulo.pack(pady=(0, 30))

        # Frame para botones
        botones_frame = tk.Frame(main_frame, bg="#f0f0f0")
        botones_frame.pack(fill="both", expand=True)

        # Botón Gestión Inventario
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
            pady=15,
            width=25
        )
        btn_inventario.pack(pady=(10, 15))

        # Botón Gestión Ventas
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
            pady=15,
            width=25
        )
        btn_ventas.pack(pady=(10, 15))

        # Botón Salir
        btn_salir = tk.Button(
            botones_frame,
            text="🚪 Salir",
            command=self.salir,
            font=("Arial", 12, "bold"),
            bg="#f44336",
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=15,
            width=25
        )
        btn_salir.pack(pady=(10, 15))

    def abrir_gestion_inventario(self):
        from gestion_inventario import menu_Inventario
        # Cerrar menú principal temporalmente
        self.root.withdraw()
        try:
            # Ejecutar gestión de inventario (esto podría abrir su propia interfaz)
            menu_Inventario()
        finally:
            # Mostrar menú principal nuevamente
            self.root.deiconify()

    def abrir_gestion_ventas(self):
        from gestion_ventas import menu_Ventas
        # Cerrar menú principal temporalmente
        self.root.withdraw()
        try:
            # Ejecutar gestión de ventas
            menu_Ventas(self.sistema)
        finally:
            # Mostrar menú principal nuevamente
            self.root.deiconify()

    def salir(self):
        if messagebox.askyesno("Confirmar salida", "¿Estás seguro de que quieres salir?"):
            self.root.quit()