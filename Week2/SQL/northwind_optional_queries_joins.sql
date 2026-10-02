--testing connexion

USE Northwind;
GO

SELECT DB_NAME() AS CurrentDatabase;



SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE';


SELECT *
FROM Customers;


SELECT *
FROM Products;


SELECT *
FROM Orders
WHERE OrderDate >= '1997-01-01';


SELECT *
FROM Products
WHERE UnitPrice > 20;


SELECT *
FROM Products
WHERE UnitPrice > 20
AND UnitsInStock < 20;


SELECT ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice DESC;



SELECT *
FROM Customers
WHERE Country = 'Germany';




SELECT ProductName, UnitPrice
FROM Products;



SELECT ProductName
FROM Products
WHERE CategoryID = 1;





--Basic Northwind Queries Exercises

SELECT *
FROM Customers
WHERE Country = 'Germany';


SELECT *
FROM Products
WHERE UnitPrice > 20;



SELECT FirstName, LastName, City
FROM Employees;


SELECT *
FROM Products
WHERE UnitsInStock = 0;


SELECT *
FROM Orders
WHERE ShipCountry = 'France';


SELECT *
FROM Customers
WHERE City LIKE 'B%';


SELECT *
FROM Products
WHERE QuantityPerUnit LIKE '%jar%'
   OR QuantityPerUnit LIKE '%bottle%';


SELECT *
FROM Employees
WHERE BirthDate > '1960-01-01';


SELECT *
FROM Products
ORDER BY UnitPrice DESC;


SELECT CompanyName, ContactName
FROM Customers
WHERE City = 'London'
   OR City = 'Madrid';




--Northwind JOIN tasks


SELECT c.CompanyName, o.OrderID
FROM Customers c
JOIN Orders o
    ON c.CustomerID = o.CustomerID;




SELECT o.OrderID, o.OrderDate, c.CompanyName
FROM Orders o
JOIN Customers c
    ON o.CustomerID = c.CustomerID;










