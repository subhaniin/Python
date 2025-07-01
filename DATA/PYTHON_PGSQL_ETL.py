from sqlalchemy import create_engine;import pandas as pd;import datetime as dt

userID= 'postgres';PWD= 'Pqsql'

pg_engine = create_engine(f"postgresql+psycopg2://{userID}:{PWD}@localhost:5432/DemoDB")
df=pd.read_sql('select emp_id,emp_name from employees', pg_engine);#print(df)
df[['emp_first_name', 'emp_last_name']] = df['emp_name'].str.title().str.split(' ', n=1, expand=True)
df['full_name'] = df['emp_name'].str.title()
import pytz
df['timestamp_Kolkata'] = dt.datetime.now(pytz.timezone('Asia/Kolkata'))
df=df[['emp_id', 'emp_first_name', 'emp_last_name', 'full_name','timestamp_Kolkata']]
print(df)
df.to_sql('emp_etl_name_split', pg_engine, if_exists='replace', index=False)
print('------------------Data load succeeeded-------------------')