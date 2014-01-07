#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			inspectionClass.py
# Ubicacion		aplicacion/clases/inspectionClass.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
# +---------------+----------------------+------+-----+-------------------+-----------------------------+
# 									Data Types
# +---------------+----------------------+------+-----+-------------------+-----------------------------+
# | Field         | Type                 | Null | Key | Default           | Extra                       |
# +---------------+----------------------+------+-----+-------------------+-----------------------------+
# | id_inspeccion | smallint(5) unsigned | NO   | PRI | NULL              | auto_increment              |
# | id_vehiculo   | varchar(17)          | NO   | MUL | NULL              |                             |
# | id_tecnico    | varchar(10)          | NO   | MUL | NULL              |                             |
# | id_contacto   | smallint(5) unsigned | NO   | MUL | NULL              |                             |
# | id_ciudad     | smallint(5) unsigned | YES  | MUL | NULL              |                             |
# | periodo       | smallint(5) unsigned | NO   |     | NULL              |                             |
# | fecha         | date                 | NO   |     | NULL              |                             |
# | notas         | text                 | YES  |     | NULL              |                             |
# | registro      | timestamp            | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
# +---------------+----------------------+------+-----+-------------------+-----------------------------+

import sys
sys.path.append('..')
from modelo.Modelo import DB
from PyQt4.QtCore import QDateTime, QDate, QTime, qDebug


class Inspection(object):
	"""estructura para Inspection"""
	def __init__(self,id_inspeccion='',id_vehiculo='',id_tecnico='',
				id_contacto='',id_ciudad='',periodo='',fecha='',notas='',registro=''):
		super(Inspection, self).__init__()
		self.id_inspeccion = id_inspeccion
		self.id_vehiculo = id_vehiculo
		self.id_tecnico = id_tecnico
		self.id_contacto = id_contacto
		self.id_ciudad = id_ciudad
		self.periodo = periodo
		self.fecha = fecha
		self.notas = notas
		self.registro = registro
		qDebug('[Debug] se inicia la clase inspection')


class inspectionCatalog(object):
	"""operaciones sobre el objeto Inspection"""
	def __init__(self):
		super(inspectionCatalog, self).__init__()
		self.table = 'inspeccion'
		self.MyDb = DB()
		qDebug('[Debug] se inicia la clase inspectionCatalog')


	def getInspection(self,inspection=''):
		'''Obtiene una inspeccion o listado de ellas
		@param (str) id_inspeccion
		@return (obj) inspeccion
		'''	
		condition = {' id_inspeccion = ' : str(inspection)}
		result = self.MyDb.selectQuery(self.table,'',condition)
		qDebug('la consulta retono %s registros'% result.size())
		if result.next():
			return self.__setObj(result)


	def listInstections(self):
		'''Lista las inspecciones 
		@return lst(inspections)'''
		else:

			inspections = []
			result = self.MyDb.selectQuery(self.table)
			while result.next():
				myinspection = Inspection()
				myinspection.id_inspeccion = str(result.value(0))
				myinspection.id_vehiculo = str(result.value(1))
				myinspection.id_tecnico = str(result.value(2))
				myinspection.id_contacto = str(result.value(3))
				myinspection.id_ciudad = str(result.value(4))
				myinspection.periodo = str(result.value(5))
				myinspection.fecha = str(result.value(6))
				myinspection.notas = str(result.value(7))
				myinspection.registro = str(result.value(8))
				inspections.append(myinspection)

			return inspections


	def firstContact(self):
		'''retorna el primer contacto de la lista
		@return (obj) Contact'''		
		result = self.MyDB.selectQuery(self.table)
		qDebug('[Debug] Se toma el primer contacto de la lista')
		if result.first():
			return self.__setObj(result)
		else:
			return False


	def lastContact(self):
		'''retorna el ultimo contacto de la Lista
		@return (obj) contacto'''
		result = self.MyDB.selectQuery(self.table)
		qDebug('[Debug] Se toma ultimo contacto de la lista')
		if result.last():
			return self.__setObj(result)
		else:
			return False


	def findContact(self,condition):
		'''Busca un contacto
		@param condition = {'id_tecnico like ' : '%4%'}
		@return list(obj) tipo Contact'''
		contacts = []
		result = self.MyDB.selectQuery(self.table,'',condition)
		while result.next():
			contacts.append(self.__setObj(result))

		return contacts



	def createInspection(self,inspection):
		'''Crea una inspeccion
		@param (obj) inspection 
		@return (bool) | (int)'''
		values = {			
			'id_vehiculo': inspection.id_vehiculo,
			'id_tecnico': inspection.id_tecnico,
			'id_contacto': inspection.id_contacto,
			'id_ciudad': inspection.id_ciudad,
			'periodo': inspection.periodo,
			'fecha': inspection.fecha,
			'notas': inspection.notas			
		}
		result = self.MyDb.insertQuery(self.table,values)

		if (result.numRowsAffected() > 0):
			return True
		else:
			return False

	def updateInspection(self,oldInspection,inspection):
		'''Actualiza una inspeccion
		@param (obj) inspection
		@param (obj) inspection
		@return (bool)
		'''
		condition = ' id_inspeccion = ' + str(oldInspection.id_inspeccion)
		values = {
			'id_vehiculo': inspection.id_vehiculo,
			'id_tecnico': inspection.id_tecnico,
			'id_contacto': inspection.id_contacto,
			'id_ciudad': inspection.id_ciudad,
			'periodo': inspection.periodo,
			'fecha': inspection.fecha,
			'notas': inspection.notas			
		}
		result = self.MyDb.updateQuery(self.table, values)

		if (result.numRowsAffected() > 0):
			return True
		else:
			return False

	def deleteInspection(self,inspection):
		'''Elimina una inspection
		@param (obj) inspection
		@return (bool)'''
		condition = ' id_inspeccion = ' + str(inspection.id_inspeccion)
		result = self.MyDb.deleteQuery(self.table,condition)

		if (result.numRowsAffected() > 0):
			return True
		else:
			return False
	

	def __setObj(self, result):
		'''Crea un objeto tipo Conctact y lo retorna
		@param (obj) result
		@return (obj) contact'''
		mycontact = Contact()
		mycontact.id_contacto = str(result.value(0))
		mycontact.id_ciudad = str(result.value(0))
		mycontact.nombre = str(result.value(0))
		mycontact.telefono = str(result.value(0))
		mycontact.celular = str(result.value(0))
		mycontact.email = str(result.value(0))
		mycontact.notas = str(result.value(0))
		mycontact.registro = str(result.value(0))

		return mycontact