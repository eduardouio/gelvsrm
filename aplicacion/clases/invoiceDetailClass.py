#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			invoiceDetailClass.py
# Ubicacion		aplicacion/clases/invoiceDetailClass.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
# +--------------------+----------------------+------+-----+-------------------+-----------------------------+
# 											Data Types
# +--------------------+----------------------+------+-----+-------------------+-----------------------------+
# | Field              | Type                 | Null | Key | Default           | Extra                       |
# +--------------------+----------------------+------+-----+-------------------+-----------------------------+
# | id_factura_detalle | mediumint(9)         | NO   | UNI | NULL              | auto_increment              |
# | id_factura         | int(11)              | NO   | PRI | NULL              |                             |
# | id_mantenimiento   | smallint(5) unsigned | NO   | PRI | 0                 |                             |
# | id_reparacion      | smallint(5) unsigned | NO   | PRI | 0                 |                             |
# | registro           | timestamp            | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
# +--------------------+----------------------+------+-----+-------------------+-----------------------------+

import sys
sys.path.append('..')
from modelo.Modelo import DB

class InvoiceDetail(object):
	"""estructura de un detalle de id_factura"""
	def __init__(self, id_factura_detalle ='',id_factura='',id_mantenimiento='',id_reparacion='',registro=''):
		super(invoiceDetail, self).__init__()
		self.id_factura_detalle = id_factura_detalle
		self.id_factura = id_factura
		self.id_mantenimiento = id_mantenimiento
		self.id_reparacion = id_reparacion
		self.registro = registro

class invoiceDetailCatalog(object):
	"""Acciones sibre detalle de factura"""
	def __init__(self):
		super(invoiceDetailCatalog, self).__init__()
		self.MyDb = DB()
		self.table = 'factura_detalle'

	def getInvoicesDetails(self,invoiceDetail=''):
		'''Obtiene un invoiceDetail o listado de ellos
		@param(str) id_factura_detalle
		@return (obj) lst(obj)'''
		if invoiceDetail:
			myinvoiceDetail = InvoiceDetail()
			condition = ' id_factura_detalle = ' + str(invoiceDetail)
			result = self.MyDb.selectQuery(self.table,'',condition)

			while result.next():
				myinvoiceDetail.id_factura_detalle = str(result.value(0))
				myinvoiceDetail.id_factura = str(result.value(1))
				myinvoiceDetail.id_mantenimiento = str(result.value(2))
				myinvoiceDetail.id_reparacion = str(result.value(3))
				myinvoiceDetail.registro = str(result.value(4))

			return myinvoiceDetail

		else:

			invoiceDetails = []
			result = self.MyDb.selectQuery(self.table)

			while result.next():
				myinvoiceDetail = InvoiceDetail()
				myinvoiceDetail.id_factura_detalle = str(result.value(0))
				myinvoiceDetail.id_factura = str(result.value(1))
				myinvoiceDetail.id_mantenimiento = str(result.value(2))
				myinvoiceDetail.id_reparacion = str(result.value(3))
				myinvoiceDetail.registro = str(result.value(4))
				invoiceDetails.append(myinvoiceDetail)

			return invoiceDetails


	def createInvoiceDetail(self,invoiceDetail):
		'''Ingresa el detalle de una factura
		@param (obj) invoiceDetail 
		@return (bool) | (int)'''
		

