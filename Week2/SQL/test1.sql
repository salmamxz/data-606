CREATE TABLE Employees (
    EmployeeID INT,
    Name VARCHAR(50),
    Department VARCHAR(50),
    Salary INT,
    Age INT
);



-- wwwwww
INSERT INTO Employees (EmployeeID, Name, Department, Salary, Age)
VALUES
(1, 'Sarah', 'Data', 30000, 23),
(2, 'James', 'IT', 35000, 27),
(3, 'Aisha', 'Data', 32000, 25),
(4, 'Tom', 'Finance', 40000, 31),
(5, 'Emily', 'IT', 38000, 29);


SELECT *
FROM Employees;


SELECT *
FROM Employees
WHERE age = 27;


SELECT *
FROM Employees



SELECT *
FROM Employees
WHERE Salary < 35000



SELECT *
FROM Employees
WHERE  Department = 'IT'
AND Salary > 35000;
