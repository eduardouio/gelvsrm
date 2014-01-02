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
#sys.setdefaultencoding('iso-8859-1')
from codecs import *
from modelo.Modelo import DB
from PyQt4.QtCore import QDateTime, QDate, QTime, qDebug

class Technical(object):
	'''Estrucntura de un objecto tecnico'''
	
	def __init__(self, id_tecnico = '',nombres ='',telefono='',
				celular='',email='',notas='',registro=''):		
		super(Technical, self).__init__()		
		self.id_tecnico = id_tecnico
		self.nombres = nombres
		self.telefono = telefono
		self.celular = celular
		self.email  = email
		self.notas = notas
		self.registro = QDateTime().currentDateTime()



##### Se Escribe un clase para manipular al objeto tecnico

class techCatalog(object):
	"""Acciones sobre catalogo"""
	def __init__(self):
		super(techCatalog, self).__init__()
		self.MyDb = DB()
		self.table = 'tecnico'
		qDebug('[Debug] Se inicia la clase techCatalog')

	def getTechnical(self,technical=''):
		'''Retonra un tecnico como objeto
		@param (str) technical id_tecnico
		@return (obj) technical'''
		mytechnical = Technical()
		condition = {'id_tecnico = ':str(technical)}
		result = self.MyDb.selectQuery(self.table,'',condition)

		qDebug('[Debug] obtener tecnico genero %s registro' % result.size())				

		if result.next():
			return self.__setObj(result)
		else:
			qDebug('[Debug] La consulta No produjo resultados')
		

	def listTechnicals(self):
		'''Retorna un listado completo de tecnicos
		@return lst(obj) technicals'''
		technicals = []
		result = self.MyDb.selectQuery(self.table)

		qDebug('[Debug] listar tecnicos genero %s registro' % result.size())				

		while result.next():
			technicals.append(self.__setObj(result))

		return technicals
						
		
	def firstTechnical(self):
		'''retorna el primer tecnico
		@return (obj) technical'''
		mytechnical = Technical()
		result = self.MyDb.selectQuery(self.table)		
		qDebug('[Debug] Se toma el primer tecnico de la lista')
		
		if result.first():			
			return self.__setObj(result)
		else:
			qDebug('[Debug] Problemas para tomar el primer tecnico de la lista')


	def lastTecnical(self):
		'''retorna el primer tecnico
		@return (obj) technical'''
		mytechnical = Technical()
		result = self.MyDb.selectQuery(self.table)		
		qDebug('[Debug] Se toma el ultimo tecnico de la lista')
		
		if result.last():			
			return self.__setObj(result)
		else:
			qDebug('[Debug] Problemas para tomar el ultimo tecnico de la lista')		
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
			'notas' : technical.notas			
		}
		result =  self.MyDb.insertQuery(self.table,values)
		if (result.numRowsAffected() > 0):
			return True
		else:
			return False


	def updateTechnical(self,oldTechnical,technical):
		'''Actualiza un técnico en la base de datos
		@param (obj) tipo technical
		@param (obj) tipo technical
		@return(bool) 
		'''
		condition = {'id_tecnico = ' : str(oldTechnical.id_tecnico)}		
		values = {			
			'id_tecnico' : technical.id_tecnico,
			'nombres' : technical.nombres,
			'telefono' : technical.telefono,
			'celular' : technical.celular,
			'email' : technical.email,
			'notas' : technical.notas			
		}
		result = self.MyDb.updateQuery(self.table,values,condition)
		if (result.numRowsAffected() > 0):
			return True
		else:
			return False


	def deleteTechnical(self, technical):
		'''Elimina un tecnico de la tabla
		@param (obj) technical
		@return (bool)'''
		condition =  {'id_tecnico = ' : str(technical.id_tecnico)}
		result = self.MyDb.deleteQuery(self.table,condition)
		if (result.numRowsAffected() > 0):
			return True
		else:
			return False


	def coutTechnicals(self):
		'''Retorna el numero de tecnicos registrados en la DB
		@return int'''
		return len(self.listTechnicals())

	def listColumns(self):
		'''Retorna una lista con la lista de las columnas
		@return (lst)'''
		result = self.MyDb.listColumns(self.table)
		colums = []
		while result.next():
			colums.append(str(result.value(0)))

		return colums
		

	def findTechnical(self,condition):
		'''Busca un técnico en la base de datos
		condition = {'id_tecnico like ' : '%4%'} 		
		@return lst(obj)'''
		technicals = []
		result = self.MyDb.selectQuery(self.table,'',condition)
		while result.next():
			technicals.append(self.__setObj(result))

		return technicals


	def __setObj(self, result):
		'''crea un objeto tipo tecnicos
		 @param result 
		 @return objeto tipo technical'''		 
		mytechnical = Technical()

		mytechnical.id_tecnico = result.value(0)
		mytechnical.nombres = result.value(1)
		mytechnical.telefono = result.value(2)
		mytechnical.celular = result.value(3)
		mytechnical.email = result.value(4)
		mytechnical.notas = result.value(5)
		mytechnical.registro = result.value(6)

		#verificamos los nulos devueltos por la consulta
		if not (isinstance(mytechnical.telefono,str)):
			mytechnical.telefono=''

		if not (isinstance(mytechnical.celular,str)):
			mytechnical.celular=''

		if not (isinstance(mytechnical.email,str)):
			mytechnical.email=''

		if not (isinstance(mytechnical.notas,str)):
			mytechnical.notas=''

		qDebug('[Debug] Se crea un objeto typo tecnico validando los campos tipo null ')
		
		return mytechnical