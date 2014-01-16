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
from clases import coustumerClass

class Viaje(QtGui.QMainWindow):
		def __init__(self):
			self.debug = QtCore.qDebug
			QtGui.QMainWindow.__init__(self)			
			ventana = uic.loadUi('plantillas/frm_cliente.ui',self)
			self.debug('Gola prueba de erencia')
			self.debug('Gola prueba de erencia')
			self.debug('Gola prueba de erencia')
			self.debug('Gola prueba de erencia')
			self.debug('Gola prueba de erencia')
			self.debug('Gola prueba de erencia')
			self.debug('Gola prueba de erencia')
			self.debug('Gola prueba de erencia')
			self.debug('Gola prueba de erencia')
			ventana.show()

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = Viaje()
	sys.exit(app.exec_())