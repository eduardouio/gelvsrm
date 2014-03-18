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

class Main(QtWidgets.QMainWindow):
    '''Clase principal de la aplicacion GELVS
    Ventana encargada de gestionar todas las ventanas
    y widgets de la aplicacion '''

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.ui = uic.loadUi('plantillas/main_window.ui')
        self.ui.show()
        
    @QtCore.pyqtSlot()
    def on_btn_vehiculosClicked(self):
       print('Se ejecutó la coneccion al evento')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())