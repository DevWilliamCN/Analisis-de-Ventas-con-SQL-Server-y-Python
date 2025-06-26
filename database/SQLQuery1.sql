
-- Esto tiene que pegarlo en SQL SERVER
-- Usar la base de datos
USE ProyectoVentasSQL;
GO


ALTER TABLE Productos
ADD etiqueta NVARCHAR(50) NULL;

SELECT id_producto, nombre_producto, etiqueta FROM Productos;


-- Eliminar vistas si ya existen
IF OBJECT_ID('vista_productos_mas_vendidos') IS NOT NULL DROP VIEW vista_productos_mas_vendidos;
IF OBJECT_ID('vista_total_compras_por_cliente') IS NOT NULL DROP VIEW vista_total_compras_por_cliente;
IF OBJECT_ID('vista_ventas_por_categoria') IS NOT NULL DROP VIEW vista_ventas_por_categoria;
IF OBJECT_ID('vista_ventas_por_pais') IS NOT NULL DROP VIEW vista_ventas_por_pais;
IF OBJECT_ID('vista_ventas_mensuales') IS NOT NULL DROP VIEW vista_ventas_mensuales;

-- Eliminar tablas si ya existen
IF OBJECT_ID('DetalleVenta') IS NOT NULL DROP TABLE DetalleVenta;
IF OBJECT_ID('Ventas') IS NOT NULL DROP TABLE Ventas;
IF OBJECT_ID('Productos') IS NOT NULL DROP TABLE Productos;
IF OBJECT_ID('Categorias') IS NOT NULL DROP TABLE Categorias;
IF OBJECT_ID('Clientes') IS NOT NULL DROP TABLE Clientes;

-- Crear tablas
CREATE TABLE Clientes (
    id_cliente INT PRIMARY KEY IDENTITY(1,1),
    nombre NVARCHAR(100) NOT NULL,
    correo NVARCHAR(100),
    pais NVARCHAR(50)
);

CREATE TABLE Categorias (
    id_categoria INT PRIMARY KEY IDENTITY(1,1),
    nombre_categoria NVARCHAR(100) NOT NULL
);

CREATE TABLE Productos (
    id_producto INT PRIMARY KEY IDENTITY(1,1),
    nombre_producto NVARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    id_categoria INT NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES Categorias(id_categoria)
);

CREATE TABLE Ventas (
    id_venta INT PRIMARY KEY IDENTITY(1,1),
    id_cliente INT NOT NULL,
    fecha DATE NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);

CREATE TABLE DetalleVenta (
    id_detalle INT PRIMARY KEY IDENTITY(1,1),
    id_venta INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_venta) REFERENCES Ventas(id_venta),
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
);

-- Insertar datos
INSERT INTO Categorias (nombre_categoria) VALUES
('Electr�nica'), ('Ropa'), ('Hogar'), ('Juguetes'), ('Libros'),
('Oficina'), ('Deportes'), ('Accesorios'), ('Tecnolog�a'), ('Mascotas'),
('Automotriz'), ('Salud'), ('Jard�n'), ('Zapatos'), ('Ni�os'),
('Cocina'), ('Videojuegos'), ('Viajes'), ('Fotograf�a'), ('Belleza');



INSERT INTO Productos (nombre_producto, precio, id_categoria) VALUES
('Aud�fonos Bluetooth', 14990.00, 1),
('Camisa Polo', 10990.00, 2),
('Almohada Memory Foam', 19990.00, 3),
('Mu�eca Interactiva', 17990.00, 4),
('Libro "Aprende SQL F�cil"', 8990.00, 5);






INSERT INTO Clientes (nombre, correo, pais) VALUES
('Luis Araya', 'luis.araya@example.com', 'Costa Rica'),
('Mar�a Gonz�lez', 'maria.gonzalez@example.com', 'Costa Rica'),
('Pedro Jim�nez', 'pedro.jimenez@example.com', 'Panam�'),
('Ana Rivera', 'ana.rivera@example.com', 'Nicaragua'),
('Carlos Brenes', 'carlos.brenes@example.com', 'Costa Rica'),
('Laura Vega', 'laura.vega@example.com', 'El Salvador'),
('Jos� M�ndez', 'jose.mendez@example.com', 'Nicaragua'),
('Sof�a Castro', 'sofia.castro@example.com', 'Costa Rica'),
('Andrea S�nchez', 'andrea.sanchez@example.com', 'Honduras'),
('Ricardo Solano', 'ricardo.solano@example.com', 'Panam�'),
('Daniela Campos', 'daniela.campos@example.com', 'Costa Rica'),
('Javier Z��iga', 'javier.zuniga@example.com', 'Guatemala'),
('Natalia Rojas', 'natalia.rojas@example.com', 'El Salvador'),
('Marco Villalobos', 'marco.villalobos@example.com', 'Costa Rica'),
('Fernanda Mora', 'fernanda.mora@example.com', 'Nicaragua'),
('Kevin Navarro', 'kevin.navarro@example.com', 'Honduras'),
('Gabriela Soto', 'gabriela.soto@example.com', 'Guatemala'),
('David Quesada', 'david.quesada@example.com', 'Costa Rica'),
('Michelle Salas', 'michelle.salas@example.com', 'Panam�'),
('Jonathan P�rez', 'jonathan.perez@example.com', 'El Salvador');










-- Cliente de El Salvador (ID 13: Natalia Rojas) ya existe
-- Crear una nueva venta (ID 21 asumido, ajust� si ya hay m�s)
INSERT INTO Ventas (id_cliente, fecha, total) VALUES
(13, '2025-06-14', 28990.00);

-- Insertar detalles (productos existentes)
INSERT INTO DetalleVenta (id_venta, id_producto, cantidad, subtotal) VALUES
(21, 1, 1, 14990.00),
(21, 5, 1, 14000.00);










INSERT INTO Ventas (id_cliente, fecha, total) VALUES
(1, '2025-06-01', 25980),
(2, '2025-06-02', 10990),
(3, '2025-06-03', 8990),
(4, '2025-06-04', 28980),
(5, '2025-06-05', 39990),
(6, '2025-06-06', 45990),
(7, '2025-06-07', 89900),
(8, '2025-06-08', 19990),
(9, '2025-06-09', 13990),
(10, '2025-06-10', 49990),
(11, '2025-06-11', 8990),
(12, '2025-06-12', 159000),
(13, '2025-06-13', 29990),
(14, '2025-06-14', 9990),
(15, '2025-06-15', 249000),
(16, '2025-06-16', 5990),
(17, '2025-06-17', 34990),
(18, '2025-06-18', 14990),
(19, '2025-06-19', 15990),
(20, '2025-06-20', 39990);


INSERT INTO DetalleVenta (id_venta, id_producto, cantidad, subtotal) VALUES
(1, 1, 1, 14990.00),
(1, 2, 1, 10990.00),
(2, 2, 1, 10990.00),
(3, 5, 1, 8990.00);

-- Crear vistas
CREATE VIEW vista_productos_mas_vendidos AS
SELECT 
    p.nombre_producto, 
    SUM(dv.cantidad) AS total_vendidos
FROM DetalleVenta dv
JOIN Productos p ON dv.id_producto = p.id_producto
GROUP BY p.nombre_producto;


----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------


CREATE VIEW vista_total_compras_por_cliente AS
SELECT 
    c.nombre AS Cliente, 
    COUNT(v.id_venta) AS Cantidad_Ventas,
    SUM(v.total) AS Monto_Total
FROM Ventas v
JOIN Clientes c ON v.id_cliente = c.id_cliente
GROUP BY c.nombre;

----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------


CREATE VIEW vista_ventas_por_categoria AS
SELECT 
    cat.nombre_categoria,
    SUM(dv.subtotal) AS Total_Vendido
FROM DetalleVenta dv
JOIN Productos p ON dv.id_producto = p.id_producto
JOIN Categorias cat ON p.id_categoria = cat.id_categoria
GROUP BY cat.nombre_categoria;

CREATE VIEW vista_ventas_por_pais AS
SELECT 
    c.pais,
    SUM(v.total) AS Total_Por_Pais
FROM Ventas v
JOIN Clientes c ON v.id_cliente = c.id_cliente
GROUP BY c.pais;

CREATE VIEW vista_ventas_mensuales AS
SELECT 
    FORMAT(v.fecha, 'yyyy-MM') AS Mes,
    COUNT(v.id_venta) AS Total_Ventas,
    SUM(v.total) AS Monto_Total
FROM Ventas v
GROUP BY FORMAT(v.fecha, 'yyyy-MM');

-- Consultar resultados
SELECT * FROM vista_productos_mas_vendidos;
SELECT * FROM vista_total_compras_por_cliente;
SELECT * FROM vista_ventas_por_categoria;
SELECT * FROM vista_ventas_por_pais;
SELECT * FROM vista_ventas_mensuales;
