-- --------------------------------------------------------
-- Host:                         localhost
-- Versión del servidor:         10.5.8-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para acortador
CREATE DATABASE IF NOT EXISTS `acortador` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `acortador`;

-- Volcando estructura para tabla acortador.url
CREATE TABLE IF NOT EXISTS `url` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `usuarios_id` int(10) unsigned DEFAULT NULL,
  `url_original` varchar(250) NOT NULL,
  `url_corta` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `url_corta` (`url_corta`),
  KEY `FK_url_usuarios` (`usuarios_id`),
  CONSTRAINT `FK_url_usuarios` FOREIGN KEY (`usuarios_id`) REFERENCES `usuarios` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=153 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla acortador.url: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `url` DISABLE KEYS */;
INSERT INTO `url` (`id`, `usuarios_id`, `url_original`, `url_corta`) VALUES
	(149, 12, 'https://github.com/URBANOIDE/Flask_Acortador', 'th2y'),
	(150, NULL, 'https://web.whatsapp.com/', 'xo8k'),
	(151, 13, 'https://web.whatsapp.com/', 'hxxf'),
	(152, NULL, 'https://drive.google.com/file/d/1YShWUQWF-suLU6WPXV6m0cCjQYdiA5Kc/view', '108q');
/*!40000 ALTER TABLE `url` ENABLE KEYS */;

-- Volcando estructura para tabla acortador.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `password` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla acortador.usuarios: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` (`id`, `nombre`, `email`, `password`) VALUES
	(12, 'Albeiro', 'Albertochind04@gmail.com', '1273'),
	(13, 'Prueba', 'yuneidysoto@gmail.com', '1273');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
