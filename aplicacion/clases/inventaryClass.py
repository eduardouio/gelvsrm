#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			inventario_class.py
# Ubicacion		aplicacion/clases/inventario_class.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
# +---------------+----------------------+------+-----+-------------------+-----------------------------+
# 												Data Types
# +---------------+----------------------+------+-----+-------------------+-----------------------------+
# | Field         | Type                 | Null | Key | Default           | Extra                       |
# +---------------+----------------------+------+-----+-------------------+-----------------------------+
# | id_inventario | smallint(5) unsigned | NO   | PRI | NULL              | auto_increment              |
# | fecha         | datetime             | NO   |     | NULL              |                             |
# | nombre        | varchar(100)         | NO   |     | NULL              |                             |
# | descripcion   | varchar(200)         | YES  |     | NULL              |                             |
# | unidad        | varchar(25)          | YES  |     | NULL              |                             |
# | stok_min      | smallint(5) unsigned | NO   |     | NULL              |                             |
# | marca         | varchar(45)          | YES  |     | NULL              |                             |
# | ubicacion     | varchar(100)         | NO   |     | NULL              |                             |
# | notas         | mediumtext           | YES  |     | NULL              |                             |
# | registro      | timestamp            | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
# +---------------+----------------------+------+-----+-------------------+-----------------------------+

import sys
sys.path.append('..')
from modelo.Modelo import DB

class Inventary(object):
	"""descripcion de la clase Inventario"""
	def __init__(self, id_inventario = '',fecha='',nombre='',descripcion='',
				unidad='',stok_min='',marca='',ubicacion='', notas='', registro=''):
		super(Inventario, self).__init__()
		self.id_inventario = id_inventario
		self.fecha = fecha
		self.nombre = nombre
		self.descripcion = descripcion
		self.unidad = unidad
		self.stok_min = stok_min
		self.marca = marca
		self.ubicacion = ubicacion
		self.notas = notas
		self.registro = registro

class inventaryCatalog(object):
	"""acciones sobre Inventary"""
	def __init__(self, arg):
		super(inventaryCatalog, self).__init__()
		self.table = 'inventario'
		self.MyDb = DB()

	def getInventary(self,inventary=''):
		'''Obtiene un listado de inventario o inventario
		@param inventary
		@return (obj) | list(obj)'''
		if inventary:
			myinventary = Inventary()
			condition = ' id_inventario = ' + str(inventary)
			result = self.MyDb.selectQuery(self.table,'',condition)
			while result.next():
				myinventary.id_inventario = str(result.value(0))
				myinventary.fecha = str(result.value(1))
				myinventary.nombre = str(result.value(2))
				myinventary.descripcion = str(result.value(3))
				myinventary.unidad = str(result.value(4))
				myinventary.stok_min = str(result.value(5))
				myinventary.marca = str(result.value(6))
				myinventary.ubicacion = str(result.value(7))
				myinventary.notas = str(result.value(8))
				myinventary.registro = str(result.value(9))

			return myinventary
		else:
			inventary = []
			result = self.MyDb.selectQuery(self.table)
			while result.next():
				myinventary = DB()
				myinventary.id_inventario = str(result.value(0))
				myinventary.fecha = str(result.value(1))
				myinventary.nombre = str(result.value(2))
				myinventary.descripcion = str(result.value(3))
				myinventary.unidad = str(result.value(4))
				myinventary.stok_min = str(result.value(5))
				myinventary.marca = str(result.value(6))
				myinventary.ubicacion = str(result.value(7))
				myinventary.notas = str(result.value(8))
				myinventary.registro = str(result.value(9))
				inventary.append(myinventary)

			return inventary

	def createInventary(self,inventary):
		'''Crea un inventario
		@param (obj) inventary
		@return (bool)'''
		values = {			
			'fecha' : str(inventary.fecha),
			'nombre' : str(inventary.nombre),
			'descripcion' : str(inventary.descripcion),
			'unidad' : str(inventary.unidad),
			'stok_min' : str(inventary.stok_min),
			'marca' : str(inventary.marca),
			'ubicacion' : str(inventary.ubicacion),
			'notas' : str(inventary.notas),
			'registro' : str(inventary.registro)
		}

		result = self.MyDb.insertQuery(self.table,values)

		if(result.numRowsAffected()>0):
			return str(result.lastInsertId())
		else:
			return False

	def updateInventary(self,oldInventary, inventary):
		'''Actualiza un inventario
		@param'''
		condition = ' id_inventario =' + str(oldInventary..id_inventario)
		values = {
			'fecha' : str(inventary.fecha),
			'nombre' : str(inventary.nombre),
			'descripcion' : str(inventary.descripcion),
			'unidad' : str(inventary.unidad),
			'stok_min' : str(inventary.stok_min),
			'marca' : str(inventary.marca),
			'ubicacion' : str(inventary.ubicacion),
			'notas' : str(inventary.notas),
			'registro' : str(inventary.registro)
		}

		result = self.updateQuery(self.table,values)

		if(result.numRowsAffected()>0):
			return str(result.lastInsertId())
		else:
			return False

	def deleteInventary(self,inventary):
		'''Elimina un item del inventario
		@param (obj)
		@return (bool)'''
		condition = ' id_inventario = ' + str(inventary.id_inventario())
		result = self.MyDb.deleteQuery(self.table, condition)

		if(result.numRowsAffected()>0):
			return str(result.lastInsertId())
		else:
			return False

	def findInventary(self,condition=''):
		'''Busca un inventary'''
		pass