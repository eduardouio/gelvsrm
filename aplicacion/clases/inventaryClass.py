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
# | descripcion   | varchar(200)         | NO   |     | NULL              |                             |
# | unidad        | varchar(25)          | NO   |     | NULL              |                             |
# | stok_min      | smallint(5) unsigned | NO   |     | NULL              |                             |
# | marca         | varchar(45)          | YES  |     | NULL              |                             |
# | ubicacion     | varchar(100)         | NO   |     | NULL              |                             |
# | notas         | mediumtext           | YES  |     | NULL              |                             |
# | registro      | timestamp            | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
# +---------------+----------------------+------+-----+-------------------+-----------------------------+

import sys
sys.path.append('..')
from modelo.Modelo import DB
from PyQt4.QtCore import QDateTime, QDate, QTime, qDebug

class Inventary(object):
	"""descripcion de la clase Inventario"""
	def __init__(self, id_inventario = int(),fecha='',nombre='',descripcion='',
				unidad='',stok_min=int(),marca='',ubicacion='', notas='', registro=''):
		super(Inventario, self).__init__()
		self.id_inventario = id_inventario
		self.fecha = QDate().currentDate()
		self.nombre = nombre
		self.descripcion = descripcion
		self.unidad = unidad
		self.stok_min = stok_min
		self.marca = marca
		self.ubicacion = ubicacion
		self.notas = notas		
		self.registro = QDateTime().currentDateTime()
		qDebug('[Debug] se inicia la clase inventary')


class inventaryCatalog(object):
	"""acciones sobre Inventary"""

	def __init__(self, arg):
		super(inventaryCatalog, self).__init__()
		self.table = 'inventario'
		self.MyDb = DB()
		qDebug('[Debug] se inicia la clase inventaryCatalog')


	def getInventary(self,idInventary):
		'''Obtiene un listado de inventario o inventario
		@param inventary
		@return (obj) | list(obj)'''
		condition = {' id_inventario = ' : str(idInventary)}
		result = self.MyDb.selectQuery(self.table,'',condition)
		qDebug('[Debug] la consulta retorno %s objetos'% str(result.size()))
		if result.next():
			return self.__setObj(result)
		else:
			qDebug('[Debug] no se puede encontrar el item de inventario')
			return False
	

	def listInventary(self):
		'''Lista todos los items del invemtario
		@return lst(inventary)'''	
		inventary = []
		result = self.MyDb.selectQuery(self.table)
		while result.next():			
			inventary.append(self.__setObj(result))

		return inventary


	def firstInventary(self):
		'''retorna el primer item del inventary de la lista
		@return (obj) Inventary'''		
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] Se toma el primer Inventario de la lista')
		if result.first():
			return self.__setObj(result)
		else:
			return False


	def lastInventary(self):
		'''retorna el ultimo Inventario de la Lista
		@return (obj) Inventario'''
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] Se toma ultimo Inventario de la lista')
		if result.last():
			return self.__setObj(result)
		else:
			return False


	def findInventary(self,condition):
		'''Busca un Inventaryo
		@param condition = {'id_tecnico like ' : '%4%'}
		@return list(obj) tipo Inventary'''
		Inventary = []
		result = self.MyDb.selectQuery(self.table,'',condition)
		while result.next():
			Inventary.append(self.__setObj(result))

		return Inventary


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
			'notas' : str(inventary.notas)			
		}

		result = self.MyDb.insertQuery(self.table,values)

		if(result.numRowsAffected()>0):
			qDebug('[Debug] Se crea un item de inventario en la tabla invemtario')
			return str(result.lastInsertId())
		else:
			qDebug('[Debug] no se puede crear un item de inventario en la tabla invemtario')
			return False


	def updateInventary(self,oldInventary, inventary):
		'''Actualiza un inventario
		@param'''
		condition = {' id_inventario =' : str(oldInventary.id_inventario)}
		values = {
			'fecha' : str(inventary.fecha),
			'nombre' : str(inventary.nombre),
			'descripcion' : str(inventary.descripcion),
			'unidad' : str(inventary.unidad),
			'stok_min' : str(inventary.stok_min),
			'marca' : str(inventary.marca),
			'ubicacion' : str(inventary.ubicacion),
			'notas' : str(inventary.notas)			
		}

		result = self.updateQuery(self.table,values)

		if(result.numRowsAffected()>0):
			qDebug('[Debug] Se Actualiza un item de inventario en la tabla invemtario')
			return True
		else:
			qDebug('[Debug] problemas para Actualizar un item de inventario en la tabla invemtario')
			return False


	def deleteInventary(self,inventary):
		'''Elimina un item del inventario
		@param (obj)
		@return (bool)'''
		condition = {' id_inventario = ' : str(inventary.id_inventario())}
		result = self.MyDb.deleteQuery(self.table, condition)

		if(result.numRowsAffected()>0):
			qDebug('[Debug] Se Elimina un item de inventario en la tabla invemtario')
			return True
		else:
			qDebug('[Debug] no se pude eliminar un item de inventario en la tabla invemtario')
			return False


	def __setObj(self, result):
		'''Crea un objeto tipo inventary y lo retorna
		@param (obj) result
		@return (obj) inventary'''
		myinventary = Inventary()
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
		#verificamos los nulos devueltos por la consulta
		if not(isinstance(myinventary.marca,str)):
			myinventary.marca=''

		if not(isinstance(myinventary.notas,str)):
			myinventary.notas=''

		qDebug('[Debug] se crea un objeto inventario validado')

		return myinventary