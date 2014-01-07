
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
from PyQt4.QtCore import QDateTime, QDate, QTime, qDebug

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
		self.registro = QDateTime().currentDateTime()
		qDebug('[Debug] se incia la clase contact')


class contactCatalog(object):
	'''Opercaciones con la clase Contact'''
	def __init__():
		'''inicializamos la clase'''
		super(contactCatalog,self).__init__()
		self.MyDb = DB()
		self.table = 'contacto'
		qDebug('[Debug] clase conctactCatalog Instanciada')


	def getContact(self,contact = ''):
		'''Obtiene un contacto de la base de datos
		@param (str) tipo contact solo con el id_contacto
		@return(obj) '''			
		condition = {'id_contacto = ' : str(contact)}
		result = self.MyDb.selectQuery(self.table,'',condition)
		qDebug('[Debug] la consulta retorno %s objetos'% str(result.size()))
		if result.next():
			return self.__setObj(result)
		else:
			qDebug('[Debug] no se encontro ningun valor')
			return False
	

	def listContacts(self):
		'''Retona un listado de los contactos
		@return list(oibj) contact'''
		contacts = []
		result = self.MyDb.selectQuery(self.table)
		qDebug('[Debug] la consulta retorno %s objetos'% str(result.size()))
		while result.next():			
			contacts.append(self.__setObj(result))

		return contacts


	def firstContact(self):
		'''retorna el primer contacto de la lista
		@return (obj) Contact'''		
		result = self.MyDB.selectQuery(self.table)
		qDebug('[Debug] Se toma el primer contacto de la lista')
		if result.first():
			return self.__setObj(result)
		else:
			return False


	def lastContact(self):
		'''retorna el ultimo contacto de la Lista
		@return (obj) contacto'''
		result = self.MyDB.selectQuery(self.table)
		qDebug('[Debug] Se toma ultimo contacto de la lista')
		if result.last():
			return self.__setObj(result)
		else:
			return False


	def findContact(self,condition):
		'''Busca un contacto
		@param condition = {'id_tecnico like ' : '%4%'}
		@return list(obj) tipo Contact'''
		contacts = []
		result = self.MyDB.selectQuery(self.table,'',condition)
		while result.next():
			contacts.append(self.__setObj(result))

		return contacts


	def createContact(self,contact):
		'''Crea un contacto
		@param (obj) contact
		@return (bool)'''
		values = {			
			'id_ciudad': contact.id_ciudad,
			'nombre': contact.nombre,
			'telefono': contact.telefono,
			'celular': contact.celular,
			'email': contact.email,
			'notas': contact.notas					
		}

		result = self.MyDb.insertQuery(self.table,value)
		
		if(result.numRowsAffected()>0):
			qDebug('[Debug] se inserto un contacto')
			return str(result.lastInsertId())
		else:
			qDebug('[Debug] problemas insertando un contacto')
			return False


	def updateContact(self,oldContact, contact):
		'''Actualiza un contacto
		@param (obj) tipo Contact
		@param (obj) tipo Contact
		@return bool
		'''
		condition = {' id_contacto = ' : str(oldContact.id_contacto)}
		values = {			
			'id_ciudad': contact.id_ciudad,
			'nombre': contact.nombre,
			'telefono': contact.telefono,
			'celular': contact.celular,
			'email': contact.email,
			'notas': contact.notas,
				}

		result = self.MyDb.updateQuery(self.table,values,condition)
		
		if (result.numRowsAffected() > 0):
			qDebug('[Debug] se Actualiza un contacto')
			return True
		else:
			qDebug('[Debug] problemas Actualizando un contacto')
			return False


	def deleteContact(self,contact):
		'''Elimina un contacto
		@param (obj) tipo contact
		@return (bool)'''
		condition = {' id_contacto = ' : str(contact.id_contacto)}
		result = self.MyDb.deleteQuery(self.table,condition)

		if (result.numRowsAffected() > 0):
			qDebug('[Debug] se elimino un contacto %s' % contact.nombre)
			return True
		else:
			qDebug('[Debug] problemas Eliminando un contacto')
			return False
			

	def __setObj(self, result):
		'''Crea un objeto tipo Conctact y lo retorna
		@param (obj) result
		@return (obj) contact'''
		mycontact = Contact()
		mycontact.id_contacto = str(result.value(0))
		mycontact.id_ciudad = str(result.value(1))
		mycontact.nombre = str(result.value(2))
		mycontact.telefono = str(result.value(3))
		mycontact.celular = str(result.value(4))
		mycontact.email = str(result.value(5))
		mycontact.notas = str(result.value(6))
		mycontact.registro = str(result.value(7))

		return mycontact