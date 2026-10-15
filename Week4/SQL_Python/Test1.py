

import pyodbc

connection = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost,1433;"
    "DATABASE=master;"
    "UID=sa;"
    "PWD=SalmaSQL2026Aa#2026;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

print("Connected to SQL Server successfully!")


cursor = connection.cursor()

cursor.execute("SELECT @@VERSION")

row = cursor.fetchone()

print(row[0])