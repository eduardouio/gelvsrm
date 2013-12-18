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
		
	def listarCuidadesProvincia(self, columnas='', id_provincia=''):
		'''Lista las ciudades de una tabla'''
		result = object

		if columnas and id_provincia:
			result = DB.selectQuery(self.tabla, columnas, 'id_provincia = ' + str(id_provincia)

		if columnas and not id_provincia:
			result = DB.selectQuery(self.tabla, columnas)

		if not columnas and id_provincia:
			result = DB.selectQuery(self.tabla,'', 'id_provincia = ' + str(id_provincia)

		if not columnas and not id_provincia:
			print('ultimo')
			result = DB.selectQuery(self.tabla)

		return result

	def actualizarCuidad(self,id_ciudad):
		'''Actualiza una ciudad en la base de datos'''
		pass

	def borrarCiudad(self,id_ciudad):
		'''Elimina una ciudad de la base de datos'''
		pass

	def obtenerCiudad(self, id_ciudad):
		'''Obtiene los datos de una ciudad'''

a = ciudadClass()
a.listarCuidadesProvincia('',3)