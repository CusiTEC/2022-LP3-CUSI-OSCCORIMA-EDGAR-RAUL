# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 09:37:01 2022

@author: usuario
"""
#Tenemos una cadena llamada nombre y se desea que se modifique el formato
import camelcase

nombre = "edgar raul cusi osccorima"

print(nombre.upper())

print(nombre.title())

#creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("con Camelcase.....")

#Imprimimos nombre en formato titulo y utilizamos camel case
print(cam.hump(nombre))


#Para reoslver le problema ceramos otro objeto 
#al definir el objeto incluimos los argumentos 
#flor y león

cam2 = camelcase.CamelCase('edgar','cusi')
print(cam2.hump(nombre))
