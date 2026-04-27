from flask import Blueprint, request, render_template, redirect, session
import sqlite3

auth_routes = Blueprint('auth', __name__)

def db():
    return sqlite3.connect("campus.db")

@auth_routes.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = db()
        cur = conn.cursor()
        cur.execute("SELECT role FROM users WHERE email=? AND password=?",(email,password))
        user = cur.fetchone()
        conn.close()

        if user:
            session['user'] = email
            session['role'] = user[0]
            return redirect('/dashboard')
        else:
            return "Invalid Login ❌"

    return render_template("login.html")