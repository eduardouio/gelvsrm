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
import viaje
from plantillas import polaris_rc

class Main(QtGui.QMainWindow):
	'''Clase principal de la aplicacion GELVS
	Ventana encargada de gestionar todas las ventanas
	y widgets de la aplicacion '''
	def __init__(self): 
		QtGui.QMainWindow.__init__(self)
		ventana = uic.loadUi('plantillas/main_window.ui',self)
		ventana.show()


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = Main()
	sys.exit(app.exec_())