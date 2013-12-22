#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			buyClass.py
# Ubicacion		aplicacion/clases/buyClass.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
# +---------------+----------------------+------+-----+-------------------+-----------------------------+
# 										Data Types
# +---------------+----------------------+------+-----+-------------------+-----------------------------+
# | Field         | Type                 | Null | Key | Default           | Extra                       |
# +---------------+----------------------+------+-----+-------------------+-----------------------------+
# | id_compra     | smallint(5) unsigned | NO   | PRI | NULL              | auto_increment              |
# | id_inventario | smallint(5) unsigned | NO   | MUL | NULL              |                             |
# | id_proveedor  | varchar(13)          | NO   | MUL | NULL              |                             |
# | nro_factura   | varchar(12)          | NO   |     | NULL              |                             |
# | fecha         | datetime             | NO   |     | NULL              |                             |
# | cantidad      | smallint(5) unsigned | NO   |     | NULL              |                             |
# | costo         | decimal(5,2)         | YES  |     | NULL              |                             |
# | notas         | mediumtext           | YES  |     | NULL              |                             |
# | registro      | timestamp            | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
# +---------------+----------------------+------+-----+-------------------+-----------------------------+

import sys
sys.path.append('..')
from modelo.Modelo import DB

class Buy(object):
	"""Estructura para compra"""
	def __init__(self, id_compra='',id_inventario='',id_proveedor='',nro_factura='',fecha='',
					cantidad='',costo='',notas='',registro=''):
		super(Buy, self).__init__()
		self.id_compra = id_compra
		self.id_inventario = id_inventario
		self.id_proveedor = id_proveedor
		self.nro_factura = nro_factura
		self.fecha = fecha
		self.cantidad = cantidad
		self.costo = costo
		self.notas = notas
		self.registro = registro


class buyCatalog(object):
	"""acciones sobre compras"""
	def __init__(self):
		super(buyCatalog, self).__init__()
		self.table = 'compra'
		self.MyDb = DB()


	def getBuys(self,buy=''):
		'''Obtiene una compra o listado
		@param (str) id_compra
		@return (obj) | list(obj) buy
		'''
		if buy:
			mybuy = Buy()
			condition = ' id_compra = ' + str(buy)
			result = self.MyDb.selectQuery(self.table,'',condition)
			while result.next():
				mybuy.id_compra = str(result.values(0))
				mybuy.id_inventario = str(result.values(1))
				mybuy.id_proveedor = str(result.values(2))
				mybuy.nro_factura = str(result.values(3))
				mybuy.fecha = str(result.values(4))
				mybuy.cantidad = str(result.values(5))
				mybuy.costo = str(result.values(6))
				mybuy.notas = str(result.values(7))
				mybuy.registro = str(result.values(8))
			
			return mybuy

		else:
			buys = []
			result = self.MyDb.selectQuery(self.table)
			while result.next():
				mybuy = Buy()
				mybuy.id_compra = str(result.values(0))
				mybuy.id_inventario = str(result.values(1))
				mybuy.id_proveedor = str(result.values(2))
				mybuy.nro_factura = str(result.values(3))
				mybuy.fecha = str(result.values(4))
				mybuy.cantidad = str(result.values(5))
				mybuy.costo = str(result.values(6))
				mybuy.notas = str(result.values(7))
				mybuy.registro = str(result.values(8))
				buys.append(mybuy)

			return buys

	def createBuy(self,buy):
		'''crea una compra
		@param (obj) buy
		@return (bool) | (int)'''
		values = {			
			'id_inventario': buy.id_inventario,
			'id_proveedor': buy.id_proveedor,
			'nro_factura': buy.nro_factura,
			'fecha': buy.fecha,
			'cantidad': buy.cantidad,
			'costo': buy.costo,
			'notas': buy.notas,
			'registro': buy.registro
		}
		result = self.MyDb.createQuery(self.table,values)

		if (result.numRowsAffected() > 0):
			return result.lastInsertId()
		else:
			return False

	def updateBuy(self,oldBuy,buy):
		'''Actualiza una compra'''
		condition = ' id_compra = ' + str(oldBuy.id_compra)
		values = {			
			'id_inventario': buy.id_inventario,
			'id_proveedor': buy.id_proveedor,
			'nro_factura': buy.nro_factura,
			'fecha': buy.fecha,
			'cantidad': buy.cantidad,
			'costo': buy.costo,
			'notas': buy.notas,
			'registro': buy.registro
		}
		result = self.MyDb.updateQuery(self.table, values, condition)
		
		if (result.numRowsAffected() > 0):
			return True
		else:
			return False

	def deleteBuy(self,buy):
		'''Elimina una compra
		@param (obj) buy
		return (bool)'''
		condition = ' id_compra = ' + str(buy.id_compra)
		result = self.MyDb.deleteQuery(self.table,condition)

		if (result.numRowsAffected() > 0):
			return True
		else:
			return False

	def findBuy(self,condition=''):
		'''Busca una compra'''
		pass