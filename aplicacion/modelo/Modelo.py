#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Conexion a la base de datos
# File			modelo.py
# Ubicacion		aplicacion/modelo/Modelo.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>

import sys
sys.path.append('..')
from PyQt4 import QtCore, QtSql, QtGui
from modelo.conn import conectar


class DB(object):
	''' Modelo de datos, lo errores ocurridos en la capa son mostrados por lastError()
	si un metodo no puede efectuar una accion retorna falso.
	Los tipos de error a soportar son errores de conexión y errores en consultas sql'''

	def __init__(self):
		'''Inicia la conexión al servidor'''		
		super(DB, self).__init__()			
		self.Conn = conectar()

	def consultDb(self,sql):
		'''Ejecuta una consulta en la base de datos, las consultas son preparadas por el metodo
		que invoca a este metodo'''
		if (self.Conn):			
			sql.exec_()
			if not sql.isActive():
				QtGui.QMessageBox.warning(None,
					QtGui.qApp.tr('Ocurrió un Error al enviar o recibir información'),
					QtGui.qApp.tr('La solicitud no se completó correctamente, inténtelo de nuevo \n'
									'El servidor dice... \n' + sql.lastError().databaseText() + 
									'\n\nSi el problema continúa comuníquese con eduardouio7@gmail.com' + str(sql.lastQuery())),					
					QtGui.QMessageBox.Ok)		
				return False
			return sql

	def listTables(self):
		'''	Lista todas las tablas de la base de datos '''		
		sql = QtSql.QSqlQuery()			
		sql.prepare('SHOW TABLES FROM gelvsrm_polaris;')
		result = self.consultDb(sql)
		if not result:			
			return False
		return result

	def listColumns(self,tabla):
		''' Lista las columnas de una tabla	'''
		sql = QtSql.QSqlQuery()		
		sql.prepare("SHOW COLUMNS FROM " + tabla + " ;")
		result = self.consultDb(sql)
		if not result:			
			return False
		return result

	def getQueryModel(self,columns,table):
		'''Retorna un modelo de solo lectura de una tabla
		se especifica las columnas con un diccionario, para 
		no escribir las cabeceras del model si la consulta tiene un error consultar 
		QSqlQueryModel.lastError()'''
		query = 'SELECT '
		#desde
		i = 1
		#hasta
		x = len(columns)
		#armamos la consulta
		for item in columns:
			if ( i < x ):
				query = query + item + ' AS ' + columns[item] + ','
			if ( i == x ):
				query = query + item + ' AS ' + columns[item] + ' FROM ' + table
			i += 1
		modelo = QtSql.QSqlQueryModel()
		modelo.setQuery(query)
		return modelo

	def getTableModel(self, table, condition):
		'''Retorna un modelo editable de una tabla, la condicion string sql
		lo errores estan en lastError() '''		
		modelo = QtSql.QSqlTableModel()		
		modelo.setTable(table)
		#los cambios al modelo se almacenan en cache y se reguistran 
		#cuando llamemos al metodo modelo.submitAll(), se tiene la posibilada de revertir
		modelo.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
		modelo.setFilter(condition)
		modelo.select()
		return modelo

	def selectQuery(self, table, columns = '' ,condition='', like= '', limit=''):
		'''Ejecuta una consulta tipo SELECT en la BD
		(str)	table 		=>	nombre de la tabla a consultar
		(list)	columns 	=>	Listado de columnas a mostrar
		(str)	condition 	=> 	condicion si no existe "1=1"
		(list)	like		=>	para filtras busquedas de no existir es False (columna  valor)
		(int)	limit		=>	limite de registros si se desa la tabla completa vale 0

		SELECT columns FROM table
		WHERE conditions | like | 1=1
		LIMIT limit | nothing
		'''		
		query = 'SELECT '
		# x(desde) i(hasta)
		x = 1 
		i = len(columns)
		if columns:
			for item in columns:
				if x < i:
					query += item + ','
				if x == i:
					query += item + ' FROM ' + table
				x+=1
		else:
			query += '* FROM ' + table
		#armamos la consulta
		query = query + ' WHERE ' 
		if condition:
			query += condition
		else:
			query += '1=1'
		#adjuntamos el like
		if like:
			query += like[0] + ' LIKE \'' + like[1] + '\''
		if limit:
			query += ' LIMIT ' + str(limit)
		sql = QtSql.QSqlQuery()
		print(query)
		sql.prepare(query)
		#ejecutamos la consulta, si hay un error acudir a last error
		result = self.consultDb(sql)
		if not result:			
			return False

		return result


	def insertQuery(self,table,values):
		'''Ejecuta una consulta tipo INSERT en la BD, si se manda una columna sin valor se reemplaza por NULL
		(str) table 	=>	nombre de la tabla 
		(dic) values 	=>  diccionario clave valor 
		INSERT INTO table (values[columns]) 
		VALUES( values[value]);'''		
		query = 'INSERT INTO ' + table +'('
		i = 1
		x = len(values)
		for item in values:
			if i<x:
				query = query + item + ','
			if i==x:
				query = query + item + ')'
			i+=1
		query = query + 'VALUES('
		i = 1
		for item in values:
			if values[item] == '':
				#si el valor esta vacio se escribe NULL
				values[item] = 'NULL'
			if i < x:
				query = query + values[item] + ','
			if i == x:
				query = query + values[item] + ');'
			i +=1
		sql = QtSql.QSqlQuery()
		sql.prepare(query)
		result = self.consultDb(sql)
		if not result:
			return False
		return result

	def updateQuery(self,table,values,condition):
		'''Ejecuta una Sentencia tipo update en la BD
		(str)	table 	=> nombre de la tabla 
		(dic)	values 	=> diccionario clave valor para update
		(srt)	condition => condicion SQL
		UPDATE table 
		SET
		values[columns] = values[value]'''
		query = 'UPDATE ' + table + ' SET '
		i = 1
		x = len(values)
		#armamos la consulta
		for item in values:
			if values[item] == '':
				#si el valor esta vacio se escribe NULL
				values[item] = 'NULL'
			if i < x :
				query = query + item + ' = ' + values[item]	+ ','
			if i == x :
				query = query + item + ' = ' + values[item]
		query = query  + ' WHERE ' + condition + ';'
		sql = QtSql.QSqlQuery()
		sql.prepare(query)
		result = self.consultDb(sql)
		if not result:
			return False
		return result

	def deleteQuery(self, table, condition ):
		'''Metodo encargad de ejecutar una Sentencia tipo DELETE en la BD
		(str)	table 	=> nombre de la tabla
		(str)	condition => condicion para el borrado
		DELETE FOM table
		WHERE condition'''
		sql = QtSql.QSqlQuery()		
		sql.prepare('DELETE FROM ' + table + ' WHERE ' + condition + ';')
		result = sefl.consultDb(sql)
		if not result:
			return False
		return result

	def lastInsertId(self):
		'''Ultimo Id ingresado en la BD'''
		sql = QtSql.QSqlQuery()
		return sql.lastInsertId()

	def lastQuery(self):
		'''	retorna el Sql de la última consulta'''
		sql = QtSql.QSqlQuery()
		return sql.lastQuery()

	def beginTransaction(self):
		'''Inicia una transaccion'''
		self.Conn = QtSql.QSqlDatabase.database()
		self.Conn.transaction()

	def commitTransaction(self):
		'''Confirma una transaccion'''
		self.Conn = QtSql.QSqlDatabase.database()
		self.Conn.commit()

	def rollBack(self):
		'''Cancela y revierte los cambios de una transaccion'''
		self.Conn = QtSql.QSqlDatabase.database()
		self.Conn.rollback()

	def lastError(self):
		'''Retorna en ultimo error producido en la base de datos'''
		return self.Conn.lastError()	