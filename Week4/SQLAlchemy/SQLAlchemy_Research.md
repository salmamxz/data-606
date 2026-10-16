# SQLAlchemy Research

## 1. What is SQLAlchemy?

SQLAlchemy is a Python library used to interact with relational databases such as SQL Server, PostgreSQL, MySQL and SQLite. It allows Python applications to execute SQL queries, manage database connections and work with database records.

### What problem does it solve?

SQLAlchemy simplifies communication between Python applications and databases. It provides tools for executing SQL queries, managing connections and processing database results. It also allows developers to work with database records as Python objects through its Object-Relational Mapper (ORM).

### Why is it popular?

- **Flexibility:** Supports both SQL-based operations and object-oriented database interactions.
- **Database portability:** Supports multiple database systems through a consistent interface.
- **Connection management:** Provides connection pooling to reuse database connections efficiently.
- **Security:** Supports parameterised queries, helping reduce the risk of SQL injection when used correctly.
- **Integration:** Works with Python libraries such as Pandas, making it useful for data analysis and data engineering.

### How does SQLAlchemy differ from pyodbc?

SQLAlchemy and pyodbc have different roles.

- **SQLAlchemy** is a higher-level SQL toolkit and ORM that provides tools for managing database interactions.
- **pyodbc** is a Python library that connects to databases through ODBC drivers and allows SQL statements to be executed directly.

SQLAlchemy can use pyodbc as its underlying driver when connecting to SQL Server. Alternatively, pyodbc can be used independently without SQLAlchemy.

| Feature | SQLAlchemy | pyodbc |
|---|---|---|
| Main purpose | Database toolkit and ORM | Database connectivity |
| Query execution | Supports SQL statements and ORM queries | Executes SQL statements |
| Connection management | Includes an Engine and connection pooling | Uses direct connections and cursors |
| ORM support | Yes | No built-in ORM |
| SQL Server support | Can use pyodbc as a driver | Uses ODBC drivers directly |

## 2. SQLAlchemy Core vs ORM

SQLAlchemy offers two main approaches to database interaction: Core and ORM.

### What is SQLAlchemy Core?

SQLAlchemy Core is the SQL toolkit within SQLAlchemy. It provides tools for constructing and executing SQL queries using tables, columns, expressions and database connections.

Core is useful when developers want direct control over database queries, joins, filtering, aggregations and data transformations.

For example, a data engineer can use Core to retrieve products above a certain price or calculate the total number of orders per customer.

### What is an ORM?

ORM stands for Object-Relational Mapper. It allows developers to interact with database tables through Python classes and objects instead of writing every database operation as a SQL statement.

For example, a Customer class can represent the Customers table, and individual customer records can be represented as Python objects.

The ORM can simplify database operations when an application needs to create, retrieve, update or delete records and manage relationships between entities.

### When might a data engineer use Core rather than ORM?

A data engineer might prefer Core when:

- Building ETL (Extract, Transform, Load) pipelines.
- Running SQL-heavy queries involving joins, filtering and aggregations.
- Processing structured data from database tables.
- Working with large datasets where creating individual Python objects for every row may add unnecessary overhead.
- Requiring explicit control over SQL execution.

Core is often a natural choice for SQL-focused data engineering tasks, while ORM is particularly useful for applications that work with entities and their relationships. Both approaches can be used together.

## 3. What is an Engine?

An Engine is SQLAlchemy's main starting point for communicating with a database. It combines the database dialect, underlying database driver and connection-pooling functionality.

### Why do most SQLAlchemy examples start by creating an Engine?

The Engine provides a reusable interface for connecting to a database and executing queries. It manages database connections and can reuse them through connection pooling, reducing the need to establish a completely new connection for every operation.

Creating an Engine does not necessarily open a database connection immediately. A connection is normally established when it is first needed.

### How does the Engine relate to pyodbc?

When connecting to SQL Server, SQLAlchemy can use pyodbc as its underlying database driver.

The Engine manages database interactions at the SQLAlchemy level, while pyodbc communicates with SQL Server through an installed ODBC driver.

The basic flow is:

Python application → SQLAlchemy Engine → pyodbc → ODBC driver → SQL Server.

## 4. References

- SQLAlchemy documentation: https://docs.sqlalchemy.org/en/20/
- SQLAlchemy Engine documentation: https://docs.sqlalchemy.org/en/21/core/engines.html
- SQLAlchemy Unified Tutorial: https://docs.sqlalchemy.org/en/20/tutorial/
- pyodbc documentation: https://github.com/mkleehammer/pyodbc
- Pandas SQL documentation: https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html

## 5. Practical Work

The practical exercises will be completed in a separate Python file, `sqlalchemy_northwind.py`.

The exercises will cover:

1. Installing and importing SQLAlchemy.
2. Connecting to the Northwind SQL Server database.
3. Retrieving customers from London.
4. Retrieving products costing more than £20.
5. Finding the ten most expensive products.
6. Loading the Orders table into a Pandas DataFrame.
7. Calculating total orders per customer.
8. Identifying the customer with the most orders, the number of unique customers who placed orders and the average number of orders per customer.
