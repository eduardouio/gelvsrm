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
from  bottle import *

@route('/hola')
@route('/')
def hola():
	return ('<b> Hola Mundo</b><p>Desde Python3</p>')

if __name__ == '__main__':
	run(host='192.168.0.150', port=80, debug=True)
	
