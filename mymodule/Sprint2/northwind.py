import sqlite3
import os

path = os.path.abspath(os.path.join(os.pardir,'../northwind_small.sqlite3'))

conn = sqlite3.connect(path)

curs = conn.cursor()

expensive_items = (
    """select ProductName,UnitPrice from Product order by UnitPrice desc limit 10"""
)
expensive_items_results = curs.execute(expensive_items).fetchall()

avg_hire_age = (
    """select avg(age) from (select(HireDate-BirthDate) as age from Employee)"""
)
avg_hire_age_results = curs.execute(avg_hire_age).fetchall()

ten_most_expensive = (
    """select ProductName,UnitPrice,CompanyName from Product left join Supplier on Product.SupplierId = Supplier.Id 
    order by UnitPrice desc limit 10"""
)
ten_most_expensive_results = curs.execute(ten_most_expensive).fetchall()

largest_category = ("""select CategoryName,count(ProductName) as COUNT from Product 
left join Category on Product.CategoryId = Category.Id group by CategoryName order by COUNT desc limit 1"""
                    )
largest_category_results = curs.execute(largest_category).fetchall()

avg_age_by_city = (
    """select City,avg(HireDate-BirthDate) as age from Employee group by City"""
)
avg_age_by_city_results = curs.execute(avg_age_by_city).fetchall()


conn.close()
