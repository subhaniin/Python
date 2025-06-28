from sqlalchemy import create_engine
import pandas as pd
import urllib.parse
import datetime as dt
import getpass  # for secure password entry

# ----- Ask user for PostgreSQL UID and password -----
pg_user = input("Enter PostgreSQL UID: ")
pg_pass = getpass.getpass("Enter PostgreSQL Password: ")
pg_host = "localhost"
pg_port = 5432 # Default PostgreSQL port
pg_db   = "etl_load"
# ----- ask user for MySQL UID and password -----
mysql_user = input("Enter MySQL UID: ")
mysql_pass = getpass.getpass("Enter MySQL Password: ")
mysql_host = "localhost"  # Default MySQL host
mysql_port = 3306  # Default MySQL port
mysql_db   = "etl_load"
# ----- postgresql connection -----
pg_engine = create_engine(f"postgresql+psycopg2://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}")
# ----- MySQL connection -----
mysql_engine = create_engine(f"mysql+pymysql://{mysql_user}:{mysql_pass}@{mysql_host}:{mysql_port}/{mysql_db}")
# ----- Extract -----
df = pd.read_sql("SELECT * FROM KYC_clean", pg_engine)
print(df.head())  # Display first few rows for verification