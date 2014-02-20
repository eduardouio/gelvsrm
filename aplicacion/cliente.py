#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Administracion de gastos
# File			viaje.py
# Ubicacion		aplicacion/basedatos/Modelo.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
#self.id_cliente = id_cliente
#self.id_contacto = id_contacto
#self.id_ciudad = id_ciudad
#self.nombre = nombre
#self.direccion = direccion
#self.telefono = telefono
#self.fax = fax
#self.mail = mail
#self.notas = notas
#self.registro = QDateTime().currentDateTime()

import sys
sys.path.append('..')
from PyQt4 import QtGui, QtCore, uic, Qt
from plantillas import polaris_rc
from clases.coustumerClass import *
from clases.cityClass import *
from clases.stateClass import *
from clases.contactClass import *
from clases import helper

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = Cliente()
	sys.exit(app.exec_())

#Estructura completa del formulario

class Cliente(QtGui.QMainWindow):
	'''Representa al cliente dentro de la aplicacion final
	Esta en capacidad de administrar los clientes y sus contactos
	'''
	def __init__(self):
		''' Se inicializan las varianbles para el entorno'''
		#propiedades de la Clase
		self.mapper = QtGui.QDataWidgetMapper(self)		

		# Si inicializa la clase
		QtGui.QMainWindow.__init__(self)              
		#carag la interfaz
		self.ui = uic.loadUi('plantillas/frm_cliente.ui',self)		
		QtCore.qDebug('[Debug] Se carga la pantalla')		

		#conectamos señales y SLOTS navegador de registros
		self.connect(self.ui.btn_ultimo,QtCore.SIGNAL('clicked()'),self.on_firstRow)	
		self.connect(self.ui.btn_anterior,QtCore.SIGNAL('clicked()'),self.mapper.toPrevious)
		self.connect(self.ui.btn_recargar,QtCore.SIGNAL('clicked()'),self.on_firstRow)
		self.connect(self.ui.btn_siguiente,QtCore.SIGNAL('clicked()'),self.mapper.toNext)		
		self.connect(self.ui.btn_primero,QtCore.SIGNAL('clicked()'),self.on_firstRow)
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
		QtCore.qDebug('Se enlanzan SIGNALS y SLOTS para todos los componenetes completos')
		#conectamos los signal del mayer
		self.mapper.currentIndexChanged.connect(self.setData)
		
		self.ui.show()

	#se programan todos los slots de programacion
	@QtCore.pyqtSlot()
	def on_firstRow(self):
		'''Coloca la seleccion el el primer registro'''
		pass

	# se programan las funcionalidades de la widget
	def load(self):
		'''Se encarga de listar todos los registros'''
		mycoustomerCatalog = coustomerCatalog()
		coustomers = mycoustomerCatalog.listCoustomers()
		#se crea el modelo
		self.__createModel(len(coustomers),helper.countColumns('cliente'),coustomers)
		QtCore.qDebug('Se carga la informacion de los clientes')

		#se carga el listado de las provincias en el list box
		myStateCatalog = stateCatalog()
		states = myStateCatalog.listStates()
		model = QtGui.QStandardItemModel(len(states),1)
		for x,state in enumerate(states):					
			item = QtGui.QStandardItem(state.nombre)
			model.setItem(x,0,item)

		self.ui.cmb_provincia.clear()
		self.ui.cmb_provincia.setModel(model)
		QtCore.qDebug('Se crea un modelo de las provincias y se alimenta el combobox')
			


	def __createModel(self, x,y,data):
		'''Se crea un standart model para alamacenar la info antes de asignarla a los widgets '''
		#se crea el model y carga los datos al model		
		self.model = QtGui.QStandardItemModel(x,y)						
		i = 0
		for x, Mycoustomer in enumerate(data):
			item = QtGui.QStandardItem(Mycoustomer.id_cliente)  
			self.model.setItem(x,0,item)
			item = QtGui.QStandardItem(Mycoustomer.id_contacto)
			self.model.setItem(x,1,item)
			item = QtGui.QStandardItem(Mycoustomer.id_ciudad)
			self.model.setItem(x,2,item)
			item = QtGui.QStandardItem(Mycoustomer.nombre)
			self.model.setItem(x,3,item)
			item = QtGui.QStandardItem(Mycoustomer.direccion)
			self.model.setItem(x,4,item)
			item = QtGui.QStandardItem(Mycoustomer.telefono)
			self.model.setItem(x,5,item)
			item = QtGui.QStandardItem(Mycoustomer.fax)
			self.model.setItem(x,6,item)
			item = QtGui.QStandardItem(Mycoustomer.mail)
			self.model.setItem(x,7,item)
			item = QtGui.QStandardItem(Mycoustomer.notas)
			self.model.setItem(x,8,item)
			item = QtGui.QStandardItem(Mycoustomer.registro)
			self.model.setItem(x,9,item)
			QtCore.qDebug('Se asiga un objeto al model')

		#se mapea los widgets
		#self.mapper.setOrientation(QtCore.Qt.Horizontal)
		self.mapper.setModel(self.model)
		self.mapper.addMapping(self.ui.txt_ruc,0)
		self.mapper.addMapping(self.ui.cmb_contacto,1)		
		self.mapper.addMapping(self.ui.txt_cuidad,2)
		self.mapper.addMapping(self.ui.txt_nombre,3)
		self.mapper.addMapping(self.ui.txt_direccion,4)
		self.mapper.addMapping(self.ui.txt_telefono,5)
		self.mapper.addMapping(self.ui.txt_fax,6)
		self.mapper.addMapping(self.ui.txt_email,7)
		self.mapper.addMapping(self.ui.rtxt_notas,8)
		self.mapper.addMapping(self.ui.lbl_fecha_registrob,9)
		QtCore.qDebug('Se crea el Mapping a los widgets')



	#Estructura para la carga de la pagina y valores relacionados 
	def loadCoustomers():
		'''Carga el listado completo de los clientes'''
		pass

	def loadVehicles(idCoustomer):
		'''retorna un modelo con todos los carros que estan registrados a
		nombre del cliente'''
		pass

	def loadInvoices(idCoustomer):
		'''Retona un modelo con todas las facturas del cliente'''
		pass

	def loadSates():
		'''carga el listado de todas las provincias en el modelo'''
		pass

	def loadCities():
		'''carga el listado de todas ciudades de la provincia seleccionada
		y retorna un autocomplatar pata el lineEdit'''
		pass

	def setData(idCoustomer):
		'''Ubica los datos en el formulario'''
		pass

	def __setCity(idCity):
		'''Obtiene un objeto ciudad y lo retorna'''
		myCityCatalog = cityCatalog()
		return myCityCatalog.getCity(idCity)


	def __setContact(idContact):
		'''Obtiene un objeto tipo contacto y lo retorna'''
		myContactCatalog = contactCatalog()
		return myContactCatalog.getContact(idContact)	

	def __setState(idState):
		'''Obtine un objeto tipo estado y lo retorna'''
		myStateCatalog = stateCatalog()
		return myStateCatalog.getState(idState)
