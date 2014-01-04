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
from clases.travelClass import Travel, travelCatalog

class frmViaje(QtGui.QMainWindow):
	def __init__(self,parent=None): 
		QtGui.QMainWindow.__init__(self,parent)			
		self.ventana = uic.loadUi('plantillas/frm_viaje.ui',self)
		self.ventana.show()
		self.myTravel = Travel()
		self.myTravelCatalog = travelCatalog()
		self.inicial()

	def inicial(self):
		'''Enlaza las señales y slots'''
		travels = self.myTravelCatalog.getTravels(2)
		#print(travels.registro)

		fecha = QtCore.QDateTime()

		#self.ventana.lbl_fecha_registrob.setText(str(travels.registro.toPyDate()))
		self.ventana.rtxt_informe.setText(travels.informe)
		self.ventana.lbl_id_viajeb.setText(travels.id_viaje)
		self.ventana.cmb_fecha_salida.setDateTime(fecha)
		
if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	myapp = frmViaje()	
	sys.exit(app.exec_())



