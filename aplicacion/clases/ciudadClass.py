#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			cuidadClass.py
# Ubicacion		aplicacion/clases/cuidadClass.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
# +-----------------------------------------------------------------------------+
# |									Data Type									|
# +--------------+----------------------+------+-----+---------+----------------+
# | Field        | Type                 | Null | Key | Default | Extra          |
# +--------------+----------------------+------+-----+---------+----------------+
# | id_ciudad    | smallint(5) unsigned | NO   | PRI | NULL    | auto_increment |
# | id_provincia | smallint(5) unsigned | NO   | MUL | NULL    |                |
# | nombre       | varchar(100)         | YES  |     | NULL    |                |
# +--------------+----------------------+------+-----+---------+----------------+

import sys
sys.path.append('..')
#coneccion a la base de datos
from modelo import conn
#modelo a la base de datos
from modelo.Modelo import DB

class ciudadClass(object):
	"""Representa a la entidad ciudad del modelo"""
	
	def __init__(self):
		'''Instancializacion de la clase'''
		super(ciudadClass, self).__init__()
		self.tabla = 'ciudad'
		
	def crearCiudad(self,values):
		'''Crea una ciudad'''
		return DB.insertQuery(self.tabla, values)
		
	def listarCuidadProvincia(self, columnas = ['*'], id_provincia = 0):
		'''Lista todas las ciudades de una id_provincia
			si no se especifica ningun id_provincia se
			listan todos los registros de la tabla'''
		return DB.selectQuery(self.tabla, columnas)


	def actualizarCuidad(self,id_ciudad):
		'''Actualiza una ciudad en la base de datos'''
		pass

	def borrarCiudad(self,id_ciudad):
		'''Elimina una ciudad de la base de datos'''
		pass

a = ciudadClass()
a.listarCuidadProvincia()