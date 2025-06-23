import pandas as pd
from sqlalchemy import create_engine
import urllib.parse

# ----- SQL Server connection -----
import urllib

mssql_params = urllib.parse.quote_plus(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=SUBHANIDEAPAD\\SQLEXPRESS;"
    "Database=MYDBSSMS;"
    "Trusted_Connection=yes;"
)

mssql_engine = create_engine(f"mssql+pyodbc:///?odbc_connect={mssql_params}")

# ----- PostgreSQL connection -----
pg_engine = create_engine(
    "postgresql+psycopg2://postgres:Pqsql@localhost:5432/etl_load"
)

# ----- Extract -----
df = pd.read_sql("SELECT * FROM KYC", mssql_engine)

# ----- Transform -----

# 1. Split Name
names = names = df["Name"].str.split(" ", n=1, expand=True)
df["first_name"] = names[0]
df["last_name"] = names[1]

# 2. Split Address
# Example format:
# "2-95, 1st street, rayudupalem, kakinada rural, kakinada district, 533006, Andhra Pradesh, India"
address_parts = df["address"].str.split(",", expand=True)

df["address_clean"] = address_parts[[0,1,2,3,4]].apply(lambda x: ", ".join(x.dropna().str.strip()), axis=1)
df["pincode"] = address_parts[5].str.strip()
df["state"] = address_parts[6].str.strip()

# Optional: remove "India" column if it exists
if address_parts.shape[1] > 7:
    df["country"] = address_parts[7].str.strip()

# Drop old Name and Address columns
df = df.drop(columns=["Name", "address"])

# Reorder columns if needed
df = df[["ID", "first_name", "last_name", "age", "address_clean", "pincode", "state"] + (["country"] if "country" in df.columns else [])]

# ----- Load -----
df.to_sql("kyc_clean", pg_engine, if_exists="replace", index=False)
print("Data loaded successfully into PostgreSQL.")