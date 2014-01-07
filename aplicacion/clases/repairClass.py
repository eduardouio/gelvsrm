#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			reairClass.py
# Ubicacion		aplicacion/clases/reairClass.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
# +---------------+----------------------+------+-----+-------------------+-----------------------------+
# 											Data Types
# +---------------+----------------------+------+-----+-------------------+-----------------------------+
# | Field         | Type                 | Null | Key | Default           | Extra                       |
# +---------------+----------------------+------+-----+-------------------+-----------------------------+
# | id_reparacion | smallint(5) unsigned | NO   | PRI | NULL              | auto_increment              |
# | id_viaje      | smallint(5) unsigned | NO   | MUL | NULL              |                             |
# | id_vehiculo   | char(17)             | NO   | MUL | NULL              |                             |
# | id_ciudad     | smallint(5) unsigned | YES  | MUL | NULL              |                             |
# | periodo       | smallint(5) unsigned | NO   |     | NULL              |                             |
# | kilometros    | varchar(45)          | NO   |     | NULL              |                             |
# | fecha_entrada | datetime             | NO   |     | NULL              |                             |
# | fecha_salida  | datetime             | YES  |     | NULL              |                             |
# | notas         | mediumtext           | YES  |     | NULL              |                             |
# | registro      | timestamp            | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
# +---------------+----------------------+------+-----+-------------------+-----------------------------+

import sys
sys.path.append('..')
from modelo.Modelo import DB

class Repair(object):
	"""estructura para Repair"""
	def __init__(self, id_reparacion='',id_viaje='',id_vehiculo='',id_ciudad='', periodo='',
					kilometros='',fecha_salida='',fecha_entrada='',notas='',registro=''):
		super(Repair, self).__init__()
		self.id_reparacion = id_reparacion
		self.id_viaje = id_viaje
		self.id_vehiculo = id_vehiculo
		self.id_ciudad = id_ciudad
		self.periodo = periodo
		self.kilometros = kilometros
		self.fecha_salida = fecha_salida
		self.fecha_entrada = fecha_entrada
		self.notas = notas
		self.registro = registro


class repairCatalog(object):
	"""acciones para la clase Catalog"""
	def __init__(self):
		super(repairCatalog, self).__init__()
		self.MyDb = DB()
		self.table = 'reparacion'

	def getRepairs(self, repair=''):
		'''Obtiene un listado de reparacion
		@param (str) repair
		@return (obj) | list(obj)
		'''
		if repair:
			myrepair = Repair()
			condition = ' id_reparacion = ' + str(repair)
			result = self.MyDb.selectQuery(self.table,'',condition)
			while result.next():
				myrepair.id_reparacion = str(result.value(0))
				myrepair.id_viaje = str(result.value(1))
				myrepair.id_vehiculo = str(result.value(2))
				myrepair.id_ciudad = str(result.value(3))
				myrepair.periodo = str(result.value(4))
				myrepair.kilometros = str(result.value(5))
				myrepair.fecha_salida = str(result.value(6))
				myrepair.fecha_entrada = str(result.value(7))
				myrepair.notas = str(result.value(8))
				myrepair.registro = str(result.value(9))

			return myrepair

		else:
			repairs = []
			result = self.MyDb.selectQuery(self.table)
			while result.next():
				myrepair = Repair()
				myrepair.id_reparacion = str(result.value(0))
				myrepair.id_viaje = str(result.value(1))
				myrepair.id_vehiculo = str(result.value(2))
				myrepair.id_ciudad = str(result.value(3))
				myrepair.periodo = str(result.value(4))
				myrepair.kilometros = str(result.value(5))
				myrepair.fecha_salida = str(result.value(6))
				myrepair.fecha_entrada = str(result.value(7))
				myrepair.notas = str(result.value(8))
				myrepair.registro = str(result.value(9))
				repairs.append(myrepair)

			return repairs


	def createRepair(self, repair):
		''''Crea una reparacion
		@param (obj) Repair 
		@return (bool) | (int)'''

		values = {
			'id_reparacion' : repair.id_reparacion,
			'id_viaje' : repair.id_viaje,
			'id_vehiculo' : repair.id_vehiculo,
			'id_ciudad' : repair.id_ciudad,
			'periodo' : repair.periodo,
			'kilometros' : repair.kilometros,
			'fecha_salida' : repair.fecha_salida,
			'fecha_entrada' : repair.fecha_entrada,
			'notas' : repair.notas,
			'registro' : repair.registro
		}

		result = self.MyDb.insertQuery(self.table, values)

		if(result.numRowsAffected()>0):
			return str(result.lastInsertId())
		else:
			return False

	def updateRepair(self,oldRepair,repair):
		'''Actualiza una reparacion
		@param (obj) repair
		@param (obj) repair
		@return (bool)
		'''
		condition = ' id_reparacion = ' + str(oldRepair.id_reparacion)

		values = {
			'id_viaje' : repair.id_viaje,
			'id_vehiculo' : repair.id_vehiculo,
			'id_ciudad' : repair.id_ciudad,
			'periodo' : repair.periodo,
			'kilometros' : repair.kilometros,
			'fecha_salida' : repair.fecha_salida,
			'fecha_entrada' : repair.fecha_entrada,
			'notas' : repair.notas,
			'registro' : repair.registro

		result = self.MyDb.updateQuery(self.table,values,condition)

		if(result.numRowsAffected()>0):
			return True
		else:
			return False

	def deleteRepair(self,repair):
		'''Elimina una reparacion
		@param (obj) repair
		@return (bool)'''
		condition = ' id_reparacion = ' + str(repair.id_reparacion)

		result = self.MyDb.deleteQuery(self.table,condition)		
		if(result.numRowsAffected()>0):
			return True
		else:
			return False

	def findRepair(self,condition=''):
		'''Busca una reparacion'''
		pass