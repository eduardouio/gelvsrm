#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			invoiceClass.py
# Ubicacion		aplicacion/clases/invoiceClass.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
# +----------------+----------------------+------+-----+-------------------+-----------------------------+
# 											Data Types
# +----------------+----------------------+------+-----+-------------------+-----------------------------+
# | Field          | Type                 | Null | Key | Default           | Extra                       |
# +----------------+----------------------+------+-----+-------------------+-----------------------------+
# | id_factura     | int(11)              | NO   | PRI | NULL              |                             |
# | id_cliente     | char(13)             | NO   | MUL | NULL              |                             |
# | id_contacto    | smallint(5) unsigned | YES  | MUL | NULL              |                             |
# | fecha          | date                 | NO   |     | NULL              |                             |
# | fecha_envio    | date                 | NO   |     | NULL              |                             |
# | guia_envio     | varchar(50)          | YES  |     | NULL              |                             |
# | servicio_envio | varchar(80)          | NO   |     | NULL              |                             |
# | estado         | varchar(50)          | NO   |     | NULL              |                             |
# | archivo        | varchar(200)         | YES  |     | NULL              |                             |
# | notas          | mediumtext           | YES  |     | NULL              |                             |
# | registro       | timestamp            | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
# +----------------+----------------------+------+-----+-------------------+-----------------------------+

import sys
sys.path.append('..')
from modelo.Modelo import DB
from PyQt5.QtCore import QDateTime, QDate, QTime, qDebug

class Invoice(object):
	"""estructura de la Invoice"""
	def __init__(self,id_factura='',id_cliente='',id_contacto=int(),fecha='',fecha_envio='',guia_envio='',
					servicio_envio='',estado='',archivo='',notas='',registro=''):
		super(Invoice, self).__init__()
		self.id_factura = id_factura
		self.id_cliente = id_cliente
		self.id_contacto = id_contacto
		self.fecha = QDate()
		self.fecha_envio = QDate()
		self.guia_envio = guia_envio
		self.servicio_envio = servicio_envio
		self.estado = estado
		self.archivo = archivo
		self.notas = notas
		self.registro = QDateTime().currentDateTime()
		qDebug('Se inicia la clase factura')


class invoiceCatalog(object):
	"""acciones sobre invoiceCatalog"""

	def __init__(self):
		super(invoiceCatalog, self).__init__()
		self.table = 'factura'
		self.MyDb = DB()
		qDebug('Se inicia la clase invoiceCatalog')


	def getInvoice(self, idInvoice):
		'''Obtiene una factura o listado'''		
		condition = {' id_factura = ' : str(idInvoice)}
		result = self.MyDb.selectQuery(self.table,'',condition)
		qDebug('La consulta retorno %s registros'% result.size())
		if result.next():
			return self.__setObj(result)
		else:
			qDebug('[Debug] no se retorna niguna factura')
			return False


	def listInvoices(self):
		'''Retorna un listado completo de facturas
		@return lst(Invoice)'''		
		invoices = []
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] La consulta retorno %s registros'% result.size())
		while result.next():			
			invoices.append(self.__setObj(result))

		return invoices

		
	def listInvoicesCoustomer(self,idCoustomer):
		'''retorna las facturas de un cliente
		@return (obj) Invoice'''		
		condition = {' id_cliente = ' : str(idCoustomer)}
		invoices = []
		result = self.MyDb.selectQuery(self.table,'',condition)		
		qDebug('La consulta retorno %s registros'% result.size())		
		while result.next():			
			invoices.append(self.__setObj(result))

		qDebug('[Debug] se retornan las facturas del cliete %s' % idCoustomer)
		return invoices				


	def lastInvoice(self):
		'''retorna ultima factura
		@return (obj) Invoice'''		
		result = self.MyDb.selectQuery(self.table)		
		qDebug('[Debug] Se toma el ultimo factura de la lista')
		
		if result.last():			
			return self.__setObj(result)
		else:
			qDebug('[Debug] Problemas para tomar el ultimo factura de la lista')		
			return False


	def findInvoice(self,condition):
		'''Busca un técnico en la base de datos
		condition = {'id_factura like ' : '%4%'} 		
		@return lst(obj)'''
		Invoices = []
		result = self.MyDb.selectQuery(self.table,'',condition)
		while result.next():
			Invoices.append(self.__setObj(result))

		return Invoices
			

	def createInvoice(self,invoice):
		'''Crea una factura
		@param (obj) Invoice
		@return (obj) | (int)
		'''
		values = {
			'id_factura' : invoice.id_factura,
			'id_cliente' : invoice.id_cliente,
			'id_contacto' : invoice.id_contacto,
			'fecha' : invoice.fecha,
			'fecha_envio' : invoice.fecha_envio,
			'guia_envio' : invoice.guia_envio,
			'servicio_envio' : invoice.servicio_envio,
			'estado' : invoice.estado,
			'archivo' : invoice.archivo,
			'notas' : invoice.notas			
		}

		result = self.MyDb.insertQuery(self.table,values)

		if (result.numRowsAffected() > 0):
			qDebug('[Debug] se Crea una factura')
			return result.lastInsertId()
		else:
			qDebug('[Debug] No se Crea una factura')
			return False


	def updateInvoice(self,oldInvoice,invoice):
		'''Actualiza una factura
		@param (obj) invoice
		@param (obj) invoice
		@return (bool)
		'''
		condition = {' id_factura = ' : str(oldInvoice.id_factura)}
		values = {
			'id_factura' : invoice.id_factura,
			'id_cliente' : invoice.id_cliente,
			'id_contacto' : invoice.id_contacto,
			'fecha' : invoice.fecha,
			'fecha_envio' : invoice.fecha_envio,
			'guia_envio' : invoice.guia_envio,
			'servicio_envio' : invoice.servicio_envio,
			'estado' : invoice.estado,
			'archivo' : invoice.archivo,
			'notas' : invoice.notas			
		}

		result = self.MyDb.updateQuery(self.table,values,condition)
		
		if (result.numRowsAffected() > 0):
			qDebug('[Debug] Se actualiza una factura')
			return True
		else:
			qDebug('[Debug] No se actualiza una factura')
			return False


	def deleteInvoice(self,invoice):
		'''Elimina una factura
		@param (obj) invoice
		@return (bool)'''		
		from invoiceItemClass import invoiceItemCatalog
		myInvoiceItemCatalog = invoiceItemCatalog()
		if(myInvoiceItemCatalog.deleteInvoiceItems(invoice.id_factura)):
			condition = {' id_factura = ' : str(invoice.id_factura)}
			result = self.MyDb.deleteQuery(self.table,condition)

			if (result.numRowsAffected() > 0):
				qDebug('[Debug] No se Elimina una factura')
				return True
			else:
				qDebug('[Debug] No se Elimina una factura')
				return False
		else:
			qDebug('No se puede eliminar los items de la factura')
			return False



	def __setObj(self, result):
		'''crea un objeto tipo facturas
		 @param result 
		 @return objeto tipo Invoice'''		 
		myinvoice = Invoice()
		myinvoice.id_factura = str(result.value(0))
		myinvoice.id_cliente = str(result.value(1))
		myinvoice.id_contacto = str(result.value(2))
		myinvoice.fecha = str(result.value(3))
		myinvoice.fecha_envio = str(result.value(4))
		myinvoice.guia_envio = str(result.value(5))
		myinvoice.servicio_envio = str(result.value(6))
		myinvoice.estado = str(result.value(7))
		myinvoice.archivo = str(result.value(8))
		myinvoice.notas = str(result.value(9))
		myinvoice.registro = str(result.value(10))

		#verificamos los nulos devueltos por la consulta

		if(myinvoice.id_contacto.find('PyQt5.QtCore.')):
			myinvoice.id_contacto = None

		if(myinvoice.guia_envio.find('PyQt5.QtCore.')):
			myinvoice.guia_envio = None

		if(myinvoice.archivo.find('PyQt5.QtCore.')):
			myinvoice.archivo = None

		if(myinvoice.notas.find('PyQt5.QtCore.')):
			myinvoice.notas = None
		
		qDebug('[Debug] Se crea un objeto typo factura validando los campos tipo null ')
		
		return myinvoice