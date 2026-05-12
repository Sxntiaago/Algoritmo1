import csv
import json
import os
from datetime import datetime
from pathlib import Path
#from main import 
log = Path(r"C:\Users\saaraujoa.CUC\OneDrive - Universidad de la Costa - CUC\Uni\Algoritmo 1\Rubrica\usuarios.json")

def login():
    Lg = False
    if not log.exists():
        print("Creando archivo")

        with open(log, "w" , encoding="utf-8") as f:
            json.dump({}, f)

    with open(log, "r", encoding="utf-8") as f:
        usuarios = json.load(f)

    print("Registro")

    #user = input("usuario: ").strip()
    #password = input("contraseña: ").strip()

    #if user in usuarios:
        #print("username ocupado")
    #else:
        #usuarios[user] = password
        #with open(log, "w", encoding="utf-8") as f:
            #json.dump(usuarios, f , indent=4)
        
        #print("Usuario creado")


    user_login = input("usuario: ").strip()
    password_login = input ("contraseña: ").strip()

    if user_login in usuarios and[user_login] == password_login:
        print("Bienvenido")
    else:
        print("Datos incorrectos")