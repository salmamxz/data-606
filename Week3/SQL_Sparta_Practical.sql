CREATE DATABASE SpartaPractical;


USE SpartaPractical;



CREATE TABLE Course
(
    CourseID VARCHAR(20) PRIMARY KEY,
    CourseName VARCHAR(100) NOT NULL,
    Trainer VARCHAR(100) NOT NULL,
    StartDate DATE NOT NULL
);



--just to check
SELECT *FROM Course;


CREATE TABLE Spartans
(
    SpartanID INT IDENTITY(1,1) PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    MiddleName VARCHAR(50),
    LastName VARCHAR(50),
    CourseID VARCHAR(20),

    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);



--to check again
SELECT * FROM Spartans;




INSERT INTO Course
(
    CourseID,
    CourseName,
    Trainer,
    StartDate
)
VALUES
('TECH 200', 'C# Dev', 'Luke', '2026-10-06'),
('DATA 200', 'Data Academy', 'Helen', '2026-10-06'),
('AI 200', 'AI Fundamentals', 'Robert', '2026-11-02');



--check again
SELECT * FROM Course;


INSERT INTO Spartans
(
    FirstName,
    MiddleName,
    LastName,
    CourseID
)
VALUES
('Salma', NULL, 'Meziane', 'DATA 200'),
('James', 'John', 'Smith', 'TECH 200'),
('Aisha', NULL, 'Khan', 'AI 200'),
('Daniel', 'Michael', 'Jones', 'DATA 200');




--just checking :)
SELECT * FROM Spartans;



ALTER TABLE Spartans
ADD Title VARCHAR(10);


-- checking again
SELECT * FROM Spartans;


UPDATE Spartans
SET Title = 'Ms'
WHERE SpartanID = 1;

UPDATE Spartans
SET Title = 'Mr'
WHERE SpartanID = 2;

UPDATE Spartans
SET Title = 'Ms'
WHERE SpartanID = 3;

UPDATE Spartans
SET Title = 'Mr'
WHERE SpartanID = 4;




SELECT * FROM Spartans;



ALTER TABLE Spartans
ADD CONSTRAINT CK_Spartans_Title
CHECK (Title IN ('Mr', 'Ms', 'Mx', 'Dr'));





ALTER TABLE Spartans
ADD Email VARCHAR(100);


SELECT * FROM Spartans;


UPDATE Spartans
SET Email = 'salma@example.com'
WHERE SpartanID = 1;

UPDATE Spartans
SET Email = 'james@example.com'
WHERE SpartanID = 2;

UPDATE Spartans
SET Email = 'aisha@example.com'
WHERE SpartanID = 3;

UPDATE Spartans
SET Email = 'daniel@example.com'
WHERE SpartanID = 4;




SELECT * FROM Spartans;

ALTER TABLE Course
ADD EndDate DATE;


ALTER TABLE Course
ADD CONSTRAINT CK_Course_EndDate
CHECK (EndDate >= StartDate);



UPDATE Course
SET EndDate = '2026-12-04'
WHERE CourseID = 'TECH 200';

UPDATE Course
SET EndDate = '2026-12-04'
WHERE CourseID = 'DATA 200';

UPDATE Course
SET EndDate = '2027-01-15'
WHERE CourseID = 'AI 200';




SELECT * FROM Course;


ALTER TABLE Course
ALTER COLUMN CourseName VARCHAR(200) NOT NULL;



SELECT * FROM Course;



ALTER TABLE Spartans
ADD Status VARCHAR(20)
    CONSTRAINT DF_Spartans_Status DEFAULT 'Active';



INSERT INTO Spartans
(
    FirstName,
    MiddleName,
    LastName,
    CourseID,
    Title,
    Email
)
VALUES
(
    'Emily',
    NULL,
    'Brown',
    'DATA 200',
    'Ms',
    'emily@example.com'
);


SELECT * FROM Spartans;




SELECT *
FROM Spartans
WHERE LastName IS NULL;





ALTER TABLE Spartans
ALTER COLUMN LastName VARCHAR(50) NOT NULL;



SELECT * FROM Spartans;




EXEC sp_rename 'Course.CourseName', 'Course_Name', 'COLUMN';


SELECT * FROM Course;




ALTER TABLE Spartans
DROP COLUMN MiddleName;


SELECT * FROM Spartans;


-- ALTER QUESTION
---ALTER TABLE is safer in a production database because it allows changes to be made to an existing table without deleting the data.
-- Dropping and recreating a table could cause data loss and could also break relationships, constraints, queries and applications that depend on the table.

SELECT * FROM Course;

SELECT * FROM Spartans;




ALTER TABLE Spartans
ADD CONSTRAINT UQ_Spartans_Email UNIQUE (Email);



SELECT * FROM Spartans;



INSERT INTO Spartans
(
    FirstName,
    LastName,
    CourseID,
    Title,
    Email
)
VALUES
(
    'Test',
    'Duplicate',
    'DATA 200',
    'Ms',
    'salma@example.com'
);