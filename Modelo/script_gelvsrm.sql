-- ----------------------------------------------------------------------------------------
-- Modelo de base de datos Gelvsrm 
-- ----------------------------------------------------------------------------------------
-- autor <@eduardouio>
-- copyrigth (c)gelvsrm.com 2013>
-- version 1.0
-- engine innodb
-- content <estrcutura del modelo de base de datos>
-- Versión del servidor: 5.5.32-0ubuntu0.12.04.1
-- ----------------------------------------------------------------------------------------

create database gelvsrm_polaris;
	use gelvsrm_polaris;
	-- -------------------------------------------------------------------
	-- Estructura de la entidad provincia
	-- -------------------------------------------------------------------
	create table provincia(
		id_provincia smallint unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
		nombre varchar(100)
		)engine=innodb
		AUTO_INCREMENT = 1
		COMMENT 'Entidad encargada de registrar, las provincias del Ecuador';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad ciudad
	-- -------------------------------------------------------------------
	create table cuidad(
		id_cuidad smallint unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
		id_provincia smallint unsigned NOT NULL,
		nombre varchar(100),

		CONSTRAINT fk_cuidad_provincia
      	FOREIGN KEY (id_provincia)
      	REFERENCES provincia(id_provincia)
      	ON DELETE RESTRICT ON UPDATE CASCADE

		)engine=innodb
		AUTO_INCREMENT = 1
		COMMENT 'Entidad encargada de registrar, ciudades del Ecuador guarda una relacion 
		con la provincia a la que corresponde, en caso de no tener una ciudad en
		la lista de ciudades, se crea una nueva permitiendole al usuario ingresarla';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad contacto
	-- -------------------------------------------------------------------
	create table contacto(
		id_contacto smallint unsigned NOT NULL AUTO_INCREMENT,
		id_cuidad smallint unsigned DEFAULT NULL,
		nombre varchar(50) NOT NULL,
		telefono varchar(15) DEFAULT NULL,
		celular varchar(15) DEFAULT NULL,
		email varchar(100) DEFAULT NULL,
		notas MEDIUMTEXT DEFAULT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_contacto),

		CONSTRAINT fk_contacto_ciudad
      	FOREIGN KEY (id_cuidad)
      	REFERENCES ciudad(id_cuidad)
      	ON DELETE RESTRICT ON UPDATE CASCADE

		)engine=innodb
		AUTO_INCREMENT = 1
		COMMENT 'Entidad encargada de registrar los contactos de la base de datos
		Estos contactos son luego referenciados a las entidades que lo requieran,
		debe tener un registro cero';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad proveedor
	-- -------------------------------------------------------------------	
	create table proveedor(
		id_proveedor varchar(13) NOT NULL,
		id_cuidad smallint unsigned DEFAULT NULL,
		id_contacto smallint unsigned DEFAULT NULL,
		nombre varchar(150) NOT NULL ,
		direccion varchar(500) NOT NULL,
		telefono varchar(15) NOT NULL ,
		email varchar(30) DEFAULT NULL,
		credito boolean DEFAULT NULL,
		notas MEDIUMTEXT DEFAULT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_proveedor),

		CONSTRAINT fk_proveedor_contacto
      	FOREIGN KEY (id_contacto)
      	REFERENCES contacto(id_contacto)
      	ON DELETE RESTRICT ON UPDATE CASCADE,

      	CONSTRAINT fk_proveedor_ciudad
      	FOREIGN KEY (id_cuidad)
      	REFERENCES cuidad(id_cuidad)
      	ON DELETE RESTRICT ON UPDATE CASCADE

		)engine=innodb
		COMMENT 'Entidad encargada de registrar los datos básicos de proeedor de materiales 
		y repuestos de vehículos';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad técnico
	-- -------------------------------------------------------------------
	create table tecnico(
		id_tecnico varchar(10) NOT NULL,
		nombres varchar(200) NOT NULL,
		telefono varchar(15) DEFAULT NULL,
		celular  varchar(15)DEFAULT NULL,
		email  varchar(100)DEFAULT NULL,
		notas MEDIUMTEXT DEFAULT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_tecnico)
		)engine=innodb
		COMMENT 'Entidad encargada de registrar los tecnicos';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad cliente
	-- -------------------------------------------------------------------
	create table cliente(
		id_cliente char(13) NOT NULL,
		id_contacto smallint unsigned DEFAULT NULL,
		id_cuidad smallint unsigned DEFAULT NULL,
		nombre varchar(200) NOT NULL,
		direccion varchar(600) NOT NULL,
		telefono varchar(15) NOT NULL,
		fax varchar(15)DEFAULT NULL,
		mail varchar(100)DEFAULT NULL,
		notas MEDIUMTEXT DEFAULT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_cliente),

		CONSTRAINT fk_cliente_contacto
      	FOREIGN KEY (id_contacto)
      	REFERENCES contacto(id_contacto)
      	ON DELETE RESTRICT ON UPDATE CASCADE,

      	CONSTRAINT fk_cliente_cuidad
      	FOREIGN KEY (id_cuidad)
      	REFERENCES cuidad(id_cuidad)
      	ON DELETE RESTRICT ON UPDATE CASCADE
		)engine=innodb
		COMMENT 'Entidad encargada de registrar a los cliente
				se sugiere que el telefono sea de la persona encargada 
				de la facturacio';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad vehículo
	-- -------------------------------------------------------------------
	create table vehiculo(
		id_vehiculo char(17) NOT NULL,
		id_cliente char(13) NOT NULL,
		id_contacto smallint unsigned DEFAULT NULL,
		id_cuidad smallint unsigned DEFAULT NULL,
		modelo varchar(45)DEFAULT NULL,
		nro_motor varchar(25)DEFAULT NULL,
		ingreso datetime DEFAULT NULL, 
		notas MEDIUMTEXT DEFAULT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_vehiculo),
		INDEX idx_vehiculo(id_vehiculo ASC),

		CONSTRAINT fk_vehiculo_cliente
      	FOREIGN KEY (id_cliente)
      	REFERENCES cliente(id_cliente)
      	ON DELETE RESTRICT ON UPDATE CASCADE,

      	CONSTRAINT fk_vehiculo_contacto
      	FOREIGN KEY (id_contacto)
      	REFERENCES contacto(id_contacto)
      	ON DELETE RESTRICT ON UPDATE CASCADE,

      	CONSTRAINT fk_vehiculo_cuidad
      	FOREIGN KEY (id_cuidad)
      	REFERENCES cuidad(id_cuidad)
      	ON DELETE RESTRICT ON UPDATE CASCADE
		)engine=innodb
		COMMENT 'Entidad encargada de registrar los vehículos el ingreso es la fecha
				en la que el vehiculo fue entregado al MAGAP';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad inspección
	-- -------------------------------------------------------------------
	create table inspeccion(
		id_inspeccion smallint unsigned NOT NULL AUTO_INCREMENT,
		id_vehiculo varchar(17) NOT NULL,
		id_tecnico varchar(10) NOT NULL,
		id_contacto smallint unsigned NOT NULL,
		id_cuidad smallint unsigned DEFAULT NULL,
		periodo smallint unsigned NOT NULL,
		fecha date NOT NULL,		
		notas TEXT DEFAULT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_inspeccion),

		CONSTRAINT fk_inspeccion_vehiculo
      	FOREIGN KEY (id_vehiculo)
      	REFERENCES vehiculo(id_vehiculo)
      	ON DELETE RESTRICT ON UPDATE CASCADE,

      	CONSTRAINT fk_inspeccion_tecnico
      	FOREIGN KEY (id_tecnico)
      	REFERENCES tecnico(id_tecnico)
      	ON DELETE RESTRICT ON UPDATE CASCADE,

      	CONSTRAINT fk_inspeccion_contacto
      	FOREIGN KEY (id_contacto)
      	REFERENCES contacto(id_contacto)
      	ON DELETE RESTRICT ON UPDATE CASCADE,

      	CONSTRAINT fk_inspeccion_cuidad
      	FOREIGN KEY (id_cuidad)
      	REFERENCES cuidad(id_cuidad)
      	ON DELETE RESTRICT ON UPDATE CASCADE

		)engine=innodb
		AUTO_INCREMENT = 1
		COMMENT 'De momento es solo un formulario de inspeccion';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad inventario
	-- -------------------------------------------------------------------
	create  table inventario(
		id_inventario smallint unsigned  NOT NULL AUTO_INCREMENT,
		fecha datetime NOT NULL,
		nombre varchar(100) NOT NULL,
		descripcion varchar(200)DEFAULT NULL,
		unidad varchar(25)DEFAULT NULL,
		stok_min smallint unsigned NOT NULL COMMENT "12 filtros,12 aceite, 4 refirgerante 1 liquido de frenos",
		marca varchar(45)DEFAULT NULL,
		ubicacion varchar(100) NOT NULL,
		notas MEDIUMTEXT DEFAULT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_inventario)
		)engine=innodb 
		AUTO_INCREMENT = 1000
		COMMENT 'Entidad que lleva un detalle de los productos en bodega
		Todos los materiales están en litros y unidades, se setablece un standar para los 
		condigos del inventario, cada producto ingresado al inventario empieza con el mail
		1000,1001,1002. la columna unidad debe contener, litros, unidades, galones, etc';

	-- -------------------------------------------------------------------
	-- Estructura de la entidad viaje
	-- -------------------------------------------------------------------
	create table viaje(
		id_viaje smallint unsigned not null AUTO_INCREMENT,
		fecha_salida date,
		fecha_regreso date,
		nro_vehiculos smallint unsigned not null COMMENT 'Cuantos veiculos se piensa reparar', 
		provincias_destino  varchar(500) not null COMMENT 'Nmbre de las provincias que se quiere visitar, separadas por comas',
		varlor_caja decimal(5,2),
		informe text,
		registro timestamp not null default current_timestamp,
		UNIQUE (fecha_salida,fecha_regreso),
		primary key(id_viaje)
		)engine=innodb
		AUTO_INCREMENT = 1
		COMMENT 'Registra los viajes realizados por los técincos, los mantenimientos dependen de los 
		viajes para existir, ya que los mantenimientos se los realiza con un viaje, se necesita
		ingresar un viaje a Quito para los mantenimientos y reparaciones realizados en Quito';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad gastos_viajes
	-- -------------------------------------------------------------------
	create table gastos_viaje(
		id_viaje smallint unsigned not null,
		nro_factura varchar(20) not null,
		fecha date not null,
		detalle varchar(300) not null,
		valor decimal(4,2) not null,
		registro timestamp not null default current_timestamp,
		primary key(id_viaje,nro_factura,valor),

		CONSTRAINT fk_gastos_viaje_viaje
		FOREIGN KEY(id_viaje)
		REFERENCES viaje(id_viaje)
		ON UPDATE CASCADE ON DELETE RESTRICT

		)engine=innodb 
		AUTO_INCREMENT=1 
		COMMENT 'Se registran los gastos de los viajes, en esta entidad se graban los 
		gastos realizados para cada viaje, se registran los datos de las facturas de acuerdo
		al formato que se tiene en gastos de viajes en la carpeta polaris de dropbox';
	-- -------------------------------------------------------------------
	-- Estructura de la reparación
	-- -------------------------------------------------------------------
	create table reparacion(
		id_reparacion smallint unsigned NOT NULL AUTO_INCREMENT,
		id_viaje smallint unsigned not null,
		id_vehiculo char(17) NOT NULL,
		id_cuidad smallint unsigned DEFAULT NULL,
		periodo smallint unsigned NOT NULL,
		fecha_entrada datetime NOT NULL,
		fecha_salida datetime DEFAULT NULL,
		notas MEDIUMTEXT DEFAULT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_reparacion),

		CONSTRAINT fk_reparacion_vehiculo
      	FOREIGN KEY (id_vehiculo)
      	REFERENCES vehiculo(id_vehiculo)
      	ON DELETE RESTRICT ON UPDATE CASCADE,

      	CONSTRAINT fk_reparacion_viaje
      	FOREIGN KEY (id_viaje)
      	REFERENCES viaje(id_viaje)
      	ON DELETE RESTRICT ON UPDATE CASCADE,

      	CONSTRAINT fk_reparacion_cuidad
      	FOREIGN KEY (id_cuidad)
      	REFERENCES cuidad(id_cuidad)
      	ON DELETE RESTRICT ON UPDATE CASCADE

		)engine=innodb
		AUTO_INCREMENT = 1
		COMMENT 'Entidad encargada de registrar las reparaciones realizadas a los vehiculos polaris,
		cada reparacion al vehiculo se registra en reparacion_detalle';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad detalles de reparación
	-- -------------------------------------------------------------------
	create table reparacion_detalle(
		id_reparacion_detalle smallint unsigned NOT NULL,
		id_reparacion smallint unsigned NOT NULL,
		id_inventario smallint unsigned NOT NULL,
		fecha time NOT NULL,
		estado varchar(25) COMMENT 'bueno, exelente,reparar,dañado,necesita cambio',
		cantidad smallint unsigned not null,		
		notas varchar(600) DEFAULT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_reparacion_detalle),

		CONSTRAINT fk_reparacion_detalle_reparacion
      	FOREIGN KEY (id_reparacion)
      	REFERENCES reparacion(id_reparacion)
      	ON DELETE RESTRICT ON UPDATE CASCADE,

      	CONSTRAINT fk_reparacion_detalle_inventario
      	FOREIGN KEY (id_inventario)
      	REFERENCES inventario(id_inventario)
      	ON DELETE RESTRICT ON UPDATE CASCADE

		)engine=innodb
		COMMENT 'Entidad encargada de registrar los detalles de las reparaciones cada detalle puede 
				contener una salida de inventario';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad mantenimiento
	-- -------------------------------------------------------------------
	create table mantenimiento(
		id_mantenimiento smallint unsigned NOT NULL AUTO_INCREMENT,
		id_viaje smallint unsigned not null,
		id_vehiculo char(17) NOT NULL,
		id_cuidad smallint unsigned DEFAULT NULL,
		periodo smallint unsigned NOT NULL,
		fecha date NOT NULL,
		kilometros varchar(10) NOT NULL,
		notas MEDIUMTEXT DEFAULT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_mantenimiento),

		CONSTRAINT fk_mantenimiento_vehiculo
      	FOREIGN KEY (id_vehiculo)
      	REFERENCES vehiculo(id_vehiculo)
      	ON DELETE RESTRICT ON UPDATE CASCADE,

      	CONSTRAINT fk_mantenimiento_viaje
      	FOREIGN KEY (id_viaje)
      	REFERENCES viaje(id_viaje)
      	ON DELETE RESTRICT ON UPDATE CASCADE,

      	CONSTRAINT fk_mantenimiento_cuidad
      	FOREIGN KEY (id_cuidad)
      	REFERENCES cuidad(id_cuidad)
      	ON DELETE RESTRICT ON UPDATE CASCADE

		)engine=innodb
		AUTO_INCREMENT = 1
		COMMENT 'Registra los mantenimientos realizados aun vehiculo, los insumos usados para el mantenimiento
				se registran en mantenimiento_detalle';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad detalle de mantenimiento
	-- -------------------------------------------------------------------
	create table mantenimiento_detalle(
		id_mantenimiento_detalle int unsigned NOT NULL AUTO_INCREMENT,
		id_mantenimiento smallint unsigned NOT NULL,
		id_inventario smallint unsigned NOT NULL,
		fecha time NOT NULL,
		estado varchar(25) COMMENT 'cambio,reparacio,correccion',
		cantidad float unsigned not null,		
		notas varchar(600) DEFAULT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		UNIQUE(id_mantenimiento_detalle),
		primary key(id_mantenimiento, id_inventario),

		CONSTRAINT fk_mantenimiento_detalle_mantenimiento
      	FOREIGN KEY (id_mantenimiento)
      	REFERENCES mantenimiento(id_mantenimiento)
      	ON DELETE RESTRICT ON UPDATE CASCADE,

		CONSTRAINT fk_mantenimiento_detalle_inventario
      	FOREIGN KEY (id_inventario)
      	REFERENCES inventario(id_inventario)
      	ON DELETE RESTRICT ON UPDATE CASCADE
      	)engine=innodb
		AUTO_INCREMENT =1
		COMMENT 'Registra los detalles del mantenimiento y los costos de los insumos';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad tecnico_mantenimiento_viaje
	-- -------------------------------------------------------------------
	create table tecnico_viaje(
		id_tecnico varchar(10) NOT NULL,
		id_viaje smallint unsigned not null,
		registro timestamp not null default current_timestamp,
		PRIMARY KEY (id_tecnico,id_viaje),

		CONSTRAINT fk_tecnico_viaje_tecnico
      	FOREIGN KEY (id_tecnico)
      	REFERENCES tecnico(id_tecnico)
      	ON DELETE RESTRICT ON UPDATE CASCADE,

      	CONSTRAINT fk_tecnico_viaje
      	FOREIGN KEY (id_viaje)
      	REFERENCES viaje(id_viaje)
      	ON DELETE RESTRICT ON UPDATE CASCADE

		)engine=innodb
		COMMENT 'Registra a los técnicos en los mantenimientos para cada viaje';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad entradas de inventario
	-- -------------------------------------------------------------------
	create table compra(
		id_compra smallint unsigned NOT NULL, 
		id_inventario smallint unsigned  NOT NULL,
		id_proveedor varchar(13) NOT NULL ,
		nro_factura varchar(12) NOT NULL ,
		fecha datetime NOT NULL, 
		cantidad smallint unsigned NOT NULL,
		costo decimal(5,2) COMMENT 'costo por unidad',
		notas MEDIUMTEXT DEFAULT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_compra),

		CONSTRAINT fk_compra_inventario
      	FOREIGN KEY (id_inventario)
      	REFERENCES inventario(id_inventario)
      	ON DELETE RESTRICT ON UPDATE CASCADE,

		CONSTRAINT fk_compra_proveedor
      	FOREIGN KEY (id_proveedor)
      	REFERENCES proveedor(id_proveedor)
      	ON DELETE RESTRICT ON UPDATE CASCADE

		)engine=innodb
		COMMENT 'Entidad encargada de manejar la entrada de stock al inventario
				las unidades de los productos son las mimas que el detalle del inventario';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad factura
	-- -------------------------------------------------------------------
	create table factura(
		id_factura int not null,
		id_cliente char(13) NOT NULL,
		id_contacto smallint unsigned DEFAULT NULL,
		fecha date NOT NULL,
		fecha_envio date NOT NULL,
		guia_envio varchar(50),
		servicio_envio varchar(80) NOT NULL,
		estado varchar(50) NOT NULL,
		archivo varchar(200)DEFAULT NULL,
		notas MEDIUMTEXT DEFAULT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_factura),

		CONSTRAINT fk_factura_cliente
      	FOREIGN KEY (id_cliente)
      	REFERENCES cliente(id_cliente)
      	ON DELETE RESTRICT ON UPDATE CASCADE,

      	CONSTRAINT fk_factura_contacto
      	FOREIGN KEY (id_contacto)
      	REFERENCES contacto(id_contacto)
      	ON DELETE RESTRICT ON UPDATE CASCADE

		)engine=innodb
	AUTO_INCREMENT = 1
		COMMENT 'Entidad encargada de registrar las facturación, se implementa una ruta
		al archivo del escaneado de la factura';	
	-- -------------------------------------------------------------------
	-- Estructura de la entidad detalles de la factura
	-- 0360015690001
	-- -------------------------------------------------------------------
	create table factura_detalle(		
		id_factura int not null,
		id_mantenimiento smallint unsigned DEFAULT NULL,
		id_reparacion smallint unsigned DEFAULT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_factura,id_mantenimiento,id_reparacion),

		CONSTRAINT fk_factura_detalle_factura
      	FOREIGN KEY (id_factura)
      	REFERENCES factura(id_factura)
      	ON DELETE RESTRICT ON UPDATE CASCADE,

      	CONSTRAINT fk_factura_detalle_mantenimiento
      	FOREIGN KEY (id_mantenimiento)
      	REFERENCES mantenimiento(id_mantenimiento)
      	ON DELETE RESTRICT ON UPDATE CASCADE,

      	CONSTRAINT fk_factura_detalle_reparacion
      	FOREIGN KEY (id_reparacion)
      	REFERENCES reparacion(id_reparacion)
      	ON DELETE RESTRICT ON UPDATE CASCADE
      	
		)engine=innodb
		COMMENT 'Entidad que registra los detalles de la facturacio se entiende por detalle
				los vehiculos a los que se le realizaron mantenimiento, un mantenimiento no
				se factura más de una vez, para poder controlar esto se obliga a que un campo de la clave
				primaria sea cero los dos campos no deben tener un valor diferente de cero los dos a la
				vez ya que la restriccion registra un mantenimiento o una reparación';