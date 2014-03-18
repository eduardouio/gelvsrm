#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version 1.0
# Autor Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package Administracion de gastos
# File viaje.py
# Ubicacion aplicacion/basedatos/Modelo.py
# Copyright (c) 2013 gelvsrm <eduardouio7@gmail.com>
#tableview = QtWidgets.QTableView(self)
# tableview.setModel(model)
# tableview.resize(940, 380)
# tableview.show()

import sys
sys.path.append('..')
from PyQt5 import QtGui, QtCore, uic, Qt
from PyQt5 import QtWidgets, Qt
from PyQt5 import QtWidgets
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

class Cliente(QtWidgets.QMainWindow):
	'''Representa al cliente dentro de la aplicacion final
	Esta en capacidad de administrar los clientes y sus contactos
	'''
	def __init__(self):
		''' Se inicializan las varianbles para el entorno'''
		# Si inicializa la clase
		QtWidgets.QMainWindow.__init__(self)

		#propiedades de la Clase
		self.mapper = QtWidgets.QDataWidgetMapper(self)	

		#caraga la interfaz
		self.ui = uic.loadUi('plantillas/frm_cliente.ui',self)	
		QtCore.qDebug('[Debug][Debug] Se carga la pantalla')	

		#conectamos señales y SLOTS navegador de registros
		self.ui.btn_ultimo.clicked.connect(self.mapper.toLast)	
		self.ui.btn_anterior.clicked.connect(self.mapper.toPrevious)
		self.ui.btn_recargar.clicked.connect(self.loadCoustomers)
		self.ui.btn_siguiente.clicked.connect(self.mapper.toNext)	
		self.ui.btn_primero.clicked.connect(self.mapper.toFirst)
		self.mapper.currentIndexChanged.connect(self.setData)
		#conectamos señales y SLOTS de botones formulario
		self.ui.btn_asignar_vehiculo.clicked.connect(self.on_firstRow)
		self.ui.btn_asignar_vehiculos.clicked.connect(self.on_firstRow)
		self.ui.btn_buscar.clicked.connect(self.on_firstRow)
		self.ui.btn_buscar_contacto.clicked.connect(self.on_firstRow)
		self.ui.btn_cancelar.clicked.connect(self.on_firstRow)
		self.ui.btn_copiar.clicked.connect(self.on_firstRow)
		self.ui.btn_eliminar.clicked.connect(self.on_firstRow)
		self.ui.btn_guardar.clicked.connect(self.on_firstRow)
		self.ui.btn_home.clicked.connect(self.on_firstRow)
		self.ui.btn_mantenimientos_4.clicked.connect(self.on_firstRow)	
		self.ui.btn_mostrar.clicked.connect(self.on_firstRow)
		self.ui.btn_nuevo.clicked.connect(self.on_firstRow)
		#conectamos señales y SLOTS a los qaction
		self.ui.actionAsignar_Polaris.triggered.connect(self.on_firstRow)	
		self.ui.actionNuevo.triggered.connect(self.on_firstRow)
		self.ui.actionRecargar.triggered.connect(self.on_firstRow)
		self.ui.action_Buscar.triggered.connect(self.on_firstRow)
		self.ui.action_Salir.triggered.connect(self.on_firstRow)
		self.ui.action_Volver.triggered.connect(self.on_firstRow)
		QtCore.qDebug('[Debug][Debug] Se enlanzan SIGNALS y SLOTS para todos los componenetes completos')
		#conectamos los signal del mayer
		self.loadCoustomers()
		self.ui.show()

	#Slot de prueba para conectar los objetos visuales
	@QtCore.pyqtSlot()
	def on_firstRow(self):
		'''Coloca la seleccion el el primer registro'''
		pass

	@QtCore.pyqtSlot()
	def setData(self):
		'''Coloca la informacion en los cuadros de texto, cuando el indedel mapper cambia
		cambia la informacion oara
		Los vehiculos => Los mantenimientos => las facturas
		Los contactos => los estados => las ciudades'''	
		#se detecta el cambio en el indice del mapper
		index = self.mapper.currentIndex()
		model = self.mapper.model()	
		QtCore.qDebug('[Debug]Se toma el el indice %s del modelo del cliente'% str(index))
		idCoustomer = model.item(index,0)
		mycoustomerCatalog = coustomerCatalog()	
		mycoustomer = mycoustomerCatalog.getCoustomer(idCoustomer.text())

		#obtengo en id del cliente
		modelInvoice = self.loadInvoices(idCoustomer.text())
		modelVehicles = self.loadVehicles(idCoustomer.text())
		self.ui.rtxt_notas.clear()
		self.ui.rtxt_notas.setHtml(mycoustomer.notas)	
		QtCore.qDebug('[Debug] se carga las notas %s'% mycoustomer.notas)

	@QtCore.pyqtSlot()
	def loadCoustomers(self):
		'''Carga el listado completo de los clientes retorna un modelo'''	
		QtCore.qDebug('[Debug][Debug] Se llama a la funcion loadCoustomers')
		mycoustomerCatalog = coustomerCatalog()
		#se crea el modelo
		model = helper.createCoustomerModel(mycoustomerCatalog.listCoustomers())
		#se mapea los widgets
		self.mapper.setModel(model)
		QtCore.qDebug('[Debug][Debug] Se hace bindig el mapper con el model')	
		#self.mapper.setOrientation(QtCore.Qt.Horizontal)
		self.mapper.addMapping(self.ui.txt_ruc,0)
		self.mapper.addMapping(self.ui.txt_nombre,3)
		self.mapper.addMapping(self.ui.txt_direccion,4)
		self.mapper.addMapping(self.ui.txt_telefono,5)
		self.mapper.addMapping(self.ui.txt_fax,6)
		self.mapper.addMapping(self.ui.txt_email,7)	
		self.mapper.addMapping(self.ui.rtxt_notas,8)
		self.mapper.addMapping(self.ui.lbl_fecha_registrob,9,"text")
		self.mapper.addMapping(self.ui.lbl_rucb,0,"text")
		self.mapper.toFirst()
		QtCore.qDebug('[Debug][Debug] Se crea el Mapping a los widgets')	


	def loadInvoices(self,idCoustomer):	
		'''Retona un modelo con todas las facturas del cliente'''
		QtCore.qDebug('[Debug][Debug] Se cargan las facturas para el cliente %s' %idCoustomer)
		myinvoiceCatalog = invoiceCatalog()	
		model = helper.createInvoiceModel(myinvoiceCatalog.listInvoicesCoustomer(idCoustomer))
		self.ui.tbl_facturas.setModel(model)


	def loadVehicles(self,idCoustomer):
		'''retorna un modelo con todos los carros que estan registrados a
		nombre del cliente'''
		QtCore.qDebug('[Debug][Debug] Se cargan los vehiculos del cliente %s' %idCoustomer)
		myVehiclesCatalog = vehicleCatalog()
		model = helper.createVehicleModel(myVehiclesCatalog.listVehiclesCoustomer(idCoustomer))
		self.ui.tbl_vehiculos.setModel(model)

	def loadSates(self):
		'''carga el listado de todas las provincias en el modelo'''	
		#se carga el listado de las provincias en el list box
		myStateCatalog = stateCatalog()
		model = helper.creaStateModel(myStateCatalog.listStates())
		return model	

	def loadCities(self,idState):
		'''carga el listado de todas ciudades de la provincia seleccionada
		y retorna un autocomplatar pata el lineEdit'''
		myCityCatalog = cityCatalog()
		model = helper.createCityModel(myCityCatalog.listCitiesState(idState))
		return model

	#Inicia el entorno de la aplicacion
if __name__ == '__main__':				
	app = QtWidgets.QApplication(sys.argv)
	window = Cliente()
	sys.exit(app.exec_())