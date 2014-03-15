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
# | fecha_salida       | date                 | NO   | MUL | NULL              |                |
# | fecha_regreso      | date                 | NO   |     | NULL              |                |
# | nro_vehiculos      | smallint(5) unsigned | NO   |     | NULL              |                |
# | provincias_destino | varchar(500)         | NO   |     | NULL              |                |
# | varlor_caja        | decimal(5,2)         | NO   |     | NULL              |                |
# | informe            | text                 | NO   |     | NULL              |                |
# | registro           | timestamp            | NO   |     | CURRENT_TIMESTAMP |                |
# +--------------------+----------------------+------+-----+-------------------+----------------+
import sys
sys.path.append('..')
from modelo.Modelo import DB
from PyQt5.QtCore import QDateTime, QDate, QTime, qDebug

class Travel(object):
	"""representa la estructura de un Travel"""
	def __init__(self, id_viaje=int(),fecha_salida='',fecha_regreso='',nro_vehiculos=int(),
				provincias_destino='',varlor_caja=float(),informe='',registro=''):
		super(Travel, self).__init__()
		self.id_viaje = id_viaje
		self.fecha_salida = QDate().currentDate()
		self.fecha_regreso = QDate().currentDate()
		self.nro_vehiculos = nro_vehiculos
		self.provincias_destino = provincias_destino
		self.varlor_caja = varlor_caja
		self.informe = informe
		self.registro = QDateTime().currentDateTime()
		qDebug('[Debug] se inicia la clase travel')

class travelCatalog(object):
	"""Acciones sobre el objeto catálogo"""

	def __init__(self):
		super(travelCatalog, self).__init__()
		self.table =  'viaje'
		self.MyDb = DB()
		qDebug('[Debug] se inicia la clase travelCatalog')

	def getTravel(self,idTravel):
		'''Obtiene un listado viajes
		@param = (str) id_viaje
		@return (obj) | list(obj) '''		
		condition = {' id_viaje = ' : str(idTravel)}
		result = self.MyDb.selectQuery(self.table,'',condition)
		qDebug('[Debug] la consulta retorno %s registros'% result.size())
		if result.next():
			return self.__setObj(result)
		else:
			qDebug('[Debug] No se retorna ningun viaje')
			return False
		

	def listTravels(self):
		'''Retorna un listado de todos los viajes
		@return lst(travel)'''
			travels = []
			result = self.MyDb.selectQuery(self.table)
			qDebug('[Debug] la consulta retorno %s registros'% result.size())
			while result.next():				
				travels.append(self.__setObj(result))

			return travels


	def firstTravel(self):
		'''retorna el primer Trave de la lista
		@return (obj) Travel'''		
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] Se toma el primer Travel de la lista')
		if result.first():
			return self.__setObj(result)
		else:
			return False


	def lastTravel(self):
		'''retorna el ultimo Travel de la Lista
		@return (obj) Travel'''
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] Se toma ultimo Travel de la lista')
		if result.last():
			return self.__setObj(result)
		else:
			return False


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
			'informe' :travel.informe			
		}
		result = self.MyDb.insertQuery(self.table,value)
		if(result.numRowsAffected()>0):
			qDebug('[Debug] se crea un viaje en la tabla')
			return str(result.lastInsertId())
		else:
			qDebug('[Debug] no se crea un viaje en la tabla')
			return False


	def updateTravel(self,oldTravel, travel):
		'''Actualiza un viaje
		@param (obj) travel
		@param (obj) travel
		@return (bool)
		'''
		condition = {' id_viaje = ' : str(oldTravel.id_viaje)}
		values = {			
			'fecha_salida' :travel.fecha_salida,
			'fecha_regreso' :travel.fecha_regreso,
			'nro_vehiculos' :travel.nro_vehiculos,
			'provincias_destino' :travel.provincias_destino,
			'varlor_caja' :travel.varlor_caja,
			'informe' :travel.informe			
		}

		result = MyDb.updateQuery(self.table,values,condition)

		if(result.numRowsAffected()>0):
			qDebug('[Debug] se actualiza un viaje en la tabla')
			return True
		else:
			qDebug('[Debug] no se actualiza un viaje en la tabla')			
			return False


	def deleteTravel(self, travel):
		'''Elimina un viaje de la tabla
		@param (obj) travel
		@return (bool)'''
		
		condition = {' id_viaje = ' : str(travel.id_viaje)}
		result = self.MyDb.deleteQuery(self.table,condition)

		if(result.numRowsAffected()>0):
			qDebug('[Debug] se elimina un viaje en la tabla')			
			return str(result.lastInsertId())
		else:
			qDebug('[Debug] no se elimina un viaje en la tabla')			
			return False



	def __setObj(self, result):
		'''Crea un objeto tipo travel y lo retorna
		@param (obj) result
		@return (obj) Travel'''
		mytravel = Travel()
		mytravel.id_viaje = str(result.value(0))
		mytravel.fecha_salida = str(result.value(1))
		mytravel.fecha_regreso = str(result.value(2))
		mytravel.nro_vehiculos = str(result.value(3))
		mytravel.provincias_destino = str(result.value(4))
		mytravel.varlor_caja = str(result.value(5))
		mytravel.informe = str(result.value(6))
		mytravel.registro = str(result.value(7))

		qDebug('[Debug] se crea un objeto viaje validando los campos NULL')
		return mytravel