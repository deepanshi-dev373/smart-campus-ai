from flask import Blueprint

attendance_routes = Blueprint('attendance', __name__)

@attendance_routes.route('/attendance')
def attendance():
    return "Attendance Marked ✅"