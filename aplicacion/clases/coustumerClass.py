#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			clienteClass.py
# Ubicacion		aplicacion/clases/clienteClass.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
# +---------------------------------------------------------------------------------------------------+
# 										Data Type
# +-------------+----------------------+------+-----+-------------------+-----------------------------+
# | Field       | Type                 | Null | Key | Default           | Extra                       |
# +-------------+----------------------+------+-----+-------------------+-----------------------------+
# | id_cliente  | char(13)             | NO   | PRI | NULL              |                             |
# | id_contacto | smallint(5) unsigned | YES  | MUL | NULL              |                             |
# | id_ciudad   | smallint(5) unsigned | YES  | MUL | NULL              |                             |
# | nombre      | varchar(200)         | NO   |     | NULL              |                             |
# | direccion   | varchar(600)         | NO   |     | NULL              |                             |
# | telefono    | varchar(15)          | NO   |     | NULL              |                             |
# | fax         | varchar(15)          | YES  |     | NULL              |                             |
# | mail        | varchar(100)         | YES  |     | NULL              |                             |
# | notas       | mediumtext           | YES  |     | NULL              |                             |
# | registro    | timestamp            | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
# +-------------+----------------------+------+-----+-------------------+-----------------------------+

import sys
sys.path.append('..')
from modelo.Modelo import DB

class Coustomer(object):
	"""Estrcutura del objeto cliente"""
	def __init__(self, id_cliente='',id_contacto='',id_ciudad='',nombre='',direccion='',
					telefono='',fax='',mail='',notas='',registro=''):
		super(Coustomer, self).__init__()
		self.id_cliente = cliente
		self.id_contacto = id_contacto
		self.id_ciudad = id_ciudad
		self.nombre = nombre
		self.direccion = direccion
		self.telefono = telefono
		self.fax = fax
		self.mail = mail
		self.notas = notas
		self.registro = registro


class coustomerCatalog(object):
	"""acciones sobre el objeto Coustomer"""
	def __init__(self):
		super(coustomerCatalog, self).__init__()
		self.table = 'cliente'
		self.MyDb = DB()

	def getCoustomer(self, coustomer=''):
		'''Obtiene un cliente o un listado
		@param (str) id_cliente
		@return (obj) | list(obj)
		'''
		if coustomer:
			condition = ' id_cliente =' + str(coustomer)
			mycoustomer = Coustomer()
			result = self.MyDb.selectQuery(self.table,'',condition)
			while result.next():
				mycoustomer.id_cliente = str(result.value(0))
				mycoustomer.id_contacto = str(result.value(1))
				mycoustomer.id_ciudad = str(result.value(2))
				mycoustomer.nombre = str(result.value(3))
				mycoustomer.direccion = str(result.value(4))
				mycoustomer.telefono = str(result.value(5))
				mycoustomer.fax = str(result.value(5))
				mycoustomer.mail = str(result.value(6))
				mycoustomer.notas = str(result.value(7))
				mycoustomer.registro = str(result.value(8))

			return mycoustomer

		else:

			coustomers = []
			result = self.selectQuery(self.table)
			while result.next():
				mycoustomer = Coustomer
				mycoustomer.id_cliente = str(result.value(0))
				mycoustomer.id_contacto = str(result.value(1))
				mycoustomer.id_ciudad = str(result.value(2))
				mycoustomer.nombre = str(result.value(3))
				mycoustomer.direccion = str(result.value(4))
				mycoustomer.telefono = str(result.value(5))
				mycoustomer.fax = str(result.value(5))
				mycoustomer.mail = str(result.value(6))
				mycoustomer.notas = str(result.value(7))
				mycoustomer.registro = str(result.value(8))
				coustomers.append(mycoustomer)

			return coustomers

	def createCoustomer(self,coustomer):
		'''Crea un cliente
		@param (obj)
		@return (bool) | int
		'''
		values = {
			'id_cliente' : coustomer.cliente,
			'id_contacto' : coustomer.id_contacto,
			'id_ciudad' : coustomer.id_ciudad,
			'nombre' : coustomer.nombre,
			'direccion' : coustomer.direccion,
			'telefono' : coustomer.telefono,
			'fax' : coustomer.fax,
			'mail' : coustomer.mail,
			'notas' : coustomer.notas,
			'registro' : coustomer.registro
		}

		result = self.MyDb.insertQuery(self.table,values)

		if (result.numRowsAffected() > 0):
			return True
		else:
			return False

	def updateCoustomer(self,oldCoustomer,coustomer):
		'''Actualiza un cliente
		@param (obj) coustomer
		@param (obj) coustomer
		@return (bool)
		'''
		condition = ' id_cliente = ' + str(oldCoustomer.id_cliente)
		values = {
			'id_cliente' : coustomer.cliente,
			'id_contacto' : coustomer.id_contacto,
			'id_ciudad' : coustomer.id_ciudad,
			'nombre' : coustomer.nombre,
			'direccion' : coustomer.direccion,
			'telefono' : coustomer.telefono,
			'fax' : coustomer.fax,
			'mail' : coustomer.mail,
			'notas' : coustomer.notas,
			'registro' : coustomer.registro
		}

		result = self.MyDb.updateQuery(self.table,values,condition)

		if (result.numRowsAffected() > 0):
			return True
		else:
			return False

	def deleteCoustomer(self,coustomer):
		'''Elimina un cliente
		@param (obj) coustomer
		@return (bool)'''
		condition = ' id_cliente= ' + str(coustomer.id_cliente)
		result = self.deleteQuery(self.table,condition)

		if (result.numRowsAffected() > 0):
			return True
		else:
			return False

	def finCoustomer(self,condition=''):
		'''Busca un cliente'''
		pass