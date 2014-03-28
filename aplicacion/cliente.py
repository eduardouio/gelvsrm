#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version 1.0
# Autor Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package Administracion de gastos
# File viaje.py
# Ubicacion aplicacion/basedatos/Modelo.py
# Copyright (c) 2013 gelvsrm <eduardouio7@gmail.com>
# tableview = QtWidgets.QTableView(self)
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
from clases.vehicleClass import *
from clases.invoiceClass import *
from clases.contactClass import *
from clases.cityClass import *
from clases.stateClass import *
from clases.maintenanceClass import *
from clases.repairClass import *
from clases import helper

class Cliente(QtWidgets.QMainWindow):
	'''Representa al cliente dentro de la aplicacion fina
	lEsta en capacidad de administrar los clientes y sus contactos
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
		self.ui.btn_primero.clicked.connect(self.mapper.toFirst)
		self.ui.btn_anterior.clicked.connect(self.mapper.toPrevious)
		self.ui.btn_siguiente.clicked.connect(self.mapper.toNext)
		self.ui.btn_ultimo.clicked.connect(self.mapper.toLast)
		self.mapper.currentIndexChanged.connect(self.setData)
		#conectamos señales y SLOTS de botones formulario
		self.ui.btn_home.clicked.connect(self.on_goHome)
		self.ui.btn_recargar.clicked.connect(self.on_loadCoustomers)
		self.ui.btn_nuevo.clicked.connect(self.on_newCoustomer)
		self.ui.btn_editar.clicked.connect(self.on_editCoustomer)
		self.ui.btn_guardar.clicked.connect(self.on_save_Coustomer)
		self.ui.btn_eliminar.clicked.connect(self.on_deleteCoutomer)
		self.ui.btn_cancelar.clicked.connect(self.on_cancelAction)
		self.ui.btn_buscar_contacto.clicked.connect(self.on_searchContact)
		self.ui.btn_asignar_vehiculo.clicked.connect(self.on_setVehicle)
		self.ui.btn_asignar_vehiculos.clicked.connect(self.on_setVehicle)
		self.ui.btn_mostrar_vehiculo.clicked.connect(self.on_showVehicle)
		self.ui.btn_crear_factura.clicked.connect(self.on_createInvoice)
		self.ui.btn_mostrar_factura.clicked.connect(self.on_showInvice)
		self.ui.btn_buscar.clicked.connect(self.on_searchCoustomer)
		self.ui.btn_mostrar_cliente.clicked.connect(self.on_showCoutomer)
		#conectamos los Slots del comobobox
		#cmb_columna.currentIndexChanged.connect(self.on_)
		#cmb_operador.currentIndexChanged.connect(self.on_)
		#cmb_provincia.currentIndexChanged.connect(self.on_)
		#conectamos señales y SLOTS a los qaction|
		self.ui.actionAsignar_Polaris.triggered.connect(self.on_setVehicle)	
		self.ui.actionNuevo.triggered.connect(self.on_newCoustomer)
		self.ui.actionRecargar.triggered.connect(self.on_loadCoustomers)
		self.ui.action_Buscar.triggered.connect(self.on_searchCoustomer)
		self.ui.action_Salir.triggered.connect(self.on_goHome)
		self.ui.action_Volver.triggered.connect(self.on_goHome)

		QtCore.qDebug('[Debug][Debug] Se enlanzan SIGNALS y SLOTS para todos los componenetes completos')
		#conectamos los signal del mayer
		self.on_loadCoustomers()
		self.ui.show()

		#variable de la clase, que ayuda a la manejar 
		self.myContact = Contact()
		self.myCity = City()
		self.myState = State()

###############################################Slots Application#####################################################
	
	@QtCore.pyqtSlot()
	def on_toFirst():
		self.mapper.toFirst()
		#obtenemos un objeto de cada una de las relaciones del objeto 
		self.myContact = getContact(self.lbl_rucb.getText())
		self.myState = getSate(self.lbl_rucb.getText())
		self.myCity = getCity(self.lbl_rucb.getText())

	@QtCore.pyqtSlot()
	def on_toPrevious():
		self.mapper.toPrevious()
		#obtenemos un objeto de cada una de las relaciones del objeto 
		self.myContact = getContact(self.lbl_rucb.getText())
		self.myState = getSate(self.lbl_rucb.getText())
		self.myCity = getCity(self.lbl_rucb.getText())
				
		self.ui.btn_siguiente.clicked.connect(self.mapper.toNext)
		self.ui.btn_ultimo.clicked.connect(self.mapper.toLast)
	@QtCore.pyqtSlot()
	@QtCore.pyqtSlot()
	@QtCore.pyqtSlot()

	@QtCore.pyqtSlot()
	def on_goHome(self):
		'''Slot encargado cierra el formulario y va al Home'''
		pass


	@QtCore.pyqtSlot()
	def on_newCoustomer(self):
		'''Slot encargado de crear un nuevo Cliente'''
		#se limpia el formulario		
		self.blank_Form()
		mycoustomer = getData()

		

	@QtCore.pyqtSlot()
	def on_editCoustomer(self):
		'''Slot encargado'''
		pass


	@QtCore.pyqtSlot()
	def on_save_Coustomer(self):
		'''Slot encargado'''
		pass


	@QtCore.pyqtSlot()
	def on_deleteCoutomer(self):
		'''Slot encargado'''
		pass


	@QtCore.pyqtSlot()
	def on_cancelAction(self):
		'''Slot encargado'''
		pass


	@QtCore.pyqtSlot()
	def on_searchContact(self):
		'''Slot encargado'''
		pass


	@QtCore.pyqtSlot()
	def on_showVehicle(self):
		'''Slot encargado'''
		pass


	@QtCore.pyqtSlot()
	def on_createInvoice(self):
		'''Slot encargado'''
		pass


	@QtCore.pyqtSlot()
	def on_showInvice(self):
		'''Slot encargado'''
		pass


	@QtCore.pyqtSlot()
	def on_showCoutomer(self):
		'''Slot encargado'''
		pass


	@QtCore.pyqtSlot()
	def on_setVehicle(self):
		'''Slot encargado'''
		pass


	@QtCore.pyqtSlot()
	def on_searchCoustomer(self):
		'''Slot encargado'''
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
	def on_loadCoustomers(self):
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


###############################################Fucniones comunes applicacion#####################################################
	
	def getData(self):
		'''Valida los datos del formulario y los retorna en un objeto'''
		mycoustomer = Coustomer()
		#validamos los datos del Form


	def blank_Form(self):
		'''Blanquea el Fomulario y bloquea controles'''
		#se elimina los datos de los labels y lineedits para evento new
		self.ui.lbl_ultimo_mantenimientob.clear()
		self.ui.lbl_fecha_registrob.clear()
		self.ui.lbl_rucb.clear()
		self.ui.lbl_vehiculosb.clear()
		self.ui.lbl_facturasb.clear()
		self.ui.lbl_contactob.clear()
		self.ui.lbl_vehiculos_asignadosb.clear()
		self.ui.lbl_mantenimientosb.clear()
		self.ui.lbl_reparacionesb.clear()
		self.ui.lbl_ultima_facturab.clear()
		self.ui.lbl_facturas_emitidasb.clear()
		self.ui.lbl_contactoob.clear()
		self.ui.lbl_telefonob.clear()		
		self.ui.txt_nombre.clear()
		self.ui.txt_email.clear()
		self.ui.txt_ruc.clear()
		self.ui.txt_direccion.clear()
		self.ui.txt_cuidad.clear()
		self.ui.txt_fax.clear()
		self.ui.txt_telefono.clear()
		self.ui.rtxt_notas.clear()
		#se deshabilita las tabs
		self.ui.tab_vehiculo.setHidden(1)
		self.ui.tab_buscar.setHidden(1)
		self.ui.tab_facturas.setHidden(1)
		#se deshabilita los botones
		#if self.ui.btn_home.isHiddenn():
		self.ui.btn_home.setHidden(1)
		self.ui.btn_editar.setHidden(1)
		self.ui.btn_primero.setHidden(1)
		self.ui.btn_anterior.setHidden(1)
		self.ui.btn_recargar.setHidden(1)
		self.ui.btn_siguiente.setHidden(1)
		self.ui.btn_ultimo.setHidden(1)
		self.ui.btn_asignar_vehiculo.setHidden(1)
		self.ui.btn_nuevo.setHidden(1)
		self.ui.btn_eliminar.setHidden(1)
		self.ui.btn_asignar_vehiculos.setHidden(1)
		self.ui.btn_mostrar_vehiculo.setHidden(1)
		self.ui.btn_crear_factura.setHidden(1)
		self.ui.btn_mostrar_factura.setHidden(1)
		self.ui.btn_buscar.setHidden(1)
		self.ui.txt_ruc.setFocus()
		QtCore.qDebug('[Debug][Debug] Se Blanquea el formulario y se elimina el mapper ')


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