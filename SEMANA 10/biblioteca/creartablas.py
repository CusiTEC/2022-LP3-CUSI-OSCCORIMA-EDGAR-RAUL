# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 12:01:44 2022

@author: usuario
"""

import sqlite3

conexion=sqlite3.connect("bdbiblioteca.db")

tabla_pais="""
            CREATE TABLE PAIS(
                IDPAIS INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE TEXT,
                ESTADO TEXT
                )
            """
            
tabla_editorial="""
            CREATE TABLE EDITORIAL(
                IDEDITORIAL INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE TEXT,
                ESTADO TEXT
                )
            """
            
tabla_autor="""
            CREATE TABLE AUTOR(
                IDAUTOR INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE TEXT,
                F_NACIMIENTO TEXT
                )
            """
            
tabla_libro="""
            CREATE TABLE LIBRO(
                IDLIBRO INTEGER PRIMARY KEY AUTOINCREMENT,
                TITULO TEXT,
                CANTIDAD INTEGER,
                ANIO INTEGER,
                PRECIO REAL,
                ESATDO TEXT,
                IDPAIS INTEGER REFERENCES PAIS,
                IDEDITORIAL INTEGER REFERENCES EDITORIAL,
                IDAUTOR INTEGER REFERENCES AUTOR
                )
            """
            
cursor = conexion.cursor()
cursor.execute(tabla_pais)
cursor.execute(tabla_editorial)
cursor.execute(tabla_autor)
cursor.execute(tabla_libro)
#nunca olviden hacer commit

conexion.commit()
conexion.close()