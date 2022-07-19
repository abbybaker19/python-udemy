import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime

try:
    conn = mysql.connector.connect(host='localhost', database='students', user='studentadmin', password='TurtleDove')
    query = "INSERT INTO students VALUES ('1', 'Wanda', 'Maximoff', 'wmaximoff@starkindustries.com', '200 Park Avenue'," \
            " 'New York', 'NY', 10001, '792-223-8901', '10-17-1989', 'F', NOW(), 3.50, NULL)"

    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    print("data entered")
    cursor.close()

except mysql.connector.Error as error:
    print("error:", error)

finally:
    if conn.is_connected():
        conn.close()
        print("connection closed")
