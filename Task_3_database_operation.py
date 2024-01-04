
# Task 3: MySQL Database Operations with Python

import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    port=3307,
    password = '',
    database = 'STUDENT_DATA'
)

cursor = mydb.cursor()
cursor.execute('create database STUDENT_DATA')

cursor.execute(
    "create table STUDENT_DETAILS(student_id int not null auto_increment ,first_name varchar(20),last_name varchar(20),age int not null,grade float not null,primary key(student_id))"
)

cursor.execute(
    "insert into STUDENT_DETAILS(first_name,last_name,age,grade) values ('Alice','Smith',18,95.5);"
)
mydb.commit()


data="insert into STUDENT_DETAILS(first_name,last_name,age,grade) values (%s, %s, %s, %s)"
value = [
    ('John','Smith',17,85),
    ('Bruse','Wayne',17,82),
    ('Ron','Smith',17,80),
    ('Ross','Baker',17,75),
    ('Allen','cooper',17,93),
    ('joey','Jones',17,90),
]
cursor.executemany(data,value)
mydb.commit()


cursor.execute("update STUDENT_DETAILS set grade = 97.0 where first_name = 'Alice' ")
mydb.commit()

cursor.execute("delete from STUDENT_DETAILS where last_name = 'Smith' ")
mydb.commit()

cursor.execute('select * from STUDENT_DETAILS')
data_value = cursor.fetchall()
for i in data_value:
    print(i)