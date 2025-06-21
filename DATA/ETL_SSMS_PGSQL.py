from sqlalchemy import create_engine
import urllib.parse, os

# ---------- SQL Server (source) ----------
mssql_params = urllib.parse.quote_plus(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=YOUR_SQLSERVER_HOST;Database=YOUR_DB;"
    "UID=YOUR_USER;PWD=YOUR_PWD;"
)
mssql_engine = create_engine(f"mssql+pyodbc:///?odbc_connect={mssql_params}")
# docs: dialect+driver://user:pass@dsn  :contentReference[oaicite:0]{index=0}

# ---------- PostgreSQL (target) ----------
pg_engine = create_engine(
    "postgresql+psycopg2://PG_USER:PG_PWD@PG_HOST:5432/PG_DB"
)

from sqlalchemy import create_engine
import urllib.parse, os

# ---------- SQL Server (source) ----------
mssql_params = urllib.parse.quote_plus(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=YOUR_SQLSERVER_HOST;Database=YOUR_DB;"
    "UID=YOUR_USER;PWD=YOUR_PWD;"
)
mssql_engine = create_engine(f"mssql+pyodbc:///?odbc_connect={mssql_params}")
# docs: dialect+driver://user:pass@dsn  :contentReference[oaicite:0]{index=0}

# ---------- PostgreSQL (target) ----------
pg_engine = create_engine(
    "postgresql+psycopg2://PG_USER:PG_PWD@PG_HOST:5432/PG_DB"
)

# split on the first space only
first_last = df["Name"].str.split(" ", 1, expand=True)
df["first_name"] = first_last[0]
df["last_name"]  = first_last[1]            # NaN if nothing after first name
df = df.drop(columns=["Name"])

df.to_sql(
    "demo_table_clean",          # new table name in Postgres
    pg_engine,
    if_exists="replace",         # or "append" / "fail"
    index=False,
)

print(pd.read_sql("SELECT * FROM demo_table_clean", pg_engine).head())