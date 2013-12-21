#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version		1.0
# Autor			Eduardo Villota <eduardouio@hotmail.com> <@eduardouio>
# Package		Clases
# File			contactoClass.py
# Ubicacion		aplicacion/clases/contactoClass.py
# Copyright		(c) 2013 gelvsrm <eduardouio7@gmail.com>
#+-------------+----------------------+------+-----+-------------------+-----------------------------+
#|											Data Type												|
#+-------------+----------------------+------+-----+-------------------+-----------------------------+
#| Field       | Type                 | Null | Key | Default           | Extra                       |
#+-------------+----------------------+------+-----+-------------------+-----------------------------+
#| id_contacto | smallint(5) unsigned | NO   | PRI | NULL              | auto_increment              |
#| id_ciudad   | smallint(5) unsigned | YES  | MUL | NULL              |                             |
#| nombre      | varchar(50)          | NO   |     | NULL              |                             |
#| telefono    | varchar(15)          | YES  |     | NULL              |                             |
#| celular     | varchar(15)          | YES  |     | NULL              |                             |
#| email       | varchar(100)         | YES  |     | NULL              |                             |
#| notas       | mediumtext           | YES  |     | NULL              |                             |
#| registro    | timestamp            | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
#+-------------+----------------------+------+-----+-------------------+-----------------------------+

import sys
sys.path.append('..')
from modelo.Modelo import DB

class Contact(object):
	"""Objeto que representa la estructura de la clase contacto"""
	def __init__(self, id_contacto = '',id_ciudad='',nombre ='',
					telefono='',celular='',	email='',notas='',registro=''):
		super(Contact, self).__init__()
		self.id_contacto = id_contacto
		self.id_ciudad = id_ciudad
		self.nombre = nombre
		self.telefono = telefono
		self.celular = celular
		self.email = email
		self.notas = notas
		self.registro = registro

class contactCatalog(object):
	'''Opercaciones con la clase Contact'''
	def __init__():
		'''inicializamos la clase'''
		super(contactCatalog,self).__init__()
		self.MyDb = DB()
		self.table = 'contacto'

	def getContacts(self,contact = ''):
		'''Obtiene un listado de contactos o un contacto
		@param (str) tipo contact solo con el id_contacto
		@return (lis(obj))|(obj) '''
		if contact:
			mycontact = Contact()
			condition = 'id_contacto = ' + str(contact)
			result = self.MyDb.selectQuery(self.table,'',condition)
			while result.next():
				mycontact.id_contacto = str(result.value(0))
				mycontact.id_ciudad = str(result.value(1))
				mycontact.nombre = str(result.value(2))
				mycontact.telefono = str(result.value(3))
				mycontact.celular = str(result.value(4))
				mycontact.email = str(result.value(5))
				mycontact.notas = str(result.value(6))
				mycontact.registro = str(result.value(7))
			
			return mycontact
		else:
			result = self.MyDb.selectQuery(self.table)
			contacts = []
			while result.next():
				mycontact = Contact()
				mycontact.id_contacto = str(result.value(0))
				mycontact.id_ciudad = str(result.value(1))
				mycontact.nombre = str(result.value(2))
				mycontact.telefono = str(result.value(3))
				mycontact.celular = str(result.value(4))
				mycontact.email = str(result.value(5))
				mycontact.notas = str(result.value(6))
				mycontact.registro = str(result.value(7))
				contacts.append(mycontact)

			return contacts

	def createContact(self,contact):
		'''Crea un contacto
		@param (obj) contact
		@return (bool)'''
		values = {
			'id_contacto': contact.id_contacto
			'id_ciudad': contact.id_ciudad
			'nombre': contact.nombre
			'telefono': contact.telefono
			'celular': contact.celular
			'email': contact.email
			'notas': contact.notas
			'registro': contact.registro		
		}
		result = self.MyDb.createQuery(self.table,value)
		if(result.numRowsAffected()>0):
			return str(result.lastInsertId())
		else
			return False

	def updateContact(self,oldContact, contact):
		'''Actualiza un contacto
		@param (obj) tipo Contact
		@param (obj) tipo Contact
		@return bool
		'''
		condition = ' id_contacto = ' + str(oldContact.id_contacto)
		values = [
			'id_contacto': contact.id_contacto
			'id_ciudad': contact.id_ciudad
			'nombre': contact.nombre
			'telefono': contact.telefono
			'celular': contact.celular
			'email': contact.email
			'notas': contact.notas
				]
		result = self.MyDb.updateQuery(self.table,values,condition)
		if (result.numRowsAffected() > 0):
			return True
		else:
			return False

	def deleteContact(self,contact):
		'''Elimina un contacto
		@param (obj) tipo contact
		@return (bool)'''
		condition = ' id_contacto = ' + str(contact.id_contacto)
		result = self.MyDb.deleteQuery(self.table,condition)

		if (result.numRowsAffected() > 0):
			return True
		else:
			return False

	def findContact(self,contact,content):
		'''Busca uno o unos con'''