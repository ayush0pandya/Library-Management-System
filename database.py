import sqlite3
from tabulate import tabulate
from datetime import date

connection = sqlite3.connect("library.db")
cursor = connection.cursor()

cursor.execute("create table if not exists Books(Serial_number int primary key, Title varchar (20), Author varchar(10), Publishing_date date, Date_added date, is_available int)")

cursor.execute("insert into Books" \
"(Serial_number, Title, Author, Publishing_date, Date_added, is_available)" \
"values" \
"(1, 'Broken Love', 'Ayush', '2024-04-22', '2026-01-29', 1)," \
"(2, 'AAAAA', 'Ayush', '2024-04-22', '2026-01-29', 1)," \
"(3, 'BBBBB', 'gogog', '2023-02-20', '2026-01-29', 0)," \
"(4, 'CCCCC', 'gagag', '2006-12-29', '2026-01-29', 1)")

cursor.execute("select * from Books")
print(tabulate(cursor.fetchall(), headers=["Serial_number", "Title", "Author", "Publishing_date", "Date_added", "is_available"]))

#cursor.execute("drop table Books")

connection.commit()
connection.close()