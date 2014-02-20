#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			maintenanceClass.py
# Ubicacion		aplicacion/clases/maintenanceClass.py
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


class Maintenance(object):
	"""Estructura para Maintenance"""
	def __init__(self, id_mantenimiento=int(),id_viaje=int(),id_vehiculo='',id_ciudad=int(),
					periodo=int(),fecha='',kilometros='',notas='',registro=''):
		super(Maintenance, self).__init__()
		self.id_mantenimiento = id_mantenimiento
		self.id_viaje = id_viaje
		self.id_vehiculo = id_vehiculo
		self.id_ciudad = id_ciudad
		self.periodo = periodo
		self.fecha = QDate().currentDate()
		self.kilometros = kilometros
		self.notas = notas
		self.registro = QDateTime().currentDateTiem()
		qDebug('[Debug] se inicia la clase mantenimiento')


class maintenanceCatalog(object):
	"""docstring for maintenanceCatalog"""

	def __init__(self):
		super(maintenanceCatalog, self).__init__()
		self.MyDb = DB()
		self.table = 'mantenimiento'
		qDebug('[Debug] se incia la clase maintenanceCatalog')


	def getMaintenance(self,IdMaintenance):
		'''Obtiene un listado de mantenimientos o mantenimiento
		@param = id_mantenimiento'''		
		condition = {' id_mantenimiento = ' : str(IdMaintenance)}
		result = self.MyDb.selectQuery(self.table,'',condition)
		qDebug('[Debug] se encuentran %s registros'% result.size())
		if result.next():
			return self.__setObj(result)
		else:
			qDebug('[Debug] problemas para devolver un mantenimiento')
			return False
			

	def listMaintenances(self):
		'''Lista todos los mantenimientos
		@return lst(obj) Maintenance'''
		maintenances = []
		result = self.selectQuery(self.table)
		qDebug('[Debug] se encuentran %s registros'% result.size())
		while result.next():			
			maintenances.append(self.__setObj(result))

		return maintenances


	def firstMaintenance(self):
		'''retorna el primer Maintenanceo de la lista
		@return (obj) Maintenance'''		
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] Se toma el primer Maintenance de la lista')
		if result.first():
			return self.__setObj(result)
		else:
			return False


	def lastMaintenance(self):
		'''retorna el ultimo Maintenance de la Lista
		@return (obj) Maintenance'''
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] Se toma ultimo Maintenance de la lista')
		if result.last():
			return self.__setObj(result)
		else:
			return False


	def findMaintenance(self,condition):
		'''Busca un Maintenanceo
		@param condition = {'id_tecnico like ' : '%4%'}
		@return list(obj) tipo Maintenance'''
		Maintenances = []
		result = self.MyDb.selectQuery(self.table,'',condition)
		while result.next():
			Maintenances.append(self.__setObj(result))

		return Maintenances


	def createMaintenaince(self,maintenance):
		'''Crea un mantenimiento
		@param (obj) maintenance
		@return (bool) | (int)'''
		values = {
		'id_viaje': str(maintenance.id_viaje),
		'id_vehiculo': str(maintenance.id_vehiculo),
		'id_ciudad': str(maintenance.id_ciudad),
		'periodo': str(maintenance.periodo),
		'fecha': str(maintenance.fecha),
		'kilometros': str(maintenance.kilometros),
		'notas': str(maintenance.notas)		
		}

		result = self.insertQuery(self.table,values)

		if(result.numRowsAffected()>0):
			qDebug('[Debug] se crea un mantenimiento en la base')
			return str(result.lastInsertId())
		else:
			qDebug('[Debug] No se crea un mantenimiento en la base')
			return False


	def updateMaintenance(self,oldMaintenance, maintenance):
		'''Actualiza un mantenimiento
		@param (obj) maintenance
		@param (obj) maintenance 
		@return (bool)
		'''
		values = {
		'id_vehiculo': str(maintenance.id_vehiculo),
		'id_ciudad': str(maintenance.id_ciudad),
		'periodo': str(maintenance.periodo),
		'fecha': str(maintenance.fecha),
		'kilometros': str(maintenance.kilometros),
		'notas': str(maintenance.notas)		
		}
		
		condition = {' id_mantenimiento = ' : str(oldMaintenance.id_mantenimiento)}

		result = self.MyDb.updateQuery(self.table,values,condition)

		if(result.numRowsAffected()>0):
			qDebug('[Debug] Se actualiza un mantenimiento en la base')
			return True
		else:
			qDebug('[Debug] No se Actualiza un mantenimiento en la base')
			return False


	def deleteMaintenance(self,maintenance):
		'''Elimina un mantenimiento completo incluido los items de mantenimiento
		@para maintenance obj Maintenance'''
		condition = {' id_mantenimiento = ' : str(maintenance.id_mantenimiento)}
		from maintenanceItemClass import MaintenanceItemCatalog
		itemsmantenimiento = MaintenanceItemCatalog()
		if (itemsmantenimiento.deleteMaintenanceItems(maintenance.id_mantenimiento)):
			result = self.MyDb.dleteQuery(self.table,condition)
			if(result.numRowsAffected()>0):
				qDebug('[Debug] Se Elimina un mantenimiento en la base')
				return True
			else:
				qDebug('[Debug] No se puede eliminar un mantenimiento en la base')
				return False
		else:
			qDebug('[Debug] no se pudo eliminar los items del mantenimiento')
			return False


	def __setObj(self, result):
		'''Crea un objeto tipo Maintenance y lo retorna
		@param (obj) result
		@return (obj) Maintenance'''
		mymaintenance = Maintenance()
		mymaintenance.id_mantenimiento = str(result.value(0))
		mymaintenance.id_viaje = str(result.value(1))
		mymaintenance.id_vehiculo = str(result.value(2))
		mymaintenance.id_ciudad = str(result.value(3))
		mymaintenance.periodo = str(result.value(4))
		mymaintenance.fecha = str(result.value(5))
		mymaintenance.kilometros = str(result.value(6))
		mymaintenance.notas = str(result.value(7))
		mymaintenance.registro = str(result.value(8))

		#Se validan los campos NULL		
		if(mymaintenance.id_ciudad.find('PyQt4.QtCore.')):
			mymaintenance.id_ciudad = None

		if(mymaintenance.notas.find('PyQt4.QtCore.')):
			mymaintenance.notas = None
		
		qDebug('[Debug] se crea un objeto Maintenance validando los campos NULL')
		return mymaintenance