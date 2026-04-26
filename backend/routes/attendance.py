from flask import Blueprint, request
import sqlite3

attendance_routes = Blueprint('attendance', __name__)

def db():
    return sqlite3.connect("campus.db")

@attendance_routes.route('/mark_attendance', methods=['POST'])
def mark():
    data = request.json

    conn = db()
    cur = conn.cursor()

    cur.execute("INSERT INTO attendance(student_id,date,status) VALUES(?,?,?)",
                (data['id'], data['date'], data['status']))

    conn.commit()
    conn.close()

    return {"msg": "Attendance Marked"}