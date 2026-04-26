import sqlite3

conn = sqlite3.connect("campus.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
email TEXT,
password TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY,
name TEXT,
attendance INTEGER
)
""")

# Default user
cur.execute("INSERT INTO users(email,password) VALUES('admin@gmail.com','1234')")

conn.commit()
conn.close()