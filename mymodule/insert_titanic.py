import pandas as pd
import psycopg2
import os

dname = os.environ['PG_DB']
user = os.environ['PG_USER']
password = os.environ['PG_PASSWORD']
host = os.environ['PG_HOST']

conn = psycopg2.connect(dbname=dname, user=user, password=password, host=host)
curs = conn.cursor()
# with open('titanic.csv','r') as f:
#     next(f)
#     curs.copy_from(f,'titanic', sep=',')
#
# conn.commit()

select_titanic_query = """select * from titanic"""

curs.execute(select_titanic_query)

results = curs.fetchall()

conn.close()

print(results)

