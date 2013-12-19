#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Conexion a la base de datos
# File			conn.py
# Ubicacion		reporte/basedatos/DB.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>

from PyQt4 import QtCore, QtSql, QtGui

def conectar():
	'''Conecta a la base de datos, si la conexion falla retorna el lastError
	de la conexion, en esta funcion tambien se establecen los parametros'''

	conn = QtSql.QSqlDatabase.addDatabase("QMYSQL")		    
	conn.setHostName('127.0.0.1')
	conn.setUserName('root')
	conn.setDatabaseName('gelvsrm_polaris')
	conn.setPassword('elian')
	
	if not conn.open():
		QtGui.QMessageBox.critical(None,QtGui.qApp.tr('No se puede conectar a la Base de Datos!...'),
			QtGui.qApp.tr('Hubo un problema al conectarse con la base de datos \n'
				'El servidor dice... \n' + conn.lastError().databaseText()),
				QtGui.QMessageBox.Cancel,QtGui.QMessageBox.Ok)				
		return False
	return True