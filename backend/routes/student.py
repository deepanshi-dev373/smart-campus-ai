from flask import Blueprint, request

student_routes = Blueprint('student', __name__)

@student_routes.route('/student/dashboard')
def dashboard():
    return {"msg": "Student Dashboard"}

@student_routes.route('/complaint', methods=['POST'])
def complaint():
    return {"msg": "Complaint submitted"}