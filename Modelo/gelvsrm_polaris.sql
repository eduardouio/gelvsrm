-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 19-05-2014 a las 16:12:30
-- Versión del servidor: 5.5.37-0ubuntu0.14.04.1
-- Versión de PHP: 5.5.9-1ubuntu4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `gelvscom_polaris`
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
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

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
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=100 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ciudad`
--

CREATE TABLE IF NOT EXISTS `ciudad` (
  `id_ciudad` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `id_provincia` smallint(5) unsigned NOT NULL,
  `nombre` varchar(100) CHARACTER SET latin1 DEFAULT NULL,
  PRIMARY KEY (`id_ciudad`),
  KEY `fk_ciudad_provincia` (`id_provincia`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Entidad encargada de registrar, ciudades del Ecuador guarda una relacion    con la provincia a la que corresponde, en caso de no tener una ciudad en    la lista de ciudades, se crea una nueva permitiendole al usuario ingresarla' AUTO_INCREMENT=252 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE IF NOT EXISTS `cliente` (
  `id_cliente` char(13) NOT NULL,
  `id_contacto` smallint(5) unsigned DEFAULT NULL,
  `id_ciudad` smallint(5) unsigned DEFAULT NULL,
  `nombre` varchar(200) NOT NULL,
  `direccion` varchar(600) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `fax` varchar(15) DEFAULT NULL,
  `mail` varchar(100) DEFAULT NULL,
  `notas` mediumtext,
  `registro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_cliente`),
  KEY `fk_cliente_contacto` (`id_contacto`),
  KEY `fk_cliente_ciudad` (`id_ciudad`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Entidad encargada de registrar a los cliente\n        se sugiere que el telefono sea de la persona encargada \n       de la facturacio';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compra`
--

CREATE TABLE IF NOT EXISTS `compra` (
  `id_compra` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `id_inventario` smallint(5) unsigned NOT NULL,
  `id_proveedor` varchar(13) NOT NULL,
  `id_tecnico` varchar(10) NOT NULL,
  `nro_factura` varchar(12) NOT NULL,
  `fecha` date NOT NULL,
  `cantidad` smallint(5) unsigned NOT NULL,
  `costo` decimal(5,2) DEFAULT NULL COMMENT 'costo por unidad',
  `notas` mediumtext,
  `registro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_compra`),
  KEY `fk_compra_inventario` (`id_inventario`),
  KEY `fk_compra_proveedor` (`id_proveedor`),
  KEY `fk_compra_tecnico` (`id_tecnico`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 COMMENT='Entidad encargada de manejar la entrada de stock al inventario\n       las unidades de los productos son las mimas que el detalle del inventario' AUTO_INCREMENT=13 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contacto`
--

CREATE TABLE IF NOT EXISTS `contacto` (
  `id_contacto` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `id_ciudad` smallint(5) unsigned DEFAULT NULL,
  `nombre` varchar(50) NOT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `celular` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `notas` mediumtext,
  `registro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_contacto`),
  KEY `fk_contacto_ciudad` (`id_ciudad`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 COMMENT='Entidad encargada de registrar los contactos de la base de datos\n   Estos contactos son luego referenciados a las entidades que lo requieran,\n   debe tener un registro cero' AUTO_INCREMENT=98 ;

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
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=106 ;

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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura`
--

CREATE TABLE IF NOT EXISTS `factura` (
  `id_factura` int(11) NOT NULL,
  `id_cliente` char(13) NOT NULL,
  `id_contacto` smallint(5) unsigned DEFAULT NULL,
  `fecha` date NOT NULL,
  `fecha_envio` date NOT NULL,
  `guia_envio` varchar(50) DEFAULT NULL,
  `servicio_envio` varchar(80) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `archivo` varchar(200) DEFAULT NULL,
  `notas` mediumtext,
  `registro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_factura`),
  KEY `fk_factura_cliente` (`id_cliente`),
  KEY `fk_factura_contacto` (`id_contacto`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Entidad encargada de registrar las facturación, se implementa una ruta\n    al archivo del escaneado de la factura';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura_detalle`
--

CREATE TABLE IF NOT EXISTS `factura_detalle` (
  `id_factura_detalle` mediumint(9) NOT NULL AUTO_INCREMENT,
  `id_factura` int(11) NOT NULL,
  `id_mantenimiento` smallint(5) NOT NULL DEFAULT '0',
  `id_reparacion` smallint(5) NOT NULL DEFAULT '0',
  `registro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_factura`,`id_mantenimiento`,`id_reparacion`),
  UNIQUE KEY `id_factura_detalle_UNIQUE` (`id_factura_detalle`),
  KEY `fk_factura_detalle_mantenimiento` (`id_mantenimiento`),
  KEY `fk_factura_detalle_reparacion` (`id_reparacion`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 COMMENT='Entidad que registra los detalles de la facturacio se entiende por detalle\n       los vehiculos a los que se le realizaron mantenimiento, un mantenimiento no\n       se factura más de una vez, para poder controlar esto se obliga a que un campo de la clave\n       primaria sea cero los dos campos no deben tener un valor diferente de cero los dos a la\n       vez ya que la restriccion registra un mantenimiento o una reparación' AUTO_INCREMENT=111 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gastos_viaje`
--

CREATE TABLE IF NOT EXISTS `gastos_viaje` (
  `id_gasto_viaje` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `id_viaje` smallint(5) unsigned NOT NULL,
  `nro_factura` varchar(20) NOT NULL,
  `fecha` date NOT NULL,
  `detalle` varchar(300) NOT NULL,
  `valor` decimal(4,2) NOT NULL,
  `tipo` varchar(45) DEFAULT NULL,
  `registro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_viaje`,`nro_factura`,`valor`),
  UNIQUE KEY `id_gasto_viaje_UNIQUE` (`id_gasto_viaje`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 COMMENT='Se registran los gastos de los viajes, en esta entidad se graban los \n    gastos realizados para cada viaje, se registran los datos de las facturas de acuerdo\n    al formato que se tiene en gastos de viajes en la carpeta polaris de dropbox' AUTO_INCREMENT=177 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inspeccion`
--

CREATE TABLE IF NOT EXISTS `inspeccion` (
  `id_inspeccion` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `id_vehiculo` varchar(17) NOT NULL,
  `id_tecnico` varchar(10) NOT NULL,
  `id_contacto` smallint(5) unsigned NOT NULL,
  `id_ciudad` smallint(5) unsigned DEFAULT NULL,
  `periodo` smallint(5) unsigned NOT NULL,
  `fecha` date NOT NULL,
  `notas` text,
  `registro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_inspeccion`),
  KEY `fk_inspeccion_vehiculo` (`id_vehiculo`),
  KEY `fk_inspeccion_tecnico` (`id_tecnico`),
  KEY `fk_inspeccion_contacto` (`id_contacto`),
  KEY `fk_inspeccion_ciudad` (`id_ciudad`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 COMMENT='De momento es solo un formulario de inspeccion' AUTO_INCREMENT=39 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario`
--

CREATE TABLE IF NOT EXISTS `inventario` (
  `id_inventario` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `fecha` datetime NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(200) NOT NULL,
  `unidad` varchar(25) NOT NULL,
  `stok_min` smallint(5) unsigned NOT NULL COMMENT '12 filtros,12 aceite, 4 refirgerante 1 liquido de frenos',
  `marca` varchar(45) DEFAULT NULL,
  `ubicacion` varchar(100) NOT NULL,
  `notas` mediumtext,
  `registro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_inventario`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 COMMENT='Entidad que lleva un detalle de los productos en bodega\n    Todos los materiales están en litros y unidades, se setablece un standar para los \n    condigos del inventario, cada producto ingresado al inventario empieza con el mail\n    1000,1001,1002. la columna unidad debe contener, litros, unidades, galones, etc' AUTO_INCREMENT=1040 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mantenimiento`
--

CREATE TABLE IF NOT EXISTS `mantenimiento` (
  `id_mantenimiento` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `id_viaje` smallint(5) unsigned NOT NULL,
  `id_vehiculo` char(17) NOT NULL,
  `id_ciudad` smallint(5) unsigned DEFAULT NULL,
  `periodo` smallint(5) unsigned NOT NULL,
  `fecha` date NOT NULL,
  `kilometros` varchar(10) NOT NULL,
  `notas` mediumtext,
  `registro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_mantenimiento`),
  KEY `fk_mantenimiento_vehiculo` (`id_vehiculo`),
  KEY `fk_mantenimiento_viaje` (`id_viaje`),
  KEY `fk_mantenimiento_ciudad` (`id_ciudad`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 COMMENT='Registra los mantenimientos realizados aun vehiculo, los insumos usados para el mantenimiento        se registran en mantenimiento_detalle' AUTO_INCREMENT=221 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mantenimiento_detalle`
--

CREATE TABLE IF NOT EXISTS `mantenimiento_detalle` (
  `id_mantenimiento_detalle` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `id_mantenimiento` smallint(5) unsigned NOT NULL,
  `id_inventario` smallint(5) unsigned NOT NULL,
  `estado` varchar(25) DEFAULT NULL COMMENT 'cambio,reparacio,correccion',
  `cantidad` float unsigned NOT NULL,
  `notas` varchar(600) DEFAULT NULL,
  `registro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_mantenimiento`,`id_inventario`),
  UNIQUE KEY `id_mantenimiento_detalle` (`id_mantenimiento_detalle`),
  KEY `fk_mantenimiento_detalle_inventario` (`id_inventario`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 COMMENT='Registra los detalles del mantenimiento y los costos de los insumos' AUTO_INCREMENT=5110 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedor`
--

CREATE TABLE IF NOT EXISTS `proveedor` (
  `id_proveedor` varchar(13) NOT NULL,
  `id_ciudad` smallint(5) unsigned DEFAULT NULL,
  `id_contacto` smallint(5) unsigned DEFAULT NULL,
  `nombre` varchar(150) NOT NULL,
  `direccion` varchar(500) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `email` varchar(30) DEFAULT NULL,
  `credito` tinyint(1) DEFAULT NULL,
  `notas` mediumtext,
  `registro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_proveedor`),
  KEY `fk_proveedor_contacto` (`id_contacto`),
  KEY `fk_proveedor_ciudad` (`id_ciudad`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Entidad encargada de registrar los datos básicos de proeedor de materiales \n   y repuestos de vehículos';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `provincia`
--

CREATE TABLE IF NOT EXISTS `provincia` (
  `id_provincia` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_provincia`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 COMMENT='Entidad encargada de registrar, las provincias del Ecuador' AUTO_INCREMENT=25 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reparacion`
--

CREATE TABLE IF NOT EXISTS `reparacion` (
  `id_reparacion` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `id_viaje` smallint(5) unsigned NOT NULL,
  `id_vehiculo` char(17) NOT NULL,
  `id_ciudad` smallint(5) unsigned DEFAULT NULL,
  `periodo` smallint(5) unsigned NOT NULL,
  `kilometros` varchar(45) NOT NULL,
  `fecha_entrada` datetime NOT NULL,
  `fecha_salida` datetime NOT NULL,
  `notas` mediumtext,
  `registro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_reparacion`),
  KEY `fk_reparacion_vehiculo` (`id_vehiculo`),
  KEY `fk_reparacion_viaje` (`id_viaje`),
  KEY `fk_reparacion_ciudad` (`id_ciudad`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 COMMENT='Entidad encargada de registrar las reparaciones realizadas a los vehiculos polaris,\n    cada reparacion al vehiculo se registra en reparacion_detalle' AUTO_INCREMENT=59 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reparacion_detalle`
--

CREATE TABLE IF NOT EXISTS `reparacion_detalle` (
  `id_reparacion_detalle` smallint(5) unsigned NOT NULL,
  `id_reparacion` smallint(5) unsigned NOT NULL,
  `id_inventario` smallint(5) unsigned NOT NULL,
  `fecha` time NOT NULL,
  `estado` varchar(25) DEFAULT NULL COMMENT 'bueno, exelente,reparar,dañado,necesita cambio',
  `cantidad` smallint(5) unsigned NOT NULL,
  `notas` varchar(600) DEFAULT NULL,
  `registro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_reparacion_detalle`),
  KEY `fk_reparacion_detalle_reparacion` (`id_reparacion`),
  KEY `fk_reparacion_detalle_inventario` (`id_inventario`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Entidad encargada de registrar los detalles de las reparaciones cada detalle puede \n       contener una salida de inventario';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tecnico`
--

CREATE TABLE IF NOT EXISTS `tecnico` (
  `id_tecnico` varchar(10) CHARACTER SET latin1 NOT NULL,
  `nombres` varchar(200) CHARACTER SET latin1 NOT NULL,
  `telefono` varchar(15) CHARACTER SET latin1 DEFAULT NULL,
  `celular` varchar(15) CHARACTER SET latin1 DEFAULT NULL,
  `email` varchar(100) CHARACTER SET latin1 DEFAULT NULL,
  `notas` mediumtext CHARACTER SET latin1,
  `registro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_tecnico`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Entidad encargada de registrar los tecnicos';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tecnico_viaje`
--

CREATE TABLE IF NOT EXISTS `tecnico_viaje` (
  `id_tecnico` varchar(10) NOT NULL,
  `id_viaje` smallint(5) unsigned NOT NULL,
  `registro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_tecnico`,`id_viaje`),
  KEY `fk_tecnico_viaje` (`id_viaje`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Registra a los técnicos en los mantenimientos para cada viaje';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vehiculo`
--

CREATE TABLE IF NOT EXISTS `vehiculo` (
  `id_vehiculo` char(17) NOT NULL,
  `id_cliente` char(13) NOT NULL,
  `id_contacto` smallint(5) unsigned DEFAULT NULL,
  `id_ciudad` smallint(5) unsigned DEFAULT NULL,
  `modelo` varchar(45) NOT NULL,
  `nro_motor` varchar(25) DEFAULT NULL,
  `ingreso` date DEFAULT NULL,
  `notas` mediumtext,
  `registro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_vehiculo`),
  KEY `idx_vehiculo` (`id_vehiculo`),
  KEY `fk_vehiculo_cliente` (`id_cliente`),
  KEY `fk_vehiculo_contacto` (`id_contacto`),
  KEY `fk_vehiculo_ciudad` (`id_ciudad`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Entidad encargada de registrar los vehículos el ingreso es la fecha\n       en la que el vehiculo fue entregado al MAGAP';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `viaje`
--

CREATE TABLE IF NOT EXISTS `viaje` (
  `id_viaje` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `fecha_salida` date NOT NULL,
  `fecha_regreso` date NOT NULL,
  `nro_vehiculos` smallint(5) unsigned NOT NULL COMMENT 'Cuantos veiculos se piensa reparar',
  `provincias_destino` varchar(500) NOT NULL COMMENT 'Nmbre de las provincias que se quiere visitar, separadas por comas',
  `varlor_caja` decimal(5,2) NOT NULL,
  `informe` text NOT NULL,
  `registro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_viaje`),
  UNIQUE KEY `fecha_salida` (`fecha_salida`,`fecha_regreso`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 COMMENT='Registra los viajes realizados por los técincos, los mantenimientos dependen de los \n   viajes para existir, ya que los mantenimientos se los realiza con un viaje, se necesita\n   ingresar un viaje a Quito para los mantenimientos y reparaciones realizados en Quito' AUTO_INCREMENT=25 ;

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `v_vehiculo`
--
CREATE TABLE IF NOT EXISTS `v_vehiculo` (
`id_vehiculo` char(17)
,`modelo` varchar(45)
,`ingreso` date
,`ciudad` varchar(100)
,`conductor` varchar(50)
,`telefono` varchar(15)
);
-- --------------------------------------------------------

--
-- Estructura para la vista `v_vehiculo`
--
DROP TABLE IF EXISTS `v_vehiculo`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_vehiculo` AS select `a`.`id_vehiculo` AS `id_vehiculo`,`a`.`modelo` AS `modelo`,`a`.`ingreso` AS `ingreso`,`b`.`nombre` AS `ciudad`,`c`.`nombre` AS `conductor`,`c`.`telefono` AS `telefono` from ((`vehiculo` `a` left join `ciudad` `b` on((`a`.`id_ciudad` = `b`.`id_ciudad`))) left join `contacto` `c` on((`a`.`id_contacto` = `c`.`id_contacto`)));

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
  ADD CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `ciudad`
--
ALTER TABLE `ciudad`
  ADD CONSTRAINT `fk_ciudad_provincia` FOREIGN KEY (`id_provincia`) REFERENCES `provincia` (`id_provincia`) ON DELETE NO ACTION ON UPDATE CASCADE;

--
-- Filtros para la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD CONSTRAINT `fk_cliente_ciudad` FOREIGN KEY (`id_ciudad`) REFERENCES `ciudad` (`id_ciudad`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_cliente_contacto` FOREIGN KEY (`id_contacto`) REFERENCES `contacto` (`id_contacto`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `compra`
--
ALTER TABLE `compra`
  ADD CONSTRAINT `fk_compra_inventario` FOREIGN KEY (`id_inventario`) REFERENCES `inventario` (`id_inventario`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_compra_proveedor` FOREIGN KEY (`id_proveedor`) REFERENCES `proveedor` (`id_proveedor`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_compra_tecnico` FOREIGN KEY (`id_tecnico`) REFERENCES `tecnico` (`id_tecnico`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `contacto`
--
ALTER TABLE `contacto`
  ADD CONSTRAINT `fk_contacto_ciudad` FOREIGN KEY (`id_ciudad`) REFERENCES `ciudad` (`id_ciudad`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `factura`
--
ALTER TABLE `factura`
  ADD CONSTRAINT `fk_factura_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_factura_contacto` FOREIGN KEY (`id_contacto`) REFERENCES `contacto` (`id_contacto`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `factura_detalle`
--
ALTER TABLE `factura_detalle`
  ADD CONSTRAINT `fk_factura_detalle_factura` FOREIGN KEY (`id_factura`) REFERENCES `factura` (`id_factura`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `gastos_viaje`
--
ALTER TABLE `gastos_viaje`
  ADD CONSTRAINT `fk_gastos_viaje_viaje` FOREIGN KEY (`id_viaje`) REFERENCES `viaje` (`id_viaje`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `inspeccion`
--
ALTER TABLE `inspeccion`
  ADD CONSTRAINT `fk_inspeccion_ciudad` FOREIGN KEY (`id_ciudad`) REFERENCES `ciudad` (`id_ciudad`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_inspeccion_contacto` FOREIGN KEY (`id_contacto`) REFERENCES `contacto` (`id_contacto`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_inspeccion_tecnico` FOREIGN KEY (`id_tecnico`) REFERENCES `tecnico` (`id_tecnico`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_inspeccion_vehiculo` FOREIGN KEY (`id_vehiculo`) REFERENCES `vehiculo` (`id_vehiculo`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `mantenimiento`
--
ALTER TABLE `mantenimiento`
  ADD CONSTRAINT `fk_mantenimiento_ciudad` FOREIGN KEY (`id_ciudad`) REFERENCES `ciudad` (`id_ciudad`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_mantenimiento_vehiculo` FOREIGN KEY (`id_vehiculo`) REFERENCES `vehiculo` (`id_vehiculo`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_mantenimiento_viaje` FOREIGN KEY (`id_viaje`) REFERENCES `viaje` (`id_viaje`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `mantenimiento_detalle`
--
ALTER TABLE `mantenimiento_detalle`
  ADD CONSTRAINT `fk_mantenimiento_detalle_inventario` FOREIGN KEY (`id_inventario`) REFERENCES `inventario` (`id_inventario`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_mantenimiento_detalle_mantenimiento` FOREIGN KEY (`id_mantenimiento`) REFERENCES `mantenimiento` (`id_mantenimiento`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `proveedor`
--
ALTER TABLE `proveedor`
  ADD CONSTRAINT `fk_proveedor_ciudad` FOREIGN KEY (`id_ciudad`) REFERENCES `ciudad` (`id_ciudad`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_proveedor_contacto` FOREIGN KEY (`id_contacto`) REFERENCES `contacto` (`id_contacto`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `reparacion`
--
ALTER TABLE `reparacion`
  ADD CONSTRAINT `fk_reparacion_ciudad` FOREIGN KEY (`id_ciudad`) REFERENCES `ciudad` (`id_ciudad`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_reparacion_vehiculo` FOREIGN KEY (`id_vehiculo`) REFERENCES `vehiculo` (`id_vehiculo`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_reparacion_viaje` FOREIGN KEY (`id_viaje`) REFERENCES `viaje` (`id_viaje`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `reparacion_detalle`
--
ALTER TABLE `reparacion_detalle`
  ADD CONSTRAINT `fk_reparacion_detalle_inventario` FOREIGN KEY (`id_inventario`) REFERENCES `inventario` (`id_inventario`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_reparacion_detalle_reparacion` FOREIGN KEY (`id_reparacion`) REFERENCES `reparacion` (`id_reparacion`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `tecnico_viaje`
--
ALTER TABLE `tecnico_viaje`
  ADD CONSTRAINT `fk_tecnico_viaje` FOREIGN KEY (`id_viaje`) REFERENCES `viaje` (`id_viaje`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_tecnico_viaje_tecnico` FOREIGN KEY (`id_tecnico`) REFERENCES `tecnico` (`id_tecnico`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `vehiculo`
--
ALTER TABLE `vehiculo`
  ADD CONSTRAINT `fk_vehiculo_ciudad` FOREIGN KEY (`id_ciudad`) REFERENCES `ciudad` (`id_ciudad`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_vehiculo_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_vehiculo_contacto` FOREIGN KEY (`id_contacto`) REFERENCES `contacto` (`id_contacto`) ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;