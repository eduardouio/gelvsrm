-- ----------------------------------------------------------------------------------------
-- Modelo de base de datos Gelvsrm 
-- ----------------------------------------------------------------------------------------
-- autor <@eduardouio>
-- copyrigth (c)gelvsrm.com 2013>
-- version 1.0
-- engine innodb
-- content <Vistas del modelo de bases de datos>
-- Versión del servidor: 5.5.32-0ubuntu0.12.04.1
-- ----------------------------------------------------------------------------------------

-- ----------------------------------------------------------------------------------------
-- Vista de los items de inventario existentes
-- ----------------------------------------------------------------------------------------
create view v_inventario
	as
	select 