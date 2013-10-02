-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 02-10-2013 a las 11:48:47
-- Versión del servidor: 5.5.32-0ubuntu0.12.04.1
-- Versión de PHP: 5.3.10-1ubuntu3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `gelvsrm_polaris`
--
CREATE DATABASE IF NOT EXISTS `gelvsrm_polaris` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `gelvsrm_polaris`;

--
-- Volcado de datos para la tabla `contacto`
--

INSERT INTO `contacto` (`id_contacto`, `fecha`, `nombre`, `telefono`, `celular`, `email`, `cuidad`, `provincia`, `registro`) VALUES
(1, '2013-10-02 00:00:00', 'Sin Nombre', NULL, NULL, NULL, NULL, NULL, '2013-10-01 16:31:48'),
(2, '2013-10-01 00:00:00', 'ING. LUIS RIVERA GUERRA', '03-2981818', '09-7455567', NULL, 'BOLIVAR', 'GURANDA', '2013-10-01 16:48:32'),
(3, '2013-10-01 00:00:00', 'ING.  FRANKLIN PILATASIG MOLINA', '03-2812986', '095883022', NULL, 'COTOPAXI', NULL, '2013-10-01 17:03:30');

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`id_cliente`, `id_contacto`, `nombre`, `direccion`, `telefono`, `fax`, `fecha`, `mail`, `registro`) VALUES
('0360015690001', 1, 'Dirección Provincial Agropecuaria del Caña', 'Andres f, cordoba sn y humberto rodrguez edf shopin Jerez 2do piso', '07-2842139', NULL, '2013-10-01 00:00:00', NULL, '2013-10-01 17:10:46'),
('0560022430001', 1, ' Director Tecnico Area de cotopaxi', 'Av Atahualpa y zamora', '03-2812808', NULL, '2013-10-01 00:00:00', NULL, '2013-10-01 17:07:11'),
('0660819660001', 1, 'Dirección Provincial Agropecuaria de Chimborazo', 'Av 9 de Octubre junto a la Quinta Macaji', '03-2610043', NULL, '2013-10-01 00:00:00', NULL, '2013-10-01 17:14:08'),
('160023480001', 1, 'Dirrecion Provincial Agropecuaria del Azuay', 'Vega muños 2-40 y tomas ordoñes - Cuenca', '07-2843550', '', '2013-10-01 00:00:00', '', '2013-10-01 16:50:52'),
('1865012760001', 1, 'Dirección Provincial Agropecuaria de Tunguragua\r\n', 'Centro Comercial Ambato Bloque nro 2 Av. 12 de Noviembre y Mariano Wgues', '03-2823900 / 03', NULL, NULL, NULL, '2013-10-01 18:22:12'),
('260004750001', 1, 'Direccion Provincial Agropecuaria de Bolivar', 'Guaranda, Av. Circunvalacion S/N y Ambato', '03-2981818', NULL, '2013-10-01 00:00:00', NULL, '2013-10-01 17:13:45');

--
-- Volcado de datos para la tabla `proveedor`
--

INSERT INTO `proveedor` (`id_proveedor`, `nombre`, `direccion`, `telefono`, `email`, `credito`, `notas`, `registro`) VALUES
('099001865001', 'ConAuto', 'Av. 10 de Agosto N 4012 y Av. Gaspar de Villarroel', '2241555-2269208', NULL, NULL, 'Aceites 5W90', '2013-10-02 16:41:12'),
('1790202321001', 'Erco Tires', 'Av.10 de Agosto y Rafael Bustamante', '6036205 - 2403-557', 'pgavilanez@tire-experts.com.ec', NULL, 'Aceites 2W50 ', '2013-10-02 16:38:31');

--
-- Volcado de datos para la tabla `tecnico`
--

INSERT INTO `tecnico` (`id_tecnico`, `nombres`, `telefono`, `celular`, `email`, `registro`) VALUES
('0803550466', 'GALO SINCHIGUANO TAIPE ', NULL, '0981913856', 'galo.st10@hotmail.com', '2013-10-01 17:25:09'),
('1711938025', 'MARCO LLUMIQUINGA', NULL, NULL, NULL, '2013-10-01 17:25:32');
--
-- Volcado de datos para la tabla `vehiculo`
--

INSERT INTO `vehiculo` (`id_vehiculo`, `id_cliente`, `id_contacto`, `modelo`, `nro_motor`, `ingreso`, `encargado`, `ubicacion`, `notas`, `registro`) VALUES
('4XATH762AD4317220', '0560022430001', 1, NULL, NULL, NULL, NULL, 'GUANGAJE', NULL, '2013-10-01 18:13:27'),
('4XATH76A0D2290773', '1865012760001', 1, NULL, NULL, NULL, NULL, 'PILLARO', NULL, '2013-10-01 18:32:30'),
('4XATH76A0D2290790', '1865012760001', 1, NULL, NULL, NULL, NULL, 'QUISAPINCHA', NULL, '2013-10-01 18:32:30'),
('4XATH76A0D2291101', '0560022430001', 1, NULL, NULL, NULL, NULL, 'EL CORAZON', NULL, '2013-10-01 18:13:27'),
('4XATH76A0D2293205', '0560022430001', 1, NULL, NULL, NULL, NULL, 'SIGCHOS', NULL, '2013-10-01 18:13:27'),
('4XATH76A0D2293222', '0560022430001', 1, NULL, NULL, NULL, NULL, 'PUJILI', NULL, '2013-10-01 18:13:27'),
('4XATH76A0D2293253', '0660819660001', 1, NULL, NULL, NULL, NULL, 'GUANO', NULL, '2013-10-01 17:50:41'),
('4XATH76A0D4317667', '0660819660001', 1, NULL, NULL, NULL, NULL, 'CHUNCHI', NULL, '2013-10-01 17:50:41'),
('4XATH76A0D4317684', '0560022430001', 1, NULL, NULL, NULL, NULL, 'LA ESPERANZA-TIN', NULL, '2013-10-01 18:13:27'),
('4XATH76A1D2290751', '0660819660001', 1, NULL, NULL, NULL, NULL, 'COLTA', NULL, '2013-10-01 17:50:41'),
('4XATH76A1D2290779', '0660819660001', 1, NULL, NULL, NULL, NULL, 'GUANO', NULL, '2013-10-01 17:50:41'),
('4XATH76A2D4315550', '0360015690001', 1, NULL, NULL, NULL, NULL, 'CAÑAR', NULL, '2013-10-01 18:00:55'),
('4XATH76A2D4315598', '0360015690001', 1, NULL, NULL, NULL, NULL, 'CAÑAR', NULL, '2013-10-01 18:00:55'),
('4XATH76A2D4317640', '0660819660001', 1, NULL, NULL, NULL, NULL, 'COLTA', NULL, '2013-10-01 17:50:41'),
('4XATH76A2D4317668', '0660819660001', 1, NULL, NULL, NULL, NULL, 'COLTA', NULL, '2013-10-01 17:50:41'),
('4XATH76A3D2290749', '0660819660001', 1, NULL, NULL, NULL, NULL, 'GUANO', NULL, '2013-10-01 17:50:41'),
('4XATH76A3D2290816', '1865012760001', 1, NULL, NULL, NULL, NULL, 'PELILEO', NULL, '2013-10-01 18:32:30'),
('4XATH76A4D2290713', '0560022430001', 1, NULL, NULL, NULL, NULL, 'PUJILI - LA VICTORIA', NULL, '2013-10-01 18:13:27'),
('4XATH76A4D2290761', '0560022430001', 1, NULL, NULL, NULL, NULL, 'LA MANA', NULL, '2013-10-01 18:13:27'),
('4XATH76A4D2290775', '1865012760001', 1, NULL, NULL, NULL, NULL, 'CEVALLOS', NULL, '2013-10-01 18:32:30'),
('4XATH76A4D2290792', '0660819660001', 1, NULL, NULL, NULL, NULL, 'CHUNCHI', NULL, '2013-10-01 17:50:42'),
('4XATH76A4D2290808', '0660819660001', 1, NULL, NULL, NULL, NULL, 'COLTA', NULL, '2013-10-01 17:50:41'),
('4XATH76A4D2290825', '0660819660001', 1, NULL, NULL, NULL, NULL, 'ALAUSI', NULL, '2013-10-01 17:50:41'),
('4XATH76A4D2291120', '0660819660001', 1, NULL, NULL, NULL, NULL, 'GUANO', NULL, '2013-10-01 17:50:41'),
('4XATH76A5D2291045', '1865012760001', 1, NULL, NULL, NULL, NULL, 'PELILEO', NULL, '2013-10-01 18:32:30'),
('4XATH76A5D2292065', '0560022430001', 1, NULL, NULL, NULL, NULL, 'CANCHAGUA', NULL, '2013-10-01 18:13:27'),
('4XATH76A5D2293216', '0660819660001', 1, NULL, NULL, NULL, NULL, 'RIOBAMBA', NULL, '2013-10-01 17:50:41'),
('4XATH76A5D4315591', '0360015690001', 1, NULL, NULL, NULL, NULL, 'LA TRONCAL', NULL, '2013-10-01 18:00:55'),
('4XATH76A5D4317678', '0660819660001', 1, NULL, NULL, NULL, NULL, 'RIOBAMBA', NULL, '2013-10-01 17:50:41'),
('4XATH76A6D2290745', '0660819660001', 1, NULL, NULL, NULL, NULL, 'COLTA', NULL, '2013-10-01 17:50:41'),
('4XATH76A6D2290759', '0660819660001', 1, NULL, NULL, NULL, NULL, 'ALAUSI', NULL, '2013-10-01 17:50:41'),
('4XATH76A6D2291121', '1865012760001', 1, 'RANGER 800', NULL, '2013-10-01 00:00:00', 'ING. JOSÉ VALENCIA TAMAYO', 'Ambato', NULL, '2013-10-01 20:13:36'),
('4XATH76A6D2293208', '0660819660001', 1, NULL, NULL, NULL, NULL, 'RIOBAMBA', NULL, '2013-10-01 17:50:41'),
('4XATH76A6D4317687', '0560022430001', 1, NULL, NULL, NULL, NULL, 'TANICUCHI', NULL, '2013-10-01 18:13:27'),
('4XATH76A7D2290771', '0560022430001', 1, NULL, NULL, NULL, NULL, 'MOROSPUNGO', NULL, '2013-10-01 18:13:27'),
('4XATH76A7D2290818', '0560022430001', 1, NULL, NULL, NULL, NULL, 'LA MANA', NULL, '2013-10-01 18:13:27'),
('4XATH76A7D2291063', '0560022430001', 1, NULL, NULL, NULL, NULL, 'LASSO (TCS)', NULL, '2013-10-01 18:13:27'),
('4XATH76A7D4315575', '0360015690001', 1, NULL, NULL, NULL, NULL, 'LA TRONCAL', NULL, '2013-10-01 18:00:55'),
('4XATH76A7D4315592', '0360015690001', 1, NULL, NULL, NULL, NULL, 'CAÑAR', NULL, '2013-10-01 18:00:55'),
('4XATH76A7D4317665', '0660819660001', 1, NULL, NULL, NULL, NULL, 'ALAUSI', NULL, '2013-10-01 17:50:41'),
('4XATH76A8D2290763', '0560022430001', 1, NULL, NULL, NULL, NULL, 'EL CORAZON', NULL, '2013-10-01 18:13:27'),
('4XATH76A8D2290777', '1865012760001', 1, NULL, NULL, NULL, NULL, 'PILLARO', NULL, '2013-10-01 18:32:30'),
('4XATH76A8D2290794', '0560022430001', 1, NULL, NULL, NULL, NULL, 'EL CORAZON', NULL, '2013-10-01 18:13:27'),
('4XATH76A8D2290830', '1865012760001', 1, NULL, NULL, NULL, NULL, 'PELILEO', NULL, '2013-10-01 18:32:30'),
('4XATH76A9D2290755', '1865012760001', 1, NULL, NULL, NULL, NULL, 'PILAHUIN', NULL, '2013-10-01 18:32:30'),
('4XATH76A9D2291033', '1865012760001', 1, NULL, NULL, NULL, NULL, 'PILLARO', NULL, '2013-10-01 18:32:30'),
('4XATH76A9D2291114', '0660819660001', 1, NULL, NULL, NULL, NULL, 'ALAUSI', NULL, '2013-10-01 17:50:41'),
('4XATH76A9D2293199', '0660819660001', 1, NULL, NULL, NULL, NULL, 'GUANO', NULL, '2013-10-01 17:50:41'),
('4XATH76A9D2293204', '1865012760001', 1, NULL, NULL, NULL, NULL, 'YANAYACU', NULL, '2013-10-01 18:32:30'),
('4XATH76A9D4315562', '0360015690001', 1, NULL, NULL, NULL, NULL, 'CAÑAR', NULL, '2013-10-01 18:00:55'),
('4XATH76AXD2290828', '1865012760001', 1, NULL, NULL, NULL, NULL, 'QUINCHICOTO', NULL, '2013-10-01 18:32:30'),
('4XATH76AXD2291073', '0560022430001', 1, NULL, NULL, NULL, NULL, 'LATACUNGA', NULL, '2013-10-01 18:13:27');

--
-- Volcado de datos para la tabla `inspeccion`
--

INSERT INTO `inspeccion` (`id_inspeccion`, `id_vehiculo`, `id_tecnico`, `id_contacto`, `fecha`, `ubicacion`, `detalle`, `contacto`, `registro`) VALUES
(1, '4XATH76A0D2293222', '1711938025', 1, '2013-08-27 00:00:00', 'Latacunga', 'Informe Inspección Vehículo\r\n\r\n\r\nLatacunga, 27 de Agosto del 2013\r\n\r\n\r\nSe procede a la inspección del vehículo con VIN 4XATH76A0D2293222 mismo que presenta lo siguiente:\r\n\r\n•	Muestra un golpe en la parte delantera derecha producido por un impacto, mismo que rompe el guarda fangos derecho, y una pequeña parte del guarda choques, el golpe afectó la posición del faro.\r\n  \r\n•	Tiene el parabrisas roto.\r\n \r\n•	Se revisa el sistema de aceleración, niveles de fluidos y el sistema eléctrico mismos que no presentan ninguna novedad.\r\n•	Motor funcionando correctamente.\r\n\r\n\r\n\r\nAtentamente:\r\n\r\n\r\n\r\nGalo Sinchiguano\r\n\r\n\r\n\r\n\r\n\r\n', NULL, '2013-10-01 20:06:54'),
(2, '4XATH76A4D2290761', '0803550466', 1, '2013-09-19 00:00:00', 'Cotopaxi, la Mana', '\r\nInforme Inspección Vehículo\r\n\r\nCotopaxi, La Mana, 19 de Septiembre de 2013\r\n\r\nSe procede con la inspección del vehículo con número de VIN  4XATH76A4D2290761,  a cargo del Ing. Henry Peñaherrera, mismo que presenta un golpe en la parte frontal derecha producto del golpe presenta el guarda choque doblado hacia dentro, se realiza una inspección completa de acuerdo al siguiente detalle:\r\n\r\nInspección	Observaciones\r\nCarrocería	Tiene roto el guarda fango derecho\r\nPuertas	Funcionando correctamente.\r\nCajón abatible	Funcionando correctamente\r\nEstructura Cabina	No presenta golpes\r\nTerminales Suspensión	Funcionando correctamente.\r\nAmortiguadores	Funcionando correctamente.\r\nTerminales de dirección	Funcionando correctamente.\r\nBrazos de Suspensión	Funcionando correctamente.\r\nGuardachoque	Presenta doblamiento en la parte izquierda.\r\nBatería	Funcionando correctamente\r\nCableado eléctrico	Funcionando correctamente..\r\nLimpia-brizas	Funcionando correctamente.\r\nCaja engranaje delantera	Funcionando correctamente.\r\nCajas engranaje posterior	Funcionando correctamente.\r\nAceite Motor	Cambiado\r\nAceite Caja Posterior	Cambiado\r\nAceite Caja Delantera	Cambiado\r\nLiquido de Frenos	Llenado completo\r\nRefrigerante	Cambiado\r\nÁcido batería	Funcionando perfectamente\r\nFiltro aire	Funcionando correctamente\r\nFiltro Aceite	Cambiado\r\nImágenes vehículo:\r\n\r\n\r\n\r\n\r\n\r\nObservaciones:\r\n•	Presenta doblamiento en la parte izquierda del guarda choque.\r\n•	Presentar rotura en la parte superior izquierda de la mascarilla.\r\n•	Se derramo el líquido de freno en un 70% a 80% estimado quedándose con el porcentaje mínimo de liquido para ser frenado.\r\n\r\n\r\nNota: Se realiza el mantenimiento completo del vehículo.\r\n\r\n\r\nResponsabe zonal: Ing. Xavier Moya (03-2812 986), Dirección Provincial Agropecuaria de Cotopaxi Latacunga Av Atahualpa y zamora\r\n\r\n\r\n\r\n\r\n\r\nAtentamente:\r\n\r\n\r\n\r\nTec. Eduardo Villota\r\nCI: 172291972-5\r\n\r\n\r\n', NULL, '2013-10-01 20:06:54'),
(3, '4XATH76AXD2290828', '1711938025', 1, '2013-09-18 00:00:00', 'Tunguragua, Quinchicoto', 'Informe Inspección Vehículo\r\nTungurahua, Quinchicoto 18 de septiembre del 2013\r\nEn la zona de Quinchicoto provincia de Tungurahua se procede con la inspección del vehículo con VIN  4XATH76AXD220828 a cargo del Ing. Luis Soliz, este vehículo presenta un sonido en la caja de cambios posterior, el sonido se produce, en el momento que se cambia de marcha, cuando inicia el recorrido,se realiza una inspección completa de acuerdo al siguiente detalle:\r\nInspección	Observaciones\r\nCarrocería	Funcionando correctamente.\r\nPuertas	Funcionando correctamente.\r\nCajón abatible	Funcionando correctamente\r\nEstructura Cabina	Funcionando correctamente.\r\nTerminales Suspensión	Funcionando correctamente.\r\nAmortiguadores	Funcionando correctamente.\r\nTerminales de dirección	Funcionando correctamente.\r\nBrazos de Suspensión	Funcionando correctamente.\r\nGuardachoque	Funcionando correctamente.\r\nBatería	Funcionando correctamente\r\nCableado eléctrico	Funcionando correctamente..\r\nLimpia-brizas	Funcionando correctamente.\r\nCaja engranaje delantera	Funcionando correctamente.\r\nCajas engranaje posterior	Funcionando correctamente.\r\nAceite Motor	Completo\r\nAceite Caja Posterior	Completo\r\nAceite Caja Delantera	Completo\r\nLiquido de Frenos	Completo\r\nRefrigerante	Completo\r\nÁcido batería	Funcionando perfectamente\r\nFiltro aire	Funcionando correctamente\r\nFiltro Aceite	Completo\r\nNotas: Se realizó el chequeo respectivo  del vehículo , analizando las siguiente , piezas  que verificó , las cruceta , los ejes trasero , o algún tornillo flojos , estas piezas estaban bien, y el sonido seguía  presente en el vehículo\r\nEl vehículo apenas cumple 6 horas de trabajo motivo por el cual no se puede hacer el cambio de aceites respectivos.\r\nEl encargado zonal solicita de manera cordial se realice el traslado a Quito inmediatamente para el arreglo del vehículo.\r\nConclusión:  Desarmar la caja de cambio para revisar los engranajes.\r\nResponsable Zonal: Dr. Jorge Cifuentes Carrión  (03-2827383) Dirección Provincial Agropecuaria del Tungurahua Av. 12 de noviembre cc. Ambato Bloque No.2 Segundo Piso.\r\nAtentamente:\r\n\r\nEduardo Villota\r\n172291972-5\r\n', 'Dr. Jorge Cifuentes Carrión  (03-2827383)', '2013-10-01 20:10:03'),
(4, '4XATH76A6D2291121', '0803550466', 1, '2013-08-01 00:00:00', 'Ambato', '\r\nInforme Vehículo Polaris Volcado\r\n\r\n\r\nAmbato, 01 de Agosto del 2013\r\n\r\n\r\nEl vehículo Polaris con numero de VIN 4XATH76A6D2291121 sufrió un volcamiento por la parte delantera izquierda, resultado de una posible perdida de pista, presenta un golpe en la parte superior izquierda del parabrisas provocando la ruptura del vidrio, la cabina se encuentra desviada hacia atrás en la dirección del golpe aproximadamente 3cm.\r\n\r\nGráfico del golpe visto desde la parte frontal de la cabina\r\n\r\n\r\nSe realizó un chequeo completo de los sistemas, encontrando las siguientes novedades:\r\n\r\nInspección	Observaciones\r\nCarrocería	Presenta golpes en el lugar del impacto, pero no presenta ningún daño\r\nPuertas	Funcionando correctamente.\r\nCajón abatible	Funcionando, presenta una torcedura en el mango derecho\r\nEstructura Cabina	Presenta una desviación en dirección al golpe de unos 3cm\r\nTerminales Suspensión	Funcionando correctamente.\r\nAmortiguadores	Funcionando correctamente.\r\nTerminales de dirección	Funcionando correctamente.\r\nBrazos de Suspensión	Funcionando correctamente.\r\nWincha	Funcionando correctamente.\r\nBatería	Funcionando correctamente, presenta un baja en la carga por perdida de ácido.\r\nCableado eléctrico	Funcionando correctamente.\r\nLimpia-brizas	Funcionando correctamente.\r\nCaja engranaje delantera	Funcionando correctamente.\r\nCajas engranaje posterior	Funcionando correctamente.\r\nAceite Motor	Cambiar\r\nAceite Caja Posterior	Correcto\r\nAceite Caja Delantera	Correcto\r\nLiquido de Frenos	Vacío\r\nRefrigerante	Vacío\r\nÁcido batería	Por completar\r\nFiltro aire	Cambiar, se encuentra cubierto de aceite\r\nFiltro Aceite	Cambiar\r\n\r\n\r\nObservaciones Adicionales:\r\n\r\n1.	El aceite del motor se derramó en un 30% a 40 % encontrándose principalmente en los ductos de entrada de aire al motor.\r\n2.	Se chequea la alineación de las llantas sin encontrar ninguna novedad.\r\n\r\n\r\nResponsable Zonal: Dr. Jorge Cifuentes Carrión  (03-2827383) Dirección Provincial Agropecuaria del Tungurahua Av. 12 de noviembre cc. Ambato Bloque No.2 Segundo Piso.\r\n\r\nAtentamente:\r\n\r\n\r\n\r\n\r\nTec. Eduardo Villota\r\nCI: 172291972-5\r\n', 'Responsable Zonal: Dr. Jorge Cifuentes Carrión  (03-2827383', '2013-10-01 20:15:09');

--
-- Volcado de datos para la tabla `inventario`
--

INSERT INTO `inventario` (`id_inventario`, `fecha`, `nombre`, `descpricion`, `unidad`, `stok_min`, `marca`, `ubicacion`, `registro`) VALUES
(1000, '2013-10-01 00:00:00', 'PS4', 'Aceite sintético para motor Polaris', 'Litros', 12, 'Polaris PS4', 'Bodega Oficina ', '2013-10-01 18:54:38'),
(1001, '0000-00-00 00:00:00', 'AGL Plus', 'Aceite de transmisión trasera', 'Litros', 12, 'Polaris AGL Plus', 'Bodega Oficina', '2013-10-01 18:56:03'),
(1002, '2013-10-01 00:00:00', 'Demand Fluid', 'Aceite para la caja delantera', 'Litros ', 5, 'Polaris Demend Fluid', 'Bodega Oficina', '2013-10-01 19:13:27'),
(1003, '2013-10-01 00:00:00', 'Filtro Aceite', 'Filtro de Aceite', 'Unidades', 12, 'Champion PH2867', 'Bodega Oficina ', '2013-10-01 19:13:27'),
(1004, '2013-10-01 00:00:00', 'Refrigerante', 'Liquito de refrigerante', 'Litros', 12, 'Lubristom', 'Bodega Oficina', '2013-10-01 19:13:27'),
(1005, '2013-10-01 00:00:00', 'Líquido de Frenos', 'Liquito de Frenos', 'Litros', 12, 'Wagner ', 'Bodega Oficina', '2013-10-01 19:13:27'),
(1006, '2013-10-01 00:00:00', 'Grasa', 'Grasa para engramajes', 'Unidades', 12, 'Abro', 'Bodega Oficina', '2013-10-01 19:16:03'),
(1007, '2013-10-01 00:00:00', 'Volante', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:28'),
(1008, '2013-10-01 00:00:00', 'Suspensión Delantera', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:28'),
(1009, '2013-10-01 00:00:00', 'Suspensión  Trasera', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:28'),
(1010, '2013-10-01 00:00:00', 'Llantas', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:28'),
(1011, '2013-10-01 00:00:00', 'Nivel de fluido de frenos', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:28'),
(1012, '2013-10-01 00:00:00', 'Cable de pedal de freno', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:28'),
(1013, '2013-10-01 00:00:00', 'Sistema de frenos', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:28'),
(1014, '2013-10-01 00:00:00', 'Tuercas de rueda 35 lb', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:28'),
(1015, '2013-10-01 00:00:00', 'Turca de marco', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:28'),
(1016, '2013-10-01 00:00:00', 'Filtro de aire de filtro', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:28'),
(1017, '2013-10-01 00:00:00', 'Filtro Aceite', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:28'),
(1018, '2013-10-01 00:00:00', 'Caja del tubo sedimentos aire', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:28'),
(1019, '2013-10-01 00:00:00', 'Filtro de aire elemento principal', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:28'),
(1020, '2013-10-01 00:00:00', 'Refrigerante (si procede )', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:29'),
(1021, '2013-10-01 00:00:00', 'Líquido refrigerante', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:29'),
(1022, '2013-10-01 00:00:00', 'Lámpara de faro/de la cola', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:29'),
(1023, '2013-10-01 00:00:00', 'Desgastes de los frenos', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:29'),
(1024, '2013-10-01 00:00:00', 'Batería', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:29'),
(1025, '2013-10-01 00:00:00', 'Liquido de batería', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:29'),
(1026, '2013-10-01 00:00:00', 'Cambio de aceite del motor', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:29'),
(1027, '2013-10-01 00:00:00', 'Aceite de la caja delantera', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:29'),
(1028, '2013-10-01 00:00:00', 'Aceite de la transmisión', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:29'),
(1029, '2013-10-01 00:00:00', 'Tensión del cable de freno de parqueo', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:29'),
(1030, '2013-10-01 00:00:00', 'Juntas', 'Revicion', 'Unidad', 0, 'Polaris', 'Servicio', '2013-10-01 19:48:29');

--
-- Volcado de datos para la tabla `mantenimiento`
--

INSERT INTO `mantenimiento` (`id_manteminiento`, `id_vehiculo`, `id_tecnico`, `periodo`, `ubicacion`, `fecha`, `kilometros`, `observacion`, `registro`) VALUES
(2, '4XATH76A2D4315550', '0803550466', 50, 'Cañar', '2013-07-22 00:00:00', '0', NULL, '2013-10-01 20:23:41'),
(3, '4XATH76A9D4315562', '1711938025', 50, 'Cañar', '2013-07-22 00:00:00', '0', NULL, '2013-10-01 20:25:07'),
(4, '4XATH76A7D4315592', '0803550466', 50, 'Cañar', '2013-07-22 00:00:00', '0', NULL, '2013-10-01 20:26:00'),
(5, '4XATH76A2D4315598', '1711938025', 50, 'Cañar', '2013-07-22 00:00:00', '0', NULL, '2013-10-01 20:26:33'),
(6, '4XATH76A5D4315591', '1711938025', 50, 'Troncal', '2013-07-23 00:00:00', '0', 'Se remplaza la abrazadera del eje trasero', '2013-10-01 20:27:58'),
(7, '4XATH76A7D4315575', '1711938025', 50, 'La Troncal', '2013-07-23 00:00:00', '0', NULL, '2013-10-01 20:29:27'),
(8, '4XATH76A4D2290713', '0803550466', 62, 'Pijuli La Victoria', '2013-08-09 00:00:00', '0', NULL, '2013-10-01 21:37:29'),
(9, '4XATH762AD4317220', '1711938025', 50, 'Guangaje', '2013-08-09 00:00:00', '0', NULL, '2013-10-01 20:38:01'),
(10, '4XATH76A5D2293216', '1711938025', 30, 'Riobamba', '2013-08-21 00:00:00', '0', 'Se ajustado los dos tornillo de parte arriba del desfogue  del motor\r\n', '2013-10-01 21:37:57'),
(11, '4XATH76A5D4317678', '0803550466', 50, 'Riobamba', '2013-10-21 00:00:00', '0', 'Se ajustado los dos tornillo de parte arriba del desfogue  del motor\r\n', '2013-10-01 20:40:59'),
(12, '4XATH76A1D2290779', '1711938025', 50, 'Guano', '2013-08-21 00:00:00', '0', 'A este  vehículo le  adatado los siguientes   objetos. Pitos  retrovisores (delanteros y traseros) guías traseras  neblineros delanteros.\r\n', '2013-10-01 20:41:42'),
(13, '4XATH76A9D2293199', '0803550466', 50, 'Guano', '2013-08-21 00:00:00', '0', NULL, '2013-10-01 20:42:31'),
(14, '4XATH76A0D2293253', '1711938025', 50, 'Guano', '2013-08-21 00:00:00', '0', NULL, '2013-10-01 20:43:57'),
(15, '4XATH76A4D2291120', '1711938025', 50, 'Guano', '2013-08-21 00:00:00', '0', 'A este  vehículo le  adatado los siguientes   objetos. Pitos  retrovisores (delanteros y traseros) guías traseras  neblineros delanteros\r\n', '2013-10-01 20:44:35'),
(16, '4XATH76A3D2290749', '0803550466', 50, 'Guano', '2013-08-21 00:00:00', '0', 'A este  vehículo le  adatado los siguientes   objetos. Pitos  retrovisores (delanteros y traseros) guías traseras  neblineros delanteros\r\n', '2013-10-01 20:45:20'),
(17, '4XATH76A2D4317668', '0803550466', 50, 'Colta', '2013-08-22 00:00:00', '0', NULL, '2013-10-01 20:45:52'),
(18, '4XATH76A6D2290745', '1711938025', 50, 'Colta', '2013-08-22 00:00:00', '0', NULL, '2013-10-01 20:46:25'),
(19, '4XATH76A4D2290808', '1711938025', 50, 'Colta', '2013-08-22 00:00:00', '0', NULL, '2013-10-01 20:46:53'),
(20, '4XATH76A1D2290751', '0803550466', 50, 'Colta', '2013-08-22 00:00:00', '0', NULL, '2013-10-01 20:47:31'),
(21, '4XATH76A2D4317640', '0803550466', 50, 'Colta', '2013-08-22 00:00:00', '0', NULL, '2013-10-01 20:48:04'),
(22, '4XATH76A7D4317665', '0803550466', 23, 'Alausi', '2013-08-22 00:00:00', '0', 'Solo se realizó los chuequeo respectivos  del vehículos  .No se realizó el cambio de aceite\r\n', '2013-10-01 20:55:44'),
(23, '4XATH76A4D2290825', '1711938025', 50, 'Alausi', '2013-08-22 00:00:00', '0', 'A este  vehículo le  adatado los siguientes   objetos. Pitos  retrovisores (delanteros y traseros) guías traseras  neblineros delanteros .\r\n', '2013-10-01 20:50:07'),
(24, '4XATH76A6D2290759', '0803550466', 50, 'Alausi', '2013-08-22 00:00:00', '0', 'A este  vehículo le  adatado los siguientes   objetos. Pitos  retrovisores (delanteros y traseros) guías traseras  neblineros delanteros .\r\n', '2013-10-01 20:50:46'),
(25, '4XATH76A9D2291114', '1711938025', 50, 'Alausi', '2013-08-22 00:00:00', '0', 'A este  vehículo le  adatado los siguientes   objetos. Pitos  retrovisores (delanteros y traseros) guías traseras  neblineros delanteros .\r\n', '2013-10-01 20:51:29'),
(26, '4XATH76A0D4317667', '0803550466', 50, 'Chunchi', '2013-08-23 00:00:00', '0', NULL, '2013-10-01 20:52:02'),
(27, '4XATH76A4D2290792', '1711938025', 23, 'Chunchi', '2013-08-23 00:00:00', '0', 'el vehículo tiene instalado retrovisores,        \r\npito, guías traseras y neblineros delanteros, adicional esta roto          \r\ncaucho eje trasero, se arregla el caucho.\r\n', '2013-10-01 20:55:05'),
(28, '4XATH76A7D2291063', '0803550466', 57, 'Lazo', '2013-08-23 00:00:00', '0', NULL, '2013-10-01 20:56:40'),
(29, '4XATH76A0D2293205', '0803550466', 51, 'Sigchos', '2013-08-26 00:00:00', '0', 'Se le completo el Líquido de freno , líquido  refrigerante  , tuerca  trasera dañada.\r\n', '2013-10-01 20:58:01'),
(30, '4XATH76AXD2291073', '0803550466', 52, 'Latacunga', '2013-08-27 00:00:00', '0', 'El vehículo  tiene  cambiado   dos  tuercas, de  la rueda trasera, y la válvula  de la rueda.\r\n', '2013-10-01 20:58:59'),
(31, '4XATH76A0D2293222', '1711938025', 36, 'Pijuli', '2013-08-27 00:00:00', '0', 'No se iso mantenimiento. Este   vehículo  se le reviso  el sistema  de aceleración y comprobamos los  niveles de líquidos, aceite, freno y refrigerante.\r\n', '2013-10-01 21:00:16'),
(32, '4XATH76A6D4317687', '1711938025', 60, 'Tanicuchi', '2013-09-10 00:00:00', '900.6', 'Mantenimiento completo, El aro de la rueda derecha se encuentra doblada un poco en parte de abajo. Y se ajustó el tornillo del desfogue del motor.\r\n', '2013-10-01 21:13:38'),
(33, '4XATH76A5D2292065', '0803550466', 61, 'Canchagua', '2013-09-10 00:00:00', '1232', 'Mantenimiento completo, El filtro tenía mucho polvo\r\n', '2013-10-01 21:14:33'),
(34, '4XATH76A0D4317684', '0803550466', 52, 'La Esperanza', '2013-09-10 00:00:00', '998.8', 'Mantenimiento completo, Tenía cortados los cables que conectan con los sensores, del aceite, temperatura. \r\n', '2013-10-01 21:14:49'),
(35, '4XATH76A9D2291033', '1711938025', 40, 'Pillaro', '2013-09-17 00:00:00', '786.4', NULL, '2013-10-01 21:15:09'),
(36, '4XATH76A8D2290777', '0803550466', 51, 'Pillaro', '2013-09-17 00:00:00', '988', NULL, '2013-10-01 21:15:25'),
(37, '4XATH76A0D2290773', '0803550466', 47, 'Pillaro', '2013-09-17 00:00:00', '794.2', NULL, '2013-10-01 21:15:35'),
(38, '4XATH76A8D2290830', '1711938025', 50, 'Pelileo', '2013-09-18 00:00:00', '670', 'Tiene retro visores delanteros, y se recalendo el motor , sin liquido de refrigerante.\r\n', '2013-10-01 21:15:48'),
(39, '4XATH76A5D2291045', '0803550466', 40, 'Pelileo', '2013-09-18 00:00:00', '440', NULL, '2013-10-01 21:15:58'),
(40, '4XATH76A3D2290816', '1711938025', 50, 'Pelileo', '2013-09-18 00:00:00', '1055', 'En la parte izquierda le falta el plastico de la puerta .\r\n', '2013-10-01 21:16:08'),
(41, '4XATH76A9D2290755', '1711938025', 52, 'Pilaguin', '2013-09-18 00:00:00', '1018.1', NULL, '2013-10-01 21:09:10'),
(43, '4XATH76A9D2293204', '1711938025', 50, 'Yanayacu', '2013-09-18 00:00:00', '936.6', NULL, '2013-10-01 21:17:19'),
(44, '4XATH76A0D2290790', '1711938025', 52, 'Quisapincha', '2013-09-18 00:00:00', '662.8', NULL, '2013-10-01 21:18:02'),
(45, '4XATH76A4D2290775', '1711938025', 50, 'Cevallos', '2013-09-18 00:00:00', '657.6', NULL, '2013-10-01 21:18:51'),
(46, '4XATH76AXD2290828', '0803550466', 6, 'Quinchicoto', '2013-09-18 00:00:00', '76', 'tiene un sonido  en parte trasera del vehiculo, cuando el vehiculo se pone en marcha.\r\n', '2013-10-01 21:20:01'),
(47, '4XATH76A4D2290761', '0803550466', 54, 'La Mana', '2013-09-19 00:00:00', '2151', 'Tiene doblado el guarda choque delantero y  dañado la caroseria del vehiculo.\r\n', '2013-10-01 21:21:19'),
(48, '4XATH76A7D2290818', '1711938025', 59, 'La Mana', '2013-09-19 00:00:00', '1530', 'Se arreglo la puerta izquierda porque estaba dura para abrir.\r\n', '2013-10-01 21:22:50'),
(49, '4XATH76A7D2290771', '1711938025', 67, 'Moraspungo', '2013-09-20 00:00:00', '1912', NULL, '2013-10-01 21:28:45'),
(50, '4XATH76A0D2291101', '1711938025', 40, 'El Corazon', '2013-09-20 00:00:00', '655', 'Cuando se enciende el vehiculo las luces trasera se quedan encenditas y no se apagan \r\n', '2013-10-01 21:31:37'),
(51, '4XATH76A8D2290794', '1711938025', 47, 'El Corazon', '2013-09-20 00:00:00', '715', 'Se le coloco el aceite que se envio al la ING.  Para complentar  los 2 lts del motor .\r\n', '2013-10-01 21:32:50'),
(52, '4XATH76A0D2290773', '0803550466', 58, 'El Corazon', '2013-09-20 00:00:00', '977', 'Se le ajusto el tormillo del desfloque del motor.\r\n', '2013-10-01 21:34:35'),
(53, '4XATH76A6D2293208', '0803550466', 45, 'Chimborazo', '2013-08-21 00:00:00', '0', NULL, '2013-10-01 21:43:20');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
