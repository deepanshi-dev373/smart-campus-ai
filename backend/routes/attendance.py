from flask import Blueprint, render_template, request

attendance_routes = Blueprint("attendance_routes", __name__)

# Dummy student data (baad me DB connect kar sakti ho)
students = [
    {"id": 1, "name": "Amit", "present": 18, "total": 20},
    {"id": 2, "name": "Neha", "present": 14, "total": 20},
    {"id": 3, "name": "Rahul", "present": 10, "total": 20},
    {"id": 4, "name": "Simran", "present": 19, "total": 20},
]

# 📌 Attendance Page
@attendance_routes.route("/attendance")
def attendance():
    for s in students:
        s["percent"] = round((s["present"] / s["total"]) * 100, 2)

    defaulter_list = [s for s in students if s["percent"] < 75]

    return render_template(
        "attendance.html",
        students=students,
        defaulters=defaulter_list
    )


# 📌 Mark Attendance (Daily)
@attendance_routes.route("/mark/<int:id>", methods=["POST"])
def mark_attendance(id):
    for s in students:
        if s["id"] == id:
            s["present"] += 1
            s["total"] += 1
    return "Marked"