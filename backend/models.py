import sqlite3

def connect():
    return sqlite3.connect("campus.db")

def setup():
    conn = connect()
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY, name TEXT, attendance INT)")
    cur.execute("CREATE TABLE IF NOT EXISTS faculty(id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS complaints(id INTEGER PRIMARY KEY, msg TEXT)")

    conn.commit()
    conn.close()

setup()