#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			Helpers.py
# Ubicacion		aplicacion/clases/Helpers.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>

import sys
sys.path.append('..')
from modelo.Modelo import DB
from PyQt4.QtGui import *
from PyQt4.QtCore import *

MyDb = DB()

def listColumns(table):
		'''Retorna una lista con la lista de las columnas
		@return (lst)'''
		result = MyDb.listColumns(table)
		colums = []
		while result.next():
			colums.append(str(result.value(0)))

		return colums


def countColumns(table):
	'''retorna el total de las columnas de la tabla'''
	return len(listColumns(table))


def countRowsTable(table):
	'''Retorna el numero de registros de la tabla'''
	result = MyDb.selectQuery(table)
	return result.size()


def createCoustomerModel(coustomers):
	'''Se crea un modelo para los clientes'''	
	model = QStandardItemModel(len(coustomers),countColumns('cliente'))
	qDebug('[Debug] se crea uin modelo vacio para cliente')
	
	for row, Mycoustomer in enumerate(coustomers):
		item = QStandardItem(Mycoustomer.id_cliente)  
		model.setItem(row,0,item)
		item = QStandardItem(Mycoustomer.id_contacto)
		model.setItem(row,1,item)
		item = QStandardItem(Mycoustomer.id_ciudad)
		model.setItem(row,2,item)
		item = QStandardItem(Mycoustomer.nombre)
		model.setItem(row,3,item)
		item = QStandardItem(Mycoustomer.direccion)
		model.setItem(row,4,item)
		item = QStandardItem(Mycoustomer.telefono)
		model.setItem(row,5,item)
		item = QStandardItem(Mycoustomer.fax)
		model.setItem(row,6,item)
		item = QStandardItem(Mycoustomer.mail)
		model.setItem(row,7,item)
		item = QStandardItem(Mycoustomer.notas)
		model.setItem(row,8,item)
		item = QStandardItem(Mycoustomer.registro)
		model.setItem(row,9,item)			
		qDebug('[Debug] Se asigna un registro al modelo de Cliente')

	qDebug('[Debug] Se retorna el modelo completo con clientes')
	return model


def createInvoiceModel(invoices):
	'''Se crea un modelo para las facturas'''
	#creo el modelo	
	model = QStandardItemModel(len(invoices),countColumns('factura'))
	qDebug('[Debug] se crea un modelo vacio para factura x %s ' % str(len(invoices)))
	#asignamos datos al modelo
	for row,invoice in enumerate(invoices):
		item = QStandardItem(invoice.id_factura)
		model.setItem(row,0,item)
		item = QStandardItem(invoice.id_cliente)
		model.setItem(row,1,item)
		item = QStandardItem(invoice.id_contacto)
		model.setItem(row,2,item)
		item = QStandardItem(invoice.fecha)
		model.setItem(row,3,item)
		item = QStandardItem(invoice.fecha_envio)
		model.setItem(row,4,item)
		item = QStandardItem(invoice.guia_envio)
		model.setItem(row,5,item)
		item = QStandardItem(invoice.servicio_envio)
		model.setItem(row,6,item)
		item = QStandardItem(invoice.estado)
		model.setItem(row,7,item)
		item = QStandardItem(invoice.archivo)
		model.setItem(row,8,item)
		item = QStandardItem(invoice.notas)
		model.setItem(row,9,item)
		item = QStandardItem(invoice.registro)
		model.setItem(row,10,item)
		qDebug('[Debug] se asigna un registro al modelo factura')

	qDebug('[Debug] se retorna un modelo de facturas con datos')
	return model


def createVehicleModel(vehicles):
	'''Crea un modelos para los vehículos'''
	#creo el modelo	
	model = QStandardItemModel(len(vehicles),countColumns('vehiculo'))
	qDebug('[Debug] se crea un modelo vacio para factura x %s ' % str(len(vehicles)))
	#asignamos datos al modelo
	for row,vehicle in enumerate(vehicles):
		item = QStandardItem(vehicle.id_vehiculo)
		model.setItem(row,0,item)
		item = QStandardItem(vehicle.id_cliente)
		model.setItem(row,1,item)
		item = QStandardItem(vehicle.id_contacto)
		model.setItem(row,2,item)
		item = QStandardItem(vehicle.id_ciudad)
		model.setItem(row,3,item)
		item = QStandardItem(vehicle.modelo)
		model.setItem(row,4,item)
		item = QStandardItem(vehicle.nro_motor)
		model.setItem(row,5,item)
		item = QStandardItem(vehicle.ingreso)
		model.setItem(row,6,item)
		item = QStandardItem(vehicle.notas)
		model.setItem(row,7,item)
		item = QStandardItem(vehicle.registro)
		model.setItem(row,8,item)		
		qDebug('[Debug] se asigna un registro al modelo vehiculo')

	qDebug('[Debug] se retorna un modelo de vehiculo con datos')
	return model


def createStateModel(states):
	'''Crea un modelos para los estados'''
	#creo el modelo	
	model = QStandardItemModel(len(states),countColumns('provincia'))
	qDebug('[Debug] se crea un modelo vacio para  %s estados ' % str(len(states)))
	#asignamos datos al modelo
	for row,state in enumerate(states):
		item = QStandardItem(state.id_provincia)
		model.setItem(row,0,item)
		item = QStandardItem(state.nombre)
		model.setItem(row,1,item)		
		qDebug('[Debug] se asigna un registro al modelo provincia')
	qDebug('[Debug] se retorna un modelo de provincia con datos')
	return model

def createCityModel(cities):
	'''Crea un modelos para las ciudades'''
	#creo el modelo	
	model = QStandardItemModel(len(cities),countColumns('ciudad'))
	qDebug('[Debug] se crea un modelo vacio para  %s ciudades ' % str(len(cities)))
	#asignamos datos al modelo
	for row,city in enumerate(cities):
		item = QStandardItem(city.id_ciudad)
		model.setItem(row,0,item)
		item = QStandardItem(city.id_provincia)
		model.setItem(row,1,item)
		item = QStandardItem(city.nombre)
		model.setItem(row,2,item)		
		qDebug('[Debug] se asigna un registro al modelo factura')
	qDebug('[Debug] se retorna un modelo de facturas con datos')
	return model
