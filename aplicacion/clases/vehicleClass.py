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
# | modelo      | varchar(45)          | YES  |     | NULL              |                             |
# | nro_motor   | varchar(25)          | YES  |     | NULL              |                             |
# | ingreso     | datetime             | YES  |     | NULL              |                             |
# | notas       | mediumtext           | YES  |     | NULL              |                             |
# | registro    | timestamp            | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
# +-------------+----------------------+------+-----+-------------------+-----------------------------+

import sys
sys.path.append('..')
from modelo.Modelo import DB

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
		self.ingreso = ingreso
		self.notas = notas
		self.registro = registro
		

class vehicleCatalog(object):
	"""operaciones sobre vehicleCatalog"""
	def __init__(self):
		super(vehicleCatalog, self).__init__()
		self.table = 'vehiculo'
		self.MyDb = DB()

	def getVehicles(self, vehicle = ''):
		'''Obtiene un vehiculo o listado de ellos
		@param (str) id_vehiculo
		@return (obj) list(obj)
		'''
		if vehicle:
			myvehicle = Vehicle()
			condition = ' id_vehiculo = ' + str(vehicle)
			result = self.MyDb.selectQuery(self.table,'',condition)
			while result.next():
				myvehicle.id_vehiculo = str(result.value(0))
				myvehicle.id_cliente = str(result.value(1))
				myvehicle.id_contacto = str(result.value(2))
				myvehicle.id_ciudad = str(result.value(3))
				myvehicle.modelo = str(result.value(4)
				myvehicle.nro_motor = str(result.value(5))
				myvehicle.ingreso = str(result.value(6))
				myvehicle.notas = str(result.value(7))
				myvehicle.registro = str(result.value(8))

			return myvehicle
		else:
			vehicles = []
			result = self.MyDb.selectQuery(self.table)
			while result.next():
				myvehicle = Vehicle()
				myvehicle.id_vehiculo = str(result.value(0))
				myvehicle.id_cliente = str(result.value(1))
				myvehicle.id_contacto = str(result.value(2))
				myvehicle.id_ciudad = str(result.value(3))
				myvehicle.modelo = str(result.value(4)
				myvehicle.nro_motor = str(result.value(5))
				myvehicle.ingreso = str(result.value(6))
				myvehicle.notas = str(result.value(7))
				myvehicle.registro = str(result.value(8))

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
			'notas' : vehicle.notas,
			'registro' : vehicle.registro
		}

		result = self.MyDb.createQuery(self.table,values)

		if(result.numRowsAffected()>0):
			return str(result.lastInsertId())
		else:
			return False

	def updateVehicle(self,old_vehicle,vehicle):
		'''Actualiza un vehiculo
		@param (obj)  vehicle
		@param (obj) vehicle
		@return (boo)
		'''
		condition = ' id_vehiculo = ' + str(old_vehicle.id_vehiculo)
		values = {
			'id_vehiculo' : vehicle.id_vehiculo,
			'id_cliente' : vehicle.id_cliente,
			'id_contacto' : vehicle.id_contacto,
			'id_ciudad' : vehicle.id_ciudad,
			'modelo' : vehicle.modelo,
			'nro_motor' : vehicle.nro_motor,
			'ingreso' : vehicle.ingreso,
			'notas' : vehicle.notas,
			'registro' : vehicle.registro
		}

		result = self.MyDb.updateQuery(self.table,values,condition)

		if (result.numRowsAffected() > 0):
			return True
		else:
			return False

	def deleteVehicle(self,vehicle):
		'''Elimina un vehiculo
		@param (obj) vehicle
		@return bool
		'''
		condition = ' id_vehiculo =' + str(vehicle.id_vehiculo)
		result = self.deleteQuery(self.table,condition)

		if (result.numRowsAffected() > 0):
			return True
		else:
			return False

	def finVehicle(self,condition=''):
		'''Busca un vehiculo'''
		pass