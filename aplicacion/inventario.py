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

class Inventario(QtGui.QMainWindow):
		def __init__(self): 
			QtGui.QMainWindow.__init__(self)
			ventana = uic.loadUi('plantillas/frm_inventario.ui',self)
			ventana.show()

def main():
	print('Hola munfio')
	app = QtGui.QApplication(sys.argv)
	window = Inventario()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()
