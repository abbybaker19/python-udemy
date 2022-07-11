import sqlite3
import sys
import csv

db_conn = sqlite3.connect('test.db')
print("database created")
cursor = db_conn.cursor()


def print_db():
    try:
        result = cursor.execute("SELECT id, f_name, l_name, age, address, salary, hire_date FROM employees")
        for row in result:
            print("id:", row[0])
            print("first name:", row[1])
            print("last name:", row[2])
            print("age:", row[3])
            print("address:", row[4])
            print("salary:", row[5])
            print("hire date:", row[6])
    except sqlite3.OperationalError:
        print("the table does not exist")
    except:
        print("could not retrieve data from database")


try:
    db_conn.execute("CREATE TABLE employees(id integer primary key autoincrement not null, f_name text not null, "
                    "l_name text not null, age int not null, address TEXT, salary REAL, hire_date TEXT);")
    db_conn.commit()
    print("table created")
except sqlite3.OperationalError as e:
    print("table could not be created:", str(e))

db_conn.execute("INSERT INTO employees(f_name, l_name, age, address, salary, hire_date) VALUES ('tony', 'stark', '45', 'Malibu', 10000000, '2008-9-3');")
db_conn.commit()
print("employee entered")

print_db()

try:
    db_conn.execute("UPDATE employees SET address = 'New York City' WHERE id =1")
    db_conn.commit()
except sqlite3.OperationalError:
    print("database could not be updated")

print_db()

try:
    db_conn.execute("DELETE FROM employees WHERE id = 1")
    db_conn.commit()
except sqlite3.OperationalError:
    print("data could not be deleted")

print_db()

db_conn.rollback()

print_db()

try:
    db_conn.execute("ALTER TABLE employees ADD COLUMN 'image' BLOB DEFAULT NULL")
    db_conn.commit()
except sqlite3.OperationalError:
    print("table could not be altered")

cursor.execute("PRAGMA TABLE_INFO(employees)")
row_names = [nameTuple[1] for nameTuple in cursor.fetchall()]
print(row_names)

cursor.execute("SELECT COUNT(*) FROM employees")
num_rows = cursor.fetchall()
print("total rows:", num_rows[0][0])

cursor.execute("SELECT SQLITE_VERSION()")
print("SQLITE VERSION: ", cursor.fetchone())

with db_conn:
    db_conn.row_factory = sqlite3.Row
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    for row in rows:
        print("{} {}".format(row["f_name"], row["l_name"]))

with open('dump.sql', 'w') as f:
    for line in db_conn.iterdump():
        f.write("%s\n" % line)

db_conn.close()

