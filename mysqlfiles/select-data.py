import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host='localhost', database='students', user='studentadmin', password='TurtleDove')
    query = 'SELECT first_name, last_name FROM students WHERE state="NY"'
    cursor = conn.cursor()
    # cursor.execute(query)
    # students = cursor.fetchall()
    # print("total results:", len(students))
    # for s in students:
    #     print(s[0], " ", s[1])

    # query = 'INSERT INTO scores VALUES (6, 3, 24)'
    # cursor.execute(query)
    # query = 'DELETE FROM absences WHERE student_id = 6'
    # cursor.execute(query)
    # query = 'SELECT student_id, test_id FROM scores WHERE student_id = 6'
    # cursor.execute(query)
    # results = cursor.fetchall()
    # for x in results:
    #     print(x[0], "", x[1])

    # altering tables:
    query = 'SELECT students.first_name, students.last_name, scores.test_id, scores.score FROM students INNER JOIN ' \
            'scores ON students.student_id = scores.student_id WHERE scores.score <= 15 ORDER BY scores.test_id'
    cursor.execute(query)
    results = cursor.fetchall()
    for x in results:
        print(x[0], " ", x[1], " ", x[2], " ", x[3])

except mysql.connector.Error as error:
    print("error:", error)

finally:
    if conn.is_connected():
        conn.close()

