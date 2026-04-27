import sqlite3

conn = sqlite3.connect("campus.db")
cur = conn.cursor()

# USERS
cur.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
email TEXT,
password TEXT,
role TEXT
)
""")

# STUDENTS
cur.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY,
name TEXT,
course TEXT,
semester TEXT,
attendance INTEGER,
fees INTEGER
)
""")

# NOTICES
cur.execute("""
CREATE TABLE IF NOT EXISTS notices(
id INTEGER PRIMARY KEY,
title TEXT,
content TEXT
)
""")

# DEFAULT USERS
cur.execute("INSERT INTO users(email,password,role) VALUES('admin@gmail.com','1234','admin')")
cur.execute("INSERT INTO users(email,password,role) VALUES('teacher@gmail.com','1234','teacher')")
cur.execute("INSERT INTO users(email,password,role) VALUES('student@gmail.com','1234','student')")

conn.commit()
conn.close()
print("Database Ready ✅")