#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			repairDetailClass.py
# Ubicacion		aplicacion/clases/repairDetailClass.py
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

class repairDetail(object):
	"""Estructura para reparacion detalle"""
	def __init__(self, id_reparacion_detalle='',id_reparacion='',id_inventario='',
					fecha='',estado='',cantidad='',notas='',registro=''):
		super(repairDetail, self).__init__()
		self.id_reparacion_detalle = id_reparacion_detalle
		self.id_reparacion = id_reparacion
		self.id_inventario = id_inventario
		self.fecha = fecha
		self.estado = estado
		self.cantidad = cantidad
		self.notas = notas
		self.registro = registro
		

class repairDetailCatalog(object):
	"""Acciones sobre repairDetail"""
	def __init__(self):
		self.MyDb = DB()
		self.table = 'reparacion_detalle'

	def getRepairDetail(self, repairDetail=''):
		'''Obtiene un reparacion o todos los reparacions
		@param (str) id_reparacion 
		@return (obj) repairDetail | list(obj) repairDetail'''
		if repairDetail:
			condition = ' id_reparacion_detalle = ' + str(repairDetail)
			myrepairDetail = repairDetail()
			result = self.MyDb.selectQuery(self.table,'',condition)

			while result.next():
				myrepairDetail.id_reparacion_detalle = str(result.value(0))
				myrepairDetail.id_reparacion = str(result.value(1))
				myrepairDetail.id_inventario = str(result.value(2))
				myrepairDetail.fecha = str(result.value(3))
				myrepairDetail.estado = str(result.value(4))
				myrepairDetail.cantidad = str(result.value(5))
				myrepairDetail.notas = str(result.value(6))
				myrepairDetail.registro = str(result.value(7))
			
			return myrepairDetail

		else:

			repairsDetail = []
			result = self.MyDb.selectQuery(self.table)

			while result.next():
				myrepairDetail = repairDetail()
				myrepairDetail.id_reparacion_detalle = str(result.value(0))
				myrepairDetail.id_reparacion = str(result.value(1))
				myrepairDetail.id_inventario = str(result.value(2))
				myrepairDetail.fecha = str(result.value(3))
				myrepairDetail.estado = str(result.value(4))
				myrepairDetail.cantidad = str(result.value(5))
				myrepairDetail.notas = str(result.value(6))
				myrepairDetail.registro = str(result.value(7))
				repairsDetail.append(myrepairDetail)

			return repairsDetail

	def getRepairDetailRepair(self, repair):
		'''Obtiene los detalles de un reparacion
		@param repair (str) id_reparacion
		@return list(repairsDetail)'''
		condition = ' id_reparacion = ' + str(repair)
		result = self.MyDb.selectQuery(self.table,'',condition)
		repairsDetail = []

		while result.next():			
			myrepairDetail = repairDetail()
			myrepairDetail.id_reparacion_detalle = str(result.value(0))
			myrepairDetail.id_reparacion = str(result.value(1))
			myrepairDetail.id_inventario = str(result.value(2))
			myrepairDetail.fecha = str(result.value(3))
			myrepairDetail.estado = str(result.value(4))
			myrepairDetail.cantidad = str(result.value(5))
			myrepairDetail.notas = str(result.value(6))
			myrepairDetail.registro = str(result.value(7))
			repairsDetail.append(myrepairDetail)

		return repairsDetail

	def createRepairDetail(self, repairDetail):
		'''Crea un reparacion detalle
		@param (obj) repairDetail
		@return (bool) | (int)'''
		values = {			
			'id_reparacion' :  repairDetail.id_reparacion,
			'id_inventario' :  repairDetail.id_inventario,
			'fecha' :  repairDetail.fecha,
			'estado' :  repairDetail.estado,
			'cantidad' :  repairDetail.cantidad,
			'notas' :  repairDetail.notas,
			'registro' :  repairDetail.registro
		}

		result = self.MyDb.createQuery(self.table, values)

		if(result.numRowsAffected()>0):
			return str(result.lastInsertId())
		else:
			return False

	def updateRepairDetail(self, oldrepairDetail, repairDetail):
		'''Actualiza un reparacion detalle
		@param (obj) repairDetail
		@param (obj)repairDetail
		@return (bool)
		'''
		condition = ' id_reparacion_detalle = ' + str(oldrepairDetail.id_reparacion_detalle)
		values = {
			'id_reparacion' :  repairDetail.id_reparacion,
			'id_inventario' :  repairDetail.id_inventario,
			'fecha' :  repairDetail.fecha,
			'estado' :  repairDetail.estado,
			'cantidad' :  repairDetail.cantidad,
			'notas' :  repairDetail.notas,
		}

		result = self.MyDb.updateQuery(self.table,values,condition)

		if(result.numRowsAffected()>0):
			return True
		else:
			return False

	def deleteRepairDetail(self, repairDetail):
		'''Elimina un repairDetail
		@param (obj) repairDetail
		@return (bool)''' 
		condition = ' id_reparacion_detalle = ' + str(repairDetail.id_reparacion_detalle)
		result = self.MyDb.deleteQuery(self.table,condition)
		
		if(result.numRowsAffected()>0):
			return True
		else:
			return False

	def findRepairDetail(self):
		'''Bsuca un detalle reparacion'''
		pass
