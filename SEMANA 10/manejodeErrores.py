# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 10:16:02 2022

@author: usuario
"""

try:
    numerador = float(input("Numerador: "))
    denominador = float(input("Denominador: "))
    resultado =numerador/denominador
    print(f"Resultado: {resultado}")
    print("Gracias")
except ZeroDivisionError:
    print("No puedes dividir entre 0")
except:
    print("Hubo un error")
else:
    print("Division correcta")
finally:
    print("La operacion terminó")