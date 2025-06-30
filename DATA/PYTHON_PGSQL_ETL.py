from sqlalchemy import create_engine;import pandas as pd

userID= 'postgres';PWD= 'Pqsql'

print(pd.read_sql('select * from employees', create_engine('postgresql+psycopg2://postgres:Pqsql@localhost:5432/DemoDB'))[['emp_id', 'emp_name']].assign(**{
    'First Name': lambda df: df['emp_name'].str.upper().str.split(' ', expand=True)[0],
    'Last Name': lambda df: df['emp_name'].str.upper().str.split(' ', expand=True)[1]
})[['emp_id', 'First Name', 'Last Name', 'emp_name']].rename(columns={'emp_name': 'Full Name'}))
# This code connects to a PostgreSQL database, retrieves employee data, and processes it to extract first and last names.
# It uses SQLAlchemy to create a database engine and pandas to read the SQL query result into a DataFrame.
# The DataFrame is then modified to include separate columns for first and last names, and the final output is displayed with specific columns renamed for clarity.
# The code assumes that the PostgreSQL server is running locally on port 5432 and that the database name is 'DemoDB'.
# The 'emp_name' column is expected to contain full names in the format "First Last".