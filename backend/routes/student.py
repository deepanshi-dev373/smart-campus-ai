from flask import Blueprint, render_template, request

student_routes = Blueprint('student', __name__)

@student_routes.route('/student/dashboard')
def dashboard():
    return render_template("student.html")

@student_routes.route('/student/attendance')
def attendance():
    return {"attendance": "85%"}

@student_routes.route('/student/fees')
def fees():
    return {"fees": "Paid ✅"}

@student_routes.route('/student/complaint', methods=['POST'])
def complaint():
    return {"msg": "Complaint submitted"}

@student_routes.route('/student/chat', methods=['POST'])
def chat():
    return {"msg": "Message sent to teacher"}