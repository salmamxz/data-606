
from sqlalchemy import create_engine, URL, text
import pandas as pd

# SQL Server connection details
password = "SalmaSQL2026Aa#2026"

connection_url = URL.create(
    "mssql+pyodbc",
    username="sa",
    password=password,
    host="localhost",
    port=1433,
    database="Northwind",
    query={
        "driver": "ODBC Driver 18 for SQL Server",
        "Encrypt": "yes",
        "TrustServerCertificate": "yes"
    }
)

# Create the engine
engine = create_engine(connection_url)

# Test the connection
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT @@VERSION"))
        print("Connected to Northwind successfully!")
        print(result.scalar())
finally:
    engine.dispose()
