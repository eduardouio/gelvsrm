#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			MantenainceItemClass.py
# Ubicacion		aplicacion/clases/MantenainceItemClass.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
# +--------------------------+----------------------+------+-----+-------------------+-----------------------------+
# 													Data Types
# +--------------------------+----------------------+------+-----+-------------------+-----------------------------+
# | Field                    | Type                 | Null | Key | Default           | Extra                       |
# +--------------------------+----------------------+------+-----+-------------------+-----------------------------+
# | id_mantenimiento_detalle | int(10) unsigned     | NO   | UNI | NULL              | auto_increment              |
# | id_mantenimiento         | smallint(5) unsigned | NO   | PRI | NULL              |                             |
# | id_inventario            | smallint(5) unsigned | NO   | PRI | NULL              |                             |
# | fecha                    | time                 | NO   |     | NULL              |                             |
# | estado                   | varchar(25)          | YES  |     | NULL              |                             |
# | cantidad                 | float unsigned       | NO   |     | NULL              |                             |
# | notas                    | varchar(600)         | YES  |     | NULL              |                             |
# | registro                 | timestamp            | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
# +--------------------------+----------------------+------+-----+-------------------+-----------------------------+

import sys
sys.path.append('..')
from modelo.Modelo import DB
from PyQt4.QtCore import QDateTime, QDate, QTime, qDebug


class MantenainceItem(object):
	"""Estructura para mantenimiento detalle"""

	def __init__(self, id_mantenimiento_detalle=int(),id_mantenimiento=int(),id_inventario=int(),
					fecha='',estado='',cantidad=int(),notas='',registro=''):
		super(MantenainceItem, self).__init__()
		self.id_mantenimiento_detalle = id_mantenimiento_detalle
		self.id_mantenimiento = id_mantenimiento
		self.id_inventario = id_inventario
		self.fecha = QDate().currentDate()
		self.estado = estado
		self.cantidad = cantidad
		self.notas = notas
		self.registro = QDateTime().currentDateTime()
		qDebug('[Debug] Se instancia la clase MantenainceItem')
		

class mantenainceItemCatalog(object):
	"""Acciones sobre MantenainceItem"""

	def __init__(self):
		self.MyDb = DB()
		self.table = 'mantenimiento_detalle'
		qDebug('[Debug] se instancia la clase MantenainceItemCatalog()')


	def getMantenainceItem(self, IdmantenainceItem):
		'''Obtiene un mantenimiento o todos los mantenimientos
		@param (str) id_mantenimiento 
		@return (obj) mantenainceItem'''
		if mantenainceItem:
			condition = {' id_mantenimiento_detalle = ' : str(IdmantenainceItem)}			
			result = self.MyDb.selectQuery(self.table,'',condition)
			qDebug('[Debug] la consulta retorna %s registros'% result.size())
			if result.next():				
				return self.__setObj(result)
			else:
				return False
		

	def listMantenainceItems(self, idMantenaince):
		'''Retona un listado con todos items de un mantenimiento
		@return lst(MantenainceItem)'''
			mantenainceItems = []
			condition = {' id_mantenimiento = ' : idMantenaince}
			result = self.MyDb.selectQuery(self.table,'',condition)
			qDebug('[Debug] la consulta retorna %s registros'% result.size())
			while result.next():				
				mantenainceItems.append(self.__setObj(result))

			return mantenainceItems


	def listMantenaincesItems(self):
		'''Retona un listado con todos items de la tabla mantenimiento_detalle
		@return lst(MantenainceItem)'''
			mantenainceItems = []			
			result = self.MyDb.selectQuery(self.table)
			qDebug('[Debug] la consulta retorna %s registros'% result.size())
			while result.next():				
				mantenainceItems.append(self.__setObj(result))

			return mantenainceItems

				
		
	def firstMantenainceItem(self, idMantenaince):
		'''retorna el primer item del mantenimiento
		@return (obj) technical'''
		condition = {' id_mantenimiento = ' : idMantenaince }
		result = self.MyDb.selectQuery(self.table,'',condition)		
		qDebug('[Debug] Se toma el primer item mantenimiento de la lista')
		
		if result.first():			
			return self.__setObj(result)
		else:
			qDebug('[Debug] Problemas para tomar el primer item mantenimiento de la lista')
			return False


	def lastMantenainceItem(self, idMantenaince):
		'''retorna el ultimo item del mantenimiento
		@return (obj) technical'''
		condition = {' id_mantenimiento = ' : idMantenaince }
		result = self.MyDb.selectQuery(self.table,'',condition)		
		qDebug('[Debug] Se toma el ultimo item mantenimiento de la lista')
		
		if result.last():			
			return self.__setObj(result)
		else:
			qDebug('[Debug] Problemas para tomar el ultimo item mantenimiento de la lista')
			return False


	
	def findMantenainceItems(self,condition):
		'''Busca un técnico en la base de datos
		condition = {'id_tecnico like ' : '%4%'} 		
		@return lst(obj)'''
		myMantenainceItem = []
		result = self.MyDb.selectQuery(self.table,'',condition)
		while result.next():
			myMantenainceItem.append(self.__setObj(result))

		return myMantenainceItem
			

	def createMantenainceItem(self, MantenainceItem):
		'''Crea un mantenimiento detalle
		@param (obj) MantenainceItem
		@return (bool) | (int)'''
		values = {			
			'id_mantenimiento' :  MantenainceItem.id_mantenimiento,
			'id_inventario' :  MantenainceItem.id_inventario,
			'fecha' :  MantenainceItem.fecha,
			'estado' :  MantenainceItem.estado,
			'cantidad' :  MantenainceItem.cantidad,
			'notas' :  MantenainceItem.notas			
		}

		result = self.MyDb.insertQuery(self.table, values)

		if(result.numRowsAffected()>0):
			qDebug('[Debug] se ingresa un Item detalle en la base')
			return str(result.lastInsertId())
		else:
			qDebug('[Debug] problemas para ingresar un Item detalle en la base')
			return False



	def updateMantenainceItem(self, oldMantenainceItem, MantenainceItem):
		'''Actualiza un mantenimiento detalle
		@param (obj) MantenainceItem
		@param (obj)MantenainceItem
		@return (bool)
		'''
		condition = {' id_mantenimiento_detalle = ' : str(oldMantenainceItem.id_mantenimiento_detalle)}
		values = {
			'id_mantenimiento' :  MantenainceItem.id_mantenimiento,
			'id_inventario' :  MantenainceItem.id_inventario,
			'fecha' :  MantenainceItem.fecha,
			'estado' :  MantenainceItem.estado,
			'cantidad' :  MantenainceItem.cantidad,
			'notas' :  MantenainceItem.notas,
		}

		result = self.MyDb.updateQuery(self.table,values,condition)

		if(result.numRowsAffected()>0):
			qDebug('[Debug] se Actualiza un Item detalle en la base')
			return True
		else:
			qDebug('[Debug] No se Actualiza un Item detalle en la base')
			return False


	def deleteMantenainceItem(self, MantenainceItem):
		'''Elimina un MantenainceItem
		@param (obj) MantenainceItem
		@return (bool)''' 
		condition = {' id_mantenimiento_detalle = ' : str(MantenainceItem.id_mantenimiento_detalle)}
		result = self.MyDb.deleteQuery(self.table,condition)
		
		if(result.numRowsAffected()>0):
			qDebug('[Debug] se Elimina un Item detalle en la base')
			return True
		else:
			qDebug('[Debug] No se Elimina un Item detalle en la base')
			return False


	def deleteMantenainceItems(self, mantenaince):
		'''Elimina todos los items de un mantenimiento
		@param (obj) MantenainceItem
		@return (bool)''' 
		condition = {' id_mantenimiento = ' : str(mantenaince.id_mantenimiento)}
		result = self.MyDb.deleteQuery(self.table,condition)
		
		if(result.numRowsAffected()>0):
			qDebug('[Debug] se Elimina un Item detalle en la base')
			return True
		else:
			qDebug('[Debug] No se Elimina un Item detalle en la base')
			return False

		

	def __setObj(self, result):
		'''crea un objeto tipo tecnicos
		 @param result 
		 @return objeto tipo technical'''		 
		myMantenainceItem = MantenainceItem()

		myMantenainceItem.id_mantenimiento_detalle = str(result.value(0))
		myMantenainceItem.id_mantenimiento = str(result.value(1))
		myMantenainceItem.id_inventario = str(result.value(2))
		myMantenainceItem.fecha = str(result.value(3))
		myMantenainceItem.estado = str(result.value(4))
		myMantenainceItem.cantidad = str(result.value(5))
		myMantenainceItem.notas = str(result.value(6))
		myMantenainceItem.registro = str(result.value(7))

		#verificamos los nulos devueltos por la consulta
		if not (isinstance(myMantenainceItem.notas,str)):
			mytechnical.notas=''

		qDebug('[Debug] Se crea un objeto typo tecnico validando los campos tipo null ')
		
		return mytechnical