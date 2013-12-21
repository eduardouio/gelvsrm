#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			clienteClass.py
# Ubicacion		aplicacion/clases/clienteClass.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
# +---------------------------------------------------------------------------------------------------+
# 										Data Type
# +-------------+----------------------+------+-----+-------------------+-----------------------------+
# | Field       | Type                 | Null | Key | Default           | Extra                       |
# +-------------+----------------------+------+-----+-------------------+-----------------------------+
# | id_cliente  | char(13)             | NO   | PRI | NULL              |                             |
# | id_contacto | smallint(5) unsigned | YES  | MUL | NULL              |                             |
# | id_ciudad   | smallint(5) unsigned | YES  | MUL | NULL              |                             |
# | nombre      | varchar(200)         | NO   |     | NULL              |                             |
# | direccion   | varchar(600)         | NO   |     | NULL              |                             |
# | telefono    | varchar(15)          | NO   |     | NULL              |                             |
# | fax         | varchar(15)          | YES  |     | NULL              |                             |
# | mail        | varchar(100)         | YES  |     | NULL              |                             |
# | notas       | mediumtext           | YES  |     | NULL              |                             |
# | registro    | timestamp            | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
# +-------------+----------------------+------+-----+-------------------+-----------------------------+

import sys
sys.path.append('..')
#coneccion a la base de datos
from modelo import conn
#modelo a la base de datos
from modelo.Modelo import DB
from PyQt4 import QtSql

class clienteClass(object):
	"""Cla encargada de representar a los clientes"""
	def __init__(self):
		'''Se crea el objeto de coneccion y el nombre de la tabla'''
		super(clienteClass, self).__init__()
		self.table = 'cliente'
		self.MyDB = DB()

	def listCustomer():
	'''Lista los clientes de la tabla'''
	pass

	def 		
		