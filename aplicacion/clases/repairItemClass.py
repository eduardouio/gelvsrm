#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			repairItemClass.py
# Ubicacion		aplicacion/clases/repairItemClass.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
# +--------------------------+----------------------+------+-----+-------------------+-----------------------------+
# 													Data Types
# +--------------------------+----------------------+------+-----+-------------------+-----------------------------+
# | Field                    | Type                 | Null | Key | Default           | Extra                       |
# +--------------------------+----------------------+------+-----+-------------------+-----------------------------+
# | id_reparacion_detalle 	 | int(10) unsigned     | NO   | UNI | NULL              | auto_increment              |
# | id_reparacion         	 | smallint(5) unsigned | NO   | PRI | NULL              |                             |
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


class repairItem(object):
	"""Estructura para reparacion detalle"""

	def __init__(self, id_reparacion_detalle=int(),id_reparacion=int(),id_inventario=int(),
					fecha='',estado='',cantidad=int(),notas='',registro=''):
		super(repairItem, self).__init__()
		self.id_reparacion_detalle = id_reparacion_detalle
		self.id_reparacion = id_reparacion
		self.id_inventario = id_inventario
		self.fecha = QDate().currentDate()
		self.estado = estado
		self.cantidad = cantidad
		self.notas = notas
		self.registro = QDateTime().currentDateTime()
		qDebug('[Debug] Se instancia la lcase repairItem')
		

class repairItemCatalog(object):
	"""Acciones sobre repairItem"""

	def __init__(self):
		self.MyDb = DB()
		self.table = 'reparacion_detalle'
		qDebug('[Debug] se instancia la clase repairItemCatalog')


	def getRepairItem(self, idRepairItem):
		'''Obtiene un reparacion o todos los reparacions
		@param (str) id_reparacion 
		@return (obj) repairItem | list(obj) repairItem'''		
		condition = {' id_reparacion_detalle = ' : str(idRepairItem)}		
		result = self.MyDb.selectQuery(self.table,'',condition)
		qDebug('[Debug] La consulta retorna %s registros'% result.size())
		if result.next():
			return self.__setObj(result)				
		else:
			qDebug('[Debug] problemas para retonrar una repairItem')
			return False


	def listRepairItems(self,idRepair):
		'''Lista los items de reparacion de una reparacion
		@return lst(obj) repairItem'''
		repairsItem = []
		condition ={' id_reparacion = ' : str(idRepair)}
		result = self.MyDb.selectQuery(self.table,'',condition)
		qDebug('[Debug] La consulta retorna %s registros'% result.size())

		while result.next():				
			repairsItem.append(self.__setObj(result))

		return repairsItem


	def listRepairsItems():
		'''Lista todos items de reparacion
		@return lst(obj) repairItem'''
		repairsItem = []			
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] La consulta retorna %s registros'% result.size())

		while result.next():				
			repairsItem.append(self.__setObj(result))

		return repairsItem


	def findRepairItem(self,condition):
		'''Busca un Inventaryo
		@param condition = {'id_tecnico like ' : '%4%'}
		@return list(obj) tipo myrepairItem'''
		myrepairItem = []
		result = self.MyDB.selectQuery(self.table,'',condition)
		while result.next():
			myrepairItem.append(self.__setObj(result))

		return myrepairItem


	def createRepairItem(self, repairItem):
		'''Crea un reparacion detalle
		@param (obj) repairItem
		@return (bool) | (int)'''
		values = {			
			'id_reparacion' :  repairItem.id_reparacion,
			'id_inventario' :  repairItem.id_inventario,
			'fecha' :  repairItem.fecha,
			'estado' :  repairItem.estado,
			'cantidad' :  repairItem.cantidad,
			'notas' :  repairItem.notas			
		}

		result = self.MyDb.insertQuery(self.table, values)

		if(result.numRowsAffected()>0):
			qDebug('[Debug] se crea un objeto tipo reparacion item')
			return str(result.lastInsertId())
		else:
			qDebug('[Debug] No se crea un objeto tipo reparacion item')
			return False


	def updateRepairItem(self, oldrepairItem, repairItem):
		'''Actualiza un reparacion detalle
		@param (obj) repairItem
		@param (obj)repairItem
		@return (bool)
		'''
		condition = {' id_reparacion_detalle = ' : str(oldrepairItem.id_reparacion_detalle)}
		values = {
			'id_reparacion' :  repairItem.id_reparacion,
			'id_inventario' :  repairItem.id_inventario,
			'fecha' :  repairItem.fecha,
			'estado' :  repairItem.estado,
			'cantidad' :  repairItem.cantidad,
			'notas' :  repairItem.notas,
		}

		result = self.MyDb.updateQuery(self.table,values,condition)

		if(result.numRowsAffected()>0):
			qDebug('[Debug] Se Actualiza un objeto tipo reparacion item')
			return True
		else:
			qDebug('[Debug] No se Actualiza un objeto tipo reparacion item')
			return False


	def deleteRepairItem(self, repairItem):
		'''Elimina un repairItem
		@param (obj) repairItem
		@return (bool)''' 
		condition = {' id_reparacion_detalle = ' : str(repairItem.id_reparacion_detalle)}
		result = self.MyDb.deleteQuery(self.table,condition)
		
		if(result.numRowsAffected()>0):
			qDebug('[Debug] Se elimina un item de reparacion')
			return True
		else:
			qDebug('[Debug] No se elimina un item de reparacion')
			return False
		

	def deleteRepairItems(self, Repair):
		'''Elimina los items de una reparacion
		@param (obj) repairItem
		@return (bool)''' 
		condition = {' id_reparacion = ' : str(repairItem.id_reparacion_detalle)}
		result = self.MyDb.deleteQuery(self.table,condition)
		
		if(result.numRowsAffected()>0):
			qDebug('Se elimina los items de una reparacion')
			return True
		else:
			qDebug('No se elimina los items de una reparacion')
			return False


	def __setObj(self,result):
		'''Crea un objeto tipo repairItem 
		@return (repairItem)'''
		myrepairItem = repairItem()
		myrepairItem.id_reparacion_detalle = str(result.value(0))
		myrepairItem.id_reparacion = str(result.value(1))
		myrepairItem.id_inventario = str(result.value(2))
		myrepairItem.fecha = str(result.value(3))
		myrepairItem.estado = str(result.value(4))
		myrepairItem.cantidad = str(result.value(5))
		myrepairItem.notas = str(result.value(6))
		myrepairItem.registro = str(result.value(7))
		#validamos los campos null
		if not(isinstance(myrepairItem.estado,str)):
			myrepairItem.estado=''

		if not(isinstance(myrepairItem.notas,str)):
			myrepairItem.notas=''

		return myrepairItem