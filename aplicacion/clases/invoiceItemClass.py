#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			invoiceItemClass.py
# Ubicacion		aplicacion/clases/invoiceItemClass.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
# +--------------------+----------------------+------+-----+-------------------+-----------------------------+
# 											Data Types
# +--------------------+----------------------+------+-----+-------------------+-----------------------------+
# | Field              | Type                 | Null | Key | Default           | Extra                       |
# +--------------------+----------------------+------+-----+-------------------+-----------------------------+
# | id_factura_detalle | mediumint(9)         | NO   | UNI | NULL              | auto_increment              |
# | id_factura         | int(11)              | NO   | PRI | NULL              |                             |
# | id_mantenimiento   | smallint(5) unsigned | YES  | PRI | 0                 |                             |
# | id_reparacion      | smallint(5) unsigned | YES  | PRI | 0                 |                             |
# | registro           | timestamp            | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
# +--------------------+----------------------+------+-----+-------------------+-----------------------------+

import sys
sys.path.append('..')
from modelo.Modelo import DB
from PyQt4.QtCore import QDateTime, QDate, QTime, qDebug

class InvoiceItem(object):
	"""estructura de un detalle de id_factura"""

	def __init__(self, id_factura_detalle ='',id_factura='',id_mantenimiento='',id_reparacion='',registro=''):
		super(invoiceItem, self).__init__()
		self.id_factura_detalle = id_factura_detalle
		self.id_factura = id_factura
		self.id_mantenimiento = id_mantenimiento
		self.id_reparacion = id_reparacion
		self.registro = QDateTime.currentDateTime()
		qDebug('[Debug] se instacia la clase invoiceItem')


class invoiceItemCatalog(object):
	"""Acciones sibre detalle de factura"""
	def __init__(self):
		super(invoiceItemCatalog, self).__init__()
		self.MyDb = DB()
		self.table = 'factura_detalle'
		qDebug('[Debug] se instancia la clase invoiceItemCatalog')


	def getInvoiceItem(self,invoiceItem=''):
		'''Obtiene un invoiceItem o listado de ellos
		@param(str) id_factura_detalle
		@return (obj) lst(obj)'''		
			condition = {' id_factura_detalle = ' : str(invoiceItem)}
			result = self.MyDb.selectQuery(self.table,'',condition)
			qDebug('[Debug] la consulta retorna %s registros'% result.size())
			if result.next():
				return self.__setObj(result)
			else:
				qDebug('[Debug] no se encontro el ítem de la factura')
				return False
				

	def listInvoicesItems(self):
		'''Lista todos los items de la tabla
		@return lst(invoiceItem)'''	
		invoiceItems = []
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] la consulta retorna %s registros'% result.size())		
		while result.next():			
			invoiceItems.append(self.__setObj(result))

		return invoiceItems


	def listInvoiceItems(self,idInvoice=''):
		'''Retorna un el listado de los items de una factura
		@return lst(invoiceItem)'''
		invoiceItems = invoiceItem()
		condition = {' id_factura = ' : str(idInvoice)}
		qDebug('[Debug] la consulta retorna %s registros'% result.size())
		while result.next():			
			invoiceItems.append(self.__setObj(result))

		return invoiceItems


	def firstInvoiceItem(self, id_invoice):
		'''retorna el primer item del la factura
		@return (obj) Invoice'''
		condition = {' id_factura = ' : str(id_invoice)}
		myInvoice = Invoice()
		result = self.MyDb.selectQuery(self.table,'',condition)		
		qDebug('[Debug] Se toma el primer item del una factura')
		
		if result.first():			
			return self.__setObj(result)
		else:
			qDebug('[Debug] Problemas para tomar el primer item del la factura de la lista')
			return False


	def lastInvoiceItem(self, id_invoice):
		'''retorna ultima item del la factura
		@return (obj) Invoice'''		
		condition = {' id_factura = ' : str(id_invoice)}
		result = self.MyDb.selectQuery(self.table)		
		qDebug('[Debug] Se toma el ultimo item de una factura')
		
		if result.last():			
			return self.__setObj(result)
		else:
			qDebug('[Debug] Problemas para tomar el ultimo item del la factura de la lista')		
			return False


	def findInvoiceItem(self,condition):
		'''Busca un técnico en la base de datos
		condition = {'id_factura like ' : '%4%'} 		
		@return lst(obj)'''
		invoiceItems = []
		result = self.MyDb.selectQuery(self.table,'',condition)
		while result.next():
			invoiceItems.append(self.__setObj(result))

		return invoiceItems
			

	def createInvoiceItem(self,invoiceItem):
		'''Crea un item en una factura
		@param (obj) Invoice
		@return (obj) | (int)
		'''
		values = {
			'id_factura_detalle':invoiceItem.id_factura_detalle,
			'id_factura' : invoiceItem.id_factura,
			'id_mantenimiento' : invoiceItem.id_mantenimiento,
			'id_reparacion' : invoiceItem.id_reparacion			
		}

		result = self.MyDb.insertQuery(self.table,values)

		if (result.numRowsAffected() > 0):
			qDebug('[Debug] se Crea una factura')
			return result.lastInsertId()
		else:
			qDebug('[Debug] No se Crea una factura')
			return False


	def updateInvoice(self,oldInvoiceItem,invoiceItem):
		'''Actualiza una factura
		@param (obj) invoiceItem
		@param (obj) invoiceItem
		@return (bool)
		'''
		condition = {' id_factura_detalle = ' : str(oldInvoice.id_factura_detalle)}
		
		values = {			
			'id_factura' : invoiceItem.id_factura,
			'id_mantenimiento' : invoiceItem.id_mantenimiento,
			'id_reparacion' : invoiceItem.id_reparacion			
		}
		

	def deleteInvoiceItem(self,invoice):
		'''Elimina un item de una factura
		@param (obj) invoice
		@return (bool)'''
		condition = ' id_factura_detalle = ' + str(invoice.id_factura)
		result = self.MyDb.deleteQuery(self.table,condition)

		if (result.numRowsAffected() > 0):
			qDebug('[Debug] Se Elimina el item de una factura')
			return True
		else:
			qDebug('[Debug] No se Elimina el item de una factura')			
			return False


	def deleteInvoiceItems(self,idInvoice):
		'''Elimina los items de una factura
		@param (obj) invoice
		@return (bool)'''
		condition = ' id_factura = ' + str(invoice.idInvoice)
		result = self.MyDb.deleteQuery(self.table,condition)

		if (result.numRowsAffected() > 0):
			qDebug('[Debug] Se elimina los items de una factura')
			return True
		else:
			qDebug('[Debug] No se elimina los items de una factura')
						return False


	def coutItemsInvoice(self, idInvoice):
		'''Retorna el numero de itemsfacturas de una factura
		@return int'''
		return len(self.listInvoiceItems(idInvoice))
		


	def __setObj(self, result):
		'''crea un objeto tipo facturas
		 @param result 
		 @return objeto tipo Invoice'''		 
		myinvoiceItem = invoiceItem()
		myinvoiceItem.id_factura_detalle = str(result.value(0))
		myinvoiceItem.id_factura = str(result.value(1))
		myinvoiceItem.id_mantenimiento = str(result.value(2))
		myinvoiceItem.id_reparacion = str(result.value(3))
		myinvoiceItem.registro = str(result.value(4))		

		qDebug('[Debug] Se crea un objeto typo item factura validando los campos tipo null ')
		
		return myinvoiceItem
		