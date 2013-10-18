-- ----------------------------------------------------------------------------------------
-- Modelo de base de datos Gelvsrm 
-- ----------------------------------------------------------------------------------------
-- autor <@eduardouio>
-- copyrigth (c)gelvsrm.com 2013>
-- version 1.0
-- engine innodb
-- content <Logica de triggers y sps>
-- Tiempo de generación: 03-10-2013 a las 17:25:25
-- Versión del servidor: 5.5.32-0ubuntu0.12.04.1
-- ----------------------------------------------------------------------------------------

-- ----------------------------------------------------------------------------------------
-- Trigger encargado de verificar que no se envíe una llave primaria con los dos
-- campos diferentes de cero.
-- ----------------------------------------------------------------------------------------
DELIMITER //
CREATE TRIGGER verificar_factura_detalle 
	BEFORE INSERT ON factura_detalle
	FOR EACH ROW 
	BEGIN
		SET @i_m = NEW.id_mantenimiento;
		SET @i_r = NEW.id_reparacion;
		IF((NEW.id_mantenimiento > 0) AND (NEW.id_reparacion > 0)) THEN
			SELECT 'Los dos valores son diferentes de cero';
		ELSE
			SET NEW.id_mantenimiento = @i_m;
			SET NEW.id_reparacion = @i_r;
		END IF;
	RETURN 0;
	END;//
DELIMITER ;