import sqlite3

def connect():
    return sqlite3.connect("campus.db")

def setup():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS attendance(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()

setup()