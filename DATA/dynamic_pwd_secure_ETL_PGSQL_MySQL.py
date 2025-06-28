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
mysql_pass = urllib.parse.quote_plus(mysql_pass)# # URL encode the password for MySQL connection

# ----- postgresql connection -----
pg_engine = create_engine(f"postgresql+psycopg2://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}")
# ----- MySQL connection -----
mysql_engine = create_engine(f"mysql+pymysql://{mysql_user}:{mysql_pass}@{mysql_host}:{mysql_port}/{mysql_db}")
# ----- Extract -----
df = pd.read_sql("SELECT * FROM KYC_clean", pg_engine)
print(df.head())  # Display first few rows for verification

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
try:    
    df.to_sql("kyc_merged", mysql_engine, if_exists="replace", index=False)
    print("✅ Data merged and loaded into MySQL.")
except Exception as e:
    print(f"❌ Error loading data into MySQL: {e}") 
# Display the first few rows of the transformed DataFrame
print(df.head())  # Display first few rows for verification