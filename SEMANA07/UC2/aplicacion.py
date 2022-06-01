# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 11:42:14 2022

@author: Edgar Cusi
"""

import gestion_archivos

def menu():
    print("***********MENÚ PRINCIPAL***********")
    print("1. Crear Archivo")
    print("2. Eliminar Archivo") 
    print("3. Agregar Contenido")
    print("4. Mostrar Contenido de archivo")
    print("5. Salir")
    
    
def crear():
    print("**Crear Archivo**")
    archivo = input( "Crear Archivo: ")
    contenido = input( "Contenido del archivo: ")
    gestion_archivos.crear_archivo(archivo, contenido)

def eliminar():
    print( "**Eliminar Archivo**")
    archivo = input( "Quiero eliminar el archivo: ")
    gestion_archivos.eliminar_archivo(archivo)
    
def agregar():
    print("**Agregar Contenido a un Archivo**")
    archivo = input("Quiero aegrar contenido al archivo: ")
    contenido = input( "El contenido adicional del archivo será: ")
    gestion_archivos.agregar_contenido_archivo(archivo, contenido)
    
def listar():
    print( "**Mostrar contenido de un archivo**")
    archivo = input("Quiero mostrar el contenido del archivo: ")
    print(gestion_archivos.leer_archivo(archivo))

def salir():
    print("Gracias por su visita, vuelva pronto")

def error():
    print("Opción Incorrecta >:v")


opcion = 1
while opcion!=5:
    menu()
    opcion = int(input("Selecciones una opcion[1-5]: "))
    
    if opcion==1:
        crear()
    elif opcion==2:
        eliminar()
    elif opcion==3:
        agregar()
    elif opcion==4:
        listar()    
    elif opcion==5:
        salir()
    else:
        error()
        
        