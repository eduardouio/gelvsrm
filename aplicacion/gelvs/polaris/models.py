from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

class Ciudad(models.Model):
    id_ciudad = models.IntegerField(primary_key=True)
    id_provincia = models.ForeignKey('Provincia', db_column='id_provincia')
    nombre = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'ciudad'


class Cliente(models.Model):
    id_cliente = models.CharField(primary_key=True, max_length=13)
    id_contacto = models.ForeignKey('Contacto', db_column='id_contacto', blank=True, null=True)
    id_ciudad = models.ForeignKey(Ciudad, db_column='id_ciudad', blank=True, null=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=600)
    telefono = models.CharField(max_length=15)
    fax = models.CharField(max_length=15, blank=True)
    mail = models.CharField(max_length=100, blank=True)
    notas = models.TextField(blank=True)
    registro = models.DateTimeField()

    def __unicode__(self):
        return str(self.nombre)

    class Meta:
        managed = False
        db_table = 'cliente'

class Compra(models.Model):
    id_compra = models.IntegerField(primary_key=True)
    id_inventario = models.ForeignKey('Inventario', db_column='id_inventario')
    id_proveedor = models.ForeignKey('Proveedor', db_column='id_proveedor')
    id_tecnico = models.ForeignKey('Tecnico', db_column='id_tecnico')
    nro_factura = models.CharField(max_length=12)
    fecha = models.DateField()
    cantidad = models.IntegerField()
    costo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    notas = models.TextField(blank=True)
    registro = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'compra'

class Contacto(models.Model):
    id_contacto = models.IntegerField(primary_key=True)
    id_ciudad = models.ForeignKey(Ciudad, db_column='id_ciudad', blank=True, null=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15, blank=True)
    celular = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=100, blank=True)
    notas = models.TextField(blank=True)
    registro = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'contacto'

class Factura(models.Model):
    id_factura = models.IntegerField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, db_column='id_cliente')
    id_contacto = models.ForeignKey(Contacto, db_column='id_contacto', blank=True, null=True)
    fecha = models.DateField()
    fecha_envio = models.DateField()
    guia_envio = models.CharField(max_length=50, blank=True)
    servicio_envio = models.CharField(max_length=80)
    estado = models.CharField(max_length=50)
    archivo = models.CharField(max_length=200, blank=True)
    notas = models.TextField(blank=True)
    registro = models.DateTimeField()

    def __unicode__(self):
        return str(self.id_factura)

    class Meta:
        managed = False
        db_table = 'factura'

class FacturaDetalle(models.Model):
    id_factura_detalle = models.IntegerField(unique=True)
    id_factura = models.ForeignKey(Factura, db_column='id_factura')
    id_mantenimiento = models.IntegerField()
    id_reparacion = models.IntegerField()
    registro = models.DateTimeField()

    def __unicode__(self):
        return str(self.id_factura)

    class Meta:
        managed = False
        db_table = 'factura_detalle'

class GastosViaje(models.Model):
    id_gasto_viaje = models.IntegerField(unique=True)
    id_viaje = models.ForeignKey('Viaje', db_column='id_viaje')
    nro_factura = models.CharField(max_length=20)
    fecha = models.DateField()
    detalle = models.CharField(max_length=300)
    valor = models.DecimalField(max_digits=4, decimal_places=2)
    tipo = models.CharField(max_length=45, blank=True)
    registro = models.DateTimeField()
    
    def __unicode__(self):
        return str(self.id_viaje)

    class Meta:
        managed = False
        db_table = 'gastos_viaje'

class Inspeccion(models.Model):
    id_inspeccion = models.IntegerField(primary_key=True)
    id_vehiculo = models.ForeignKey('Vehiculo', db_column='id_vehiculo')
    id_tecnico = models.ForeignKey('Tecnico', db_column='id_tecnico')
    id_contacto = models.ForeignKey(Contacto, db_column='id_contacto')
    id_ciudad = models.ForeignKey(Ciudad, db_column='id_ciudad', blank=True, null=True)
    periodo = models.IntegerField()
    fecha = models.DateField()
    notas = models.TextField(blank=True)
    registro = models.DateTimeField()
    def __unicode__(self):
        cadena = "Inspeccion:%s Cliente %s"%(self.id_inspeccion, self.id_vehiculo)
        return str(cadena)


    class Meta:
        managed = False
        db_table = 'inspeccion'

class Inventario(models.Model):
    id_inventario = models.IntegerField(primary_key=True)
    fecha = models.DateTimeField()
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    unidad = models.CharField(max_length=25)
    stok_min = models.IntegerField()
    marca = models.CharField(max_length=45, blank=True)
    ubicacion = models.CharField(max_length=100)
    notas = models.TextField(blank=True)
    registro = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'inventario'

class Mantenimiento(models.Model):
    id_mantenimiento = models.IntegerField(primary_key=True)
    id_viaje = models.ForeignKey('Viaje', db_column='id_viaje')
    id_vehiculo = models.ForeignKey('Vehiculo', db_column='id_vehiculo')
    id_ciudad = models.ForeignKey(Ciudad, db_column='id_ciudad', blank=True, null=True)
    periodo = models.IntegerField()
    fecha = models.DateField()
    kilometros = models.CharField(max_length=10)
    notas = models.TextField(blank=True)
    registro = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'mantenimiento'

class MantenimientoDetalle(models.Model):
    id_mantenimiento_detalle = models.IntegerField(unique=True)
    id_mantenimiento = models.ForeignKey(Mantenimiento, db_column='id_mantenimiento')
    id_inventario = models.ForeignKey(Inventario, db_column='id_inventario')
    fecha = models.TimeField()
    estado = models.CharField(max_length=25, blank=True)
    cantidad = models.FloatField()
    notas = models.CharField(max_length=600, blank=True)
    registro = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'mantenimiento_detalle'

class Proveedor(models.Model):
    id_proveedor = models.CharField(primary_key=True, max_length=13)
    id_ciudad = models.ForeignKey(Ciudad, db_column='id_ciudad', blank=True, null=True)
    id_contacto = models.ForeignKey(Contacto, db_column='id_contacto', blank=True, null=True)
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=500)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=30, blank=True)
    credito = models.IntegerField(blank=True, null=True)
    notas = models.TextField(blank=True)
    registro = models.DateTimeField()
    def __unicode__(self):
        return str(self.nombre)

    class Meta:
        managed = False
        db_table = 'proveedor'

class Provincia(models.Model):
    id_provincia = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True)
    def __unicode__(self):
        return str(self.nombre)
    class Meta:
        managed = False
        db_table = 'provincia'

class Reparacion(models.Model):
    id_reparacion = models.IntegerField(primary_key=True)
    id_viaje = models.ForeignKey('Viaje', db_column='id_viaje')
    id_vehiculo = models.ForeignKey('Vehiculo', db_column='id_vehiculo')
    id_ciudad = models.ForeignKey(Ciudad, db_column='id_ciudad', blank=True, null=True)
    periodo = models.IntegerField()
    kilometros = models.CharField(max_length=45)
    fecha_entrada = models.DateTimeField()
    fecha_salida = models.DateTimeField()
    notas = models.TextField(blank=True)
    registro = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'reparacion'

class ReparacionDetalle(models.Model):
    id_reparacion_detalle = models.IntegerField(primary_key=True)
    id_reparacion = models.ForeignKey(Reparacion, db_column='id_reparacion')
    id_inventario = models.ForeignKey(Inventario, db_column='id_inventario')
    fecha = models.TimeField()
    estado = models.CharField(max_length=25, blank=True)
    cantidad = models.IntegerField()
    notas = models.CharField(max_length=600, blank=True)
    registro = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'reparacion_detalle'

class Tecnico(models.Model):
    id_tecnico = models.CharField(primary_key=True, max_length=10)
    nombres = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15, blank=True)
    celular = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=100, blank=True)
    notas = models.TextField(blank=True)
    registro = models.DateTimeField()
    def __unicode__(self):
        return str(self.nombre)
    class Meta:
        managed = False
        db_table = 'tecnico'

class TecnicoViaje(models.Model):
    id_tecnico = models.ForeignKey(Tecnico, db_column='id_tecnico')
    id_viaje = models.ForeignKey('Viaje', db_column='id_viaje')
    registro = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'tecnico_viaje'

class Vehiculo(models.Model):
    id_vehiculo = models.CharField(max_length=17)
    id_cliente = models.ForeignKey(Cliente, db_column='id_cliente')
    id_contacto = models.ForeignKey(Contacto, db_column='id_contacto', blank=True, null=True)
    id_ciudad = models.ForeignKey(Ciudad, db_column='id_ciudad', blank=True, null=True)
    modelo = models.CharField(max_length=45)
    nro_motor = models.CharField(max_length=25, blank=True)
    ingreso = models.DateField(blank=True, null=True)
    notas = models.TextField(blank=True)
    registro = models.DateTimeField()

    def __unicode__(self):
        return str(self.id_vehiculo)

    class Meta:
        managed = False
        db_table = 'vehiculo'

class Viaje(models.Model):
    id_viaje = models.IntegerField(primary_key=True)
    fecha_salida = models.DateField()
    fecha_regreso = models.DateField()
    nro_vehiculos = models.IntegerField()
    provincias_destino = models.CharField(max_length=500)
    varlor_caja = models.DecimalField(max_digits=5, decimal_places=2)
    informe = models.TextField()
    registro = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'viaje'
"""
-- phpMyAdmin SQL Dump
-- version 4.1.12
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 07-04-2014 a las 14:43:39
-- Versión del servidor: 5.5.35-0ubuntu0.13.10.2
-- Versión de PHP: 5.5.3-1ubuntu2.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `gelvsrm_polaris`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=76 ;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add ciudad', 7, 'add_ciudad'),
(20, 'Can change ciudad', 7, 'change_ciudad'),
(21, 'Can delete ciudad', 7, 'delete_ciudad'),
(22, 'Can add cliente', 8, 'add_cliente'),
(23, 'Can change cliente', 8, 'change_cliente'),
(24, 'Can delete cliente', 8, 'delete_cliente'),
(25, 'Can add compra', 9, 'add_compra'),
(26, 'Can change compra', 9, 'change_compra'),
(27, 'Can delete compra', 9, 'delete_compra'),
(28, 'Can add contacto', 10, 'add_contacto'),
(29, 'Can change contacto', 10, 'change_contacto'),
(30, 'Can delete contacto', 10, 'delete_contacto'),
(31, 'Can add factura', 11, 'add_factura'),
(32, 'Can change factura', 11, 'change_factura'),
(33, 'Can delete factura', 11, 'delete_factura'),
(34, 'Can add factura detalle', 12, 'add_facturadetalle'),
(35, 'Can change factura detalle', 12, 'change_facturadetalle'),
(36, 'Can delete factura detalle', 12, 'delete_facturadetalle'),
(37, 'Can add gastos viaje', 13, 'add_gastosviaje'),
(38, 'Can change gastos viaje', 13, 'change_gastosviaje'),
(39, 'Can delete gastos viaje', 13, 'delete_gastosviaje'),
(40, 'Can add inspeccion', 14, 'add_inspeccion'),
(41, 'Can change inspeccion', 14, 'change_inspeccion'),
(42, 'Can delete inspeccion', 14, 'delete_inspeccion'),
(43, 'Can add inventario', 15, 'add_inventario'),
(44, 'Can change inventario', 15, 'change_inventario'),
(45, 'Can delete inventario', 15, 'delete_inventario'),
(46, 'Can add mantenimiento', 16, 'add_mantenimiento'),
(47, 'Can change mantenimiento', 16, 'change_mantenimiento'),
(48, 'Can delete mantenimiento', 16, 'delete_mantenimiento'),
(49, 'Can add mantenimiento detalle', 17, 'add_mantenimientodetalle'),
(50, 'Can change mantenimiento detalle', 17, 'change_mantenimientodetalle'),
(51, 'Can delete mantenimiento detalle', 17, 'delete_mantenimientodetalle'),
(52, 'Can add proveedor', 18, 'add_proveedor'),
(53, 'Can change proveedor', 18, 'change_proveedor'),
(54, 'Can delete proveedor', 18, 'delete_proveedor'),
(55, 'Can add provincia', 19, 'add_provincia'),
(56, 'Can change provincia', 19, 'change_provincia'),
(57, 'Can delete provincia', 19, 'delete_provincia'),
(58, 'Can add reparacion', 20, 'add_reparacion'),
(59, 'Can change reparacion', 20, 'change_reparacion'),
(60, 'Can delete reparacion', 20, 'delete_reparacion'),
(61, 'Can add reparacion detalle', 21, 'add_reparaciondetalle'),
(62, 'Can change reparacion detalle', 21, 'change_reparaciondetalle'),
(63, 'Can delete reparacion detalle', 21, 'delete_reparaciondetalle'),
(64, 'Can add tecnico', 22, 'add_tecnico'),
(65, 'Can change tecnico', 22, 'change_tecnico'),
(66, 'Can delete tecnico', 22, 'delete_tecnico'),
(67, 'Can add tecnico viaje', 23, 'add_tecnicoviaje'),
(68, 'Can change tecnico viaje', 23, 'change_tecnicoviaje'),
(69, 'Can delete tecnico viaje', 23, 'delete_tecnicoviaje'),
(70, 'Can add vehiculo', 24, 'add_vehiculo'),
(71, 'Can change vehiculo', 24, 'change_vehiculo'),
(72, 'Can delete vehiculo', 24, 'delete_vehiculo'),
(73, 'Can add viaje', 25, 'add_viaje'),
(74, 'Can change viaje', 25, 'change_viaje'),
(75, 'Can delete viaje', 25, 'delete_viaje');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$12000$jTLiRWOnhKNM$23HrrIzbkLPMFdruVomoDKarBXFlC4mE0ihh4V5DzDY=', '2014-04-06 03:15:57', 1, 'polaris', '', '', 'eduardouio7@gmail.com', 1, 1, '2014-04-06 02:30:14');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=26 ;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'log entry', 'admin', 'logentry'),
(2, 'permission', 'auth', 'permission'),
(3, 'group', 'auth', 'group'),
(4, 'user', 'auth', 'user'),
(5, 'content type', 'contenttypes', 'contenttype'),
(6, 'session', 'sessions', 'session'),
(7, 'ciudad', 'polaris', 'ciudad'),
(8, 'cliente', 'polaris', 'cliente'),
(9, 'compra', 'polaris', 'compra'),
(10, 'contacto', 'polaris', 'contacto'),
(11, 'factura', 'polaris', 'factura'),
(12, 'factura detalle', 'polaris', 'facturadetalle'),
(13, 'gastos viaje', 'polaris', 'gastosviaje'),
(14, 'inspeccion', 'polaris', 'inspeccion'),
(15, 'inventario', 'polaris', 'inventario'),
(16, 'mantenimiento', 'polaris', 'mantenimiento'),
(17, 'mantenimiento detalle', 'polaris', 'mantenimientodetalle'),
(18, 'proveedor', 'polaris', 'proveedor'),
(19, 'provincia', 'polaris', 'provincia'),
(20, 'reparacion', 'polaris', 'reparacion'),
(21, 'reparacion detalle', 'polaris', 'reparaciondetalle'),
(22, 'tecnico', 'polaris', 'tecnico'),
(23, 'tecnico viaje', 'polaris', 'tecnicoviaje'),
(24, 'vehiculo', 'polaris', 'vehiculo'),
(25, 'viaje', 'polaris', 'viaje');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('aa7s9xq2815aa65o2fm4twxdrp1kzbzp', 'ZjhhMjcyOTA3OTEyYzgyZWJkY2VlNmY0NTdkMjRmMmY2MTE2YjIxMzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=', '2014-04-20 03:15:57'),
('pjcbtx2i8rjoycme8r1exdpeyvz30pf5', 'ZjhhMjcyOTA3OTEyYzgyZWJkY2VlNmY0NTdkMjRmMmY2MTE2YjIxMzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=', '2014-04-20 02:30:46');

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
"""