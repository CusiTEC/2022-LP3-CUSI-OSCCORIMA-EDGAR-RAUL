# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:47:49 2022

@author: usuario
"""

archivo=open("archivo_de_prueba.txt","wt")
contenido = "Linea1 hola amigos ¿Como estan?\nLinea2 Bienvenidos a la UNTELS"
archivo.write(contenido)
archivo.close()