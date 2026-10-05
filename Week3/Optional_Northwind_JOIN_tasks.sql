USE Northwind;
GO

SELECT DB_NAME() AS CurrentDatabase;



SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE';


-- joins


--1. Customers + Orders
SELECT c.CompanyName, o.OrderID
FROM Customers c
JOIN Orders o
    ON c.CustomerID = o.CustomerID;



--2. Orders with Customer Names
SELECT o.OrderID, o.OrderDate, c.CompanyName
FROM Orders o
JOIN Customers c
    ON o.CustomerID = c.CustomerID;


--3. Orders with Product Names
SELECT od.OrderID, p.ProductName, od.Quantity
FROM [Order Details] od
JOIN Products p
    ON od.ProductID = p.ProductID;


--4. Order Totals
SELECT od.OrderID, SUM(od.Quantity * od.UnitPrice) AS OrderTotal
FROM [Order Details] od
GROUP BY od.OrderID;


--5. Total Spend per Customer
SELECT c.CompanyName, SUM(od.Quantity * od.UnitPrice) AS TotalSpend
FROM Customers c
JOIN Orders o
    ON c.CustomerID = o.CustomerID
JOIN [Order Details] od
    ON o.OrderID = od.OrderID
GROUP BY c.CompanyName;


--6. Customers with No Orders
SELECT c.CompanyName
FROM Customers c
LEFT JOIN Orders o
    ON c.CustomerID = o.CustomerID
WHERE o.OrderID IS NULL;


--7. Products Never Ordered
SELECT p.ProductName
FROM Products p
LEFT JOIN [Order Details] od
    ON p.ProductID = od.ProductID
WHERE od.ProductID IS NULL;


--8. Orders per Employee
SELECT e.FirstName, e.LastName, COUNT(o.OrderID) AS OrderCount
FROM Employees e
LEFT JOIN Orders o
    ON e.EmployeeID = o.EmployeeID
GROUP BY e.FirstName, e.LastName;


--9. Top 5 Customers by Spend
SELECT TOP 5 c.CompanyName,
       SUM(od.Quantity * od.UnitPrice) AS TotalSpend
FROM Customers c
JOIN Orders o
    ON c.CustomerID = o.CustomerID
JOIN [Order Details] od
    ON o.OrderID = od.OrderID
GROUP BY c.CompanyName
ORDER BY TotalSpend DESC;


--10. Revenue by Category
SELECT c.CategoryName,
       SUM(od.Quantity * od.UnitPrice) AS Revenue
FROM Categories c
JOIN Products p
    ON c.CategoryID = p.CategoryID
JOIN [Order Details] od
    ON p.ProductID = od.ProductID
GROUP BY c.CategoryName;


--11. Full Order Breakdown
SELECT o.OrderID,
       c.CompanyName,
       p.ProductName,
       od.Quantity,
       od.UnitPrice
FROM Orders o
JOIN Customers c
    ON o.CustomerID = c.CustomerID
JOIN [Order Details] od
    ON o.OrderID = od.OrderID
JOIN Products p
    ON od.ProductID = p.ProductID;


--12. Average Order Value per Customer
SELECT c.CompanyName,
       COUNT(DISTINCT o.OrderID) AS NumberOfOrders,
       SUM(od.Quantity * od.UnitPrice) AS TotalSpend,
       SUM(od.Quantity * od.UnitPrice) / COUNT(DISTINCT o.OrderID) AS AverageOrderValue
FROM Customers c
JOIN Orders o
    ON c.CustomerID = o.CustomerID
JOIN [Order Details] od
    ON o.OrderID = od.OrderID
GROUP BY c.CompanyName;


--13. Employees with No Orders
SELECT e.FirstName, e.LastName
FROM Employees e
LEFT JOIN Orders o
    ON e.EmployeeID = o.EmployeeID
WHERE o.OrderID IS NULL;


--14. Most Popular Product
SELECT TOP 1 p.ProductName,
       SUM(od.Quantity) AS TotalQuantity
FROM Products p
JOIN [Order Details] od
    ON p.ProductID = od.ProductID
GROUP BY p.ProductName
ORDER BY TotalQuantity DESC;


--15. Orders with Shipping Company
SELECT o.OrderID, s.CompanyName
FROM Orders o
JOIN Shippers s
    ON o.ShipVia = s.ShipperID;

