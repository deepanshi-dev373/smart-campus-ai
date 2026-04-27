from flask import Flask, render_template, request, redirect, session, jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

def db():
    return sqlite3.connect("campus.db")

@app.route('/')
def home():
    return redirect('/login')

# LOGIN
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = db()
        cur = conn.cursor()
        cur.execute("SELECT role FROM users WHERE email=? AND password=?", (email,password))
        user = cur.fetchone()
        conn.close()

        if user:
            session['role'] = user[0]

            if user[0] == 'admin':
                return redirect('/admin')
            elif user[0] == 'teacher':
                return redirect('/teacher')
            else:
                return redirect('/student')

        return "Invalid Login"

    return render_template("login.html")

# ================= ADMIN DASHBOARD =================
@app.route('/admin')
def admin():
    conn = db()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM students")
    students = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM users WHERE role='teacher'")
    teachers = cur.fetchone()[0]

    cur.execute("SELECT AVG(attendance) FROM students")
    attendance = cur.fetchone()[0] or 0

    cur.execute("SELECT COUNT(*) FROM students WHERE fees=0")
    pending_fees = cur.fetchone()[0]

    cur.execute("SELECT title FROM notices ORDER BY id DESC LIMIT 3")
    notices = cur.fetchall()

    conn.close()

    return render_template("admin.html",
        students=students,
        teachers=teachers,
        attendance=attendance,
        fees=pending_fees,
        notices=notices)

# ================= STUDENTS =================
@app.route('/students')
def students():
    conn = db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    conn.close()
    return render_template("students.html", data=data)

@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    course = request.form['course']
    semester = request.form['semester']

    conn = db()
    cur = conn.cursor()
    cur.execute("INSERT INTO students(name,course,semester,attendance,fees) VALUES(?,?,?,?,?)",
                (name,course,semester,80,1))
    conn.commit()
    conn.close()

    return redirect('/students')

# ================= NOTICE =================
@app.route('/notice')
def notice():
    conn = db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM notices")
    data = cur.fetchall()
    conn.close()
    return render_template("notice.html", data=data)

@app.route('/add_notice', methods=['POST'])
def add_notice():
    title = request.form['title']
    content = request.form['content']

    conn = db()
    cur = conn.cursor()
    cur.execute("INSERT INTO notices(title,content) VALUES(?,?)",(title,content))
    conn.commit()
    conn.close()

    return redirect('/notice')

# ================= API FOR MOBILE =================
@app.route('/api/students')
def api_students():
    conn = db()
    cur = conn.cursor()
    cur.execute("SELECT name,attendance FROM students")
    data = cur.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)