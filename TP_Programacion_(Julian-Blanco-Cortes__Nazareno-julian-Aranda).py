


### Código completo corregido y limpio

import os
from datetime import datetime
import random
from getpass import getpass

# Variables globales
intentos = 3
cont_est = 0
cont_mod = 0
id_est = None
id_mod = None

matriz_estudiantes = [["" for _ in range(8)] for _ in range(8)]
matriz_likes = [[0 for _ in range(8)] for _ in range(8)]
matriz_posi = [0 for _ in range(8)]

# Funciones auxiliares
def calcular_edad(fecha_nacimiento):
    hoy = datetime.now()
    return hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

def buscar_array(matriz, dato, max_elementos, max_columnas):
    for i in range(max_elementos):
        for j in range(max_columnas):
            if matriz[i][j] == dato:
                return i
    return -1

# Menús y funciones principales
def menu_principal_est():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Menú principal estudiante:\n")
        print("1. Gestionar mi perfil")
        print("2. Gestionar candidatos")
        print("3. Reportes estadísticos")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "0":
            break
        elif opcion == "1":
            editar_mi_perfil()
        elif opcion == "2":
            gestionar_candidatos()
        elif opcion == "3":
            reportes_estadisticos()
        else:
            print("Opción inválida")
            input("Presione Enter para continuar")

def editar_mi_perfil():
    global id_est
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Editar perfil:\n")
        print("1. Nombre")
        print("2. Fecha de nacimiento")
        print("3. Biografía")
        print("4. Hobbies")
        print("0. Volver")
        opcion = input("Seleccione el campo a editar: ")
        if opcion == "0":
            break
        elif opcion == "1":
            matriz_estudiantes[id_est][0] = input("Nuevo nombre: ")
        elif opcion == "2":
            fecha = input("Nueva fecha (YYYY-MM-DD): ")
            matriz_estudiantes[id_est][3] = datetime.strptime(fecha, "%Y-%m-%d")
            matriz_estudiantes[id_est][4] = calcular_edad(matriz_estudiantes[id_est][3])
        elif opcion == "3":
            matriz_estudiantes[id_est][5] = input("Nueva biografía: ")
        elif opcion == "4":
            matriz_estudiantes[id_est][6] = input("Nuevos hobbies (separados por coma): ")
        else:
            print("Opción inválida")
            input("Presione Enter para continuar")

def gestionar_candidatos():
    global id_est
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(cont_est):
        if matriz_estudiantes[i][7] == "ACTIVO":
            print(f"{i}) {matriz_estudiantes[i][0]} - Estado: {matriz_estudiantes[i][7]}")
    me_gusta = input("Ingrese el nombre del estudiante que le gusta: ")
    id_target = buscar_array(matriz_estudiantes, me_gusta, 8, 8)
    if id_target != -1:
        matriz_likes[id_est][id_target] = 1
        if matriz_likes[id_target][id_est] == 1:
            print(f"¡Match con {me_gusta}!")
        else:
            print(f"Like enviado a {me_gusta}")
    else:
        print("No se encontró ese estudiante")
    input("Presione Enter para continuar")

def reportes_estadisticos():
    global id_est
    matches = likes_dados = likes_recibidos = 0
    for i in range(cont_est):
        if i != id_est:
            if matriz_likes[id_est][i] == 1 and matriz_likes[i][id_est] == 1:
                matches += 1
            elif matriz_likes[id_est][i] == 1:
                likes_dados += 1
            elif matriz_likes[i][id_est] == 1:
                likes_recibidos += 1
    total = cont_est - 1 if cont_est > 1 else 1
    print(f"Porcentaje de matches: {matches / total * 100:.2f}%")
    print(f"Likes dados y no recibidos: {likes_dados}")
    print(f"Likes recibidos no respondidos: {likes_recibidos}")
    input("Presione Enter para continuar")

