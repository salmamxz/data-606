CREATE DATABASE sparta_demo;

USE sparta_demo

CREATE TABLE personnel (
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    notes VARCHAR(max),
    phone_number CHAR(11),
    birthdate DATE,
    first_shift_start DATETIME,
    lunch_break TIME,
    number_of_awards INT,
    hourly_rate DECIMAL(4,2),
    height_metres FLOAT(24),
    is_full_time BIT
);


DROP TABLE IF EXISTS personnel;

CREATE TABLE personnel (
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    notes VARCHAR(max),
    phone_number CHAR(11),
    birthdate DATE,
    first_shift_start DATETIME,
    lunch_break TIME,
    number_of_awards INT,
    hourly_rate DECIMAL(4,2),
    height_metres FLOAT(24),
    is_full_time BIT
);


INSERT INTO personnel (
    first_name, last_name, notes, phone_number,
    birthdate, first_shift_start, lunch_break, number_of_awards,
    hourly_rate, height_metres,
    is_full_time
)
VALUES (
    'Joe', -- VARCHAR
    'Bloggs', -- VARCHAR
    'An excellent employee', -- VARCHAR
    '07123456789', -- CHAR
    '1990-01-23', -- DATE
    '2020-04-01 09:00:00', -- DATETIME
    '13:00:00', -- TIME
    4, -- INT
    12.75, -- DECIMAL
    1.77e1, -- FLOAT
    1 -- BIT
);



DROP TABLE IF EXISTS films;

CREATE TABLE films (
    film_title VARCHAR(180),
    release_date DATE,
    box_office_usd DECIMAL(10,0),
    runtime_mins INT,
    is_oscar_winning BIT
);


INSERT INTO films (
    film_title, release_date, box_office_usd, runtime_mins, is_oscar_winning
) VALUES
('Shrek', '2001-05-29', 484000000, 95, 1),
('Shrek 2', '2004-07-02', 919800000, 105, 0),
('Shrek the Third', '2007-05-06', 813400000, 93, 0);



INSERT INTO films
(release_date, is_oscar_winning, film_title)
VALUES
('2010-07-02', 0, 'Shrek Forever After');





DROP TABLE IF EXISTS films;

CREATE TABLE films (
    film_title VARCHAR(180) NOT NULL,
    release_date DATE,
    box_office_usd DECIMAL(10,0),
    runtime_mins INT,
    is_oscar_winning BIT DEFAULT 0
);




DROP TABLE IF EXISTS films;

CREATE TABLE films (
    film_title VARCHAR(180) NOT NULL,
    release_date DATE,
    box_office_usd DECIMAL(10,0),
    runtime_mins INT,
    is_oscar_winning BIT DEFAULT 0
);

INSERT INTO films
(film_title, release_date)
VALUES
('Shrek', '2001-6-29');



DROP TABLE IF EXISTS courses;

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(20)
);

INSERT INTO courses
(course_id, course_name)
VALUES
(1, 'C# Development'),
(2, 'Java Development'),
(3, 'Data Engineering');





DROP TABLE IF EXISTS courses;

CREATE TABLE courses (
    course_id INT PRIMARY KEY IDENTITY(1,1),
    course_name VARCHAR(20) UNIQUE
);

INSERT INTO courses
(course_name)
VALUES
('C# Development'),
('Java Development'),
('Data Engineering');





ALTER TABLE films
ADD budget DECIMAL(10,0), synopsis VARCHAR(200);

ALTER TABLE films
ALTER COLUMN runtime_mins DECIMAL(5,2);

ALTER TABLE films
DROP COLUMN box_office_usd;