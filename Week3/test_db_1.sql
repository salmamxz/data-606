


CREATE DATABASE my_db

USE my_db;

CREATE TABLE film_table(
    film_name VARCHAR(20),
    film_type VARCHAR(20),
)


SELECT * FROM film_table;

DROP TABLE film_table;


CREATE TABLE film_table
(
    film_id INT IDENTITY(1,1) PRIMARY KEY,
    film_name VARCHAR(20) NOT NULL,
    film_type VARCHAR(20) NOT NULL,
    date_of_release DATE NOT NULL,
    director VARCHAR(40) NOT NULL,
    writer VARCHAR(20) NOT NULL,
    star VARCHAR(20) NOT NULL,
    film_language VARCHAR(20) NOT NULL,
    official_website VARCHAR(255),
    plot_summary VARCHAR(MAX) NOT NULL
);


ALTER TABLE film_table
ADD release_date DATETIME;


INSERT INTO film_table
(
    film_name,
    film_type,
    date_of_release,
    director,
    writer,
    star,
    film_language,
    official_website,
    plot_summary
)
VALUES
(
    'Titanic','Romance','1997-12-19','James Cameron',
    'James Cameron',
    'Leonardo DiCaprio',
    'English',
    'https://www.titanicmovie.com',
    'A romance develops between two passengers aboard the Titanic.'
);


INSERT INTO film_table
(
    film_name,
    film_type,
    date_of_release,
    director,
    writer,
    star,
    film_language,
    official_website,
    plot_summary
)
VALUES
(
    'Titanic',
    'Romance',
    '1997-12-19',
    'James Cameron',
    'James Cameron',
    'Leonardo DiCaprio',
    'English',
    'https://www.titanicmovie.com',
    'A romance develops between two passengers aboard the Titanic.'
),
(
    'Barbie',
    'Comedy',
    '2023-07-21',
    'Greta Gerwig',
    'Greta Gerwig',
    'Margot Robbie',
    'English',
    'https://www.barbie-themovie.com',
    'Barbie leaves Barbieland and discovers the real world.'
),
(
    'Inception',
    'Sci-Fi',
    '2010-07-16',
    'Christopher Nolan',
    'Christopher Nolan',
    'Leonardo DiCaprio',
    'English',
    'https://www.inceptionmovie.net',
    'A skilled thief enters peoples dreams to steal information.'
),
(
    'The Notebook',
    'Romance',
    '2004-06-25',
    'Nick Cassavetes',
    'Jeremy Leven',
    'Ryan Gosling',
    'English',
    NULL,
    'Two people fall in love despite coming from different backgrounds.'
),
(
    'Frozen',
    'Animation',
    '2013-11-27',
    'Chris Buck',
    'Jennifer Lee',
    'Idina Menzel',
    'English',
    'https://movies.disney.com/frozen',
    'A young woman searches for her sister after a magical winter begins.'
);







SELECT TABLE_SCHEMA, TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES;




CREATE PROCEDURE GetCustomerContactName
    @CustomerID NCHAR(5)
AS
BEGIN
    SELECT ContactName
    FROM Customers
    WHERE CustomerID = @CustomerID;
END;

EXEC GetCustomerContactName @CustomerID = 'ALFKI';