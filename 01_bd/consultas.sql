-- Valores aleatorios --
select round( rand()*100000);

select round (rand() *(SELECT max(c.ID) from Cliente c)); 


-- funciones de fecha --
select CURRENT_DATE(), CURRENT_TIMESTAMP(), NOW(), CURRENT_TIME();


-- fechas aleatorias --
SELECT CURRENT_DATE() - INTERVAL ROUND(Rand() * 300) DAY;

select now() - INTERVAL round(RAND()*10000) hour;

select round(rand()* (select max(c.ID) from Cliente c));

-- Valores aleatorios para Deposito -- 
insert into Deposito 
select round(rand()*10000) NumDeposito, CURRENT_DATE() - INTERVAL ROUND(Rand() * 200) DAY FechaDeposito , 
round( rand()*100000) ImporteDeposito, round(rand()*3)+1 Moneda, round(rand()*3)+1 TipoDeposito, round(rand()* (select max(c.ID) from Cliente c)) IdCliente,
round(rand()* (select max(s.ID) from Sucursal s)) IdSucursa, round(rand()* (select max(b.ID) from Banquero b)) IdBanquero,
NOW() - INTERVAL ROUND(Rand() * 10000) HOUR FechaRegistro;