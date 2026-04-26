from flask import Blueprint

attendance_routes = Blueprint('attendance', __name__)

@attendance_routes.route('/mark')
def mark():
    return "Attendance Marked ✅"