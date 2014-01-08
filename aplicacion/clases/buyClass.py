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
# | id_tecnico    | varchar(10)          | NO   | MUL | NULL              |                             |
# | nro_factura   | varchar(12)          | NO   |     | NULL              |                             |
# | fecha         | date  			     | NO   |     | NULL              |                             |
# | cantidad      | smallint(5) unsigned | NO   |     | NULL              |                             |
# | costo         | decimal(5,2)         | YES  |     | NULL              |                             |
# | notas         | mediumtext           | YES  |     | NULL              |                             |
# | registro      | timestamp            | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
# +---------------+----------------------+------+-----+-------------------+-----------------------------+
# mysql = fecha32.toString('yyyy-MM-dd hh:mm:ss')

import sys
sys.path.append('..')
from modelo.Modelo import DB
from PyQt4.QtCore import QDateTime, QDate, QTime, qDebug


class Buy(object):
	"""Estructura para compra"""
	def __init__(self, id_compra='',id_inventario='',id_proveedor='', id_tecnico='',
						nro_factura='',fecha='',cantidad='',costo='',notas='',registro=''):
		super(Buy, self).__init__()
		self.id_compra = id_compra
		self.invetario = id_inventario
		self.id_proveedor = id_proveedor
		self.id_tecnico = id_tecnico
		self.nro_factura = nro_factura		
		self.fecha = QDate().currentDate()		
		self.cantidad = cantidad
		self.costo = costo
		self.notas = notas
		self.registro = QDateTime().currentDateTime()
		qDebug('[Debug] se inicia la clase buy')


class buyCatalog(object):
	"""acciones sobre compras"""

	def __init__(self):
		super(buyCatalog, self).__init__()
		self.table = 'compra'
		self.MyDb = DB()
		qDebug('[Debug] se inicia la clase buyCatalog')


	def getBuys(self,buy=''):
		'''Obtiene una compra o listado
		@param (str) id_compra
		@return (obj) | list(obj) buy
		'''
		condition = {' id_compra = ' : str(buy)}
		result = self.MyDb.selectQuery(self.table,'',condition)
		qDebug('[Debug] la consulta retorno %s objetos'% str(result.size()))
		if result.next():
			return self.__setObj(result)
		else:
			qDebug('[Debug] no se puede retornar niguna vemta')
			return False


	def listBuys():
		'''Retorna un listado de compras
		@return lst(Buy)'''		
		buys = []
		result = self.MyDb.selectQuery(self.table)
		while result.next():				
			buys.append(self.__setObj(result))

		return buys


	def firstBuy(self):
		'''retorna el primer Buy de la lista
		@return (obj) Buy'''		
		result = self.MyDB.selectQuery(self.table)
		qDebug('[Debug] Se toma el primer Buy de la lista')
		if result.first():
			return self.__setObj(result)
		else:
			return False


	def lastBuy(self):
		'''retorna el ultimo Buyo de la Lista
		@return (obj) Buy'''
		result = self.MyDB.selectQuery(self.table)
		qDebug('[Debug] Se toma ultimo Buy de la lista')
		if result.last():
			return self.__setObj(result)
		else:
			return False


	def findBuy(self,condition):
		'''Busca un Buyo
		@param condition = {'id_tecnico like ' : '%4%'}
		@return list(obj) tipo Buy'''
		buys = []
		result = self.MyDB.selectQuery(self.table,'',condition)
		while result.next():
			buys.append(self.__setObj(result))

		return Buys


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
			'notas': buy.notas			
		}

		result = self.MyDb.insertQuery(self.table,values)

		if (result.numRowsAffected() > 0):
			qDebug('[Debug] se inserto una compra')
			return result.lastInsertId()
		else:
			qDebug('[Debug] no se inserto ninguna compra')
			return False


	def updateBuy(self,oldBuy,buy):
		'''Actualiza una compra'''
		condition = {' id_compra = ' : str(oldBuy.id_compra)}
		values = {			
			'id_inventario': buy.id_inventario,
			'id_proveedor': buy.id_proveedor,
			'nro_factura': buy.nro_factura,
			'fecha': buy.fecha,
			'cantidad': buy.cantidad,
			'costo': buy.costo,
			'notas': buy.notas
		}
		result = self.MyDb.updateQuery(self.table, values, condition)
		
		if (result.numRowsAffected() > 0):
			qDebug('[Debug] se Actualiza una compra')
			return True
		else:
			qDebug('[Debug] No se actualoza una compra')
			return False


	def deleteBuy(self,buy):
		'''Elimina una compra
		@param (obj) buy
		return (bool)'''
		condition = {' id_compra = ' : str(buy.id_compra)}
		result = self.MyDb.deleteQuery(self.table,condition)

		if (result.numRowsAffected() > 0):
			qDebug('[Debug] se elinino una compra')
			return True
		else:
			qDebug('[Debug] no se elimino una compra')
			return False


	def __setObj(self, result):
		'''Crea un objeto tipo Conctact y lo retorna
		@param (obj) result
		@return (obj) Buy'''
		mybuy = Buy()
		mybuy.id_compra = str(result.value(0))
		mybuy.id_inventario = str(result.value(1))
		mybuy.id_proveedor = str(result.value(2))
		mybuy.id_tecnico = str(result.value(3))
		mybuy.nro_factura = str(result.value(4))
		mybuy.fecha = str(result.value(5))
		mybuy.cantidad = str(result.value(6))
		mybuy.costo = str(result.value(7))
		mybuy.notas = str(result.value(8))
		mybuy.registro = str(result.value(9))
		qDebug('[Debug] se crea una venta')
		return mybuy
		
		#verificamos los nulos devueltos por la consulta
		if not (isinstance(mybuy.notas,str)):
			mybuy.notas = ''