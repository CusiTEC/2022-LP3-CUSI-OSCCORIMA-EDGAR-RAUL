# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:43:40 2022

@author: usuario
"""

import sqlite3

conexion=sqlite3.connect("bdbiblioteca.db")

consulta="""INSERT INTO
                PAIS(NOMBRE,ESTADO)
                VALUES('Brasil','A')
            """
cursor = conexion.cursor()
cursor.execute(consulta)

#nunca olviden hacer commit

conexion.commit()
conexion.close()