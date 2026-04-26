from flask import Blueprint, render_template

teacher_routes = Blueprint('teacher', __name__)

@teacher_routes.route('/teacher/dashboard')
def teacher_dashboard():
    return render_template("teacher.html")