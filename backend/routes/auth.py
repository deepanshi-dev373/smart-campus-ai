from flask import Blueprint, request, render_template, redirect, session

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['user'] = "admin"
        return redirect('/dashboard')

    return render_template("login.html")