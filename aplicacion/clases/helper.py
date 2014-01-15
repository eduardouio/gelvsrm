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
from PyQt4.QtCore import QDateTime, QDate, QTime, qDebug

MyDb = DB()

def listColumns(table):
		'''Retorna una lista con la lista de las columnas
		@return (lst)'''
		result = MyDb.listColumns(self.table)
		colums = []
		while result.next():
			colums.append(str(result.value(0)))

		return colums

def countRowsTable(table):
	'''Retorna el numero de registros de la tabla'''
	result = MyDb.selectQuery(table)
	return result.size()


def selectTable(objeto):
	'''Verifica la instacia de la clase y reconoce la tabla a la 
	que pertenece para que las funciones anteriores puedan hacer su trabajo
	@return (str)'''
	#instacia = ''
	#if not(isinstance()
	pass
