from flask import Blueprint, request, render_template, redirect
import sqlite3

student_routes = Blueprint('student', __name__)

def db():
    return sqlite3.connect("campus.db")

@student_routes.route('/students')
def students():
    conn = db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    conn.close()
    return render_template("students.html", data=data)

@student_routes.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    course = request.form['course']
    semester = request.form['semester']

    conn = db()
    cur = conn.cursor()
    cur.execute("INSERT INTO students(name,course,semester,attendance) VALUES(?,?,?,0)",
                (name,course,semester))
    conn.commit()
    conn.close()

    return redirect('/students')