import pandas as pd
from sqlalchemy import create_engine
import urllib.parse

# ----- PostgreSQL Source -----
pg_engine = create_engine("postgresql+psycopg2://postgres:Pqsql@localhost:5432/etl_load")

# ----- MySQL Target -----
mysql_engine = create_engine("mysql+pymysql://root:Sql%403690@127.0.0.1:3306/etl_load")

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
