import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import urllib.parse
import getpass  # for secure password entry'
# ----- Ask user for PostgreSQL UID and password -----
pg_user = input("postgres UID: ")
pg_pass = getpass.getpass("PostgreSQL Password:")
pg_host = "localhost"
pg_port = 5432 # Default PostgreSQL port
pg_db   = "company"
pg_pass = urllib.parse.quote_plus(pg_pass) # URL encode the password for PostgreSQL connection
# ----- postgresql connection ----- 
pg_engine = create_engine(f"postgresql+psycopg2://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}")
# ----- Extract -----
df = pd.read_sql("SELECT * FROM employees", pg_engine)
print(df.head())  # Display first few rows for verification