import sqlite3

def connect():
    return sqlite3.connect("campus.db")

def setup():
    conn = connect()
    cur = conn.cursor()

    # Students
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        course TEXT,
        semester TEXT,
        attendance INTEGER DEFAULT 0,
        fees INTEGER DEFAULT 0
    )
    """)

    # Attendance
    cur.execute("""
    CREATE TABLE IF NOT EXISTS attendance(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        date TEXT,
        status TEXT
    )
    """)

    # Notices
    cur.execute("""
    CREATE TABLE IF NOT EXISTS notices(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        message TEXT
    )
    """)

    conn.commit()
    conn.close()

setup()