# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:52:18 2022

@author: usuario
"""

#dado el total, calcular el IGV y el subtotal

import Financieros
total = 1000.49
print(f"Subtotal: {Financieros.obtenerSubTotalconTotal(total): .2f}")
print(f"IGV: {Financieros.obtenerIGVconTotal(total): .2f}")
print(f"Total: {total}")