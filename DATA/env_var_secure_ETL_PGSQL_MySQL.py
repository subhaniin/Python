import pandas as pd
from sqlalchemy import create_engine
import urllib.parse

import os

# PostgreSQL
pg_user = os.getenv("PGUID")
pg_pass = os.getenv("PGPWD")
pg_host = "localhost"
pg_port = 5432
pg_db   = "etl_load"

pg_engine = create_engine(f"postgresql+psycopg2://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}")

# MySQL
mysql_user = os.getenv("MysqlUID")
mysql_pass = os.getenv("MysqlPWD")
mysql_host = "127.0.0.1"
mysql_port = 3306
mysql_db   = "etl_load"

mysql_engine = create_engine(f"mysql+pymysql://{mysql_user}:{mysql_pass}@{mysql_host}:{mysql_port}/{mysql_db}")

# ----- Extract -----
df = pd.read_sql("SELECT * FROM \"KYC_clean\"", pg_engine)

# ----- Transform -----

# 1. Merge Name
df["Name"] = df["first_name"].str.strip() + " " + df["last_name"].str.strip()

# 2. Merge Address
address_parts = [df["address_clean"], df["pincode"], df["state"]]
if "country" in df.columns:
    address_parts.append(df["country"])

df["address"] = address_parts[0].fillna("").str.strip()
for part in address_parts[1:]:
    df["address"] += ", " + part.fillna("").str.strip()

# 3. Drop individual columns
cols_to_drop = ["first_name", "last_name", "address_clean", "pincode", "state"]
if "country" in df.columns:
    cols_to_drop.append("country")

df = df.drop(columns=cols_to_drop)

# Optional: Reorder columns
df = df[["ID", "Name", "age", "address"]]

# ----- Load -----
df.to_sql("kyc_merged", mysql_engine, if_exists="replace", index=False)
print("✅ Data merged and loaded into MySQL.")