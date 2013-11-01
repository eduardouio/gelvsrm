#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Manipulacion de la tabla tecnico
# File			técnico.py
# Ubicacion		reporte/controlador/tecnico.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
from PyQt4 import QtSql, QtCore, QtDebug
import Modelo

class Tecnico(Object):
	'''Representa un técnico de la base de datos'''

	def __init__(self):
		'''__init__ de la clase técnico'''
		self.Tabla_ = 'tecnico'

	def listarTecnicos(self):
		'''Lista los técnicos de la tabla'''
		



