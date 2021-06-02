import pandas as pd
import sqlite3
from sqlalchemy import create_engine

df = pd.read_csv('/Users/gianpaolocombatti/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.csv')

conn = sqlite3.connect('/Users/gianpaolocombatti/dspt11.3.1.2/buddymove_holidayiq.sqlite3')

c = conn.cursor()

df.to_sql('review', conn)

count_of_rows = c.execute("""select count(*) from review""").fetchall()

user_count = c.execute("""select count(*) from review where Nature >100 and Shopping >100""").fetchall()

print(count_of_rows)

print(user_count)

conn.close()

# buddymove = create_engine('sqlite://', echo=False)
#
# df.to_sql('review', con=buddymove)
#
# print(buddymove.execute("select count(*) from review").fetchall())
#
# print(buddymove.execute("select count(*) from review where Nature > 100 and Shopping > 100").fetchall())
