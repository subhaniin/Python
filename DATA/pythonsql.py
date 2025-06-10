import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Sql@3690",
    database="ecom"
)

# Create a cursor object
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM customers")  # Change table name

# Fetch and print results
for row in cursor.fetchall():
    print(row)

# Close connection
cursor.close()
conn.close()
    
    #The above code establishes a connection to a MySQL database, creates a cursor object, executes a query, fetches and prints the results, and closes the connection. 
    #Conclusion 
    #In this article, we have discussed how to connect to a MySQL database using Python. We have also