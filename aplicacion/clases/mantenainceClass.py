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
		self.fecha = fecha
		self.kilometros = kilometros
		self.notas = notas
		self.registro = registro


class mantenainceCatalog(object):
	"""docstring for mantenainceCatalog"""
	def __init__(self):
		super(mantenainceCatalog, self).__init__()
		self.MyDb = DB()
		self.table = 'mantenimiento'


	def getMantenaince(self,mantenaince=''):
		'''Obtiene un listado de mantenimientos o mantenimiento
		@param = id_mantenimiento'''

		if mantenaince:
			condition = ' id_mantenimiento = ' + str(mantenaince)
			result = self.MyDb.selectQuery(self.table,'',condition)
			mymantenaince = Mantenaince()
			while result.next():
				mymantenaince.id_mantenimiento = str(result.value(0))
				mymantenaince.id_viaje = str(result.value(1))
				mymantenaince.id_vehiculo = str(result.value(2))
				mymantenaince.id_ciudad = str(result.value(3))
				mymantenaince.periodo = str(result.value(4))
				mymantenaince.fecha = str(result.value(5))
				mymantenaince.kilometros = str(result.value(6))
				mymantenaince.notas = str(result.value(7))
				mymantenaince.registro = str(result.value(8))
			
			return mymantenaince

		else:

			mantenainces = []
			result = self.selectQuery(self.table)
			while result.next():
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
				mantenainces.append(mymantenaince)

			return mantenainces

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
		'notas': str(mantenaince.notas),
		'registro': str(mantenaince.registro)
		}

		result = self.createQuery(self.table,values)

		if(result.numRowsAffected()>0):
			return str(result.lastInsertId())
		else:
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
		'notas': str(mantenaince.notas),
		'registro': str(mantenaince.registro)
		}
		condition = ' id_mantenimiento = ' + str(oldMantenaince.id_mantenimiento)

		result = self.MyDb.updateQuery(self.table,values,condition)

		if(result.numRowsAffected()>0):
			return True
		else:
			return False

	def deleteMantenaince(self,mantenaince):
		'''Elimina un mantenimiento'''
		condition = ' id_mantenimiento = ' + str(mantenaince.id_mantenimiento)
		result = self.MyDb.dleteQuery(self.table,condition)

		if(result.numRowsAffected()>0):
			return True
		else:
			return False

	def findMantenaince(self,condition=''):
		'''Busca un mantenimiento'''
		pass