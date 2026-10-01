# Introduction to SQL

## What is SQL?

SQL is used to work with databases and is a reliable way for businesses to store, manage and retrieve data.

### Types of data storage

* Flat files: e.g. CSV, usually one table
* NoSQL databases: non-relational databases
* SQL databases: relational databases

## RDBMS

**Relational Database Management System (RDBMS)** is software used to create, manage and interact with relational databases.

Examples:

* MySQL: open source and free
* PostgreSQL: open source and free
* SQLite: lightweight database
* Oracle Database
* Microsoft SQL Server

## What is a database?

A database is an organised collection of data.

### Tables

Relational databases store data in **tables**. Tables contain:

* Rows = records
* Columns = attributes/fields

Tables are connected using **keys**.

### Primary Key (PK)

A primary key identifies each record in a table.

* Must be unique
* Cannot be NULL
* A table has one primary key (which can contain multiple columns)
* Used to identify a specific record

### Foreign Key (FK)

A foreign key is a column that references a primary key in another table.

* Used to connect tables
* Does not have to be unique
* Can appear multiple times in a table

---

# Data Modelling

A **data model** shows how information is organised and how tables relate to each other.

### Three levels

1. **Conceptual**: high-level view of entities and relationships
2. **Logical**: entities, attributes, PKs and FKs
3. **Physical**: actual tables, column names, data types, PKs and FKs

### Relationships

* **One-to-one (1:1)**
* **One-to-many (1:M)**
* **Many-to-many (M:M)**

---

# Entity Relationship Diagram (ERD)

An **ERD** represents the entities in a data model and the relationships between them.

It can be used to:

* Create a database structure
* Understand how tables are connected
* Identify PKs and FKs

**Crow's Foot notation** is commonly used to represent relationships.

---

# Database Normalisation

Normalisation organises data to reduce **data redundancy** and improve data consistency.

### Advantages

* Reduces duplicated data
* Makes inserting data easier
* Makes deleting/updating data safer
* Improves data consistency

### Disadvantage

* Can increase the number of tables and make the database structure more complex.

## Normal Forms

### 1NF - First Normal Form

* Each cell contains a single value
* No repeating groups
* Each row is unique

### 2NF - Second Normal Form

* Must already be in 1NF
* All non-key attributes must depend on the **whole primary key**

### 3NF - Third Normal Form

* Must already be in 2NF
* No **transitive dependencies**
* Non-key attributes should depend only on the primary key
