# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:36:26 2022

Los modulos te permitiran crear librerias de funcionalidalidades
que puedes utilizar o reutilizar en cualquier momento
"""

igv = 0.18

def obtenerIGVsubTotal(subtotal):
    return subtotal*igv

def obtenerTotalconSubTotal(subtotal):
    #subtotal + igv * subtotal
    #subtotal *( 1.18 )
    return subtotal * (1 + igv)

def obtenerSubTotalconTotal(total):
    return total/(1+igv)

def obtenerIGVconTotal(total):
    return total - obtenerSubTotalconTotal(total)

