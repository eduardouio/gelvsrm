#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Administracion de gastos
# File			viaje.py
# Ubicacion		aplicacion/basedatos/Modelo.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>

import sys
sys.path.append('..')
from PyQt4 import QtGui, QtCore, uic, Qt
from plantillas import polaris_rc
from clases.coustumerClass import *
from clases.invoiceClass import *
from clases.contactClass import *
from clases.cityClass import *
from clases.stateClass import *
from clases.vehicleClass import *
from clases.maintenanceClass import *
from clases.repairClass import *
from clases import helper

class Cliente(QtGui.QMainWindow):
	'''Representa al cliente dentro de la aplicacion final
	Esta en capacidad de administrar los clientes y sus contactos
	'''
	def __init__(self):
		''' Se inicializan las varianbles para el entorno'''
		# Si inicializa la clase
		QtGui.QMainWindow.__init__(self)              
		
		#propiedades de la Clase
		self.mapper = QtGui.QDataWidgetMapper(self)		

		#carag la interfaz
		self.ui = uic.loadUi('plantillas/frm_cliente.ui',self)		
		QtCore.qDebug('[Debug] Se carga la pantalla')		

		#conectamos señales y SLOTS navegador de registros
		self.connect(self.ui.btn_ultimo,QtCore.SIGNAL('clicked()'),self.mapper.toLast)	
		self.connect(self.ui.btn_anterior,QtCore.SIGNAL('clicked()'),self.mapper.toPrevious)
		self.connect(self.ui.btn_recargar,QtCore.SIGNAL('clicked()'),self.loadCoustomers)
		self.connect(self.ui.btn_siguiente,QtCore.SIGNAL('clicked()'),self.mapper.toNext)		
		self.connect(self.ui.btn_primero,QtCore.SIGNAL('clicked()'),self.mapper.toFirst)
		#self.mapper.currentIndexChanged.connect(self.setData)
		#conectamos señales y SLOTS de botones formulario
		self.connect(self.ui.btn_asignar_vehiculo,QtCore.SIGNAL('clicked()'),self.on_firstRow)
		self.connect(self.ui.btn_asignar_vehiculos,QtCore.SIGNAL('clicked()'),self.on_firstRow)
		self.connect(self.ui.btn_buscar,QtCore.SIGNAL('clicked()'),self.on_firstRow)
		self.connect(self.ui.btn_buscar_contacto,QtCore.SIGNAL('clicked()'),self.on_firstRow)
		self.connect(self.ui.btn_cancelar,QtCore.SIGNAL('clicked()'),self.on_firstRow)
		self.connect(self.ui.btn_copiar,QtCore.SIGNAL('clicked()'),self.on_firstRow)
		self.connect(self.ui.btn_eliminar,QtCore.SIGNAL('clicked()'),self.on_firstRow)
		self.connect(self.ui.btn_guardar,QtCore.SIGNAL('clicked()'),self.on_firstRow)
		self.connect(self.ui.btn_home,QtCore.SIGNAL('clicked()'),self.on_firstRow)
		self.connect(self.ui.btn_mantenimientos_4,QtCore.SIGNAL('clicked()'),self.on_firstRow)		
		self.connect(self.ui.btn_mostrar,QtCore.SIGNAL('clicked()'),self.on_firstRow)
		self.connect(self.ui.btn_nuevo,QtCore.SIGNAL('clicked()'),self.on_firstRow)
		#conectamos señales y SLOTS a los qaction
		self.connect(self.ui.actionAsignar_Polaris,QtCore.SIGNAL('triggered()'),self.on_firstRow)		
		self.connect(self.ui.actionNuevo,QtCore.SIGNAL('triggered()'),self.on_firstRow)
		self.connect(self.ui.actionRecargar,QtCore.SIGNAL('triggered()'),self.on_firstRow)
		self.connect(self.ui.action_Buscar,QtCore.SIGNAL('triggered()'),self.on_firstRow)
		self.connect(self.ui.action_Salir,QtCore.SIGNAL('triggered()'),self.on_firstRow)
		self.connect(self.ui.action_Volver	,QtCore.SIGNAL('triggered()'),self.on_firstRow)
		QtCore.qDebug('[Debug] Se enlanzan SIGNALS y SLOTS para todos los componenetes completos')
		#conectamos los signal del mayer
		self.loadCoustomers()
		self.ui.show()

	#Slot de prueba para conectar los objetos visuals
	@QtCore.pyqtSlot()
	def on_firstRow(self):
		'''Coloca la seleccion el el primer registro'''
		pass

	#Estructura para la carga de la pagina y valores relacionados 
	def loadCoustomers(self):
		'''Carga el listado completo de los clientes retorna un modelo'''	
		QtCore.qDebug('[Debug] Se llama a la funcion loadCoustomers')
		mycoustomerCatalog = coustomerCatalog()
		#se crea el modelo
		model = helper.createCoustomerModel(mycoustomerCatalog.listCoustomers())
		#se mapea los widgets
		self.mapper.setModel(model)
		QtCore.qDebug('[Debug] Se hace bindig el mapper con el model')			
		#self.mapper.setOrientation(QtCore.Qt.Horizontal)
		self.mapper.addMapping(self.ui.txt_ruc,0)				
		self.mapper.addMapping(self.ui.txt_nombre,3)
		self.mapper.addMapping(self.ui.txt_direccion,4)
		self.mapper.addMapping(self.ui.txt_telefono,5)
		self.mapper.addMapping(self.ui.txt_fax,6)
		self.mapper.addMapping(self.ui.txt_email,7)
		self.mapper.addMapping(self.ui.rtxt_notas,8)
		self.mapper.addMapping(self.ui.lbl_fecha_registrob,9)
		self.mapper.toFirst()
		QtCore.qDebug('[Debug] Se crea el Mapping a los widgets')

		self.loadInvoices('0560022430001')
		self.loadVehicles('0560022430001')


	def loadInvoices(self,idCoustomer):
		'''Retona un modelo con todas las facturas del cliente'''
		QtCore.qDebug('[Debug] Se cargan las facturas para el cliente %s' %idCoustomer)
		myinvoiceCatalog = invoiceCatalog()		
		model = helper.createInvoiceModel(myinvoiceCatalog.listInvoicesCoustomer(idCoustomer))
		self.ui.tbl_facturas.setModel(model)


	def loadVehicles(self,idCoustomer):
		'''retorna un modelo con todos los carros que estan registrados a
		nombre del cliente'''
		QtCore.qDebug('[Debug] Se cargan los vehiculos del cliente %s' %idCoustomer)
		myVehiclesCatalog = vehicleCatalog()
		model = helper.createVehicleModel(myVehiclesCatalog.listVehiclesCoustomer(idCoustomer))
		self.ui.tbl_vehiculos.setModel(model)

	def loadSates(self):
		'''carga el listado de todas las provincias en el modelo'''		
		#se carga el listado de las provincias en el list box
		myStateCatalog = stateCatalog()
		model = helper.creaStateModel(myStateCatalog.listStates())
		


	def loadCities(self,idState):
		'''carga el listado de todas ciudades de la provincia seleccionada
		y retorna un autocomplatar pata el lineEdit'''
		myCityCatalog = cityCatalog()
		model = myCityCatalog.listCitiesState(idState)


	def __setCity(self,City):
		'''Obtiene un objeto ciudad y lo retorna'''
		


	def __setContact(self,Contact):
		'''Obtiene un objeto tipo contacto y lo retorna'''
		

	def __setState(self,State):
		'''Obtine un objeto tipo estado y lo retorna'''
		

		

#Inicia el entorno de la aplicacion
if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = Cliente()
	sys.exit(app.exec_())