#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			stateCatalog.py
# Ubicacion		aplicacion/clases/stateCatalog.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
# +-----------------------------------------------------------------------------+
# |									Data Type									|
# +--------------+----------------------+------+-----+---------+----------------+
# | Field        | Type                 | Null | Key | Default | Extra          |
# +--------------+----------------------+------+-----+---------+----------------+
# | id_provincia | smallint(5) unsigned | NO   | PRI | NULL    | auto_increment |
# | nombre       | varchar(100)         | YES  |     | NULL    |                |
# +--------------+----------------------+------+-----+---------+----------------+
import sys
sys.path.append('..')
from modelo.Modelo import DB

class State(object):
	"""Objeto que representa la estructura una provincia"""
	def __init__(self, id_provincia='',nombre=''):
		'''Inizializacion de las propiedades de la clase'''
		super(State, self).__init__()
		self.id_provincia = id_provincia
		self.nombre = nombre		

class stateCatalog(object):
	"""Representa las operaciones sobre provincia"""

	def __init__(self):
		'''Instancializacion de la clase creamos el objeto MyDB 
		creamos la variable con el nombre de la tabla
		'''
		super(stateCatalog, self).__init__()		
		self.table = 'provincia'
		self.MyDB = DB()
		

	def getStates(self,state=''):
		'''Lista Las provinciaes		
		@param (str) identificador del estado
		@return (list(obj) | obj) tipo city'''
		result = object
		if state:
			result = self.MyDB.selectQuery(self.table,'','id_provincia = ' + str(state))
			mystate = State()
			while result.next():
				mystate.id_provincia = (str(result.value(0)))
				mystate.nombre = (str(result.value(1)))		
			return mystate		

		else:
			result = self.MyDB.selectQuery(self.table)
		
			state = []
			while result.next():
				mystate = State()
				mystate.id_provincia = (str(result.value(0)))
				mystate.nombre = (str(result.value(1)))
				state.append(mystate)		
			return state		

	def createState(self,state):
		'''Crea una provincia en el sistema
		@param (obj) tipo state 
		@return bool|int
		'''
		values = {'nombre': str(state.nombre)}
		result = self.MyDB.insertQuery(self.table,values)
		if (result.numRowsAffected() > 0):
			return str(result.lastInsertId())
		else:
			return False

	def updateState(self, oldState, state):
		'''Actualiza un Estado
		@param (obj) representa datos antiguos
		@param (obj) representa nuevos datos
		@return (bool) 
		'''
		condition = 'id_provincia = ' + str(oldState.id_provincia)
		values = {'nombre': str(state.nombre)}
		result = self.MyDB.updateQuery(self.table,condition)
		
		if (result.numRowsAffected() > 0):
			return True
		else:
			return False

	def deleteState(self, state):
		'''Elima una ciudad
		@param (obj) tipo state
		@return (bool)
		'''
		condition = 'id_provincia = ' + str(state.id_provincia)
		result = self.MyDB.deleteQuery(self.table, condition)

		if (result.numRowsAffected() > 0):
			return True
		else:
			return False

	def findState(self, column, value):
		'''Busca una provincia
		@param (str) nombre de la columna
		@param (str) el valor para la columna
		@retun list((obj)) state'''
		states = []
		content = [str(column),str(value)]
		result = self.MyDB.selectQuery(self.table,'','',content)
		while result.next():
			mystate = State()
			mystate.id_provincia = (str(result.value(0)))
			mystate.nombre = (str(result.value(1)))
			states.append(mystate)
		return states