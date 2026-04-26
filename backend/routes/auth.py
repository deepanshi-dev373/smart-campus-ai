from flask import Blueprint, request, redirect, render_template

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html")