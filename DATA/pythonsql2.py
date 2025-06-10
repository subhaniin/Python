import mysql.connector

# Connect to MySQL using correct host and port
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sql@3690",
    database="ecom",
    port=3306
)

cursor = conn.cursor()

# Show all tables
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

# Print all tables
print("Tables in 'ecom' database:")
for table in tables:
    print(table[0])  # table is a tuple like ('customers',)

# Fetch and print all rows from each table
for table in tables:
    table_name = table[0]
    print(f"\nRows from table '{table_name}':")
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

cursor.close()
conn.close()