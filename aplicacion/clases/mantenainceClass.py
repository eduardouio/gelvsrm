#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			mantenainceClass.py
# Ubicacion		aplicacion/clases/mantenainceClass.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
# +------------------+----------------------+------+-----+-------------------+-----------------------------+
# 											Data Types
# +------------------+----------------------+------+-----+-------------------+-----------------------------+
# | Field            | Type                 | Null | Key | Default           | Extra                       |
# +------------------+----------------------+------+-----+-------------------+-----------------------------+
# | id_mantenimiento | smallint(5) unsigned | NO   | PRI | NULL              | auto_increment              |
# | id_viaje         | smallint(5) unsigned | NO   | MUL | NULL              |                             |
# | id_vehiculo      | char(17)             | NO   | MUL | NULL              |                             |
# | id_ciudad        | smallint(5) unsigned | YES  | MUL | NULL              |                             |
# | periodo          | smallint(5) unsigned | NO   |     | NULL              |                             |
# | fecha            | date                 | NO   |     | NULL              |                             |
# | kilometros       | varchar(10)          | NO   |     | NULL              |                             |
# | notas            | mediumtext           | YES  |     | NULL              |                             |
# | registro         | timestamp            | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
# +------------------+----------------------+------+-----+-------------------+-----------------------------+

import sys
sys.path.append('..')
from modelo.Modelo import DB
from PyQt4.QtCore import QDateTime, QDate, QTime, qDebug


class Mantenaince(object):
	"""Estructura para Mantenaince"""
	def __init__(self, id_mantenimiento='',id_viaje='',id_vehiculo='',id_ciudad='',
					periodo='',fecha='',kilometros='',notas='',registro=''):
		super(Mantenaince, self).__init__()
		self.id_mantenimiento = id_mantenimiento
		self.id_viaje = id_viaje
		self.id_vehiculo = id_vehiculo
		self.id_ciudad = id_ciudad
		self.periodo = periodo
		self.fecha = QDate()
		self.kilometros = kilometros
		self.notas = notas
		self.registro = QDateTime().currentDateTiem()
		qDebug('[Debug] se inicia la clase mantenimiento')


class mantenainceCatalog(object):
	"""docstring for mantenainceCatalog"""

	def __init__(self):
		super(mantenainceCatalog, self).__init__()
		self.MyDb = DB()
		self.table = 'mantenimiento'
		qDebug('[Debug] se incia la clase mantenainceCatalog')


	def getMantenaince(self,mantenaince=''):
		'''Obtiene un listado de mantenimientos o mantenimiento
		@param = id_mantenimiento'''		
		condition = [' id_mantenimiento = ' : str(mantenaince)]
		result = self.MyDb.selectQuery(self.table,'',condition)
		qDebug('[Debug] se encuentran %s registros'% result.size())
		if result.next():
			return self.__setObj(result)
		else:
			qDebug('[Debug] problemas para devolver un mantenimiento')
			return False
			

	def listMantenainces(self):
		'''Lista todos los mantenimientos
		@return lst(obj) Mantenaince'''
		mantenainces = []
		result = self.selectQuery(self.table)
		qDebug('[Debug] se encuentran %s registros'% result.size())
		while result.next():			
			mantenainces.append(self.__setObj(result))

		return mantenainces


	def firstMantenaince(self):
		'''retorna el primer Mantenainceo de la lista
		@return (obj) Mantenaince'''		
		result = self.MyDB.selectQuery(self.table)
		qDebug('[Debug] Se toma el primer Mantenaince de la lista')
		if result.first():
			return self.__setObj(result)
		else:
			return False


	def lastMantenaince(self):
		'''retorna el ultimo Mantenaince de la Lista
		@return (obj) Mantenaince'''
		result = self.MyDB.selectQuery(self.table)
		qDebug('[Debug] Se toma ultimo Mantenaince de la lista')
		if result.last():
			return self.__setObj(result)
		else:
			return False


	def findMantenaince(self,condition):
		'''Busca un Mantenainceo
		@param condition = {'id_tecnico like ' : '%4%'}
		@return list(obj) tipo Mantenaince'''
		Mantenainces = []
		result = self.MyDB.selectQuery(self.table,'',condition)
		while result.next():
			Mantenainces.append(self.__setObj(result))

		return Mantenainces


	def createMaintenaince(self,mantenaince):
		'''Crea un mantenimiento
		@param (obj) mantenaince
		@return (bool) | (int)'''
		values = {
		'id_viaje': str(mantenaince.id_viaje),
		'id_vehiculo': str(mantenaince.id_vehiculo),
		'id_ciudad': str(mantenaince.id_ciudad),
		'periodo': str(mantenaince.periodo),
		'fecha': str(mantenaince.fecha),
		'kilometros': str(mantenaince.kilometros),
		'notas': str(mantenaince.notas)		
		}

		result = self.insertQuery(self.table,values)

		if(result.numRowsAffected()>0):
			qDebug('[Debug] se crea un mantenimiento en la base')
			return str(result.lastInsertId())
		else:
			qDebug('[Debug] No se crea un mantenimiento en la base')
			return False


	def updateMantenaince(self,oldMantenaince, mantenaince):
		'''Actualiza un mantenimiento
		@param (obj) mantenaince
		@param (obj) mantenaince 
		@return (bool)
		'''
		values = {
		'id_vehiculo': str(mantenaince.id_vehiculo),
		'id_ciudad': str(mantenaince.id_ciudad),
		'periodo': str(mantenaince.periodo),
		'fecha': str(mantenaince.fecha),
		'kilometros': str(mantenaince.kilometros),
		'notas': str(mantenaince.notas)		
		}
		
		condition = {' id_mantenimiento = ' : str(oldMantenaince.id_mantenimiento)}

		result = self.MyDb.updateQuery(self.table,values,condition)

		if(result.numRowsAffected()>0):
			qDebug('[Debug] Se actualiza un mantenimiento en la base')
			return True
		else:
			qDebug('[Debug] No se Actualiza un mantenimiento en la base')
			return False


	def deleteMantenaince(self,mantenaince):
		'''Elimina un mantenimiento'''
		condition = {' id_mantenimiento = ' : str(mantenaince.id_mantenimiento)}
		result = self.MyDb.dleteQuery(self.table,condition)

		if(result.numRowsAffected()>0):
			qDebug('[Debug] Se Elimina un mantenimiento en la base')
			return True
		else:
			qDebug('[Debug] No se puede eliminar un mantenimiento en la base')
			return False


	def __setObj(self, result):
		'''Crea un objeto tipo Mantenaince y lo retorna
		@param (obj) result
		@return (obj) Mantenaince'''
		mymantenaince = Mantenaince()
		mymantenaince.id_mantenimiento = str(result.value(0))
		mymantenaince.id_viaje = str(result.value(1))
		mymantenaince.id_vehiculo = str(result.value(2))
		mymantenaince.id_ciudad = str(result.value(3))
		mymantenaince.periodo = str(result.value(4))
		mymantenaince.fecha = str(result.value(5))
		mymantenaince.kilometros = str(result.value(6))
		mymantenaince.notas = str(result.value(7))
		mymantenaince.registro = str(result.value(8))
		qDebug('[Debug] se crea un objeto Mantenaince')
		return mymantenaince