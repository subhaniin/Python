import psycopg2
U=input('Please enter Pgsql UID: ')
P=input('Please enter Pgsql PWD: ')

conn=psycopg2.connect(host="localhost",database="company",user=U,password=P)

cur=conn.cursor()

cur.execute('select * from employees order by emp_id')

rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()