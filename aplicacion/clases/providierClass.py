#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			provClass.py
# Ubicacion		aplicacion/clases/provClass.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
# +--------------+----------------------+------+-----+-------------------+-----------------------------+
#         									Data Types
# +--------------+----------------------+------+-----+-------------------+-----------------------------+
# | Field        | Type                 | Null | Key | Default           | Extra                       |
# +--------------+----------------------+------+-----+-------------------+-----------------------------+
# | id_proveedor | varchar(13)          | NO   | PRI | NULL              |                             |
# | id_ciudad    | smallint(5) unsigned | YES  | MUL | NULL              |                             |
# | id_contacto  | smallint(5) unsigned | YES  | MUL | NULL              |                             |
# | nombre       | varchar(150)         | NO   |     | NULL              |                             |
# | direccion    | varchar(500)         | NO   |     | NULL              |                             |
# | telefono     | varchar(15)          | NO   |     | NULL              |                             |
# | email        | varchar(30)          | YES  |     | NULL              |                             |
# | credito      | tinyint(1)           | YES  |     | NULL              |                             |
# | notas        | mediumtext           | YES  |     | NULL              |                             |
# | registro     | timestamp            | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
# +--------------+----------------------+------+-----+-------------------+-----------------------------+

import sys
sys.path.append('..')
from modelo.Modelo import DB

class Providier(object):
	"""Estructura del objeto Providier"""
	def __init__(self, id_proveedor='',id_ciudad='',id_contacto='',nombre='',
				direccion='',telefono='',email='', credito='',notas='',registro=''):
		super(Providier, self).__init__()
		self.id_proveedor = id_proveedor
		self.id_ciudad = id_ciudad
		self.id_contacto = id_contacto
		self.nombre = nombre
		self.direccion = direccion
		self.telefono = telefono
		self.email = email
		self.credito = credito
		self.notas = notas
		self.registro = registro

class providierCatalog(object):
	"""docstring for providierCatalog"""
	def __init__(self):
		super(providierCatalog, self).__init__()
		self.table = 'proveedor'
		self.MyDb = DB()

	def getProvidiers(self, providier=''):
		'''Obtiene un proveedor un una lista de ellos
		@param (str) id_proveedor
		@return (obj) | list(obj) topo Providier
		'''
		if providier:
			myprovidier = Providier()
			condition = ' id_proveedor = ' + str(providier)
			result = self.MyDb.selectQuery(self.table,'',condition)
			while result.next():
				myprovidier.id_proveedor = str(result.value(0))
				myprovidier.id_ciudad = str(result.value(1))
				myprovidier.id_contacto = str(result.value(2))
				myprovidier.nombre = str(result.value(3))
				myprovidier.direccion = str(result.value(4))
				myprovidier.telefono = str(result.value(5))
				myprovidier.email = str(result.value(6))
				myprovidier.credito = str(result.value(7))
				myprovidier.notas = str(result.value(8))
				myprovidier.registro = str(result.value(9))

			return myprovidier

		else:
			providiers = []
			result = self.MyDb.selectQuery(self.table)
			while result.next():
				myprovidier = Providier()
				myprovidier.id_proveedor = str(result.value(0))
				myprovidier.id_ciudad = str(result.value(1))
				myprovidier.id_contacto = str(result.value(2))
				myprovidier.nombre = str(result.value(3))
				myprovidier.direccion = str(result.value(4))
				myprovidier.telefono = str(result.value(5))
				myprovidier.email = str(result.value(6))
				myprovidier.credito = str(result.value(7))
				myprovidier.notas = str(result.value(8))
				myprovidier.registro = str(result.value(9))
				providiers.append(myprovidier)

			return providiers

	def createProvidier(self,providier):
		'''Crea un proveedor
		@param (obj) providier
		@return (bool) 
		'''
		values = {		
			'id_proveedor' : providier.id_proveedor,
			'id_ciudad' : providier.id_ciudad,
			'id_contacto' : providier.id_contacto,
			'nombre' : providier.nombre,
			'direccion' : providier.direccion,
			'telefono' : providier.telefono,
			'email' : providier.email,
			'credito' : providier.credito,
			'notas' : providier.notas,
			'registro' : providier.registro
		}

		result = self.MyDb.createQuery(self.table,values)

		if(result.numRowsAffected()>0):
			return str(result.lastInsertId())
		else:
			return False

	def updateProvidier(self, oldProvidier, providier):
		'''Actualiza un proveedor
		@param (obj) tipo proveedor
		@param (obj) tipo proveedor
		@return (bool)
		'''
		condition = ' id_proveedor = ' + str(oldProvidier.id_proveedor)
		values = {				
			'id_ciudad' : providier.id_ciudad,
			'id_contacto' : providier.id_contacto,
			'nombre' : providier.nombre,
			'direccion' : providier.direccion,
			'telefono' : providier.telefono,
			'email' : providier.email,
			'credito' : providier.credito,
			'notas' : providier.notas,
			'registro' : providier.registro
		}

		result = self.MyDb.updateQuery(self.table,values)

		if(result.numRowsAffected()>0):
			return str(result.lastInsertId())
		else:
			return False

	def deleteProvideir(self,providier):
		'''Elimina un proveedor
		@param (obj) providier
		@return (bool)'''

		condition = ' id_proveedor = ' + str(providier.id_proveedor)
		result = self.MyDb.deleteQuery(self.table,condition)

		if(result.numRowsAffected()>0):
			return str(result.lastInsertId())
		else:
			return False

	def findProvidier(self,condition=''):
		'''Busca un proveedor'''
		pass