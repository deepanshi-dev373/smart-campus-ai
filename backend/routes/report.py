from flask import Blueprint
import sqlite3
import matplotlib.pyplot as plt

report_routes = Blueprint('report', __name__)

@report_routes.route('/report')
def report():
    conn = sqlite3.connect("campus.db")
    cur = conn.cursor()

    cur.execute("SELECT username, COUNT(*) FROM attendance GROUP BY username")
    data = cur.fetchall()
    conn.close()

    names = [d[0] for d in data]
    counts = [d[1] for d in data]

    plt.bar(names, counts)
    plt.savefig("static/report.png")

    return "Report Generated ✅"