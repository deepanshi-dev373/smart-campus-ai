from flask import Blueprint, request, render_template, redirect
import sqlite3

notice_routes = Blueprint('notice', __name__)

def db():
    return sqlite3.connect("campus.db")

@notice_routes.route('/notice')
def notice():
    conn = db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM notices")
    data = cur.fetchall()
    conn.close()
    return render_template("notice.html", data=data)

@notice_routes.route('/add_notice', methods=['POST'])
def add_notice():
    title = request.form['title']
    content = request.form['content']

    conn = db()
    cur = conn.cursor()
    cur.execute("INSERT INTO notices(title,content) VALUES(?,?)",(title,content))
    conn.commit()
    conn.close()

    return redirect('/notice')