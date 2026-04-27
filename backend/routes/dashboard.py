from flask import Blueprint, render_template, session
import sqlite3

dashboard_routes = Blueprint('dashboard', __name__)

def db():
    return sqlite3.connect("campus.db")

@dashboard_routes.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return "Login First"

    conn = db()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM students")
    total_students = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM users WHERE role='teacher'")
    total_teachers = cur.fetchone()[0]

    cur.execute("SELECT AVG(attendance) FROM students")
    avg_attendance = cur.fetchone()[0] or 0

    cur.execute("SELECT title FROM notices ORDER BY id DESC LIMIT 3")
    notices = cur.fetchall()

    conn.close()

    return render_template("dashboard.html",
        students=total_students,
        teachers=total_teachers,
        attendance=avg_attendance,
        notices=notices)