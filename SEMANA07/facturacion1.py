# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:47:42 2022

@author: usuario
"""

#DADO EL SUBTOTAL, CALCULAR EL IGV Y EL TOTAL

import Financieros

subtotal = 800.77
print(f"Subtotal: {subtotal}")
print(f"IGV: {Financieros.obtenerIGVsubTotal(subtotal): .2f}")
print(f"Total: {Financieros.obtenerTotalconSubTotal(subtotal): .2f}")
