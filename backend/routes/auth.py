from flask import Blueprint, request, render_template, redirect, session
import sqlite3

auth_routes = Blueprint('auth', __name__)

def connect():
    return sqlite3.connect("campus.db")

@auth_routes.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        u = request.form['username']
        p = request.form['password']

        conn = connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO users(username,password) VALUES (?,?)",(u,p))
        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template("register.html")

@auth_routes.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        u = request.form['username']
        p = request.form['password']

        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?",(u,p))
        data = cur.fetchone()
        conn.close()

        if data:
            session['user'] = u
            return redirect('/dashboard')

        return "Invalid Login ❌"

    return render_template("login.html")