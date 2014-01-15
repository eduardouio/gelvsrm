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
	def __init__(self,id_inspeccion=int(),id_vehiculo='',id_tecnico='',
				id_contacto=int(),id_ciudad=int(),periodo=int(),fecha='',notas='',registro=''):
		super(Inspection, self).__init__()
		self.id_inspeccion = id_inspeccion
		self.id_vehiculo = id_vehiculo
		self.id_tecnico = id_tecnico
		self.id_contacto = id_contacto
		self.id_ciudad = id_ciudad
		self.periodo = periodo
		self.fecha = QDate().currentDate()
		self.notas = notas
		self.registro = QDateTime.currentDateTime()
		qDebug('[Debug] se inicia la clase inspection')


class inspectionCatalog(object):
	"""operaciones sobre el objeto Inspection"""

	def __init__(self):
		super(inspectionCatalog, self).__init__()
		self.table = 'inspeccion'
		self.MyDb = DB()
		qDebug('[Debug] se inicia la clase inspectionCatalog')


	def getInspection(self,idInspection):
		'''Obtiene una inspeccion o listado de ellas
		@param (str) id_inspeccion
		@return (obj) inspeccion
		'''	
		condition = {' id_inspeccion = ' : str(idInspection)}
		result = self.MyDb.selectQuery(self.table,'',condition)
		qDebug('la consulta retono %s registros'% result.size())
		if result.next():
			return self.__setObj(result)
		else:
			return False


	def listInspections(self):
		'''Lista las inspecciones 
		@return lst(inspections)'''
		inspections = []
		result = self.MyDb.selectQuery(self.table)
		qDebug('la consulta retono %s registros'% result.size())
		while result.next():			
			inspections.append(self.__setObj(result))

		return inspections


	def firstInspection(self):
		'''retorna el primer Inspection de la lista
		@return (obj) Inspection'''		
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] Se toma el primer Inspection de la lista')
		if result.first():
			return self.__setObj(result)
		else:
			return False


	def lastInspection(self):
		'''retorna el ultimo Inspection de la Lista
		@return (obj) Inspection'''
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] Se toma ultimo Inspection de la lista')
		if result.last():
			return self.__setObj(result)
		else:
			return False


	def findInspection(self,condition):
		'''Busca un Inspection
		@param condition = {'id_tecnico like ' : '%4%'}
		@return list(obj) tipo Inspection'''
		inspections = []
		result = self.MyDb.selectQuery(self.table,'',condition)
		while result.next():
			inspections.append(self.__setObj(result))

		return inspections


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
			qDebug('[Debug] se crea una inspection en la base')
			return self.MyDb.lastInsertId()
		else:
			qDebug('[Debug] no se puede crear una inspection en la base')
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
			qDebug('[Debug] se Actualiza una inspection en la base')
			return True
		else:
			qDebug('[Debug] No se Actualiza una inspection en la base')
			return False


	def deleteInspection(self,inspection):
		'''Elimina una inspection
		@param (obj) inspection
		@return (bool)'''
		condition = ' id_inspeccion = ' + str(inspection.id_inspeccion)
		result = self.MyDb.deleteQuery(self.table,condition)

		if (result.numRowsAffected() > 0):
			qDebug('[Debug] se Elimina una inspection en la base')
			return True
		else:
			qDebug('[Debug] No se Elimina una inspection en la base')
			return False
	

	def __setObj(self, result):
		'''Crea un objeto tipo Conctact y lo retorna
		@param (obj) result
		@return (obj) contact'''
		myinspection = Inspection()
		myinspection.id_inspeccion = str(result.value(1))
		myinspection.id_vehiculo = str(result.value(2))
		myinspection.id_contacto = str(result.value(3))
		myinspection.id_ciudad = str(result.value(4))
		myinspection.periodo = str(result.value(5))
		myinspection.fecha = str(result.value(6))
		myinspection.notas = str(result.value(7))
		myinspection.registro = str(result.value(8))
		#verificamos los nulos devueltos por la consulta

		if not(isinstance(myinspection.id_ciudad,str)):
			myinspection.id_ciudad=''

		if not(isinstance(myinspection.notas,str)):
			myinspection.notas=''


		return myinspection