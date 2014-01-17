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
from PyQt4 import QtGui, QtCore, uic
from plantillas import polaris_rc
from clases.coustumerClass import Coustomer, coustomerCatalog
from clases.cityClass import City, cityCatalog

class Cliente(QtGui.QMainWindow):
	'''Representa al cliente dentro de la aplicacion final
	Esta en capacidad de administrar los clientes y sus contactos
	'''
	def __init__(self):
		''' Se crea los objetos y se realiza las conexiones necesarias para
		el funcionamiento del formulario
		'''
		self.debug = QtCore.qDebug
		QtGui.QMainWindow.__init__(self)              
		#concectamos señales pushbutton
		self.ui = uic.loadUi('plantillas/frm_cliente.ui',self)
		self.connect(self.ui.btn_anterior,QtCore.SIGNAL('clicked()'),self.on_firstRow)
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
		self.connect(self.ui.btn_monstrar_3,QtCore.SIGNAL('clicked()'),self.on_firstRow)
		self.connect(self.ui.btn_monstrar_seleccionados,QtCore.SIGNAL('clicked()'),self.on_firstRow)
		self.connect(self.ui.btn_mostrar,QtCore.SIGNAL('clicked()'),self.on_firstRow)
		self.connect(self.ui.btn_nuevo,QtCore.SIGNAL('clicked()'),self.on_firstRow)
		self.connect(self.ui.btn_primero,QtCore.SIGNAL('clicked()'),self.on_firstRow)
		self.connect(self.ui.btn_recargar,QtCore.SIGNAL('clicked()'),self.on_firstRow)
		self.connect(self.ui.btn_siguiente,QtCore.SIGNAL('clicked()'),self.on_firstRow)
		self.connect(self.ui.btn_ultimo,QtCore.SIGNAL('clicked()'),self.on_firstRow)	
		#conecatmos señales qaction
		self.connect(self.ui.actionAsignar_Polaris,QtCore.SIGNAL('triggered()'),self.on_firstRow)		
		self.connect(self.ui.actionNuevo,QtCore.SIGNAL('triggered()'),self.on_firstRow)
		self.connect(self.ui.actionRecargar,QtCore.SIGNAL('triggered()'),self.on_firstRow)
		self.connect(self.ui.action_Buscar,QtCore.SIGNAL('triggered()'),self.on_firstRow)
		self.connect(self.ui.action_Salir,QtCore.SIGNAL('triggered()'),self.on_firstRow)
		self.connect(self.ui.action_Volver	,QtCore.SIGNAL('triggered()'),self.on_firstRow)
		self.ui.show()


	@QtCore.pyqtSlot(str)
	def on_firstRow(self):
		mycliente = coustomerCatalog().firstCoustomer()
		self.ui.txt_nombre.setText(mycliente.nombre)
		self.ui.txt_ruc.setText(mycliente.id_cliente)
		self.ui.txt_direccion.setText(mycliente.direccion)
		
		

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = Cliente()
	sys.exit(app.exec_())
