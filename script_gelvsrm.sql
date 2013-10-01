
create database gelvsrm_polaris;
	use gelvsrm_polaris;
	-- -------------------------------------------------------------------
	-- Estructura de la entidad contacto
	-- -------------------------------------------------------------------
	create table contacto(
		id_contacto smallint unsigned NOT NULL AUTO_INCREMENT,
		fecha datetime NOT NULL,
		nombre varchar(50) NOT NULL,
		telefono varchar(15) DEFAULT NULL,
		celular varchar(15) DEFAULT NULL,
		email varchar(100) DEFAULT NULL,
		cuidad varchar(50) DEFAULT NULL,
		provincia varchar(50) DEFAULT NULL,
		registro timestamp not null default current_timestamp 
		primary key(id_contacto),
		on update current_timestamp,
		)engine=innodb
		AUTO_INCREMENT = 1
		COMMENT 'Entidad encargada de registrar los contactos de la base de datos
		Estos contactos son luego referenciados a las entidades que lo requieran,
		debe tener un registro cero';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad proveedor
	-- -------------------------------------------------------------------	
	create table proveedor(
		id_proveedor varchar(13) NOT NULL ,
		nombre varchar(150) NOT NULL ,
		direccion varchar(500) NOT NULL,
		telefono varchar(15) NOT NULL ,
		email varchar(30) DEFAULT NULL,
		credito boolean DEFAULT NULL,
		notas text DEFAULT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_proveedor)
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
		registro timestamp not null default current_timestamp 
		on update current_timestamp
		primary key(id_tecnico)
		)engine=innodb
		COMMENT 'Entidad encargada de registrar los tecnicos';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad cliente
	-- -------------------------------------------------------------------
	create table cliente(
		id_cliente char(13) NOT NULL,
		id_contacto smallint unsigned NOT NULL,
		nombre varchar(200) NOT NULL,
		direccion varchar(600) NOT NULL,
		telefono varchar(15) NOT NULL,
		fax varchar(15)DEFAULT NULL,
		fecha datetime DEFAULT NULL,
		mail varchar(100)DEFAULT NULL,,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_cliente),
		CONSTRAINT fk_cliente_contacto
      	FOREIGN KEY (id_contacto)
      	REFERENCES contacto(id_contacto)
      	ON DELETE RESTRICT ON UPDATE CASCADE
		)engine=innodb
		COMMENT 'Entidad encargada de registrar a los cliente
				se sugiere que el telefono sea de la persona encargada 
				de la facturacio';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad vehículo
	-- -------------------------------------------------------------------
	create table vehiculo(
		id_vehiculo char(16) NOT NULL,
		id_cliente char(13) NOT NULL,
		id_contacto smallint unsigned NOT NULL,
		modelo varchar(45)DEFAULT NULL,
		nro_motor varchar(25)DEFAULT NULL,
		ingreso datetime DEFAULT NULL, 
		encargado varchar(50)DEFAULT NULL,
		ubicacion varchar(100)DEFAULT NULL,
		notas text DEFAULT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_vehiculo),
		CONSTRAINT fk_vehiculo_cliente
      	FOREIGN KEY (id_cliente)
      	REFERENCES cliente(id_cliente)
      	ON DELETE RESTRICT ON UPDATE CASCADE,
      	CONSTRAINT fk_vehiculo_contacto
      	FOREIGN KEY (id_contacto)
      	REFERENCES contacto(id_contacto)
      	ON DELETE RESTRICT ON UPDATE CASCADE      	
		)engine=innodb
		COMMENT 'Entidad encargada de registrar los vehículos el ingreso es la fecha
				en la que el vehiculo fue entregado al MAGAP';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad inspección
	-- -------------------------------------------------------------------
	create table inspeccion(
		id_inspeccion smallint unsigned NOT NULL AUTO_INCREMENT,
		id_vehiculo varchar(16) NOT NULL,
		id_tecnico varchar(10) NOT NULL,
		id_contacto smallint unsigned NOT NULL,
		fecha datetime NOT NULL,
		ubicacion varchar(100)DEFAULT NULL,
		detalle text,
		contacto varchar(45)DEFAULT NULL,
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
      	ON DELETE RESTRICT ON UPDATE CASCADE
		)engine=innodb
	AUTO_INCREMENT = 1
		COMMENT 'De momento es solo un formulario de inspeccion';
	-- -------------------------------------------------------------------
	-- Estructura de la reparación
	-- -------------------------------------------------------------------
	create table reparacion(
		id_reparacion smallint unsigned NOT NULL AUTO_INCREMENT,
		id_vehiculo char(16) NOT NULL,
		id_tecnico varchar(10) NOT NULL,
		fecha_entrada datetime NOT NULL,
		fecha_salida datetime DEFAULT NULL,
		detalles text DEFAULT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_reparacion),
		CONSTRAINT fk_reparacion_vehiculo
      	FOREIGN KEY (id_vehiculo)
      	REFERENCES vehiculo(id_vehiculo)
      	ON DELETE RESTRICT ON UPDATE CASCADE,
      	CONSTRAINT fk_reparacion_tecnico
      	FOREIGN KEY (id_tecnico)
      	REFERENCES tecnico(id_tecnico)
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
		item varchar(200)DEFAULT NULL,
		estado varchar(25) COMMENT 'bueno, exelente,reparar,dañado,necesita cambio',
		observaciones varchar(600)DEFAULT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_reparacion_detalle),
		CONSTRAINT fk_reparacion_detalle_reparacion
      	FOREIGN KEY (id_reparacion)
      	REFERENCES reparacion(id_reparacion)
      	ON DELETE RESTRICT ON UPDATE CASCADE
		)engine=innodb
		COMMENT 'Entidad encargada de registrar los detalles de las reparaciones cada detalle puede 
				contener una salida de inventario';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad mantenimiento
	-- -------------------------------------------------------------------
	create table mantenimiento(
		id_manteminiento smallint unsigned NOT NULL AUTO_INCREMENT,
		id_vehiculo char(16) NOT NULL,
		id_tecnico varchar(10) NOT NULL,
		periodo smallint unsigned NOT NULL,
		ubicacion varchar(100),
		fecha datetime NOT NULL,
		kilometros varchar(10) NOT NULL,
		observacion text DEFAULT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_manteminiento),
		CONSTRAINT fk_mantenimiento_vehiculo
      	FOREIGN KEY (id_vehiculo)
      	REFERENCES vehiculo(id_vehiculo)
      	ON DELETE RESTRICT ON UPDATE CASCADE,
      	CONSTRAINT fk_mantenimiento_tecnico
      	FOREIGN KEY (id_tecnico)
      	REFERENCES tecnico(id_tecnico)
      	ON DELETE RESTRICT ON UPDATE CASCADE
		)engine=innodb
	AUTO_INCREMENT = 1
		COMMENT 'Registra los mantenimientos realizados aun vehiculo, los insumos usados para el mantenimiento
				se registran en mantenimiento_detalle';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad detalle de mantenimiento
	-- -------------------------------------------------------------------
	create table mantenimiento_detalle(
		id_manteminiento_detalle int unsigned NOT NULL,
		id_manteminiento smallint unsigned NOT NULL,
		item varchar(200)DEFAULT NULL,
		estado varchar(25) COMMENT 'cambio,reparacio,correccio',
		observaciones varchar(600),
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_manteminiento_detalle),
		CONSTRAINT fk_mantenimiento_detalle_mantenimiento
      	FOREIGN KEY (id_manteminiento)
      	REFERENCES mantenimiento(id_manteminiento)
      	ON DELETE RESTRICT ON UPDATE CASCADE
      	)engine=innodb
		COMMENT 'Registra los detalles del mantenimiento y los costos de los insumos';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad inventario
	-- -------------------------------------------------------------------
	create  table inventario(
		id_inventario smallint unsigned  NOT NULL AUTO_INCREMENT,
		fecha datetime NOT NULL,
		nombre varchar(100) NOT NULL,
		descpricion varchar(200)DEFAULT NULL,
		unidad varchar(25)DEFAULT NULL,
		stok_min smallint unsigned NOT NULL COMMENT "12 filtros,12 aceite, 4 refirgerante 1 liquido de frenos",
		marca varchar(45)DEFAULT NULL,
		ubicacion varchar(100) NOT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_inventario)
		)engine=innodb 
	AUTO_INCREMENT = 1
		COMMENT 'Entidad que lleva un detalle de los productos en bodega
		Todos los materiales están en litros y unidades, se setablece un standar para los 
		condigos del inventario, cada producto ingresado al inventario empieza con el mail
		1000,1001,1002. la columna unidad debe contener, litros, unidades, galones, etc';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad entradas de inventario
	-- -------------------------------------------------------------------
	create table inventario_entrada(
		id_inventario_entrada smallint unsigned NOT NULL, 
		id_inventario smallint unsigned  NOT NULL,
		id_proveedor varchar(13) NOT NULL ,
		nro_factura varchar(12) NOT NULL ,
		fecha datetime,
		cantidad smallint unsigned NOT NULL,
		costo decimal(5,2) COMMENT 'costo por unidad',
		notas text,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_inventario_entrada),
		CONSTRAINT fk_inventario_entrada_inventario
      	FOREIGN KEY (id_inventario)
      	REFERENCES inventario(id_inventario)
      	ON DELETE RESTRICT ON UPDATE CASCADE,
		CONSTRAINT fk_inventario_entrada_proveedor
      	FOREIGN KEY (id_proveedor)
      	REFERENCES proveedor(id_proveedor)
      	ON DELETE RESTRICT ON UPDATE CASCADE
		)engine=innodb
		COMMENT 'Entidad encargada de manejar la entrada de stock al inventario
				las unidades de los productos son las mimas que el detalle del inventario';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad salida de inventario
	-- -------------------------------------------------------------------
create table inventario_salida(
		id_inventario_salida smallint unsigned NOT NULL ,
		id_inventario smallint unsigned  NOT NULL,
		id_manteminiento_detalle int unsigned NOT NULL,
		id_reparacion_detalle smallint unsigned NOT NULL,
		cantidad smallint unsigned NOT NULL,
		fecha datetime DEFAULT NULL,
		notas text DEFAULT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_inventario_salida),
		CONSTRAINT fk_inventario_salida_inventario
      	FOREIGN KEY (id_inventario)
      	REFERENCES inventario(id_inventario)
      	ON DELETE RESTRICT ON UPDATE CASCADE,
      	CONSTRAINT fk_invetario_salida_mantenimiento_detalle
      	FOREIGN KEY (id_manteminiento_detalle)
      	REFERENCES mantenimiento_detalle(id_manteminiento_detalle)
      	ON DELETE RESTRICT ON UPDATE CASCADE,
      	CONSTRAINT fk_inventario_salida_reparacion_detalle
      	FOREIGN KEY (id_reparacion_detalle)
      	REFERENCES reparacion_detalle(id_reparacion_detalle)
      	ON DELETE RESTRICT ON UPDATE CASCADE
		)engine=innodb
		COMMENT 'Entidad encargada de registrar las salidas del stok_min
		del inventario, para el inventario de salida se crea dos relaciones
		una con mantenimiento_detalle y otra con reparacion_detalle, en ambas entidades 
		se debe crear un registro cero para que proceda a registrar un mantenimiento u una 
		una reparacion';
	-- -------------------------------------------------------------------
	-- Estructura de la entidad factura
	-- -------------------------------------------------------------------
	create table factura(
		id_factura smallint unsigned NOT NULL AUTO_INCREMENT,
		id_cliente char(13) NOT NULL,
		fecha datetime NOT NULL,
		fecha_envio datetime NOT NULL,
		estado boolean NOT NULL,
		archivo varchar(200)DEFAULT NULL,
		notas text DEFAULT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_factura),
		CONSTRAINT fk_factura_cliente
      	FOREIGN KEY (id_cliente)
      	REFERENCES cliente(id_cliente)
      	ON DELETE RESTRICT ON UPDATE CASCADE
		)engine=innodb
	AUTO_INCREMENT = 1
		COMMENT 'Entidad encargada de registrar las facturación, se implementa una ruta
		al archivo del escaneado de la factura';	
	-- -------------------------------------------------------------------
	-- Estructura de la entidad detalles de la factura
	-- -------------------------------------------------------------------
	create table factura_detalle(		
		id_manteminiento smallint unsigned NOT NULL,
		id_reparacion smallint unsigned NOT NULL,
		id_factura smallint unsigned NOT NULL,
		registro timestamp not null default current_timestamp 
		on update current_timestamp,
		primary key(id_manteminiento, id_factura,id_reparacion),
		CONSTRAINT fk_factura_detalle_factura
      	FOREIGN KEY (id_factura)
      	REFERENCES factura(id_factura)
      	ON DELETE RESTRICT ON UPDATE CASCADE,
      	CONSTRAINT fk_factura_detalle_mantenimiento
      	FOREIGN KEY (id_manteminiento)
      	REFERENCES mantenimiento(id_manteminiento)
      	ON DELETE RESTRICT ON UPDATE CASCADE,
      	CONSTRAINT fk_factura_detalle_reparacion
      	FOREIGN KEY (id_reparacion)
      	REFERENCES reparacion(id_reparacion)
      	ON DELETE RESTRICT ON UPDATE CASCADE
		)engine=innodb
		COMMENT 'Entidad que registra los detalles de la facturacio se entiende por detalle
				los vehiculos a los que se le realizaron mantenimiento, un mantenimiento no
				se factura más de una veza';