#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Administracion de gastos
# File			gasto.py
# Ubicacion		aplicacion/basedatos/Modelo.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
import sys
sys.path.append('..')
from modelo.Modelo import Modelo

class gasto(object):
	'''Representa un gasto en el sistema'''
	def __init__(self):
		'''Se crea una instancia de la base de datos'''
		self.db = Modelo()

	def listarGastos(self,id_viaje=0):
		'''Lista los gastos de un id_viaje
		@param id_viaje => identificador del viaje'''
		