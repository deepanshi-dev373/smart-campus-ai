from flask import Blueprint, request

teacher_routes = Blueprint('teacher', __name__)

@teacher_routes.route('/attendance')
def attendance():
    return {"msg": "Attendance marked"}

@teacher_routes.route('/assignment', methods=['POST'])
def assignment():
    return {"msg": "Assignment uploaded"}

@teacher_routes.route('/notice', methods=['POST'])
def notice():
    return {"msg": "Notice sent"}