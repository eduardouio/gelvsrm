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
from PyQt5 import QtGui, QtCore, uic, Qt
from PyQt5 import QtWidgets
from plantillas import polaris_rc

class Viaje(QtWidgets.QMainWindow):
		def __init__(self): 
			QtWidgets.QMainWindow.__init__(self)
			ventana = uic.loadUi('plantillas/frm_vehiculo.ui',self)
			ventana.show()

app = QtWidgets.QApplication(sys.argv)
window = Viaje()
sys.exit(app.exec_())
