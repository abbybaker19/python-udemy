import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host='localhost', database='students', user='studentadmin', password='TurtleDove')
    query = 'SELECT first_name, last_name FROM students WHERE state="NY"'
    cursor = conn.cursor()
    cursor.execute(query)
    students = cursor.fetchall()
    print("total results:", len(students))
    for s in students:
        print(s[0], " ", s[1])

except mysql.connector.Error as error:
    print("error:", error)

finally:
    if conn.is_connected():
        conn.close()
