#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			reairClass.py
# Ubicacion		aplicacion/clases/reairClass.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
# +---------------+----------------------+------+-----+-------------------+-----------------------------+
# 											Data Types
# +---------------+----------------------+------+-----+-------------------+-----------------------------+
# | Field         | Type                 | Null | Key | Default           | Extra                       |
# +---------------+----------------------+------+-----+-------------------+-----------------------------+
# | id_reparacion | smallint(5) unsigned | NO   | PRI | NULL              | auto_increment              |
# | id_viaje      | smallint(5) unsigned | NO   | MUL | NULL              |                             |
# | id_vehiculo   | char(17)             | NO   | MUL | NULL              |                             |
# | id_ciudad     | smallint(5) unsigned | YES  | MUL | NULL              |                             |
# | periodo       | smallint(5) unsigned | NO   |     | NULL              |                             |
# | kilometros    | varchar(45)          | NO   |     | NULL              |                             |
# | fecha_entrada | datetime             | NO   |     | NULL              |                             |
# | fecha_salida  | datetime             | YES  |     | NULL              |                             |
# | notas         | mediumtext           | YES  |     | NULL              |                             |
# | registro      | timestamp            | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
# +---------------+----------------------+------+-----+-------------------+-----------------------------+

import sys
sys.path.append('..')
from modelo.Modelo import DB
from PyQt4.QtCore import QDateTime, QDate, QTime, qDebug


class Repair(object):
	"""estructura para Repair"""

	def __init__(self, id_reparacion=int(),id_viaje=int(),id_vehiculo='',id_ciudad=int(), periodo=int(),
					kilometros='',fecha_salida='',fecha_entrada='',notas='',registro=''):
		super(Repair, self).__init__()
		self.id_reparacion = id_reparacion
		self.id_viaje = id_viaje
		self.id_vehiculo = id_vehiculo
		self.id_ciudad = id_ciudad
		self.periodo = periodo
		self.kilometros = kilometros
		self.fecha_salida = QDate().currentDate()
		self.fecha_entrada = QDate().currentDate()
		self.notas = notas
		self.registro = QDateTime().currentDateTime()
		qDebug('[Debug] se instancia la clas Repair')


class repairCatalog(object):
	"""acciones para la clase Catalog"""

	def __init__(self):
		super(repairCatalog, self).__init__()
		self.MyDb = DB()
		self.table = 'reparacion'
		qDebug('[Debug] se instancia la clase repairCatalog')


	def getRepair(self, idRepair):
		'''Obtiene un listado de reparacion
		@param (str) repair
		@return (obj) | list(obj)
		'''
		myrepair = Repair()
		condition = {' id_reparacion = ' : str(idRepair)}
		result = self.MyDb.selectQuery(self.table,'',condition)
		qDebug('[Debug] La consulta retorno %s registros'% result.size())
		if result.next():
			return self.__setObj(result)
		else:
			return False
		

	def listRepairs(self):
		'''Retorna un listado de reparaciones
		@return lst(repair)'''
		repairs = []
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] La consulta retorno %s registros'% result.size())
		while result.next():				
			repairs.append(self.__setObj(result))

		return repairs


	def firstRepair(self):
		'''retorna la primera reparacion
		@return (obj) Repair'''		
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] Se toma el la primera reparacion de la lista')
		if result.first():
			return self.__setObj(result)
		else:
			return False


	def lastRepair(self):
		'''retorna el ultimo reparacion
		@return (obj) Repair'''		
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] Se toma el ultimo reparacion de la lista')
		if result.last():
			return self.__setObj(result)
		else:
			return False


	def findRepair(self,condition):
		'''Busca un Reparacion
		@param condition = {'id_tecnico like ' : '%4%'}
		@return list(obj) tipo myrepair'''
		myrepairs = []
		result = self.MyDb.selectQuery(self.table,'',condition)
		while result.next():
			myrepairs.append(self.__setObj(result))

		return myrepairs


	def createRepair(self, repair):
		''''Crea una reparacion
		@param (obj) Repair 
		@return (bool) | (int)'''

		values = {
			'id_reparacion' : repair.id_reparacion,
			'id_viaje' : repair.id_viaje,
			'id_vehiculo' : repair.id_vehiculo,
			'id_ciudad' : repair.id_ciudad,
			'periodo' : repair.periodo,
			'kilometros' : repair.kilometros,
			'fecha_salida' : repair.fecha_salida,
			'fecha_entrada' : repair.fecha_entrada,
			'notas' : repair.notas			
		}

		result = self.MyDb.insertQuery(self.table, values)

		if(result.numRowsAffected()>0):
			qDebug('[Debug] se crea una reparacion')
			return str(result.lastInsertId())
		else:
			qDebug('[Debug] No se crea una reparacion')
			return False


	def updateRepair(self,oldRepair,repair):
		'''Actualiza una reparacion
		@param (obj) repair
		@param (obj) repair
		@return (bool)
		'''
		condition = {' id_reparacion = ' : str(oldRepair.id_reparacion)}

		values = {
			'id_viaje' : repair.id_viaje,
			'id_vehiculo' : repair.id_vehiculo,
			'id_ciudad' : repair.id_ciudad,
			'periodo' : repair.periodo,
			'kilometros' : repair.kilometros,
			'fecha_salida' : repair.fecha_salida,
			'fecha_entrada' : repair.fecha_entrada,
			'notas' : repair.notas
			}

		result = self.MyDb.updateQuery(self.table,values,condition)

		if(result.numRowsAffected()>0):
			qDebug('[Debug] se Actualiza una reparacion')
			return True
		else:
			qDebug('[Debug] No se Actualiza una reparacion')
			return False


	def deleteRepair(self,repair):
		'''Elimina una reparacion
		@param (obj) repair
		@return (bool)'''		
		from repairItemClass import repairItemCatalog
		myrepairitemCatalog = repairItemCatalog()

		if(myrepairitemCatalog.deleteRepairItems(repair.id_reparacion)):			
			condition = {' id_reparacion = ' : str(repair.id_reparacion)}
			result = self.MyDb.deleteQuery(self.table,condition)		
			if(result.numRowsAffected()>0):
				qDebug('[Debug] se Elimina una reparacion')
				return True
			else:
				qDebug('[Debug] No se Elimina una reparacion')
				return False
		else:
			qDebug('No se puede eliminar los items de reparacion')
			return False


	def __setObj(self,result):
		'''Crea un objeto tipo repair
		@return (obj) repair '''
		myrepair = Repair()
		myrepair.id_reparacion = str(result.value(0))
		myrepair.id_viaje = str(result.value(1))
		myrepair.id_vehiculo = str(result.value(2))
		myrepair.id_ciudad = str(result.value(3))
		myrepair.periodo = str(result.value(4))
		myrepair.kilometros = str(result.value(5))
		myrepair.fecha_entrada = str(result.value(6))
		myrepair.fecha_salida = str(result.value(7))
		myrepair.notas = str(result.value(8))
		myrepair.registro = str(result.value(9))

		#validamos los campos nulos


		if(myrepair.id_ciudad.find('PyQt4.QtCore.')):
			myrepair.id_ciudad = None
		
		if(myrepair.notas.find('PyQt4.QtCore.')):
			myrepair.notas = None
		
		qDebug('Se crea una reparacion validados los campos nulos')

		return myrepair