from flask import Blueprint, render_template

teacher_routes = Blueprint('teacher', __name__)

@teacher_routes.route('/teacher/dashboard')
def dashboard():
    return render_template("teacher.html")

@teacher_routes.route('/teacher/attendance')
def attendance():
    return {"msg": "Attendance marked"}

@teacher_routes.route('/teacher/assignment')
def assignment():
    return {"msg": "Assignment uploaded"}

@teacher_routes.route('/teacher/notice')
def notice():
    return {"msg": "Notice sent"}