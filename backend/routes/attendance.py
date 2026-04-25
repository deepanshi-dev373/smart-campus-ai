from flask import Blueprint, session
import sqlite3, datetime
from ai.face_attendance import start_camera

attendance_routes = Blueprint('attendance', __name__)

def connect():
    return sqlite3.connect("campus.db")

@attendance_routes.route('/mark')
def mark():
    if 'user' not in session:
        return "Login First"

    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO attendance(username,date) VALUES (?,?)",
                (session['user'], str(datetime.datetime.now())))
    conn.commit()
    conn.close()

    return "Attendance Marked ✅"

@attendance_routes.route('/ai-attendance')
def ai_attendance():
    start_camera()
    return "AI Started"