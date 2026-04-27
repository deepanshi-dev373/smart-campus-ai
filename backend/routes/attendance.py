from flask import Blueprint, render_template
import sqlite3

attendance_routes = Blueprint('attendance', __name__)

def db():
    return sqlite3.connect("campus.db")

@attendance_routes.route('/attendance')
def attendance():
    conn = db()
    cur = conn.cursor()
    cur.execute("SELECT name, attendance FROM students")
    data = cur.fetchall()
    conn.close()

    return render_template("attendance.html", data=data)