# Q.34 Python Program to delete records from MySQL table
print("Name: Rathod Ankitha  \nEnrollment: 92600565030")

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS assignment_db")
mycursor.execute("USE assignment_db")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
)
""")

mycursor.execute("""
INSERT INTO students VALUES (1, 'Ankitha', 23)
ON DUPLICATE KEY UPDATE name='Ankitha', age=23
""")

mydb.commit()

sql = "DELETE FROM students WHERE id = %s"

value = (1,)

mycursor.execute(sql, value)

mydb.commit()

print("Record deleted successfully")

mycursor.execute("SELECT * FROM students")

records = mycursor.fetchall()

print("Remaining Student Records:")

for row in records:
    print(row)

mydb.close()
