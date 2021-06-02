import sqlite3

conn = sqlite3.connect("demo_data.sqlite3")

curs = conn.cursor()
#
# create_table = """create table demo (s text, x int, y int)"""
# create_table_execute = curs.execute(create_table)
#
# insert_information = """insert into demo (s,x,y) values ('g',3,9),('v',5,7),('f',8,7)"""
# insert_information_execute = curs.execute(insert_information)
#
# # commit = conn.commit()

row_count = """select count(*) from demo"""
row_count_results = curs.execute(row_count).fetchall()

xy_at_least_5 = """select count(*) from demo where x >4 and y >4"""
xy_at_least_5_results = curs.execute(xy_at_least_5).fetchall()

unique_y = """select count(distinct y) from demo"""
unique_y_results = curs.execute(unique_y).fetchall()

conn.close()

print(row_count_results)
print(xy_at_least_5_results)
print(unique_y_results)
