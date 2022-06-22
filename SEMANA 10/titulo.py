# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 08:55:08 2022

@author: usuario
"""

import camelcase 

nombre="edgar raul cusi osccorima"

print(nombre.upper())
print(nombre.title())


#creamos un objeto lamdo cam

cam= camelcase.CamelCase()
print("con camelcase...")

#imprimimos el nombre en formato titulo
#utilizamo camelcase

print(cam.hump(nombre))

#Para resolver el sisguiente problema
#creamos otro objeto lllamdo cam2
#al definir el obejto , incluimos los argumewntos
#flor y leon 


cam2=camelcase.CamelCase('edgar','cusi')
print(cam2.hump(nombre))