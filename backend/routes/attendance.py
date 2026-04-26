from flask import Blueprint

attendance_routes = Blueprint('attendance', __name__)

@attendance_routes.route('/attendance', methods=['GET','POST'])
def attendance():
    return "Attendance Working ✅"