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
from PyQt4.QtCore import QDateTime, QDate, QTime, qDebug

class City(object):
	"""Objeto que representa la estructura una ciudad"""
	def __init__(self, id_provincia=int(),id_ciudad=int(),nombre=''):
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


	def getCity(self,idCity):
		'''Lista Las ciudades		
		@param (str) id_ciudad
		@return (obj) tipo city'''	
		condition = {'id_ciudad = ' : str(idCity)}
		result = self.MyDB.selectQuery(self.table,'',condition)
		qDebug('[Debug] get city la consulta retorno %s regitros'% result.size())
		if result.next():
			return self.__setObj(result)
		else:
			return False


	def listCities(self):
		'''Lista todas ciudades 
		@return lst(obj) tipo city'''
		cities = []
		result = self.MyDB.selectQuery(self.table)
		qDebug('[Debug] list cityes la consulta retorno %s regitros'% result.size())
		while result.next():			
			cities.append(self.__setObj(result))

		return cities


	def listCitiesState(self,idState):
		'''Lista todas ciudades de una provincia
		@return lst(obj) tipo city'''
		cities = []
		condition = {'id_provincia = ' : str(idState)}
		result = self.MyDB.selectQuery(self.table,'',condition)
		qDebug('[Debug] list cityesstatela consulta retorno %s regitros'% result.size())
		while result.next():			
			cities.append(self.__setObj(result))	

		return cities
	

	def firstCity(self):
		'''retorna la primera ciudad de la Lista
		@return (obj) city'''		
		result = self.MyDB.selectQuery(self.table)
		qDebug('[Debug] Se toma la primera ciudad de la lista')
		if result.first():
			return self.__setObj(result)
		else:
			return False


	def lastCity(self):
		'''retorna la ultima ciudad de la Lista
		@return (obj) city'''
		result = self.MyDB.selectQuery(self.table)
		qDebug('[Debug] Se toma la ultima ciudad de la lista')
		if result.last():
			return self.__setObj(result)
		else:
			return False
	

	def findCity(self,condition):
		'''Busca una ciudad
		@param condition = {'id_tecnico like ' : '%4%'}
		@return list(obj) tipo city'''
		cities = []
		result = self.MyDB.selectQuery(self.table,'',condition)
		while result.next():
			cities.append(self.__setObj(result))

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
			qDebug('[Debug] se inserto correctamente una ciudad')
			return str(result.lastInsertId())
		else:
			qDebug('[Debug] problemas para insertar una ciudad')
			return False

			
	def updateCity(self,oldcity, city):
		'''Actualiza una ciudad el identificador de la ciudad no cambia
		@param (obj) oldcity tipo city
		@param (obj) city tipo city
		@return (bool)'''
		condition = {'id_ciudad = ' : str(oldcity.id_ciudad)}
		values = {
				'id_provincia' : city.id_provincia,
				'nombre' : city.nombre
				}
		result =  self.MyDB.updateQuery(self.table,values,condition)

		if (result.numRowsAffected() > 0):
			qDebug('[Debug] se Actualiza correctamente una ciudad')
			return True
		else:
			qDebug('[Debug] problemas para Actualizar correctamente una ciudad')
			return False

		
	def deleteCity(self,city):
		'''Elimina una ciudad
		@param (obj) tipo city
		@return (bool)'''				
		print(city.id_ciudad)
		condition = {'id_ciudad = ' : city.id_ciudad}
		print(condition)
		result = self.MyDB.deleteQuery(self.table, condition)

		if (result.numRowsAffected() > 0):
			qDebug('[Debug] se Elimina correctamente una ciudad')
			return True
		else:
			qDebug('[Debug] No se Elimina correctamente una ciudad')			
			return False


	def __setObj(self,result):
		'''Crea un objeto tipo city
		@return (obj) city'''
		mycity = City()
		mycity.id_ciudad = str(result.value(0))
		mycity.id_provincia = str(result.value(1)) 
		mycity.nombre = str(result.value(2))
		qDebug('[Debug] se crea una ciudad')

		return mycity