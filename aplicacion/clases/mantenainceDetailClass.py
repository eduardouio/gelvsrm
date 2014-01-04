#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			mantenainceDetailClass.py
# Ubicacion		aplicacion/clases/mantenainceDetailClass.py
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

class MantenainceDetail(object):
	"""Estructura para mantenimiento detalle"""
	def __init__(self, id_mantenimiento_detalle='',id_mantenimiento='',id_inventario='',
					fecha='',estado='',cantidad='',notas='',registro=''):
		super(MantenainceDetail, self).__init__()
		self.id_mantenimiento_detalle = id_mantenimiento_detalle
		self.id_mantenimiento = id_mantenimiento
		self.id_inventario = id_inventario
		self.fecha = fecha
		self.estado = estado
		self.cantidad = cantidad
		self.notas = notas
		self.registro = registro
		

class mantenainceDetailCatalog(object):
	"""Acciones sobre mantenainceDetail"""
	def __init__(self):
		self.MyDb = DB()
		self.table = 'mantenimiento_detalle'

	def getMantenainceDetail(self, mantenainceDetail=''):
		'''Obtiene un mantenimiento o todos los mantenimientos
		@param (str) id_mantenimiento 
		@return (obj) mantenainceDetail | list(obj) mantenainceDetail'''
		if mantenainceDetail:
			condition = ' id_mantenimiento_detalle = ' + str(mantenainceDetail)
			mymantenainceDetail = MantenainceDetail()
			result = self.MyDb.selectQuery(self.table,'',condition)

			while result.next():
				mymantenainceDetail.id_mantenimiento_detalle = str(result.value(0))
				mymantenainceDetail.id_mantenimiento = str(result.value(1))
				mymantenainceDetail.id_inventario = str(result.value(2))
				mymantenainceDetail.fecha = str(result.value(3))
				mymantenainceDetail.estado = str(result.value(4))
				mymantenainceDetail.cantidad = str(result.value(5))
				mymantenainceDetail.notas = str(result.value(6))
				mymantenainceDetail.registro = str(result.value(7))
			
			return mymantenainceDetail

		else:

			mantenaincesDetail = []
			result = self.MyDb.selectQuery(self.table)

			while result.next():
				mymantenainceDetail = MantenainceDetail()
				mymantenainceDetail.id_mantenimiento_detalle = str(result.value(0))
				mymantenainceDetail.id_mantenimiento = str(result.value(1))
				mymantenainceDetail.id_inventario = str(result.value(2))
				mymantenainceDetail.fecha = str(result.value(3))
				mymantenainceDetail.estado = str(result.value(4))
				mymantenainceDetail.cantidad = str(result.value(5))
				mymantenainceDetail.notas = str(result.value(6))
				mymantenainceDetail.registro = str(result.value(7))
				mantenaincesDetail.append(mymantenainceDetail)

			return mantenaincesDetail

	def getMantenainceDetailMantenaince(self, mantenaince):
		'''Obtiene los detalles de un mantenimiento
		@param mantenaince (str) id_mantenimiento
		@return list(mantenaincesDetail)'''
		condition = ' id_mantenimiento = ' + str(mantenaince)
		result = self.MyDb.selectQuery(self.table,'',condition)
		mantenaincesDetail = []

		while result.next():			
			mymantenainceDetail = MantenainceDetail()
			mymantenainceDetail.id_mantenimiento_detalle = str(result.value(0))
			mymantenainceDetail.id_mantenimiento = str(result.value(1))
			mymantenainceDetail.id_inventario = str(result.value(2))
			mymantenainceDetail.fecha = str(result.value(3))
			mymantenainceDetail.estado = str(result.value(4))
			mymantenainceDetail.cantidad = str(result.value(5))
			mymantenainceDetail.notas = str(result.value(6))
			mymantenainceDetail.registro = str(result.value(7))
			mantenaincesDetail.append(mymantenainceDetail)

		return mantenaincesDetail

	def createMantenainceDetail(self, mantenainceDetail):
		'''Crea un mantenimiento detalle
		@param (obj) mantenainceDetail
		@return (bool) | (int)'''
		values = {			
			'id_mantenimiento' :  mantenainceDetail.id_mantenimiento,
			'id_inventario' :  mantenainceDetail.id_inventario,
			'fecha' :  mantenainceDetail.fecha,
			'estado' :  mantenainceDetail.estado,
			'cantidad' :  mantenainceDetail.cantidad,
			'notas' :  mantenainceDetail.notas,
			'registro' :  mantenainceDetail.registro
		}

		result = self.MyDb.createQuery(self.table, values)

		if(result.numRowsAffected()>0):
			return str(result.lastInsertId())
		else:
			return False

	def updateMantenainceDetail(self, oldMantenainceDetail, mantenainceDetail):
		'''Actualiza un mantenimiento detalle
		@param (obj) mantenainceDetail
		@param (obj)mantenainceDetail
		@return (bool)
		'''
		condition = ' id_mantenimiento_detalle = ' + str(oldMantenainceDetail.id_mantenimiento_detalle)
		values = {
			'id_mantenimiento' :  mantenainceDetail.id_mantenimiento,
			'id_inventario' :  mantenainceDetail.id_inventario,
			'fecha' :  mantenainceDetail.fecha,
			'estado' :  mantenainceDetail.estado,
			'cantidad' :  mantenainceDetail.cantidad,
			'notas' :  mantenainceDetail.notas,
		}

		result = self.MyDb.updateQuery(self.table,values,condition)

		if(result.numRowsAffected()>0):
			return True
		else:
			return False

	def deleteMantenainceDetail(self, mantenainceDetail):
		'''Elimina un mantenainceDetail
		@param (obj) mantenainceDetail
		@return (bool)''' 
		condition = ' id_mantenimiento_detalle = ' + str(mantenainceDetail.id_mantenimiento_detalle)
		result = self.MyDb.deleteQuery(self.table,condition)
		
		if(result.numRowsAffected()>0):
			return True
		else:
			return False

	def findMantenaindeDetail(self):
		'''Bsuca un detalle mantenimiento'''
		pass