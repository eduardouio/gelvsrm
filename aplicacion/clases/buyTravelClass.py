#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			buyTravelClass.py
# Ubicacion		aplicacion/clases/buyTravelClass.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
# +----------------+-----------------------+------+-----+-------------------+----------------+
# 									Data Types
# +----------------+-----------------------+------+-----+-------------------+----------------+
# | Field          | Type                  | Null | Key | Default           | Extra          |
# +----------------+-----------------------+------+-----+-------------------+----------------+
# | id_gasto_viaje | mediumint(8) unsigned | NO   | UNI | NULL              | auto_increment |
# | id_viaje       | smallint(5) unsigned  | NO   | PRI | NULL              |                |
# | nro_factura    | varchar(20)           | NO   | PRI | NULL              |                |
# | fecha          | date                  | NO   |     | NULL              |                |
# | detalle        | varchar(300)          | NO   |     | NULL              |                |
# | valor          | decimal(4,2)          | NO   | PRI | NULL              |                |
# | tipo           | varchar(45)           | YES  |     | NULL              |                |
# | registro       | timestamp             | NO   |     | CURRENT_TIMESTAMP |                |
# +----------------+-----------------------+------+-----+-------------------+----------------+

import sys
sys.path.append('..')
from modelo.Modelo import DB

class buyTravel(object):
	"""estructura para los gastos viajes"""
	def __init__(self,id_gasto_viaje= '', id_viaje='',nro_factura='',fecha='',
					detalle='',valor='',tipo='',registro=''):
		super(buyTravel, self).__init__()
		self.id_gasto_viaje = id_gasto_viaje
		self.id_viaje = id_viaje
		self.nro_factura = nro_factura
		self.fecha = fecha
		self.detalle = detalle
		self.valor = valor
		self.tipo = tipo
		self.registro = registro
		

class buyTravelCatalog(object):
	"""acciones para buyTravel"""
	def __init__(self):
		super(buyTravelCatalog, self).__init__()
		self.table = 'gastos_viaje'
		self.MyDb = DB()

	def getBuysTravels(self, buyTravel=''):
		'''Obtiene un listado de gastos de un viaje o todos los gastos
		@param (str) id_gasto_viaje
		@result lst(obj)'''

		if buyTravel:
			condition = ' id_gasto_viaje = ' + str(buyTravel)
			result = self.MyDb.selectQuery(self.table,'',condition)
			mybuyravel = buyTravel()
			while result.next():
				mybuyravel.id_gasto_viaje = str(result.value(0))
				mybuyravel.id_viaje = str(result.value(1))
				mybuyravel.nro_factura = str(result.value(2))
				mybuyravel.fecha = str(result.value(3))
				mybuyravel.detalle = str(result.value(4))
				mybuyravel.valor = str(result.value(5))
				mybuyravel.tipo = str(result.value(6))
				mybuyravel.registro = str(result.value(7))
			
			return mybuyravel

		else:
			buystravel = []
			result = self.MyDb.selectQuery(self.table)
			while result.next():
				mybuyravel = buyTravel()
				mybuyravel.id_gasto_viaje = str(result.value(0))
				mybuyravel.id_viaje = str(result.value(1))
				mybuyravel.nro_factura = str(result.value(2))
				mybuyravel.fecha = str(result.value(3))
				mybuyravel.detalle = str(result.value(4))
				mybuyravel.valor = str(result.value(5))
				mybuyravel.tipo = str(result.value(6))
				mybuyravel.registro = str(result.value(7))
				buystravel.append(mybuyravel)

			return buystravel

	def getBuysTravel(self,buyTravel):
		'''Obtiene un listado de gastos de un viaje 
		@param (str) id_viaje
		@result lst(obj)'''
		buystravel = []
		condition = ' id_viaje = ' +  str(buyTravel)
		result = self.MyDb.selectQuery(self.table,'',condition)
			while result.next():
				mybuyravel = buyTravel()
				mybuyravel.id_gasto_viaje = str(result.value(0))
				mybuyravel.id_viaje = str(result.value(1))
				mybuyravel.nro_factura = str(result.value(2))
				mybuyravel.fecha = str(result.value(3))
				mybuyravel.detalle = str(result.value(4))
				mybuyravel.valor = str(result.value(5))
				mybuyravel.tipo = str(result.value(6))
				mybuyravel.registro = str(result.value(7))
				buystravel.append(mybuyravel)

		return buystravel


	def createBuyTravel(self,buyTravel):
		'''Se crea un gasto de viaje
		@param (obj) gastos_viaje
		@param (bool) | (int)
		'''
		values = {
			'id_viaje' : str(buyTravel.id_viaje),
			'nro_factura' : str(buyTravel.nro_factura),
			'fecha' : str(buyTravel.fecha),
			'detalle' : str(buyTravel.detalle),
			'valor' : str(buyTravel.valor),
			'tipo' : str(buyTravel.tipo),
			'registro' : str(buyTravel.registro)
		}

		result = self.MyDb.createQuery(self.table,values)

		if (result.numRowsAffected() > 0):
			return result.lastInsertId()
		else:
			return False

	def updateBuyTravel(self,oldBuyTravel, buyTravel):
		'''Actualiza un gasto de viaje
		@param (obj) buyTravel
		@param (obj) buyTravel
		@return (bool)
		'''
		condition = ' id_gasto_viaje =  ' + str(oldBuyTravel.id_gasto_viaje)
		values = {
			'id_viaje' : str(buyTravel.id_viaje),
			'nro_factura' : str(buyTravel.nro_factura),
			'fecha' : str(buyTravel.fecha),
			'detalle' : str(buyTravel.detalle),
			'valor' : str(buyTravel.valor),
			'tipo' : str(buyTravel.tipo),
			'registro' : str(buyTravel.registro)
		}

		result = self.MyDb.updateQuery(self.table,values,condition)

		if (result.numRowsAffected() > 0):
			return True
		else:
			return False

	def deleteBuyTravel(self,buyTravel):
		'''Elimina un gasto de viaje
		@param (obj) buyTravel
		@return (bool)'''
		condition = ' id_gasto_viaje = ' + str(buyTravel.id_gasto_viaje)
		result = self.deleteQuery(self.table,condition)

		if (result.numRowsAffected() > 0):
			return True
		else:
			return False

	def findBuyTravel(self):
		'''Buscamos un gasto de viaje'''
		pass