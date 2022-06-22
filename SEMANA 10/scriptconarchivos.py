# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 10:11:59 2022

@author: usuario
"""

noticia = open("noticia.txt","rt",encoding='utf-8-sig')
datos_noticia = noticia.read()
lista = datos_noticia.split()
print(datos_noticia)

print(lista)
