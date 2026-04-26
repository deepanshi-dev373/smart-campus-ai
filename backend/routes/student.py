from flask import Blueprint, render_template

student_routes = Blueprint('student', __name__)

@student_routes.route('/student/dashboard')
def student_dashboard():
    return render_template("student.html")