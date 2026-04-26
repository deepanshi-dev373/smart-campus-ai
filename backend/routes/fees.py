from flask import Blueprint, request
import sqlite3

fees_routes = Blueprint('fees', __name__)

def db():
    return sqlite3.connect("campus.db")

@fees_routes.route('/pay_fees', methods=['POST'])
def pay():
    data = request.json

    conn = db()
    cur = conn.cursor()

    cur.execute("UPDATE students SET fees=? WHERE id=?",
                (data['amount'], data['id']))

    conn.commit()
    conn.close()

    return {"msg": "Fees Updated"}