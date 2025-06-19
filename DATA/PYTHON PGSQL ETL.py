from sqlalchemy import create_engine
import pyodbc
import pandas as pd
import os
from datetime import datetime

uid = 'postgres'
pwd = 'Pqsql'


# Database connection settings
host = 'localhost'      # Change to your host if different
port = '5432'           # Default PostgreSQL port

# Source: DemoDB
source_engine = create_engine(
    f"postgresql+psycopg2://{uid}:{pwd}@{host}:{port}/DemoDB"
)

# Target: ETLLoadDB
target_engine = create_engine(
    f"postgresql+psycopg2://{uid}:{pwd}@{host}:{port}/etl_load"
)   

# Step 1: Extract
query = "SELECT * FROM employees"
df = pd.read_sql(query, source_engine)

# Step 2: (Optional) Transform
# For example: df['full_name'] = df['first_name'] + ' ' + df['last_name']

# Step 2: Transform
df['loaded_at'] = datetime.now()

# Step 3: Load into ETLLoadDB.etl_employees
df.to_sql('etl_employees', target_engine, if_exists='replace', index=False)

print("✅ ETL completed: 'employees' → 'etl_employees'")

#This script extract data from DemoDB employees table and load it to etl_load.etl_employees table.