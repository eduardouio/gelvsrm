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

class Invoice(object):
	"""estructura de la Invoice"""
	def __init__(self,id_factura='',id_cliente='',id_contacto='',fecha='',fecha_envio='',guia_envio='',
					servicio_envio='',estado='',archivo='',notas='',registro=''):
		super(Invoice, self).__init__()
		self.id_factura = id_factura
		self.id_cliente = id_cliente
		self.id_contacto = id_contacto
		self.fecha = fecha
		self.fecha_envio = fecha_envio
		self.guia_envio = guia_envio
		self.servicio_envio = servicio_envio
		self.estado = estado
		self.archivo = archivo
		self.notas = notas
		self.registro = registro


class invoiceCatalog(object):
	"""acciones sobre invoiceCatalog"""
	def __init__(self):
		super(invoiceCatalog, self).__init__()
		self.table = 'factura'
		self.MyDb = DB()

	def getInvoices(self, invoice=''):
		'''Obtiene una factura o listado'''
		if invoice:
			myinvoice = Invoice()
			condition = ' id_factura = ' + str(invoice)
			result = self.MyDb.selectQuery(self.table,'',condition)
			while result.next():
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

			return myinvoice

		else:
			invoices = []
			result = self.MyDb.selectQuery(self.table)
			while result.next():
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
				invoices.append(myinvoice)

			return invoices

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
			'notas' : invoice.notas,
			'registro' : invoice.registro
		}

		result = self.MyDb.createQuery(self.table,values)

		if (result.numRowsAffected() > 0):
			return result.lastInsertId()
		else:
			return False

	def updateInvoice(self,oldInvoice,invoice):
		'''Actualiza una factura
		@param (obj) invoice
		@param (obj) invoice
		@return (bool)
		'''
		condition = ' id_factura = ' + str(oldInvoice.id_factura)
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
			'notas' : invoice.notas,
			'registro' : invoice.registro
		}

		result = self.MyDb.updateQuery(self.table,values,condition)
		
		if (result.numRowsAffected() > 0):
			return True
		else:
			return False

	def deleteInvoice(self,invoice):
		'''Elimina una factura
		@param (obj) invoice
		@return (bool)'''
		condition = ' id_factura = ' + str(invoice.id_factura)
		result = self.MyDb.deleteQuery(self.table,condition)

		if (result.numRowsAffected() > 0):
			return True
		else:
			return False

	def findInvoice(self,condition=''):
		'''Busca una factura
		@param (obj)
		'''
		pass
