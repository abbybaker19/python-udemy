import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime

try:
    conn = mysql.connector.connect(host='localhost', database='students', user='studentadmin', password='TurtleDove')
    query = "INSERT INTO absences VALUES (6, '2014-08-29'),(7, '2014-08-29'),(8,'2014-08-27')"
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
