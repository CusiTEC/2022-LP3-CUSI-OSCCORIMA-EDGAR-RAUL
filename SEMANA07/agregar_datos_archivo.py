# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:57:45 2022

@author: usuario
"""

archivo = open("noticia.txt", "at")
#\n para agregar el contenido en una línea final
contenido = "\nFuente: RPP"

archivo.write(contenido)
archivo.close()
