BEGIN TRANSACTION;
CREATE TABLE employees(id integer primary key autoincrement not null, f_name text not null, l_name text not null, age int not null, address TEXT, salary REAL, hire_date TEXT, 'image' BLOB DEFAULT NULL);
INSERT INTO "employees" VALUES(2,'tony','stark',45,'Malibu',10000000.0,'2008-9-3',NULL);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('employees',2);
COMMIT;
