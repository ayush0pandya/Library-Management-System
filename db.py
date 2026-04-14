import sqlite3

def get_connection():
    connection = sqlite3.connect("library.db")
    return connection

def setup():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("create table if not exists Books(Serial_number int primary key, Title varchar (20), Author varchar(10), Publishing_date date, Date_added date, is_available int, is_present int)")
    cursor.execute("create table if not exists Member(ID int primary key, First_Name varchar(10), Last_name varchar(10), age int, email varchar(30) unique)")
    cursor.execute("create table if not exists Borrows(member_id references Member(ID), book_id references Books(Serial_number), primary key(member_id, book_id))")
    connection.commit()
    connection.close()
