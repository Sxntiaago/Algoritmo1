import csv
import json
import os
from datetime import datetime
from pathlib import Path
log = Path(r"C:\Users\santy\OneDrive\Escritorio\Algoritmo1\usuarios.json")



if not log.exists():
    print("Creando archivo")

    with open(log, "w" , encoding="utf-8") as f:
        json.dump({}, f)

with open(log, "r", encoding="utf-8") as f:
    usuarios = json.load(f)
def login():
        while True:
            print("\nLogin")

            user_login = input("usuario: ").strip()
            password_login = input("contraseña: ").strip()

            if user_login in usuarios and usuarios[user_login].get("contrasena") == password_login:
                print("Bienvenido")
                return True
            else:
                print("Datos incorrectos")
def registrar():
    print("Registro")

    user = input("usuario: ").strip()
    password = input("contraseña: ").strip()
    password_confirm = input("Confirme su contraseña: ").strip()

    if user in usuarios:
        print("username ocupado")
    elif password != password_confirm:
        print("Las contraseñas no coinciden")
    else:
        usuarios[user] = {"user": user, "contrasena": password, "rol": "empleado"}
        with open(log, "w", encoding="utf-8") as f:
            json.dump(usuarios, f, indent=4)
        print("Usuario creado")