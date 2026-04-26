from flask import Blueprint, render_template, session
import sqlite3

dashboard_routes = Blueprint('dashboard', __name__)

def db():
    return sqlite3.connect("campus.db")

@dashboard_routes.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return "Login First ❌"

    conn = db()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM students")
    total = cur.fetchone()[0]

    cur.execute("SELECT AVG(attendance) FROM students")
    avg = cur.fetchone()[0] or 0

    conn.close()

    return render_template("dashboard.html", total=total, avg=avg)