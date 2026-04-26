from flask import Blueprint, request

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.json

    if data['role'] == "admin":
        return {"msg": "Admin Login"}
    elif data['role'] == "teacher":
        return {"msg": "Teacher Login"}
    else:
        return {"msg": "Student Login"}