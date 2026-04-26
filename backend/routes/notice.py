from flask import Blueprint, request, jsonify
import sqlite3

notice_routes = Blueprint('notice', __name__)

def db():
    return sqlite3.connect("campus.db")

@notice_routes.route('/add_notice', methods=['POST'])
def add():
    msg = request.json.get("msg")

    conn = db()
    cur = conn.cursor()

    cur.execute("INSERT INTO notices(message) VALUES(?)", (msg,))
    conn.commit()
    conn.close()

    return {"msg": "Notice Added"}

@notice_routes.route('/notices')
def get():
    conn = db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM notices")
    data = cur.fetchall()

    conn.close()
    return jsonify(data)