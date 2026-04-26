from flask import Blueprint, request, jsonify
import sqlite3

student_routes = Blueprint('student', __name__)

def db():
    return sqlite3.connect("campus.db")

# ADD STUDENT
@student_routes.route('/add_student', methods=['POST'])
def add_student():
    data = request.json
    conn = db()
    cur = conn.cursor()

    cur.execute("INSERT INTO students(name, course, semester) VALUES(?,?,?)",
                (data['name'], data['course'], data['semester']))

    conn.commit()
    conn.close()
    return {"msg": "Student Added"}

# GET STUDENTS
@student_routes.route('/students')
def get_students():
    conn = db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")
    data = cur.fetchall()

    conn.close()
    return jsonify(data)

# DELETE
@student_routes.route('/delete_student/<int:id>')
def delete(id):
    conn = db()
    cur = conn.cursor()

    cur.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return {"msg": "Deleted"}