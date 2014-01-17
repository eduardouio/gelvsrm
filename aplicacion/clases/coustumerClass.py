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
from PyQt4.QtCore import QDateTime, QDate, QTime, qDebug

class Coustomer(object):
	"""Estrcutura del objeto cliente"""
	def __init__(self, id_cliente='',id_contacto=int(),id_ciudad=int(),nombre='',direccion='',
					telefono='',fax='',mail='',notas='',registro=''):
		super(Coustomer, self).__init__()
		self.id_cliente = id_cliente
		self.id_contacto = id_contacto
		self.id_ciudad = id_ciudad
		self.nombre = nombre
		self.direccion = direccion
		self.telefono = telefono
		self.fax = fax
		self.mail = mail
		self.notas = notas
		self.registro = QDateTime().currentDateTime()
		qDebug('[Debug] se crea un objeto tipo coustomer')


class coustomerCatalog(object):
	"""acciones sobre el objeto Coustomer"""
	
	def __init__(self):
		super(coustomerCatalog, self).__init__()
		self.table = 'cliente'
		self.MyDb = DB()
		qDebug('[Debug] se crea un objeto tipo coustomerCatalog')


	def getCoustomer(self, idCoustomer):
		'''Obtiene un cliente 
		@param (str) id_cliente
		@return (obj) coustomer
		'''	
		condition = {' id_cliente =' : str(idCoustomer)}
		result = self.MyDb.selectQuery(self.table,'',condition)
		qDebug('[Debug] la consulta retorna %s valores'% result.size())
		if result.next():
			return self.__setObj(result)
		else:
			qDebug('[Debug] no se puede retornar ningun valor ')
			return False


	def listCoustomers(self):
		'''Retorna un listado completo de clienteClass
		@return lst(obj) Coustomer'''
		coustomers = []
		result = self.selectQuery(self.table)
		qDebug('[Debug] la consulta retorna %s valores'% result.size())
		while result.next():				
			coustomers.append(self.__setObj(result))
		
		return coustomers


	def firstCoustomer(self):
		'''retorna el primer cliente de la tabla
		@return (obj) Coustomer'''		
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] Se toma el primer cliente de la lista')
		if result.first():
			return self.__setObj(result)
		else:
			return False


	def lastCoustomer(self):
		'''retorna la ultima cliente de la Lista
		@return (obj) Coustomer'''
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] Se toma la ultimo cliente de la lista')
		if result.last():
			return self.__setObj(result)
		else:
			return False
	

	def findCoustomer(self,condition):
		'''Busca una ciudad
		@param condition = {'id_tecnico like ' : '%4%'}
		@return list(obj) tipo Coustomer'''
		coustomers = []
		result = self.MyDb.selectQuery(self.table,'',condition)
		while result.next():
			coustomers.append(self.__setObj(result))

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
			'notas' : coustomer.notas			
		}

		result = self.MyDb.insertQuery(self.table,values)

		if (result.numRowsAffected() > 0):
			qDebug('[Debug] cliete ingresado a la base de datos')
			return True
		else:
			qDebug('[Debug] problemas para guaradar cliente a la base de datos')
			return False


	def updateCoustomer(self,oldCoustomer,coustomer):
		'''Actualiza un cliente
		@param (obj) coustomer
		@param (obj) coustomer
		@return (bool)
		'''
		condition = {' id_cliente = ' : str(oldCoustomer.id_cliente)}
		values = {
			'id_cliente' : coustomer.cliente,
			'id_contacto' : coustomer.id_contacto,
			'id_ciudad' : coustomer.id_ciudad,
			'nombre' : coustomer.nombre,
			'direccion' : coustomer.direccion,
			'telefono' : coustomer.telefono,
			'fax' : coustomer.fax,
			'mail' : coustomer.mail,
			'notas' : coustomer.notas			
		}

		result = self.MyDb.updateQuery(self.table,values,condition)

		if (result.numRowsAffected() > 0):
			qDebug('[Debug] cliete editado en la base de datos')
			return True
		else:
			qDebug('[Debug] problemas para editar cliente en la base de datos')
			return False


	def deleteCoustomer(self,coustomer):
		'''Elimina un cliente
		@param (obj) coustomer
		@return (bool)'''
		condition = {' id_cliente= ' : str(coustomer.id_cliente)}
		result = self.deleteQuery(self.table,condition)

		if (result.numRowsAffected() > 0):
			qDebug('[Debug] se elimina cliente en la base de datos')
			return True
		else:
			qDebug('[Debug] problemas para eliminar cliente en la base de datos')
			return False


	def __setObj(self,result):
		'''Crea un objeto tipo city
		@return (obj) city'''
		mycoustomer = Coustomer()
		mycoustomer.id_cliente = str(result.value(0))
		mycoustomer.id_contacto = str(result.value(1))
		mycoustomer.id_ciudad = str(result.value(2))
		mycoustomer.nombre = str(result.value(3))
		mycoustomer.direccion = str(result.value(4))
		mycoustomer.telefono = str(result.value(5))
		mycoustomer.fax = str(result.value(6))
		mycoustomer.mail = str(result.value(7))
		mycoustomer.notas = str(result.value(8))
		mycoustomer.registro = str(result.value(9))		
		qDebug('[Debug] se crea un cliente')
		return mycoustomer
