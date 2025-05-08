-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS opticlinic CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE opticlinic;

-- Tabla Usuario
CREATE TABLE Usuario (
     id_usuario INT AUTO_INCREMENT PRIMARY KEY,
     nombre VARCHAR(100) NOT NULL,
     email VARCHAR(100) NOT NULL UNIQUE,
     contraseña VARCHAR(255) NOT NULL,
     telefono VARCHAR(15)
);

-- Tabla Servicio
CREATE TABLE Servicio (
  id_servicio INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  descripcion TEXT,
  precio DECIMAL(10,2) NOT NULL
);

-- Tabla Cita
CREATE TABLE Cita (
  id_cita INT AUTO_INCREMENT PRIMARY KEY,
  fecha DATE NOT NULL,
  hora TIME NOT NULL,
  id_usuario INT NOT NULL,
  id_servicio INT NOT NULL,
  estado VARCHAR(50) NOT NULL,
  FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
  FOREIGN KEY (id_servicio) REFERENCES Servicio(id_servicio)
);

-- Tabla Información de Contacto
CREATE TABLE InformacionContacto (
     id_contacto INT AUTO_INCREMENT PRIMARY KEY,
     id_usuario INT NOT NULL,
     direccion VARCHAR(255) NOT NULL,
     telefono VARCHAR(15) NOT NULL,
     email VARCHAR(100) NOT NULL,
     FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

-- Tabla Método de Pago
CREATE TABLE MetodoPago (
    id_metodo_pago INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL,
    detalles TEXT
);

-- Tabla Pedido
CREATE TABLE Pedido (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    id_usuario INT NOT NULL,
    id_metodo_pago INT NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_metodo_pago) REFERENCES MetodoPago(id_metodo_pago)
);

-- Tabla Producto
CREATE TABLE Producto (
      id_producto INT AUTO_INCREMENT PRIMARY KEY,
      nombre VARCHAR(100) NOT NULL,
      descripcion TEXT,
      stock INT NOT NULL,
      precio DECIMAL(10,2) NOT NULL
);

-- Tabla DetallePedido
CREATE TABLE DetallePedido (
   id_detalle INT AUTO_INCREMENT PRIMARY KEY,
   id_pedido INT NOT NULL,
   id_producto INT NOT NULL,
   cantidad INT NOT NULL,
   subtotal DECIMAL(10,2) NOT NULL,
   FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido),
   FOREIGN KEY (id_producto) REFERENCES Producto(id_producto)
);

-- Tabla Carrito
CREATE TABLE Carrito (
     id_carrito INT AUTO_INCREMENT PRIMARY KEY,
     id_usuario INT NOT NULL,
     total DECIMAL(10,2) NOT NULL,
     FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

-- Tabla DetalleCarrito
CREATE TABLE DetalleCarrito (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_carrito INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_carrito) REFERENCES Carrito(id_carrito),
    FOREIGN KEY (id_producto) REFERENCES Producto(id_producto)
);