CREATE DATABASE if not exists  NOVO_MUNDO;
USE bd_NOVO_MUNDO;
-- Tabla "Productos"

CREATE TABLE Productos (
    ID_Producto INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(50),
    Descripcion VARCHAR(255),
    Precio DECIMAL(10, 2)
);

-- Tabla "Insumos"
CREATE TABLE Insumos (
    ID_Insumo INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(50),
    Cantidad INT
);

-- Tabla "Producción Diaria"
CREATE TABLE ProduccionDiaria (
    ID_Produccion INT PRIMARY KEY AUTO_INCREMENT,
    Fecha DATE,
    Cantidad_Productos INT,
    Puesto VARCHAR(50)
);

-- Tabla "Recetas"
CREATE TABLE Recetas (
    ID_Receta INT PRIMARY KEY AUTO_INCREMENT,
    ID_Producto INT,
    ID_Insumo INT,
    Cantidad_Usada INT,
    FOREIGN KEY (ID_Producto) REFERENCES Productos(ID_Producto),
    FOREIGN KEY (ID_Insumo) REFERENCES Insumos(ID_Insumo)
);

-- Tabla "Empleados"
CREATE TABLE Empleados (
    ID_Empleado INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Puesto VARCHAR(50)
);
