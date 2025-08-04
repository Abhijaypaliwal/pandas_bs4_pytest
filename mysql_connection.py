import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="database-2.cnk646w46gc7.ap-south-1.rds.amazonaws.com",       # or your MySQL server IP
    user="digit1808",   # e.g., "root"
    password="Welcome!12345",
    database="classicmodels"
)

# Create cursor object
cursor = connection.cursor()

# Example: Create a table

# Commit changes
connection.commit()

# Example: Fetch data
cursor.execute("SELECT * FROM customers")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
cursor.close()
connection.close()
