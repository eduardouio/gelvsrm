#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			vehicleClass.py
# Ubicacion		aplicacion/clases/vehicleClass.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
# +-------------+----------------------+------+-----+-------------------+-----------------------------+
# |											Data Types												  |
# +-------------+----------------------+------+-----+-------------------+-----------------------------+
# | Field       | Type                 | Null | Key | Default           | Extra                       |
# +-------------+----------------------+------+-----+-------------------+-----------------------------+
# | id_vehiculo | char(17)             | NO   | PRI | NULL              |                             |
# | id_cliente  | char(13)             | NO   | MUL | NULL              |                             |
# | id_contacto | smallint(5) unsigned | YES  | MUL | NULL              |                             |
# | id_ciudad   | smallint(5) unsigned | YES  | MUL | NULL              |                             |
# | modelo      | varchar(45)          | NO   |     | NULL              |                             |
# | nro_motor   | varchar(25)          | YES  |     | NULL              |                             |
# | ingreso     | datetime             | YES  |     | NULL              |                             |
# | notas       | mediumtext           | YES  |     | NULL              |                             |
# | registro    | timestamp            | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
# +-------------+----------------------+------+-----+-------------------+-----------------------------+

import sys
sys.path.append('..')
from modelo.Modelo import DB
from PyQt4.QtCore import QDateTime, QDate, QTime, qDebug

class Vehicle(object):
	"""Estructura de la clse  Vehicle"""
	def __init__(self, id_vehiculo='',id_cliente='',id_contacto='',id_ciudad='',
				modelo='',nro_motor='',ingreso='',notas='',registro=''):
		super(Vehicle, self).__init__()
		self.id_vehiculo = id_vehiculo
		self.id_cliente = id_cliente
		self.id_contacto = id_contacto
		self.id_ciudad = id_ciudad
		self.modelo = modelo
		self.nro_motor = nro_motor
		self.ingreso = QDate.currentDate()
		self.notas = notas
		self.registro = QDateTime().currentDatetime()
		qDebug('[Debug] se inicia la clase vehicle')
		

class vehicleCatalog(object):
	"""operaciones sobre vehicleCatalog"""

	def __init__(self):
		super(vehicleCatalog, self).__init__()
		self.table = 'vehiculo'
		self.MyDb = DB()
		qDebug('[Debug] se inicia la clase vehicleCatalog')


	def getVehicle(self, vehicle = ''):
		'''Obtiene un vehiculo o listado de ellos
		@param (str) id_vehiculo
		@return (obj) vehicle
		'''	
		condition = {' id_vehiculo = ' : str(vehicle)}
		result = self.MyDb.selectQuery(self.table,'',condition)
		qDebug('[Debug] la consulta retorna %s registros' % result.size())
		if result.next():
			return self.__setObj(result)
		else:
			qDebug('[Debug] problemas para retornar un vehiculo')
			return False

	
	def listVehicles(self):
		'''Retona un listado de los vehiculos
		@return lst(vehicle))'''
		vehicles = []
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] la consulta retorna %s registros' % result.size())
		while result.next():
			vehicles.append(self.__setObj(result))

		return vehicles


	def firstVehicle(self):
		'''retorna el primer Vehicle de la lista
		@return (obj) Vehicle'''		
		result = self.MyDB.selectQuery(self.table)
		qDebug('[Debug] Se toma el primer Vehicle de la lista')
		if result.first():
			return self.__setObj(result)
		else:
			return False


	def lastVehicle(self):
		'''retorna el ultimo Vehicle de la Lista
		@return (obj) Vehicle'''
		result = self.MyDB.selectQuery(self.table)
		qDebug('[Debug] Se toma ultimo Vehicle de la lista')
		if result.last():
			return self.__setObj(result)
		else:
			return False


	def findVehicle(self,condition):
		'''Busca un Vehicleo
		@param condition = {'id_tecnico like ' : '%4%'}
		@return list(obj) tipo Vehicle'''
		vehicles = []
		result = self.MyDB.selectQuery(self.table,'',condition)
		while result.next():
			vehicles.append(self.__setObj(result))

		return vehicles


	def createVehicle(self,vehicle):
		'''Crea un vehiclo
		@param (obj) vehicle
		@return (bool) | (int)'''
		values = {
			'id_vehiculo' : vehicle.id_vehiculo,
			'id_cliente' : vehicle.id_cliente,
			'id_contacto' : vehicle.id_contacto,
			'id_ciudad' : vehicle.id_ciudad,
			'modelo' : vehicle.modelo,
			'nro_motor' : vehicle.nro_motor,
			'ingreso' : vehicle.ingreso,
			'notas' : vehicle.notas			
		}

		result = self.MyDb.insertQuery(self.table,values)

		if(result.numRowsAffected()>0):
			qDebug('[Debug] se ingresa un vehiculo a la tabla')
			return str(result.lastInsertId())
		else:
			qDebug('[Debug] problemas para ingresar un vehiculo a la tabla')
			return False


	def updateVehicle(self,old_vehicle,vehicle):
		'''Actualiza un vehiculo
		@param (obj)  vehicle
		@param (obj) vehicle
		@return (boo)
		'''
		condition = {' id_vehiculo = ' : str(old_vehicle.id_vehiculo)}
		values = {
			'id_vehiculo' : vehicle.id_vehiculo,
			'id_cliente' : vehicle.id_cliente,
			'id_contacto' : vehicle.id_contacto,
			'id_ciudad' : vehicle.id_ciudad,
			'modelo' : vehicle.modelo,
			'nro_motor' : vehicle.nro_motor,
			'ingreso' : vehicle.ingreso,
			'notas' : vehicle.notas			
		}

		result = self.MyDb.updateQuery(self.table,values,condition)

		if (result.numRowsAffected() > 0):
			qDebug('[Debug] se Actualiza un vehiculo a la tabla')
			return True
		else:
			qDebug('[Debug] problemas para actualizar un vehiculo a la tabla')
			return False


	def deleteVehicle(self,vehicle):
		'''Elimina un vehiculo
		@param (obj) vehicle
		@return bool
		'''
		condition = {' id_vehiculo =' : str(vehicle.id_vehiculo)}
		result = self.deleteQuery(self.table,condition)

		if (result.numRowsAffected() > 0):
			qDebug('[Debug] se elimina un vehiculo a la tabla')
			return True
		else:
			qDebug('[Debug] priblemas para eliminar un vehiculo a la tabla')
			return False


	def __setObj(self, result):
		'''Crea un objeto tipo vehicle y lo retorna
		@param (obj) result
		@return (obj) vehicle'''
		myvehicle = Vehicle()
		myvehicle.id_vehiculo = str(result.value(0))
		myvehicle.id_cliente = str(result.value(1))
		myvehicle.id_contacto = str(result.value(2))
		myvehicle.id_ciudad = str(result.value(3))
		myvehicle.modelo = str(result.value(4))
		myvehicle.nro_motor = str(result.value(5))
		myvehicle.ingreso = str(result.value(6))
		myvehicle.notas = str(result.value(7))
		myvehicle.registro = str(result.value(8))

		if not(isinstance(myvehicle.id_contacto,str)):
			myvehicle.id_contacto=''

		if not(isinstance(myvehicle.id_ciudad,str)):
			myvehicle.id_ciudad=''

		if not(isinstance(myvehicle.nro_motor,str)):
			myvehicle.nro_motor=''

		if not(isinstance(myvehicle.ingreso,str)):
			myvehicle.ingreso=''

		if not(isinstance(myvehicle.notas,str)):
			myvehicle.notas=''

		qDebug('[Debug] se crea un objeto vehiculo')
		return myvehicle

# | id_contacto | smallint(5) unsigned | YES  | MUL | NULL              |                             |
# | id_ciudad   | smallint(5) unsigned | YES  | MUL | NULL              |                             |
# | nro_motor   | varchar(25)          | YES  |     | NULL              |                             |
# | ingreso     | datetime             | YES  |     | NULL              |                             |
# | notas       | mediumtext           | YES  |     | NULL              |                             |