#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			MaintenanceItemClass.py
# Ubicacion		aplicacion/clases/MaintenanceItemClass.py
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


class MaintenanceItem(object):
	"""Estructura para mantenimiento detalle"""

	def __init__(self, id_mantenimiento_detalle=int(),id_mantenimiento=int(),id_inventario=int(),
					fecha='',estado='',cantidad=int(),notas='',registro=''):
		super(MaintenanceItem, self).__init__()
		self.id_mantenimiento_detalle = id_mantenimiento_detalle
		self.id_mantenimiento = id_mantenimiento
		self.id_inventario = id_inventario
		self.fecha = QDate().currentDate()
		self.estado = estado
		self.cantidad = cantidad
		self.notas = notas
		self.registro = QDateTime().currentDateTime()
		qDebug('[Debug] Se instancia la clase MaintenanceItem')
		

class maintenanceItemCatalog(object):
	"""Acciones sobre MaintenanceItem"""

	def __init__(self):
		self.MyDb = DB()
		self.table = 'mantenimiento_detalle'
		qDebug('[Debug] se instancia la clase MaintenanceItemCatalog()')


	def getMaintenanceItem(self, IdmaintenanceItem):
		'''Obtiene un mantenimiento o todos los mantenimientos
		@param (str) id_mantenimiento 
		@return (obj) maintenanceItem'''
		if maintenanceItem:
			condition = {' id_mantenimiento_detalle = ' : str(IdmaintenanceItem)}			
			result = self.MyDb.selectQuery(self.table,'',condition)
			qDebug('[Debug] la consulta retorna %s registros'% result.size())
			if result.next():				
				return self.__setObj(result)
			else:
				return False
		

	def listMaintenanceItems(self, idMaintenance):
		'''Retona un listado con todos items de un mantenimiento
		@return lst(MaintenanceItem)'''
			maintenanceItems = []
			condition = {' id_mantenimiento = ' : idMaintenance}
			result = self.MyDb.selectQuery(self.table,'',condition)
			qDebug('[Debug] la consulta retorna %s registros'% result.size())
			while result.next():				
				maintenanceItems.append(self.__setObj(result))

			return maintenanceItems


	def listMaintenancesItems(self):
		'''Retona un listado con todos items de la tabla mantenimiento_detalle
		@return lst(MaintenanceItem)'''
			maintenanceItems = []			
			result = self.MyDb.selectQuery(self.table)
			qDebug('[Debug] la consulta retorna %s registros'% result.size())
			while result.next():				
				maintenanceItems.append(self.__setObj(result))

			return maintenanceItems

				
		
	def firstMaintenanceItem(self, idMaintenance):
		'''retorna el primer item del mantenimiento
		@return (obj) technical'''
		condition = {' id_mantenimiento = ' : idMaintenance }
		result = self.MyDb.selectQuery(self.table,'',condition)		
		qDebug('[Debug] Se toma el primer item mantenimiento de la lista')
		
		if result.first():			
			return self.__setObj(result)
		else:
			qDebug('[Debug] Problemas para tomar el primer item mantenimiento de la lista')
			return False


	def lastMaintenanceItem(self, idMaintenance):
		'''retorna el ultimo item del mantenimiento
		@return (obj) technical'''
		condition = {' id_mantenimiento = ' : idMaintenance }
		result = self.MyDb.selectQuery(self.table,'',condition)		
		qDebug('[Debug] Se toma el ultimo item mantenimiento de la lista')
		
		if result.last():			
			return self.__setObj(result)
		else:
			qDebug('[Debug] Problemas para tomar el ultimo item mantenimiento de la lista')
			return False


	
	def findMaintenanceItems(self,condition):
		'''Busca un técnico en la base de datos
		condition = {'id_tecnico like ' : '%4%'} 		
		@return lst(obj)'''
		myMaintenanceItem = []
		result = self.MyDb.selectQuery(self.table,'',condition)
		while result.next():
			myMaintenanceItem.append(self.__setObj(result))

		return myMaintenanceItem
			

	def createMaintenanceItem(self, MaintenanceItem):
		'''Crea un mantenimiento detalle
		@param (obj) MaintenanceItem
		@return (bool) | (int)'''
		values = {			
			'id_mantenimiento' :  MaintenanceItem.id_mantenimiento,
			'id_inventario' :  MaintenanceItem.id_inventario,
			'fecha' :  MaintenanceItem.fecha,
			'estado' :  MaintenanceItem.estado,
			'cantidad' :  MaintenanceItem.cantidad,
			'notas' :  MaintenanceItem.notas			
		}

		result = self.MyDb.insertQuery(self.table, values)

		if(result.numRowsAffected()>0):
			qDebug('[Debug] se ingresa un Item detalle en la base')
			return str(result.lastInsertId())
		else:
			qDebug('[Debug] problemas para ingresar un Item detalle en la base')
			return False



	def updateMaintenanceItem(self, oldMaintenanceItem, MaintenanceItem):
		'''Actualiza un mantenimiento detalle
		@param (obj) MaintenanceItem
		@param (obj)MaintenanceItem
		@return (bool)
		'''
		condition = {' id_mantenimiento_detalle = ' : str(oldMaintenanceItem.id_mantenimiento_detalle)}
		values = {
			'id_mantenimiento' :  MaintenanceItem.id_mantenimiento,
			'id_inventario' :  MaintenanceItem.id_inventario,
			'fecha' :  MaintenanceItem.fecha,
			'estado' :  MaintenanceItem.estado,
			'cantidad' :  MaintenanceItem.cantidad,
			'notas' :  MaintenanceItem.notas,
		}

		result = self.MyDb.updateQuery(self.table,values,condition)

		if(result.numRowsAffected()>0):
			qDebug('[Debug] se Actualiza un Item detalle en la base')
			return True
		else:
			qDebug('[Debug] No se Actualiza un Item detalle en la base')
			return False


	def deleteMaintenanceItem(self, MaintenanceItem):
		'''Elimina un MaintenanceItem
		@param (obj) MaintenanceItem
		@return (bool)''' 
		condition = {' id_mantenimiento_detalle = ' : str(MaintenanceItem.id_mantenimiento_detalle)}
		result = self.MyDb.deleteQuery(self.table,condition)
		
		if(result.numRowsAffected()>0):
			qDebug('[Debug] se Elimina un Item detalle en la base')
			return True
		else:
			qDebug('[Debug] No se Elimina un Item detalle en la base')
			return False


	def deleteMaintenanceItems(self, maintenance):
		'''Elimina todos los items de un mantenimiento
		@param (obj) MaintenanceItem
		@return (bool)''' 
		condition = {' id_mantenimiento = ' : str(maintenance.id_mantenimiento)}
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
		myMaintenanceItem = MaintenanceItem()

		myMaintenanceItem.id_mantenimiento_detalle = str(result.value(0))
		myMaintenanceItem.id_mantenimiento = str(result.value(1))
		myMaintenanceItem.id_inventario = str(result.value(2))
		myMaintenanceItem.fecha = str(result.value(3))
		myMaintenanceItem.estado = str(result.value(4))
		myMaintenanceItem.cantidad = str(result.value(5))
		myMaintenanceItem.notas = str(result.value(6))
		myMaintenanceItem.registro = str(result.value(7))

		#verificamos los nulos devueltos por la consulta
		if not (isinstance(myMaintenanceItem.notas,str)):
			mytechnical.notas=''

		qDebug('[Debug] Se crea un objeto typo tecnico validando los campos tipo null ')
		
		return mytechnical