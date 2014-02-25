#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			buyTravelClass.py
# Ubicacion		aplicacion/clases/buyTravelClass.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
# +----------------+-----------------------+------+-----+-------------------+----------------+
# 									Data Types
# +----------------+-----------------------+------+-----+-------------------+----------------+
# | Field          | Type                  | Null | Key | Default           | Extra          |
# +----------------+-----------------------+------+-----+-------------------+----------------+
# | id_gasto_viaje | mediumint(8) unsigned | NO   | UNI | NULL              | auto_increment |
# | id_viaje       | smallint(5) unsigned  | NO   | PRI | NULL              |                |
# | nro_factura    | varchar(20)           | NO   | PRI | NULL              |                |
# | fecha          | date                  | NO   |     | NULL              |                |
# | detalle        | varchar(300)          | NO   |     | NULL              |                |
# | valor          | decimal(4,2)          | NO   | PRI | NULL              |                |
# | tipo           | varchar(45)           | YES  |     | NULL              |                |
# | registro       | timestamp             | NO   |     | CURRENT_TIMESTAMP |                |
# +----------------+-----------------------+------+-----+-------------------+----------------+

import sys
sys.path.append('..')
from modelo.Modelo import DB
from PyQt4.QtCore import QDateTime, QDate, QTime, qDebug, QPyNullVariant

class buyTravel(object):
	"""estructura para los gastos viajes"""
	def __init__(self,id_gasto_viaje=int(), id_viaje=int(),nro_factura='',fecha='',
					detalle='',valor=float(),tipo='',registro=''):
		super(buyTravel, self).__init__()
		self.id_gasto_viaje = id_gasto_viaje
		self.id_viaje = id_viaje
		self.nro_factura = nro_factura
		self.fecha = QDate().currentDate()
		self.detalle = detalle
		self.valor = valor
		self.tipo = tipo
		self.registro = QDateTime().currentDateTime()
		qDebug('[Debug] se instancia la clase buyTravel')
		

class buyTravelCatalog(object):
	"""acciones para buyTravel"""

	def __init__(self):
		super(buyTravelCatalog, self).__init__()
		self.table = 'gastos_viaje'
		self.MyDb = DB()
		qDebug('[Debug] se inicia la clase buyTravelCatalog')


	def getBuyTravel(self, idBuyTravel):
		'''Obtiene un gastos 
		@param (str) id_gasto_viaje
		@result (buyTravel)'''				
		condition = {' id_gasto_viaje = ' : str(idBuyTravel)}
		result = self.MyDb.selectQuery(self.table,'',condition)
		qDebug('[Debug] la consulta retorno %s resultados' % result.size())		
		if result.next():
			return self.__setObj(result)
		else:
			qDebug('[Debug] Problemas para retornar un valor')
			return False

		
	def listBuysTravel(self, idTravel):
		'''Lista las compras de un viaje
		@return lst(buyTravel) si el viaje no existe retorna una lista vacia'''
		condition = {' id_viaje = ' : str(idTravel)}
		result = self.MyDb.selectQuery(self.table,'',condition)
		qDebug('[Debug] la consulta retorno %s resultados' % result.size())		
		mybuysTravel = []
		while result.next:
			mybuysTravel.append(self.__setObj(result))

		return mybuysTravel
			

	def listBuysTravels(self):
		'''Lista todas las compras de la tabla
		@return lst(buyTravel)'''	
		buystravel = []
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] la consulta retorno %s resultados' % result.size())		
		while result.next():			
			buystravel.append(self.__setObj(result))

		return buystravel


	def firstBuyTravel(self):
		'''retorna el primer buyTravel de la lista
		@return (obj) buyTravel'''		
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] Se toma el primer buyTravel de la lista')
		if result.first():
			return self.__setObj(result)
		else:
			return False


	def lastBuyTravel(self):
		'''retorna el ultimo buyTravel de la Lista
		@return (obj) buyTravelo'''
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] Se toma ultimo buyTravel de la lista')
		if result.last():
			return self.__setObj(result)
		else:
			return False


	def findBuyTravel(self,condition):
		'''Busca un buyTravel
		@param condition = {'id_tecnico like ' : '%4%'}
		@return list(obj) tipo buyTravel'''
		buyTravels = []
		result = self.MyDb.selectQuery(self.table,'',condition)
		while result.next():
			buyTravels.append(self.__setObj(result))

		return buyTravels


	def createBuyTravel(self,buyTravel):
		'''Se crea un gasto de viaje
		@param (obj) gastos_viaje
		@param (bool) | (int)
		'''
		values = {
			'id_viaje' : str(buyTravel.id_viaje),
			'nro_factura' : str(buyTravel.nro_factura),
			'fecha' : str(buyTravel.fecha),
			'detalle' : str(buyTravel.detalle),
			'valor' : str(buyTravel.valor),
			'tipo' : str(buyTravel.tipo)			
		}

		result = self.MyDb.insertQuery(self.table,values)

		if (result.numRowsAffected() > 0):
			qDebug('[Debug] Se crea un buyTravel en la base de datos')		
			return result.lastInsertId()
		else:
			qDebug('[Debug] No se crea un buyTravel en la base de datos')		
			return False


	def updateBuyTravel(self,oldBuyTravel, buyTravel):
		'''Actualiza un gasto de viaje
		@param (obj) buyTravel
		@param (obj) buyTravel
		@return (bool)
		'''
		condition = {' id_gasto_viaje =  ' : str(oldBuyTravel.id_gasto_viaje)}
		values = {
			'id_viaje' : str(buyTravel.id_viaje),
			'nro_factura' : str(buyTravel.nro_factura),
			'fecha' : str(buyTravel.fecha),
			'detalle' : str(buyTravel.detalle),
			'valor' : str(buyTravel.valor),
			'tipo' : str(buyTravel.tipo)			
		}

		result = self.MyDb.updateQuery(self.table,values,condition)

		if (result.numRowsAffected() > 0):
			qDebug('[Debug] Se Actualiza un buyTravel en la base de datos')		
			return True
		else:
			qDebug('[Debug] No se Actualiza un buyTravel en la base de datos')		
			return False


	def deleteBuyTravel(self,buyTravel):
		'''Elimina un gasto de viaje
		@param (obj) buyTravel
		@return (bool)'''
		condition = {' id_gasto_viaje = ' : str(buyTravel.id_gasto_viaje)}
		result = self.deleteQuery(self.table,condition)

		if (result.numRowsAffected() > 0):
			qDebug('[Debug] Se Elimina un buyTravel en la base de datos')		
			return True
		else:
			qDebug('[Debug] No se Elimina un buyTravel en la base de datos')		
			return False


	def __setObj(self, result):
		'''Crea un objeto tipo Conctact y lo retorna
		@param (obj) result
		@return (obj) buyTravel'''
		mybuyTravel = buyTravel()
		mybuyTravel.id_gasto_viaje = result.value(0)
		mybuyTravel.id_viaje = result.value(1)
		mybuyTravel.nro_factura = result.value(2)
		mybuyTravel.fecha = result.value(3)
		mybuyTravel.detalle = result.value(4)
		mybuyTravel.valor = float(result.value(5))
		mybuyTravel.tipo = result.value(6)
		registro = result.value(7)

		#se validan los campos NULL
		if isinstance(mybuy.tipo,QPyNullVariant):
			mybuy.tipo = None

		mybuyTravel.registro = registro.toString()

		qDebug('[DEbug] Se inicia un objeto compra viaje validado los campos NULL')
		return mybuyTravel