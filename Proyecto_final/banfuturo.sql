-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-08-2024 a las 03:50:08
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `banfuturo`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administradores`
--

CREATE TABLE `administradores` (
  `id` int(16) NOT NULL,
  `nombres` text DEFAULT NULL,
  `apellido_paterno` text DEFAULT NULL,
  `apellido_materno` text DEFAULT NULL,
  `rfc` text DEFAULT NULL,
  `pin` varchar(4) DEFAULT NULL,
  `salario` float DEFAULT NULL,
  `puesto` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `administradores`
--

INSERT INTO `administradores` (`id`, `nombres`, `apellido_paterno`, `apellido_materno`, `rfc`, `pin`, `salario`, `puesto`) VALUES
(1029384756, 'Alberto', 'González', 'Alcántar', 'GOAA980706TR5', '9876', 25000, 'Gerente'),
(1234567890, 'Jose', 'Valles', 'Chave', 'UVACJ980907TK2', '1234', 20000, 'Jefe'),
(2147483647, 'Jaqueline', 'Gutierrez', 'Lopez', 'GULJ780502RO2', '1234', 50000, 'Jefe');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id_clientes` int(20) NOT NULL,
  `pin` varchar(4) DEFAULT NULL,
  `nombres` text DEFAULT NULL,
  `apellido_paterno` text DEFAULT NULL,
  `apellido_materno` text DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `rfc` varchar(40) DEFAULT NULL,
  `regimen` varchar(255) DEFAULT NULL,
  `calle` varchar(255) DEFAULT NULL,
  `numero` varchar(10) DEFAULT NULL,
  `colonia` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id_clientes`, `pin`, `nombres`, `apellido_paterno`, `apellido_materno`, `fecha_nacimiento`, `rfc`, `regimen`, `calle`, `numero`, `colonia`) VALUES
(415231361, '1234', 'Sebastian', 'Martínez', 'Gurrola', '1993-09-03', 'MAGS930903FD9', 'Sueldos', 'Dolores del Rio', '108', 'Cienega'),
(415231362, '1234', 'Martha', 'Flores', 'Barraza', '1968-05-02', 'FLBM680205FG9', 'Sueldos', 'Las Juntas', '110', 'Rancho San Miguel'),
(415231363, '1234', 'David', 'Saldivar', 'Ortega', '2001-08-21', 'SAOD010821TR5', 'RIF', 'Urano', '106', 'Vallesol'),
(415231364, '1234', 'Carlos', 'Garcia', 'Flores', '1993-11-11', 'GAFC931111UY8', 'Sueldos', 'Gomez Palacio', '21', 'Centro');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `credito`
--

CREATE TABLE `credito` (
  `id_credito` int(16) NOT NULL,
  `saldo_aprobado` int(11) DEFAULT NULL,
  `saldo_pendientes` int(11) DEFAULT NULL,
  `id_cuenta` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `credito`
--

INSERT INTO `credito` (`id_credito`, `saldo_aprobado`, `saldo_pendientes`, `id_cuenta`) VALUES
(44444, 28000, 1000, 415231362),
(66666, 22000, 0, 415231363);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `debito`
--

CREATE TABLE `debito` (
  `id_debito` int(16) NOT NULL,
  `saldo_debito` int(11) DEFAULT NULL,
  `id_cuenta` int(16) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `debito`
--

INSERT INTO `debito` (`id_debito`, `saldo_debito`, `id_cuenta`) VALUES
(33333, 700, 415231362),
(55555, 100, 415231363);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `movimiento_credito`
--

CREATE TABLE `movimiento_credito` (
  `id_movimiento_c` int(16) NOT NULL,
  `n_movimiento` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `tipo` varchar(100) DEFAULT NULL,
  `monto` int(11) DEFAULT NULL,
  `descripcion` varchar(800) DEFAULT NULL,
  `saldo_final` int(11) DEFAULT NULL,
  `id_credito` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `movimiento_credito`
--

INSERT INTO `movimiento_credito` (`id_movimiento_c`, `n_movimiento`, `fecha`, `tipo`, `monto`, `descripcion`, `saldo_final`, `id_credito`) VALUES
(1, 1, '2024-08-17', 'Retiro', 5000, 'Retiro', 23000, 44444),
(2, 2, '2024-08-17', 'Pago', 4000, 'Pago de tarjeta', 27000, 44444);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `movimiento_debito`
--

CREATE TABLE `movimiento_debito` (
  `id_movimiento_d` int(16) NOT NULL,
  `n_movimiento` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `tipo` varchar(100) DEFAULT NULL,
  `monto` int(11) DEFAULT NULL,
  `descripcion` varchar(800) DEFAULT NULL,
  `saldo_final` int(11) DEFAULT NULL,
  `id_debito` int(16) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `movimiento_debito`
--

INSERT INTO `movimiento_debito` (`id_movimiento_d`, `n_movimiento`, `fecha`, `tipo`, `monto`, `descripcion`, `saldo_final`, `id_debito`) VALUES
(1, 1, '2024-08-17', 'Deposito', 1200, 'Deposito', 1200, 33333),
(2, 2, '2024-08-17', 'Retiro', 400, 'Retiro', 800, 33333),
(3, 3, '2024-08-17', 'Transferencia', 200, 'Pago', 600, 33333),
(4, 1, '2024-08-17', 'Tranferencia', 200, 'Pago', 200, 55555);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `administradores`
--
ALTER TABLE `administradores`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id_clientes`);

--
-- Indices de la tabla `credito`
--
ALTER TABLE `credito`
  ADD PRIMARY KEY (`id_credito`),
  ADD KEY `id_cuenta` (`id_cuenta`);

--
-- Indices de la tabla `debito`
--
ALTER TABLE `debito`
  ADD PRIMARY KEY (`id_debito`),
  ADD KEY `id_cuenta` (`id_cuenta`);

--
-- Indices de la tabla `movimiento_credito`
--
ALTER TABLE `movimiento_credito`
  ADD PRIMARY KEY (`id_movimiento_c`),
  ADD KEY `id_credito` (`id_credito`);

--
-- Indices de la tabla `movimiento_debito`
--
ALTER TABLE `movimiento_debito`
  ADD PRIMARY KEY (`id_movimiento_d`),
  ADD KEY `id_debito` (`id_debito`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `credito`
--
ALTER TABLE `credito`
  ADD CONSTRAINT `credito_ibfk_1` FOREIGN KEY (`id_cuenta`) REFERENCES `clientes` (`id_clientes`);

--
-- Filtros para la tabla `debito`
--
ALTER TABLE `debito`
  ADD CONSTRAINT `debito_ibfk_1` FOREIGN KEY (`id_cuenta`) REFERENCES `clientes` (`id_clientes`);

--
-- Filtros para la tabla `movimiento_credito`
--
ALTER TABLE `movimiento_credito`
  ADD CONSTRAINT `movimiento_credito_ibfk_1` FOREIGN KEY (`id_credito`) REFERENCES `credito` (`id_credito`);

--
-- Filtros para la tabla `movimiento_debito`
--
ALTER TABLE `movimiento_debito`
  ADD CONSTRAINT `movimiento_debito_ibfk_1` FOREIGN KEY (`id_debito`) REFERENCES `debito` (`id_debito`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
