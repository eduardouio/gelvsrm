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
from PyQt5.QtCore import QDateTime, QDate, QTime, qDebug, QVarinat


class Provider(object):
	"""Estructura del objeto Provider"""
	def __init__(self, id_proveedor='',id_ciudad=int(),id_contacto=int(),nombre='',
				direccion='',telefono='',email='', credito='',notas='',registro=''):
		super(Provider, self).__init__()
		self.id_proveedor = id_proveedor
		self.id_ciudad = id_ciudad
		self.id_contacto = id_contacto
		self.nombre = nombre
		self.direccion = direccion
		self.telefono = telefono
		self.email = email
		self.credito = credito
		self.notas = notas
		self.registro = QDateTime().currentDateTime()
		qDebug('[Debug] se inicia la clase provider')


class providerCatalog(object):
	"""docstring for providerCatalog"""

	def __init__(self):
		super(providerCatalog, self).__init__()
		self.table = 'proveedor'
		self.MyDb = DB()
		qDebug('[Debug] se inicia la clase providerCatalog')


	def getProvider(self, idProvider):
		'''Obtiene un proveedor un una lista de ellos
		@param (str) id_proveedor
		@return (obj) | list(obj) topo Provider'''		
		condition = [' id_proveedor = ' + str(idProvider)]
		result = self.MyDb.selectQuery(self.table,'',condition)
		qDebug('[Ddebug] La consulta retorna %s registros'% result.size())
		if result.next():			
			return self.__setObj(result)
		else:
			qDebug('[Ddebug] no se encontró ningun resultado')
			return False			
		

	def listProviders(self):
		'''Retorna un listado de proveedores
		@return lst(obj) provider'''		
		providers = []
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Ddebug] La consulta retorna %s registros'% result.size())
		while result.next():			
			providers.append(self.__setObj(result))

		return providers


	def firstProvider(self):
		'''retorna el primer Provider de la lista
		@return (obj) Provider'''		
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] Se toma el primer provider de la lista')
		if result.first():
			return self.__setObj(result)
		else:
			qDebug('[Debug] no se encuentra el primer proveedor')
			return False


	def lastProvider(self):
		'''retorna el ultimo Provideie de la Lista
		@return (obj) Provideie'''
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] Se toma ultimo Providero de la lista')
		if result.last():
			return self.__setObj(result)
		else:
			qDebug('[Debug] no se encuentra el ultimo proveedor')
			return False


	def findProvider(self,condition):
		'''Busca un Provider
		@param condition = {'id_tecnico like ' : '%4%'}
		@return list(obj) tipo Provider'''
		providers = []
		result = self.MyDb.selectQuery(self.table,'',condition)
		while result.next():
			providers.append(self.__setObj(result))

		return Providers


	def createProvider(self,provider):
		'''Crea un proveedor
		@param (obj) provider
		@return (bool) | (int)
		'''
		values = {		
			'id_proveedor' : provider.id_proveedor,
			'id_ciudad' : provider.id_ciudad,
			'id_contacto' : provider.id_contacto,
			'nombre' : provider.nombre,
			'direccion' : provider.direccion,
			'telefono' : provider.telefono,
			'email' : provider.email,
			'credito' : provider.credito,
			'notas' : provider.notas			
		}

		result = self.MyDb.insertQuery(self.table,values)

		if(result.numRowsAffected()>0):
			qDebug('[Debug] se crea un priveedor en la base de datos')
			return str(result.lastInsertId())
		else:
			qDebug('[Debug] problemas para crear un proveedor de la base de datos')
			return False


	def updateProvider(self, oldProvider, provider):
		'''Actualiza un proveedor
		@param (obj) tipo proveedor
		@param (obj) tipo proveedor
		@return (bool)
		'''
		condition = {' id_proveedor = ' : str(oldProvider.id_proveedor)}
		values = {				
			'id_ciudad' : provider.id_ciudad,
			'id_contacto' : provider.id_contacto,
			'nombre' : provider.nombre,
			'direccion' : provider.direccion,
			'telefono' : provider.telefono,
			'email' : provider.email,
			'credito' : provider.credito,
			'notas' : provider.notas,
			'registro' : provider.registro
		}

		result = self.MyDb.updateQuery(self.table,values)

		if(result.numRowsAffected()>0):
			qDebug('[Debug] se Actualiza un priveedor en la base de datos')
			return True
		else:
			qDebug('[Debug] problemas para Actualizar un priveedor en la base de datos')
			return False


	def deleteProvideir(self,provider):
		'''Elimina un proveedor
		@param (obj) provider
		@return (bool)'''

		condition = {' id_proveedor = ' : str(provider.id_proveedor)}
		result = self.MyDb.deleteQuery(self.table,condition)

		if(result.numRowsAffected()>0):
			qDebug('[Debug] se Elimina un priveedor en la base de datos')
			return True
		else:
			qDebug('[Debug] problemas para Eliminar un priveedor en la base de datos')
			return False


	def __setObj(self, result):
		'''Crea un objeto tipo Conctact y lo retorna
		@param (obj) result
		@return (obj) contact'''
		myprovider = Provider()
		myprovider.id_proveedor = result.value(0)
		myprovider.id_ciudad = result.value(1)
		myprovider.id_contacto = result.value(2)
		myprovider.nombre = result.value(3)
		myprovider.direccion = result.value(4)
		myprovider.telefono = result.value(5)
		myprovider.email = result.value(6)
		myprovider.credito = result.value(7)
		myprovider.notas = result.value(8)
		registro = result.value(9)
		#validamos los campos nulos

		if isinstance(myprovider.id_ciudad, QVarinat):
			myprovider.id_ciudad = None

		if isinstance(myprovider.id_contacto, QVarinat):
			myprovider.id_contacto = None

		if isinstance(myprovider.email, QVarinat):
			myprovider.email = None

		if isinstance(myprovider.credito, QVarinat):
			myprovider.credito = None

		if isinstance(myprovider.notas, QVarinat):
			myprovider.notas = None

		#Validamos las fechas

		myprovider.registro = registro.toString()

		qDebug('[Debug] Se crea un objeto proveedor validando los campos NULL')
		return myprovider