import os
from datetime import datetime
import random
from getpass import getpass

# Constantes
MAX_ESTUDIANTES = 8
MAX_PROFESORES = 4
MATERIAS = ["Matemática", "Lengua", "Programación", "Geografía"]

# Variables globales
cont_est = 0
cont_prof = 0
id_est = None
id_prof = None

matriz_estudiantes = [["" for _ in range(8)] for _ in range(MAX_ESTUDIANTES)]
matriz_likes = [[0 for _ in range(MAX_ESTUDIANTES)] for _ in range(MAX_ESTUDIANTES)]
matriz_posi = [0 for _ in range(MAX_ESTUDIANTES)]
matriz_notas = [[-1 for _ in MATERIAS] for _ in range(MAX_ESTUDIANTES)]
matriz_profesores = [["" for _ in range(3)] for _ in range(MAX_PROFESORES)]

# Funciones auxiliares
def calcular_edad(fecha_nacimiento):
    hoy = datetime.now()
    return hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

def buscar_email(matriz, correo, max_elementos):
    for i in range(max_elementos):
        if matriz[i][1] == correo:
            return i
    return -1

def buscar_nombre(matriz, nombre, max_elementos):
    for i in range(max_elementos):
        if matriz[i][0].lower() == nombre.lower():
            return i
    return -1

def pausar_mensaje(mensaje):
    print(mensaje)
    input("Presione Enter para continuar")

# Registro
def registrarse():
    global cont_est, cont_prof
    continuar = True
    while continuar:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Tipo de cuenta a registrar:")
        print("1. Estudiante")
        print("2. Profesor")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if cont_est < MAX_ESTUDIANTES:
                nombre = input("Nombre: ")
                correo = input("Correo: ")
                contraseña = input("Contraseña: ")
                fecha_str = input("Fecha de nacimiento (YYYY-MM-DD): ")
                fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
                edad = calcular_edad(fecha)
                biografia = input("Biografía: ")
                hobbies = input("Hobbies: ")
                matriz_estudiantes[cont_est] = [nombre, correo, contraseña, fecha, edad, biografia, hobbies, "ACTIVO"]
                cont_est += 1
                pausar_mensaje("Estudiante registrado exitosamente")
            else:
                pausar_mensaje("Límite de estudiantes alcanzado")

        elif opcion == "2":
            if cont_prof < MAX_PROFESORES:
                nombre = input("Nombre del profesor: ")
                correo = input("Correo: ")
                contraseña = input("Contraseña: ")
                matriz_profesores[cont_prof] = [nombre, correo, contraseña]
                cont_prof += 1
                pausar_mensaje("Profesor registrado exitosamente")
            else:
                pausar_mensaje("Límite de profesores alcanzado")

        elif opcion == "0":
            continuar = False

        else:
            pausar_mensaje("Opción inválida")
def menu_principal_est():
    global id_est
    continuar = True
    while continuar:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Menú Principal - Estudiante: {matriz_estudiantes[id_est][0]}")
        print("1. Ver perfil")
        print("2. Editar perfil")
        print("3. Dar like")
        print("4. Ver top popularidad")
        print("0. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            estudiante = matriz_estudiantes[id_est]
            print("Nombre:", estudiante[0])
            print("Correo:", estudiante[1])
            print("Fecha de nacimiento:", estudiante[3].strftime("%Y-%m-%d"))
            print("Edad:", estudiante[4])
            print("Biografía:", estudiante[5])
            print("Hobbies:", estudiante[6])
            print("Estado:", estudiante[7])
            print("Likes recibidos:", matriz_posi[id_est])
            input("Presione Enter para continuar")

        elif opcion == "2":
            print("Editar perfil:")
            matriz_estudiantes[id_est][5] = input("Nueva biografía: ")
            matriz_estudiantes[id_est][6] = input("Nuevos hobbies: ")
            pausar_mensaje("Perfil actualizado.")

        elif opcion == "3":
            print("Lista de estudiantes para dar like:")
            for i in range(cont_est):
                if i != id_est and matriz_estudiantes[i][7] == "ACTIVO":
                    print(f"{i}) {matriz_estudiantes[i][0]}")
            idx = int(input("Ingrese el índice del estudiante que desea likear: "))
            if 0 <= idx < cont_est and idx != id_est and matriz_estudiantes[idx][7] == "ACTIVO":
                matriz_likes[id_est][idx] += 1
                matriz_posi[idx] += 1
                pausar_mensaje("Like enviado exitosamente.")
            else:
                pausar_mensaje("Índice inválido o no se puede likear a uno mismo o a cuentas inactivas.")

        elif opcion == "4":
            ranking = sorted([(matriz_estudiantes[i][0], matriz_posi[i]) for i in range(cont_est)], key=lambda x: x[1], reverse=True)
            print("Top de popularidad:")
            for i, (nombre, likes) in enumerate(ranking):
                print(f"{i+1}. {nombre} - Likes: {likes}")
            input("Presione Enter para continuar")

        elif opcion == "0":
            continuar = False

        else:
            pausar_mensaje("Opción inválida")

# Menú profesor
def menu_profesor():
    continuar = True
    while continuar:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Menú Profesor")
        print("1. Activar/Desactivar cuentas")
        print("2. Cargar notas")
        print("3. Buscar estudiante y ver notas")
        print("0. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for i in range(cont_est):
                print(f"{i}) {matriz_estudiantes[i][0]} - Estado: {matriz_estudiantes[i][7]}")
            idx = int(input("Ingrese el índice del estudiante a modificar: "))
            if 0 <= idx < cont_est:
                estado_actual = matriz_estudiantes[idx][7]
                nuevo_estado = "INACTIVO" if estado_actual == "ACTIVO" else "ACTIVO"
                matriz_estudiantes[idx][7] = nuevo_estado
                pausar_mensaje(f"Cuenta actualizada a: {nuevo_estado}")
            else:
                pausar_mensaje("Índice inválido")

        elif opcion == "2":
            for i in range(cont_est):
                print(f"{i}) {matriz_estudiantes[i][0]}")
            idx = int(input("Ingrese el índice del estudiante: "))
            if 0 <= idx < cont_est:
                for j, materia in enumerate(MATERIAS):
                    nota = int(input(f"Nota en {materia} (0-10): "))
                    matriz_notas[idx][j] = nota
                pausar_mensaje("Notas actualizadas")
            else:
                pausar_mensaje("Índice inválido")

        elif opcion == "3":
            nombre = input("Nombre del estudiante: ")
            idx = buscar_nombre(matriz_estudiantes, nombre, cont_est)
            if idx != -1:
                print(f"Notas de {matriz_estudiantes[idx][0]}:")
                for j, materia in enumerate(MATERIAS):
                    nota = matriz_notas[idx][j]
                    nota_str = str(nota) if nota != -1 else "Sin nota"
                    print(f"{materia}: {nota_str}")
            else:
                pausar_mensaje("Estudiante no encontrado")
            input("Presione Enter para continuar")

        elif opcion == "0":
            continuar = False

        else:
            pausar_mensaje("Opción inválida")

# Menú inicial
continuar = True
while continuar:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Bienvenido al sistema")
    print("1. Registrarse")
    print("2. Iniciar sesión como estudiante")
    print("3. Iniciar como profesor")
    print("4. Cargar estudiantes (modo debug)")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "0":
        continuar = False

    elif opcion == "1":
        registrarse()

    elif opcion == "2":
        if cont_est == 0:
            pausar_mensaje("No hay estudiantes registrados. Registre al menos uno para iniciar sesión.")
        else:
            correo = input("Correo: ")
            contraseña = getpass("Contraseña: ")
            id_est = buscar_email(matriz_estudiantes, correo, MAX_ESTUDIANTES)
            if id_est != -1 and matriz_estudiantes[id_est][2] == contraseña and matriz_estudiantes[id_est][7] == "ACTIVO":
                print(f"Bienvenido {matriz_estudiantes[id_est][0]}")
                input("Presione Enter para continuar")
                menu_principal_est()
            else:
                pausar_mensaje("Credenciales incorrectas o cuenta inactiva")

    elif opcion == "3":
        correo = input("Correo profesor: ")
        contraseña = getpass("Contraseña: ")
        id_prof = buscar_email(matriz_profesores, correo, cont_prof)
        if id_prof != -1 and matriz_profesores[id_prof][2] == contraseña:
            print(f"Bienvenido profesor {matriz_profesores[id_prof][0]}")
            input("Presione Enter para continuar")
            menu_profesor()
        else:
            pausar_mensaje("Credenciales incorrectas")

    elif opcion == "4":
        if cont_est + 4 <= MAX_ESTUDIANTES:
            nombres_debug = ["Ana", "Luis", "Marta", "Carlos"]
            for i in range(4):
                matriz_estudiantes[cont_est] = [
                    nombres_debug[i],
                    f"{nombres_debug[i].lower()}@mail.com",
                    "1234",
                    datetime(2000+i, 1, 1),
                    2025 - (2000+i),
                    "Bio de prueba",
                    "leer, juegos",
                    "ACTIVO"
                ]
                cont_est += 1
            pausar_mensaje("Estudiantes cargados en modo debug")
        else:
            pausar_mensaje("No hay espacio suficiente para cargar más estudiantes en modo debug")

    else:
        pausar_mensaje("Opción inválida")