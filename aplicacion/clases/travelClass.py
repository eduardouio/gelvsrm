#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			travelClass.py
# Ubicacion		aplicacion/clases/travelClass.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
# +--------------------+----------------------+------+-----+-------------------+----------------+
#										Data Types
# +--------------------+----------------------+------+-----+-------------------+----------------+
# | Field              | Type                 | Null | Key | Default           | Extra          |
# +--------------------+----------------------+------+-----+-------------------+----------------+
# | id_viaje           | smallint(5) unsigned | NO   | PRI | NULL              | auto_increment |
# | fecha_salida       | date                 | YES  | MUL | NULL              |                |
# | fecha_regreso      | date                 | YES  |     | NULL              |                |
# | nro_vehiculos      | smallint(5) unsigned | NO   |     | NULL              |                |
# | provincias_destino | varchar(500)         | NO   |     | NULL              |                |
# | varlor_caja        | decimal(5,2)         | YES  |     | NULL              |                |
# | informe            | text                 | YES  |     | NULL              |                |
# | registro           | timestamp            | NO   |     | CURRENT_TIMESTAMP |                |
# +--------------------+----------------------+------+-----+-------------------+----------------+
import sys
sys.path.append('..')
from modelo.Modelo import DB

class Travel(object):
	"""representa la estructura de un Travel"""
	def __init__(self, id_viaje='',fecha_salida='',fecha_regreso='',nro_vehiculos='',
				provincias_destino='',varlor_caja='',informe='',registro=''):
		super(Travel, self).__init__()
		self.id_viaje = id_viaje
		self.fecha_salida = fecha_salida
		self.fecha_regreso = fecha_regreso
		self.nro_vehiculos = nro_vehiculos
		self.provincias_destino = provincias_destino
		self.varlor_caja = varlor_caja
		self.informe = informe
		self.registro = registro

class travelCatalog(object):
	"""Acciones sobre el objeto catálogo"""
	def __init__(self):
		super(travelCatalog, self).__init__()
		self.table =  'viaje'
		self.MyDb = DB()

	def getTravels(self,travel=''):
		'''Obtiene un listado viajes
		@param = (str) id_viaje
		@return (obj) | list(obj) '''
		if travel:
			mytravel = Travel()
			condition = ' id_viaje = ' + str(travel)
			result = self.MyDb.selectQuery(self.table,'',condition)

			while result.next():
				mytravel.id_viaje = str(result.value(0))
				mytravel.fecha_salida = str(result.value(1))
				mytravel.fecha_regreso = str(result.value(2))
				mytravel.nro_vehiculos = str(result.value(3))
				mytravel.provincias_destino = str(result.value(4))
				mytravel.varlor_caja = str(result.value(5))
				mytravel.informe = str(result.value(6))
				mytravel.registro = str(result.value(7))

			return mytravel

		else:
			travels = []
			result = self.MyDb.selectQuery(self.table)
			while result.next():
				mytravel = Travel()
				mytravel.id_viaje = str(result.value(0))
				mytravel.fecha_salida = str(result.value(1))
				mytravel.fecha_regreso = str(result.value(2))
				mytravel.nro_vehiculos = str(result.value(3))
				mytravel.provincias_destino = str(result.value(4))
				mytravel.varlor_caja = str(result.value(5))
				mytravel.informe = str(result.value(6))
				mytravel.registro = str(result.value(7))
				travels.append(mytravel)

			return travels

	def createTravel(self, travel):
		'''Creae un  viaje
		@param (obj) tipo travel
		@return (bool) | str'''

		values = {
			'fecha_salida' :travel.fecha_salida,
			'fecha_regreso' :travel.fecha_regreso,
			'nro_vehiculos' :travel.nro_vehiculos,
			'provincias_destino' :travel.provincias_destino,
			'varlor_caja' :travel.varlor_caja,
			'informe' :travel.informe,
			'registro' :travel.registro
		}

		result = self.MyDb.createQuery(self.table,value)

		if(result.numRowsAffected()>0):
			return str(result.lastInsertId())
		else:
			return False

	def updateTravel(self,oldTravel, travel):
		'''Actualiza un viaje
		@param (obj) travel
		@param (obj) travel
		@return (bool)
		'''
		condition = ' id_viaje = ' + str(oldTravel.id_viaje)
		values = {			
			'fecha_salida' :travel.fecha_salida,
			'fecha_regreso' :travel.fecha_regreso,
			'nro_vehiculos' :travel.nro_vehiculos,
			'provincias_destino' :travel.provincias_destino,
			'varlor_caja' :travel.varlor_caja,
			'informe' :travel.informe,
			'registro' :travel.registro	
		}

		result = MyDb.updateQuery(self.table,values,condition)

		if(result.numRowsAffected()>0):
			return True
		else:
			return False

	def deleteTravel(self, travel):
		'''Elimina un viaje de la tabla
		@param (obj) travel
		@return (boo)'''
		
		condition = ' id_viaje = ' + str(travel.id_viaje)
		result = self.MyDb.deleteQuery(self.table,condition)

		if(result.numRowsAffected()>0):
			return str(result.lastInsertId())
		else:
			return False

	def findTravel(self,condition):
		'''Busca un viaje'''
		pass

# +------------+--------------+------+-----+-------------------+-----------------------------+
# 							Funcionalidades para la tabla hija viajes_tecnico
#								Implementacion de viajes para tecnico
# +------------+--------------+------+-----+-------------------+-----------------------------+

	def getTravelTechnicals(self,technical=''):
		'''Obtiene un tecnico o listado de ellos
		@param (str) id_tecnico'''		
		#primero recuperamos los identificadores de los tecnicos
		idtravels = []
		condition = ' id_tecnico = ' + str(technical)
		result = self.MyDb.selectQuery(' tecnico_viaje = ','',condition)
		while result.next():
			idtravels.append(str(result.value(1)))				

		mytravels = []			
		# armamos los objetos tecnicos que pertenecen a un viaje
		for x in idtravels:
			idtravels.append(self.getTravels(str(x)))

		return mytravels