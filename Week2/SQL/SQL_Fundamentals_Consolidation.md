# SQL Consolidation Notes

## Database Fundamentals

* **Database:** organised collection of data.
* **DBMS:** software used to create, manage and access databases.
* Databases provide a structured way to store, manage and retrieve data.
* **Flat file:** usually a single file/table, e.g. CSV.
* **Relational database:** data stored in related tables.
* Examples: SQL Server, MySQL, PostgreSQL, Oracle.

## Relational Database Concepts

* **Relational:** tables are connected through relationships.
* **Table:** collection of related data.
* **Row:** one record.
* **Column:** one attribute.
* **Entity:** something we store data about, e.g. Customer.
* **Attribute:** information about an entity, e.g. CustomerName.
* Data is separated into tables to reduce duplicate data and improve consistency.

## Keys & Relationships

### Primary Key (PK)

Uniquely identifies each record.

* Must be unique
* Cannot be NULL
* Can contain multiple columns

**Good:** `CustomerID`
**Bad:** `CustomerName`

### Foreign Key (FK)

References a primary key in another table and connects tables.

* Does not have to be unique.

### Relationships

* **1:1:** one record relates to one record.
* **1:M:** one record relates to many records.
* **M:M:** many records relate to many records.
* **Junction table:** used to connect two tables in a many-to-many relationship.

## Database Design

* **Data modelling:** planning how data is organised and connected.
* **ERD:** diagram showing entities, attributes and relationships.
* Databases are planned before building to create a clear and efficient structure.
* Identify:
  * entities 
  * attributes 
  * relationships.

## Normalisation

**Normalisation:** organising data to reduce redundancy and improve consistency.

* **1NF:** single values, no repeating groups, unique rows.
* **2NF:** 1NF + all non-key attributes depend on the whole PK.
* **3NF:** 2NF + no transitive dependencies.

**Benefit:** less duplicate data.
**Drawback:** more tables and complexity.

## Core SQL Concepts

**SQL** is the language used to interact with relational databases.

**SQL Server** is a DBMS that uses SQL.

### SQL Categories

* **DDL:** defines database structure.
* **DML:** works with data.
* **DCL:** controls permissions.
* **TCL:** manages transactions.

## Basic SQL Commands

```sql
CREATE DATABASE
CREATE TABLE
ALTER TABLE
DROP TABLE

INSERT INTO
UPDATE
DELETE

SELECT
```

## Querying Data

### SELECT

Retrieves data.

```sql
SELECT FirstName, LastName
FROM Customers;
```

### WHERE

Filters records.

```sql
SELECT *
FROM Customers
WHERE Country = 'UK';
```

### Comparison Operators

```sql
=    >    <    >=    <=
```

### AND / OR

```sql
WHERE Country = 'UK' AND City = 'London';
```

### LIKE

Searches for patterns.

```sql
WHERE FirstName LIKE 'S%';
```

### ORDER BY

Sorts results.

```sql
ORDER BY FirstName ASC;
```

### DISTINCT

Removes duplicate results.

```sql
SELECT DISTINCT Country
FROM Customers;
```

### NULL

Represents a missing/unknown value.

```sql
WHERE Phone IS NULL;
```
