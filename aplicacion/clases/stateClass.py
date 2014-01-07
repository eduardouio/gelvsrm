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
# | nombre       | varchar(100)         | NO   |     | NULL    |                |
# +--------------+----------------------+------+-----+---------+----------------+
import sys
sys.path.append('..')
from modelo.Modelo import DB
from PyQt4.QtCore import qDebug

class State(object):
	"""Objeto que representa la estructura una provincia"""
	def __init__(self, id_provincia='',nombre=''):
		'''Inizializacion de las propiedades de la clase'''
		super(State, self).__init__()
		self.id_provincia = id_provincia
		self.nombre = nombre
		qDebug('[Debug] se instancia la clase State')

class stateCatalog(object):
	"""Representa las operaciones sobre provincia"""

	def __init__(self):
		'''Instancializacion de la clase creamos el objeto MyDB 
		creamos la variable con el nombre de la tabla
		'''
		super(stateCatalog, self).__init__()		
		self.table = 'provincia'
		self.MyDB = DB()
		qDebug('[Debug] se instancia la clase stateCatalog')
		

	def getState(self,state=''):
		'''Lista Las provinciaes		
		@param (str) identificador del estado
		@return (obj) tipo stateC'''		
		condition = {'id_provincia = ':str(state)}
		result = self.MyDB.selectQuery(self.table,'',condition)		
		if result.next():			
			return self.__setObj(result)
			qDebug('[Debug] se retorna %s registros'% result.size())
		else:
			qDebug('[Debug] no se retorna ningun registro')
			
			return False			

	
	def listStates(self):
		'''Lista todos los estados de la table
		@return list(obj) state'''	
		states = []
		result = self.MyDB.selectQuery(self.table)	
		qDebug('[Debug] se retorna %s registros'% result.size())
		while result.next():
			states.append(self.__setObj(result))		

		return states


	def firstState(self):
		'''retorna el primer estado de la Lista
		@return (obj) state'''
		result = self.MyDB.selectQuery(self.table)
		qDebug('[Debug] Se toma el primer estado de la lista')
		if result.first():
			return self.__setObj(result)
		else:
			return False


	def lastState(self):
		'''retorna el ultimo estado de la Lista
		@return (obj) state'''
		result = self.MyDB.selectQuery(self.table)
		qDebug('[Debug] Se toma el ultimo estado de la lista')
		if result.last():
			return self.__setObj(result)
		else:
			return False

	
	def findState(self, condition):
		'''Busca una provincia
		@param (dic) condicion de la consulta
		condition = {'id_tecnico like ' : '%4%'}
		@retun list((obj)) state'''
		states = []
		result = self.MyDB.selectQuery(self.table,'',condition)
		qDebug('[Debug] la busqueda retorno %s registros'% result.size())
		while result.next():
			states.append(self.__setObj(result))
		
		return states


	def createState(self,state):
		'''Crea una provincia en el sistema
		@param (obj) tipo state 
		@return bool|int
		'''
		values = {'nombre': str(state.nombre)}
		result = self.MyDB.insertQuery(self.table,values)
		if (result.numRowsAffected() > 0):
			qDebug('[Debug] Se inserta correctamente %d registrs' % result.numRowsAffected())
			return int(result.lastInsertId())
		else:
			qDebug('[Debug] no se inserto ningun valor')
			return False


	def updateState(self, oldState, state):
		'''Actualiza un Estado
		@param (obj) representa datos antiguos
		@param (obj) representa nuevos datos
		@return (bool) 
		'''
		condition = {'id_provincia = ' : str(oldState.id_provincia)}
		values = {'nombre': str(state.nombre)}
		result = self.MyDB.updateQuery(self.table,values,condition)
		
		if (result.numRowsAffected() > 0):
			qDebug('[Debug] Se modifica correctamente %d registrs' % result.numRowsAffected())
			return True
		else:
			qDebug('[Debug] no se actualizo ningun valor')
			return False


	def deleteState(self, state):
		'''Elima una ciudad
		@param (obj) tipo state
		@return (bool)
		'''
		condition = {'id_provincia = ' : str(state.id_provincia)}
		result = self.MyDB.deleteQuery(self.table, condition)

		if (result.numRowsAffected() > 0):
			qDebug('[Debug] se Elimina un Estado')
			return True
		else:
			qDebug('[Debug] problemas para Eliminar un Estado')
			return False

	
    def __setObj(self,result):
        '''coloca las propiedades de un estado
        @return (obj) estado'''
        mystate = State()
        mystate.id_provincia = str(result.value(0))
        mystate.nombre = str(result.value(1))
        qDebug('[Debug] se crea un objeto tipo estado')
        return mystate