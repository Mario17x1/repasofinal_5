import os
import time
import numpy as np
import funciones_medicas as fm
# -----------variables----------
opcion = ""  # selecion del usuario
tamaño = 2   # Cantidad maxima de pacientes
rut = ""  # rut del paciente
arr_ruts = np.empty(tamaño, dtype=object)
nombre = ""  # nombre del paciente
arr_nombres = np.empty(tamaño, dtype=object)
edad = 0  # edad del paciente
arr_edades = np.empty(tamaño, dtype=int)
# ------------codigo principal---------

while True:
    os.system("cls")
    opcion = str(input('''
    ------------MENU-------------      
    1.- Ingresar Datos
    2.- Buscar paciente
    3.- Imprimir Ficha Medica
    4.- Salir      
    \nElija opcion: '''))

    if opcion == "1":
        os.system("cls")
        for k in range(tamaño):
            rut = str(input("Ingrese rut: ")).strip().upper()
            while not (fm.validar_rut(rut)):
                print("Error, no puede ser vacio")
                rut = str(input("Ingrese rut: ")).strip().upper()
            arr_ruts[k] = rut.strip().upper()

            nombre = str(input("Ingrese nombre:")).strip()
            while not (fm.validar_nombre(nombre)):
                print("Error, no puede ser vacio")
                nombre = str(input("Ingrese nombre:")).strip()
            arr_nombres[k] = nombre.strip()

            edad = int(input("Ingrese edad:"))
            while not (fm.validar_edad(edad)):
                print("Error, maryor o igual a 0")
                edad = int(input("Ingrese edad:"))
            arr_edades[k] = edad

            fm.imprimir_ficha_medica(rut, nombre, edad)

        os.system("pause")
    if opcion == "2":
        os.system("cls")
        print("\n----buscar paciente por RUT---")
        rut = str("Ingrese rut: ").strip().upper()
        if rut in arr_ruts:
            for k in range(tamaño):
                if rut == arr_ruts[k]:
                    posicion=k
            fm.imprimir_ficha_medica(arr_ruts[k],arr_nombres[k],arr_edades[k])        
        else:
            print("No esta!!!")

        os.system("pause")
    if opcion == "3":
        os.system("cls")

        os.system("pause")
    if opcion == "4":
        os.system("cls")

        os.system("pause")
