#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			tecnicoClass.py
# Ubicacion		aplicacion/clases/tecnicoClass.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
# +------------+--------------+------+-----+-------------------+-----------------------------+
# |										Data Types										     |
# +------------+--------------+------+-----+-------------------+-----------------------------+
# | Field      | Type         | Null | Key | Default           | Extra                       |
# +------------+--------------+------+-----+-------------------+-----------------------------+ 
# | id_tecnico | varchar(10)  | NO   | PRI | NULL              |                             |
# | nombres    | varchar(200) | NO   |     | NULL              |                             |
# | telefono   | varchar(15)  | YES  |     | NULL              |                             |
# | celular    | varchar(15)  | YES  |     | NULL              |                             |
# | email      | varchar(100) | YES  |     | NULL              |                             |
# | notas      | mediumtext   | YES  |     | NULL              |                             |
# | registro   | timestamp    | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
# +------------+--------------+------+-----+-------------------+-----------------------------+
import sys
sys.path.append('..')
from modelo.Modelo import DB
from PyQt4.QtCore import QDateTime, QDate, QTime

class Technical(object):
	'''Estrucntura de un objecto tecnico'''
	
	def __init__(self, id_tecnico = '',nombres = '',telefono='',
				celular='',email='',notas='',registro=''):		
		super(Tecnico, self).__init__()
		self.id_tecnico = id_tecnico
		self.nombres = nombres
		self.telefono = telefono
		self.celular = celular
		self.email  = email
		self.notas = notas
		#objeto vacio con la fecha actual
		self.registro = QDateTime().currentDateTime()



##### Se Escribe un clase para manipular al objeto tecnico

class techCatalog(object):
	"""Acciones sobre catalogo"""
	def __init__(self):
		super(tecnicoCatalog, self).__init__()
		self.MyDb = DB()
		self.table = 'tecnico'

	def getTechnical(self,technical=''):
		'''Obtiene un tecnico o listado de ellos
		@param (str) id_tecnico'''
		if technical:
			mytechnigetcal = Technical()
			condition = ' id_tecnico = ' + str(technical)
			result = self.MyDb.selectQuery(self.table,'',condition)
			while result.next():
				mytechnical.id_tecnico = str(result.value(0))
				mytechnical.nombres = str(result.value(1))
				mytechnical.telefono = str(result.value(2))
				mytechnical.celular = str(result.value(3))
				mytechnical.email = str(result.value(4))
				mytechnical.notas = str(result.value(5))
				mytechnical.registro = str(result.value(6))

			return mytechnical
		else:
			technicals = []
			result = self.MyDb.selectQuery(self.table)
			while result.next():
				mytechnical = Technical()
				mytechnical.id_tecnico = str(result.value(0))				
				mytechnical.nombres = str(result.value(1))
				mytechnical.telefono = str(result.value(2))
				mytechnical.celular = str(result.value(3))
				mytechnical.email = str(result.value(4))
				mytechnical.notas = str(result.value(5))
				mytechnical.registro = str(result.value(6))
				technicals.append(mytechnical)

			return technicals

	def updateTechnical(self,oldTechnical,technical):
		'''Actualiza un técnico en la base de datos
		@param (obj) tipo technical
		@param (obj) tipo technical
		@return(bool) 
		'''
		condition = 'id_tecnico = ' + str(oldTechnical.id_tecnico)
		values = {			
			'nombres' : technical.nombres,
			'telefono' : technical.telefono,
			'celular' : technical.celular,
			'email' : technical.email,
			'notas' : technical.notas,
			'registro' : technical.registro
		}
		result = self.MyDb.updateQuery(self.table,values,condition)
		if (result.numRowsAffected() > 0):
			return True
		else:
			return False

	def createTechnical(self, technical):
		'''Crea un tecnico en la base de datos
		@param (obj) tipo tecnico
		@return (boo)| last id'''
		values = {
			'id_tecnico' : technical.id_tecnico,
			'nombres' : technical.nombres,
			'telefono' : technical.telefono,
			'celular' : technical.celular,
			'email' : technical.email,
			'notas' : technical.notas,
			'registro' : technical.registro
		}
		result =  self.MyDb.insertQuery(self.table,values)
		if (result.numRowsAffected() > 0):
			return True
		else:
			return False

	def deleteTechnical(self, technical):
		'''Elimina un tecnico de la tabla
		@param (obj) technical
		@return (bool)'''
		condition = ' id_tecnico = ' + str(technical.id_tecnico)
		result = self.deleteQuery(self.table,condition)
		if (result.numRowsAffected() > 0):
			return True
		else:
			return False

	def findTechnical(self,technical):
		'''Busca un técnico en la base de datos'''
		pass

	def lastTecnical(self,technical):
		pass

	def coutTechnical(self):
		pass