#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			cityClass.py
# Ubicacion		aplicacion/clases/cityClass.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
# +-----------------------------------------------------------------------------+
# |									Data Type									|
# +--------------+----------------------+------+-----+---------+----------------+
# | Field        | Type                 | Null | Key | Default | Extra          |
# +--------------+----------------------+------+-----+---------+----------------+
# | id_ciudad    | smallint(5) unsigned | NO   | PRI | NULL    | auto_increment |
# | id_provincia | smallint(5) unsigned | NO   | MUL | NULL    |                |
# | nombre       | varchar(100)         | YES  |     | NULL    |                |
# +--------------+----------------------+------+-----+---------+----------------+
import sys
sys.path.append('..')
from modelo.Modelo import DB
import stateClass

class City(object):
	"""Objeto que representa la estructura una ciudad"""
	def __init__(self, id_provincia='',id_ciudad='',nombre=''):
		'''Inizializacion de las propiedades de la clase'''
		super(City, self).__init__()
		self.id_ciudad = id_ciudad
		self.id_provincia = id_provincia
		self.nombre = nombre

		
class cityCatalog(object):
	"""Representa las operaciones sobre ciudad"""

	def __init__(self):
		'''Instancializacion de la clase creamos el objeto MyDB 
		creamos la variable con el nombre de la tabla
		'''
		super(cityCatalog, self).__init__()		
		self.table = 'ciudad'
		self.MyDB = DB()

	def getCities(self,state=''):
		'''Lista Las ciudades
		@param (obj) tipo city
		@param (str) tipo state
		@return (list(obj) | obj) tipo city'''
		if state:
			mycity = City()
			condition = 'id_provincia = ' + str(state)
			result = self.MyDB.selectQuery(self.table,'',condition)
			while result.next():
				mycity.id_ciudad = (str(result.value(0)))
				mycity.id_provincia = (str(result.value(1)))
				mycity.nombre = (str(result.value(2)))									
			return mycity()

		else:
			result = self.MyDB.selectQuery(self.table)
			cities = []

			while result.next():
				mycity = City()
				mycity.id_ciudad = (str(result.value(0)))
				mycity.id_provincia = (str(result.value(1)))
				mycity.nombre = (str(result.value(2)))						
				cities.append(mycity)	

			return cities
		
						
	def createCity(self,city):
		'''crea una ciudad
		@param (obj) tipo city
		@return (bool)|int'''
		values = {
				'id_provincia' : city.id_provincia,
				'nombre' : city.nombre
				}
		result = self.MyDB.insertQuery(self.table,values)
		if (result.numRowsAffected() > 0):
			return str(result.lastInsertId())
		else:
			return False
			
	def updateCity(self,oldcity, city):
		'''Actualiza una ciudad el identificador de la ciudad no cambia
		@param (obj) oldcity tipo city
		@param (obj) city tipo city
		@return (bool)'''
		condition = 'id_ciudad = ' + oldcity.id_ciudad()
		values = {
				'id_provincia' : city.id_provincia,
				'nombre' : city.nombre
				}

		result =  self.MyDB.updateQuery(self.table,values,condition)

		if (result.numRowsAffected() > 0):
			return True
		else:
			return False
		
	def deleteCity(self,city):
		'''Elimina una ciudad
		@param (obj) tipo city
		@return (bool)'''
		condition = 'id_ciudad = ' + str(city.id_ciudad)
		result = self.MyDB.deleteQuery(self.table, condition)

		if (result.numRowsAffected() > 0):
			return True
		else:
			return False
	
	def getCity(self, city):
		'''Obtiene los datos de una ciudad el objeto ciudad recibido solo administra en id_ciudad
		@param (str) tipo city
		@return (obj) tipo cityad 
		'''
		condition = 'id_ciudad = ' + str(city)
		result = self.MyDB.selectQuery(self.table,'',condition)
		mycity = City()
		while result.next():
			mycity.id_ciudad = (str(result.value(0)))
			mycity.id_provincia = (str(result.value(1)))
			mycity.nombre = (str(result.value(2)))
		
		return mycity

	def getStateCity(self,city):
		'''Obtiene al estado-provincua al que pertence una ciudad
		@param (obj) tipo city
		@return (obj) tipo state'''
		condition = 'id_ciudad = ' + str(city.id_ciudad())
		result = self.MyDB.selectQuery(self.table,'',condition)
		mystate = State()
		while result.next():
			mystate.id_provincia = str(result.value(0))
			mystate.nombre = str(result.value(1))

		return mystate

	
	def findCity(self,column, value):
		'''Busca una ciudad
		@param (str) columna estado (id_provincia = state)
		@return list(obj) tipo city'''
		cities = []
		content = [str(column),str(value)]
		result = self.MyDB.selectQuery(self.table,'','',content)
		while result.next():
			mycity = City()
			mycity.id_ciudad = (str(result.value(0)))
			mycity.id_provincia = (str(result.value(1)))
			mycity.nombre = (str(result.value(2)))
			cities.append(mycity)

		return cities