USE tienda_adso;
-- Ejecutar solo una vez, para evitar duplicados.
INSERT INTO clientes (nombre, correo) VALUES ('Ana Pérez','ana@example.com'),('Carlos Ruiz','carlos@example.com'),('Julian Gutierrez','julian@example.com'),('Liliana Mendez','liliana@example.com'),('Santiago Torres','santiago@example.com'),('Valentina Rojas','valentina@example.com');
INSERT INTO productos (nombre,precio,stock) VALUES ('Mouse',35000,12),('Teclado',80000,8),('Monitor',650000,4),('Auriculares',120000,15),('Webcam',150000,10),('Parlantes',200000,6);
