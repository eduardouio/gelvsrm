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

class City(object):
	"""Objeto que representa la estructura una ciudad"""
	def __init__(self, id_provincia='',id_ciudad='',nombre=''):
		'''Inizializacion de las propiedades de la clase'''
		super(City, self).__init__()
		self.id_provincia = id_provincia
		self.id_ciudad = id_ciudad
		self.nombre = nombre

		
class cityCatalog(object):
	"""Representa las operaciones sobre ciudad"""

	def __init__(self):
		'''Instancializacion de la clase creamos el objeto MyDB 
		creamos la variable con el nombre de la tabla
		'''
		super(cityClass, self).__init__()		
		self.table = 'ciudad'
		self.MyDB = DB()

	def getCities(self):
		'''Lista Las ciudades
		@param (obj) tipo city
		@return (list(obj)) tipo city'''
		Ciudades = []		
				
	def createCity(self,city):
		'''crea una ciudad
		@param (obj) tipo city
		@return (bool)'''
			
	def updateCity(self,city):
		'''Actualiza una ciudad el identificador de la ciudad no cambia
		@param (obj) tipo city
		@return (bool)'''
		
	def deleteCity(self,city):
		'''Elimina una ciudad
		@param (obj) tipo city
		@return (bool)'''
	
	def getCity(self, city):
		'''Obtiene los datos de una ciudad el objeto ciudad recibido solo administra en id_ciudad
		@param (obj) tipo city
		@return (obj) tipo cityad 
		'''

	def getStateCity(self,city):
		'''Obtiene al estado-provincua al que pertence una ciudad
		@param (obj) tipo city
		@return (obj) tipo state
		pendiente'''
	
	def findCity(self, columns,condition, valor):
		'''Busca una ciudad
		@param (obj) tipo city
		@return (obj) tipo city
		pendiente'''