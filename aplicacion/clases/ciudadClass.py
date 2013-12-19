#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			cuidadClass.py
# Ubicacion		aplicacion/clases/cuidadClass.py
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
#coneccion a la base de datos
from modelo import conn
#modelo a la base de datos
from modelo.Modelo import DB
from PyQt4 import QtSql

class cityClass(object):
	"""Representa a la entidad ciudad del modelo"""

	def __init__(self):
		'''Instancializacion de la clase creamos el objeto MyDB 
		creamos la variable con el nombre de la tabla
		'''
		super(cityClass, self).__init__()
		self.table = 'ciudad'
		self.MyDB = DB()

	def listCitiesPro(self,colums='',id_provincia=''):
		'''Lista las ciudaes de una provincia o todas las ciudades
		@param (list) colums
		@param (int) id_provincia
		@return QtSql.QSqlQuery | False
		'''
		result = QtSql.QSqlQuery()

		if colums and id_provincia:
			result = self.MyDB.selectQuery(self.table, colums, 'id_provincia = ' + str(id_provincia))

		if colums and not id_provincia:
			result = self.MyDB.selectQuery(self.table, colums)

		if not colums and id_provincia:
			result = self.MyDB.selectQuery(self.table,'', 'id_provincia = ' + str(id_provincia))

		if not colums and not id_provincia:
			result = self.MyDB.selectQuery(self.table)

		return result
			
	def createCity(self,values):
		'''Crea una ciudad en la tabla
		@param (dict) values
		@return QtSql.QSqlQuery | False'''
		return self.MyDB.insertQuery(self.table, values)

	def updateCity(self,values,id_ciudad):
		'''Actualiza una ciudad en la base de datos
		@param (dict) values
		@param (int) id_ciudad
		@return QtSql.QSqlQuery | False
		'''
		return self.MyDB.updateQuery(self.table,values,id_ciudad)
		
	def deleteCity(self,id_ciudad,columna,valor):
		'''Elimina una ciudad de la base de datos
		@param (str) ciudad
		@param (str) columna
		@valor (str) valor
		@return bool
		'''
		condition = str(columna) + ' = \'' + str(valor) + '\''
		return self.MyDB.deleteQuery(self.table,condition)

	def getCity(self, id_ciudad):
		'''Obtiene los datos de una ciudad
		@param (int) id_ciudad
		@return QtSql.QSqlQuery | False'''
		return self.MyDB.selectQuery(self.table,'',' id_ciudad = ' + str(id_ciudad))

	def findCity(self, columns,condition, valor):
		'''Busca un ciudad en la tabla
		@param (list) columns si no se tiene columnas envia espacio en blanco
		@param (str) condition ejem [=;like;!=;<;>;>=;<=]
		@param (str) valor
		@return QtSql.QSqlQuery | False	
		a = cityClass()
		a.findCity('nombre like',"%a")'''		
		if columns:
			return self.MyDB.selectQuery(self.table,columns, condition + ' \'' + str(valor) + '\'')
		else:
			return self.MyDB.selectQuery(self.table,'', condition + ' \'' + str(valor) + '\'')