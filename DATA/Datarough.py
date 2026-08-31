import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

username = "postgres"
password = "Sql@3690"
host = "localhost"
port = 5433
database = "postgres"

encoded_password = quote_plus(password)

engine = create_engine(
    f"postgresql+psycopg2://{username}:{encoded_password}@{host}:{port}/{database}"
)
#----------------------------------------------------------------------------------------

print("ETL tests on employees table: ")
sourceEmp = pd.read_sql("SELECT * FROM employees", engine)

print("Data from employees table:")
print(sourceEmp.head())
print("\n")
dupes = sourceEmp[sourceEmp.duplicated(subset=['sl','names','email','salary','joiningdate','dept_id'], keep=False)]
if not dupes.empty:
    print("Duplicate sl values found:")
    print(dupes)    
print("\n")
print(sourceEmp.columns)
print("\n")
print("Data types in employees table:")
print(sourceEmp.dtypes)
print("\n")
print("Null values in employees table:")
print(sourceEmp.isnull().sum())
print("\n")
print("Description of employees table:")
print(sourceEmp.describe())
print("\n")
print("Information about employees table:")
sourceEmp.info()
print("\n")
print("Shape of employees table:")
print(sourceEmp.shape)
print("employee table tests completed successfully.")
print("\n")
print("#-----------------------------------------------------------------------------------")
print("\n")

print("ETL tests on departments table: ")
SourceDep = pd.read_sql("SELECT * FROM departments", engine)

print("Data from departments table:")
print(SourceDep.head())
print("\n")
print("Column names in departments table:")
print(SourceDep.columns)
print("\n")
print("Data types in departments table:")
print(SourceDep.dtypes)
print("\n")
print("Null values in departments table:")
print(SourceDep.isnull().sum()) 
print("\n")
print("description of departments table:")
print(SourceDep.describe())
print("\n")
print("Information about departments table:")
SourceDep.info()
print("\n")
print("Shape of departments table:")
print(SourceDep.shape) 
print("departments table tests completed successfully.")